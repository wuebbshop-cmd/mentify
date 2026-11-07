## 1. Concept and Use Case

### 1.1 The naming problem in a packet-switched network

Forwarding in an Internet Protocol network is driven entirely by addresses. A router examines the destination address in the header of each datagram, matches it against a routing table, and forwards the datagram out of the indicated interface. No stage of that process consults a name. Names therefore have no operational meaning to the infrastructure; they are a convenience for people, and they must be translated into addresses before the first packet can be sent.

The translation could be done in three ways. Names could be abolished and users could be asked to remember addresses, which fails on memorability and on change. Names could be bound to addresses inside every application, which fails because a change of address would require every client in the world to be rebuilt. Or the binding could be held in a separate, shared database consulted at the moment of use, which is the option the Internet adopted. That database is the Domain Name System, abbreviated DNS, and the act of consulting it is called name resolution.

The architectural value of the third option is indirection. Because the binding is looked up rather than compiled in, an organisation can move a service to a new address without any client noticing, provided only that the record is updated. Because the binding is looked up at use time, it can be varied by location, by time, or by health of the server. Indirection is the reason a service can be migrated, load-balanced or failed over without a change to client software, and it is the single most important idea in this topic.

### 1.2 Why a single shared file stopped working

The first operational solution was not a distributed database at all. The Advanced Research Projects Agency Network maintained a single text file, conventionally called HOSTS.TXT, which listed every host on the network with its address. Sites downloaded the file periodically and consulted it locally. In the early 1970s that was adequate: there were few hosts, one administrator, and change was slow.

Three properties made the arrangement untenable as the network grew, and each is worth naming because each maps to a design requirement of the replacement.

**Size.** One file describing every host grows linearly with the number of hosts. Around the mid 1980s the file was growing by hundreds of entries per week and had become expensive merely to transfer.

**Consistency.** Every copy had to be refreshed whenever any host changed. With one writer and a weekly cycle, copies diverged for days at a time, and a name would resolve differently on two machines.

**Authority.** A single administrator had to approve every change, which made the network's growth dependent on one organisation's throughput and made that organisation a single point of failure.

The design that replaced it, specified in 1983 and refined in 1987, inverted all three properties. Instead of one file, the name space is a tree that can be *delegated*: the administrator of a subtree can create names beneath it without asking anyone. Size becomes irrelevant because no server holds the whole tree. Consistency becomes local because only the servers that hold a zone need agree about it. Authority becomes distributed because delegation is recursive.

### 1.3 Design requirements the system had to meet

Stated as requirements rather than history, the system had to satisfy the following, and every mechanism described later exists to satisfy one of them.

| Requirement | Why it matters | Mechanism that satisfies it |
|---|---|---|
| Scale to millions of names | A flat database cannot | Hierarchical name space with delegation |
| Delegate authority | Owners must add names without a central queue | Zones, zone cuts, NS records |
| Tolerate server failure | No server can be a single point of failure | Redundant authoritative servers, resolver retries |
| Answer quickly under load | Every connection begins with a lookup | Multi-level caching governed by time to live |
| Tolerate differing implementations | Many vendors must interoperate | Fixed message format and record types |
| Extend without redesign | New services appear continuously | Type codes and unknown-type handling |

The requirement that is easiest to underestimate is the last. Because the protocol defines a numeric type field and requires resolvers to pass through types they do not understand, new record types could be introduced for decades without changing the transport. Mail routing, service discovery, email authentication and certificate authority restrictions all arrived as new record types in an unchanged protocol.

### 1.4 The services DNS actually provides

DNS is often described as a name-to-address translator, which is accurate but far too narrow. It is better described as a distributed, hierarchical database with a query protocol, in which the most common record type happens to hold an address.

The services that depend on it include the following.

**Host addressing.** Address records map a name to an IP version 4 address, and quad-A records map a name to an IP version 6 address. A single name may carry several of each, which is how round-robin distribution and, in more sophisticated deployments, health-aware answering work.

**Mail routing.** Mail exchanger records tell a sending mail server where to deliver mail for a domain, with a preference value that establishes an order. This decouples the mail service from the web service completely; the two usually run on different infrastructure and often on different networks.

**Aliasing.** Canonical name records let one name be an alternative label for another, which is how a provider can rename a service while every existing link keeps working.

**Delegation.** Name server records are the mechanism by which a parent hands authority for a subtree to a child. This is the record type that makes the whole architecture possible.

**Reverse mapping.** Pointer records in the special reverse zones map addresses back to names, which is used in log correlation and in some anti-abuse checks.

**Policy publication.** Text records carry arbitrary strings and are the standard way to publish a Sender Policy Framework policy, a DomainKeys Identified Mail key, a Domain-based Message Authentication policy, and the token that proves control of a domain to a third-party service.

**Service discovery.** Service records describe not only a host but a port and a protocol for a named service, which is used by directory services and by some messaging systems.

**Certificate issuance control.** Certification Authority Authorization records restrict which certificate authorities may issue certificates for a domain, which is a DNS-based control over a completely different protocol.

An answer to a question about what DNS is used for should therefore list at least addressing, mail routing, aliasing, delegation and policy publication, and should make clear that the database is extensible rather than fixed.

### 1.5 Position in the protocol stack and the trust model

DNS is an application-layer protocol. It runs over the User Datagram Protocol, abbreviated UDP, on port 53 for ordinary queries, and over the Transmission Control Protocol, abbreviated TCP, on the same port 53 for responses that exceed the datagram size the transport can carry and for zone transfers. The choice of UDP as the default is a deliberate latency decision: a query and a response fit in single datagrams, so no connection setup is required and a failed query can simply be retried.

The protocol was designed in an era of small, mutually trusting networks, and its trust model reflects that. A resolver asks a server a question and, absent additional mechanisms, believes the answer if the answer looks like a reply to its question. The referral chain provides *delegation* of authority but not *proof* of it. Everything in the security section of this note follows from that observation: the protocol has no intrinsic authentication, and the mechanisms added later supply unpredictability, verification or confidentiality on top.

Traditional DNS traffic is also unencrypted. Any party on the path between a client and its resolver can read the names being queried, which is a privacy exposure distinct from the integrity exposure. Encrypted transports, namely DNS over Transport Layer Security on port 853 and DNS over Hypertext Transfer Protocol Secure on port 443, address the privacy exposure. They do not by themselves make the data authentic; that is the separate job of the signed-record extensions described in Section 2.

### 1.6 The formal anatomy of a domain name

A domain name is a sequence of labels separated by dots, terminated in its absolute form by a final dot that denotes the root. Written as www.example.com. the name has four components in wire order from most specific to least: the label www, the label example, the label com, and the empty root label.

Four rules govern the syntax and are examined more often than their apparent importance suggests.

Each label may be at most 63 octets. The complete name in wire format, including the length octets and the terminating root label, may be at most 255 octets. Comparison is case-insensitive, so Example.COM and example.com are the same name, although the case of the original spelling is preserved in some responses. A name with a trailing dot is fully qualified and is interpreted from the root; a name without one is relative to a configured origin, and the difference produces a large share of real configuration errors.

Names outside the original ASCII repertoire are supported through a separate encoding that converts a Unicode label into an ASCII form prefixed with a special marker, so that the wire protocol never had to change. This is why an internationalised domain appears in tools as a string beginning with the letters xn followed by two hyphens.

## 2. Data, Syntax, and Core Concepts

### 2.1 The hierarchical name space

The name space is a tree. Every node has a label, every node except the root has exactly one parent, and a node may have any number of children. The root is the single node from which all names descend.

**The root domain.** The root zone is served by the root name servers. Its content is minimal and entirely structural: it contains the delegation records for every top-level domain, together with the records needed to operate the root zone itself. The root holds no web addresses. Every uncached lookup that is not answered lower in the tree begins with a query to a root server, whose only useful answer is a referral downwards.

**Top-level domains.** Beneath the root sit the top-level domains, of which there are three families worth distinguishing. Generic top-level domains, abbreviated gTLDs, are defined by category or commercial policy and include the original trio of com, org and net together with several hundred newer ones such as app, dev and shop. Country-code top-level domains, abbreviated ccTLDs, are two-letter codes assigned to countries and territories under a published standard list, for example ke, uk, de and jp. Sponsored top-level domains are restricted to a defined community, for example edu for accredited post-secondary institutions, gov for United States government bodies and mil for its military. The distinction matters because policy differs: ccTLD registration rules are set nationally and can require local presence, whereas gTLDs are governed by ICANN policy.

**Second-level domains.** The layer below a top-level domain is where registrations happen. A second-level domain such as example.com is created when a registrant asks an accredited registrar to reserve the name; the registrar instructs the registry for com to publish a delegation naming the registrant's chosen name servers. From that moment the registrant controls everything below the name, subject only to the registry's policy.

**Subdomains.** Any name created beneath a registered domain is a subdomain, and the registrant creates it by adding records to their own zone. No external party is informed. The label can describe a host (www), a service (mail, vpn, api), an environment (dev, staging), a region (eu, us-east) or a tenant (customer42). The only constraints are the label length limits and the requirement that names remain unique within the zone.

A **zone** is not the same thing as a domain. A zone is the set of names for which one particular set of name servers holds authoritative data. A zone begins at a zone apex, which is the domain name that the zone describes, and it extends downwards until it meets a delegation. When the owner of example.com delegates shop.example.com to a separate set of name servers, a zone cut occurs at that name: above the cut the parent zone is authoritative, and below it the child zone is. If no cut is made, every subdomain remains part of the parent zone, which is the normal arrangement for small sites.

| Level | Example | Controlled by | Contents |
|---|---|---|---|
| Root | the trailing dot | Root server operators | Delegations for every top-level domain |
| gTLD | com, org, app | The registry for that TLD | Delegations for every registered second-level domain |
| ccTLD | ke, uk, de | The national registry | Delegations, often with local policy rules |
| Second-level | example.com | The registrant | Address, mail, name server and policy records |
| Subdomain | www.example.com, api.example.com | The registrant | Records for one host, service or tenant |

### 2.2 The server hierarchy and the role of each tier

Five roles appear in a resolution, and a correct answer distinguishes all five.

The **stub resolver** is a minimal client in the operating system. It reads the local configuration to learn which recursive resolver to use, formulates a query with the recursion-desired flag set, and returns the response to the calling application. It performs no iteration, holds a small cache in some implementations, and does not follow referrals.

The **recursive resolver** accepts queries from stubs and takes on the obligation to produce a final answer. It performs the iteration described in Section 3, caches every record it learns in accordance with the time to live of that record, and returns either the requested data, a definitive statement that the name does not exist, or a server failure. Recursive resolvers are operated by Internet service providers, by enterprises, by router firmware in a forwarding role, and by public providers such as the services at 8.8.8.8 and 1.1.1.1. A resolver that only forwards queries to another resolver is called a forwarder; it caches but does not iterate.

The **root name servers** answer the first iteration step. There are 13 logical server identities, named a.root-servers.net through m.root-servers.net, each operated by an independent organisation. Thirteen is a protocol artefact of the original packet-size design, not a statement about physical capacity: each of the 13 addresses is announced from many locations using anycast routing, in which the same address is advertised from multiple sites and each query is delivered by the routing system to the nearest instance. The number of physical instances is well over a thousand, spread across every inhabited continent. An examination answer that describes the root as 13 machines is wrong; the correct description is 13 logical identities served by many anycast instances.

The **top-level domain name servers** answer the second step. Each TLD registry operates a set of servers that hold, for every registered domain in that TLD, the delegation records naming that domain's authoritative servers.

The **authoritative name servers** hold the actual zone data. They are configured by the zone owner or by a DNS hosting provider acting for the owner. An authoritative server answers queries about its own zones from its own data, sets the authoritative-answer flag, does not recurse on behalf of clients, and gives a definitive negative answer when a name inside its zones does not exist.

Authoritative service is normally deployed as a primary and one or more secondaries. The primary holds the master copy of the zone, edited by the administrator or generated by a provisioning system. Secondaries obtain the zone by a full transfer, historically over TCP, and refresh it periodically by checking the serial number in the start-of-authority record. Modern deployments notify secondaries immediately when the zone changes, and transfer only the differences where the implementation supports incremental transfer. This arrangement is what allows an authoritative service to survive the loss of any one server.

| Role | Answers | Sets which flag | Caches |
|---|---|---|---|
| Stub resolver | Nothing itself; forwards the question | Recursion desired | Optionally, small |
| Recursive resolver | Everything, by iterating | Recursion available | Yes, the main cache |
| Root server | Where each top-level domain lives | Authoritative | No |
| Top-level domain server | Where each registered domain lives | Authoritative | No |
| Authoritative server | The records of its own zones | Authoritative | No |

### 2.3 The DNS message format

Every DNS query and response has the same structure: a header, a question section, and up to three data sections. Understanding the header explains most of the diagnostic output you will ever read.

The header is twelve octets. Its fields are fixed and small, which is why the protocol is cheap to parse.

| Field | Size | Meaning |
|---|---|---|
| Identifier | 16 bits | Chosen by the client, copied into the reply, used to match the two |
| QR | 1 bit | Zero for a query, one for a response |
| Opcode | 4 bits | Zero for a standard query, five for a dynamic update |
| AA | 1 bit | The responding server is authoritative for the name |
| TC | 1 bit | The response was truncated and must be retried over TCP |
| RD | 1 bit | Recursion is desired by the client |
| RA | 1 bit | Recursion is available at this server |
| Z | 3 bits | Reserved, must be zero |
| AD | 1 bit | The data was authenticated by the resolver |
| CD | 1 bit | Checking was disabled by the client |
| RCODE | 4 bits | Result code: zero is success, three is name error, two is server failure |
| QDCOUNT and others | 16 bits each | Counts of entries in the four sections |

The sections are the payload. The **question** section repeats the name, type and class being asked about. The **answer** section holds records that answer the question, which may include a canonical name chain before the terminal record. The **authority** section holds records that describe the zone rather than answer the question, which in a referral means the delegation records of the child and in a negative answer means the start-of-authority record of the zone. The **additional** section holds records expected to be useful next, most importantly the addresses of the name servers named in a referral, known as glue.

The original specification limited a UDP response to 512 octets, which is why the truncation flag exists. An extension defined in later standards, known as EDNS version zero, allows the client to advertise a larger buffer and allows the protocol to carry options; modern resolvers commonly advertise between 1,232 and 4,096 octets. The value 1,232 is widely recommended because it avoids fragmentation on typical paths. When a response would exceed the advertised size, the server truncates it and sets the truncation flag, and the client repeats the query over TCP.

### 2.4 Resource record semantics

A resource record is the unit of data in a zone. Every record has the same five fields, and the type field determines how the final field is interpreted.

| Field | Meaning |
|---|---|
| Name | The owner name, in fully qualified form inside a zone file |
| Type | The kind of data, for example address or mail exchanger |
| Class | Almost always IN, meaning Internet |
| Time to live | Seconds for which the record may be cached |
| Data | Type-specific content |

The seven types that must be known precisely are set out below, with the semantics and the constraints that examiners test.

**Address record, type A.** Maps an owner name to one IP version 4 address. Several address records at the same name are legal and mean that any of the addresses is acceptable; clients typically use the first and fall back to the others. A name with several addresses is the simplest form of load distribution, though it has no health awareness of its own.

**Quad-A record, type AAAA.** Maps an owner name to one IP version 6 address, stored as sixteen octets. It is a separate type rather than a widened address record because the original protocol fixed the address record at four octets. A name with both types is reachable over either version; a name with only an address record is, in practice, unreachable from a network that has migrated fully to version 6.

**Canonical name record, type CNAME.** Declares that the owner name is an alias for another name, and that resolution must continue at that other name. Two constraints apply and both are frequently examined. A canonical name record may not coexist with any other record at the same owner name, because the other records could never be reached once the alias redirected the query. A canonical name record may not be placed at the zone apex, because the apex must carry a start-of-authority record and name server records, which would violate the first constraint. The practical consequence is that a zone apex is never an alias, and a web host that wants both example.com and www.example.com to serve the same site publishes an address record at the apex and an alias at www.

**Mail exchanger record, type MX.** Names a host that accepts mail for the domain, preceded by a preference value. A lower preference is tried first. The target must be a name with an address record, not a name that is only an alias, because mail transfer agents are not required to follow aliases when routing mail. A published preference of zero pointing at the root name is a deliberate null record meaning that the domain accepts no mail at all.

**Name server record, type NS.** Names a server authoritative for a zone. Every zone apex must carry at least two, on distinct networks where possible. The same type appears at the parent as the delegation record. When parent and child disagree, the parent's copy governs, because that is the copy the rest of the world follows when it descends the tree.

**Pointer record, type PTR.** Maps an address to a name, and exists only inside the reverse zones. The reverse zone for IP version 4 is a subtree of in-addr.arpa in which the octets of the address are written in reverse order. The reverse zone for IP version 6 is a subtree of ip6.arpa in which the thirty-two hexadecimal nibbles are written in reverse order, separated by dots. A pointer record is not the inverse of an address record in any automatic sense: it must be published deliberately, it may disagree with the forward record, and it carries no authority.

**Text record, type TXT.** Carries one or more character strings. It is the general-purpose extension point of DNS and is used for the Sender Policy Framework, for DomainKeys Identified Mail public keys, for Domain-based Message Authentication Reporting and Conformance policy, for site-verification tokens, and for arbitrary documentation. Multiple strings in one record are concatenated by consumers.

Two further types appear in ordinary operation even though they are not on the core list. The start-of-authority record, type SOA, sits at every zone apex and carries the zone's primary server, the responsible mailbox, a serial number, refresh, retry and expire intervals, and a negative-caching value. The service record, type SRV, carries priority, weight, port and target for a named service. Both are discussed where they are needed.

| Type | Data content | Typical use | Key constraint |
|---|---|---|---|
| A | 4-octet address | Host addressing over version 4 | Several may exist at one name |
| AAAA | 16-octet address | Host addressing over version 6 | Independent of the A record |
| CNAME | A domain name | Aliasing one name to another | Excludes all other records; not at apex |
| MX | Preference plus host name | Mail routing | Target must not be an alias |
| NS | A domain name | Delegation and zone authority | Required at every apex |
| PTR | A domain name | Reverse mapping | Lives only in reverse zones |
| TXT | One or more strings | Policy and verification | Free-form content |

### 2.5 Zone files and concrete entries

A zone file is the textual representation of a zone. It is the form in which records are written by hand or generated by tooling, and reading one fluently is the practical test of whether the record semantics have been understood.

The example below is a complete and valid zone for example.com, with explicit owner names and explicit lifetimes so that no directive context is required. The addresses are taken from the documentation ranges reserved for examples.

```text
example.com.        3600  IN  SOA   ns1.example.com. hostmaster.example.com. (
                              2024110701 ; serial
                              7200       ; refresh
                              3600       ; retry
                              1209600    ; expire
                              300 )      ; negative caching

example.com.        3600  IN  NS    ns1.example.com.
example.com.        3600  IN  NS    ns2.example.com.

example.com.        3600  IN  A     192.0.2.10
example.com.        3600  IN  MX    10 mail1.example.com.
example.com.        3600  IN  MX    20 mail2.example.com.
example.com.        3600  IN  TXT   "v=spf1 mx -all"

www.example.com.     300  IN  CNAME example.com.
shop.example.com.   3600  IN  A     192.0.2.40
api.example.com.     600  IN  A     192.0.2.50
api.example.com.     600  IN  AAAA  2001:db8:1::50

ns1.example.com.    3600  IN  A     198.51.100.53
ns2.example.com.    3600  IN  A     198.51.100.54
mail1.example.com.  3600  IN  A     192.0.2.25
mail2.example.com.  3600  IN  A     192.0.2.26
```

Each line carries one record, and the columns are owner name, lifetime, class, type and data. Reading the zone rather than merely recognising its syntax is the point.

The start-of-authority record declares that ns1.example.com is the primary server and that mail about the zone should be sent to the mailbox hostmaster at example.com. The serial number is the zone's version; secondaries compare it to decide whether to transfer. The refresh and retry intervals govern how often a secondary checks and how long it waits after a failure. The expire interval is the period after which a secondary that cannot reach the primary must stop answering, which prevents it from serving indefinitely stale data. The final value sets the ceiling for negative caching.

The two name server records declare the authoritative servers, and the matching address records for those names are inside the same zone. Because the names are inside the delegated zone, the parent must supply their addresses as glue; otherwise a resolver asking for the address of ns1.example.com would need the very servers it is trying to find.

The address record at the apex makes the bare name reachable, which matters because the bare name is what people type. The alias at www points at the apex, which is legal because the alias is not at the apex itself, and it carries a shorter lifetime because web addresses are the records most likely to change.

The two mail exchanger records give a preferred and a fallback server. The preference values order them; the lower number is tried first, and the higher one is used only if the preferred host is unreachable. The text record publishes a sender policy that authorises the domain's own mail exchangers and rejects everything else.

The two address records at api.example.com demonstrate dual-stack publishing: the same name is reachable over both address families, and a client on a version 6 only network uses the quad-A record.

The corresponding reverse zone for the 192.0.2.0 network, delegated to the same operator, contains the following entries.

```text
10.2.0.192.in-addr.arpa.   3600  IN  PTR   example.com.
40.2.0.192.in-addr.arpa.   3600  IN  PTR   shop.example.com.
50.2.0.192.in-addr.arpa.   3600  IN  PTR   api.example.com.
```

The octets are reversed because the delegation of reverse zones follows the same hierarchical logic as forward zones: the registry for 192.in-addr.arpa delegates 2.0.192.in-addr.arpa to the network operator, who then owns the whole address block's reverse name space. Reversal is what makes the most specific part of the address the leftmost label, so that the hierarchy reads in the same direction as it does for ordinary names.

### 2.6 Delegation, referrals and glue

Delegation is the mechanism that makes the name space unbounded, and it operates through a simple exchange. The parent zone contains a name server record for the child, with the child's owner name on the left and the child's server name on the right. It contains no other data about the child, except the addresses of those servers when the server names fall inside the child zone.

A query that arrives at a server for a name below a delegation produces a *referral*: a response with an empty answer section, the child's name server records in the authority section, and glue address records in the additional section where required. The authoritative flag is clear, because this server is not authoritative for the child. The referring server is not being unhelpful; it is doing exactly what the design requires, which is to point the asker at the next level of authority.

Glue is needed when a name server's own name is inside the zone it serves. Consider a delegation for example.com whose name server is ns1.example.com. To ask ns1.example.com anything, a resolver must first know its address. If it asks the com servers for that address, they must refer it to the example.com servers, which is the server whose address is in question. The circular dependency is broken by including the address in the parent as glue: data that is not authoritative but is necessary for the delegation to function.

Glue introduces a security consideration that is examined in the security section. A server must not accept data that is outside its bailiwick, meaning outside the zone for which it is authoritative. Without that check, a malicious delegation could cause a resolver to cache records for unrelated names.

### 2.7 Caching and the meaning of time to live

Every record carries a lifetime in seconds. The value is an instruction to any cache: keep this data for at most this long, then discard it. A resolver that has cached a record is not obliged to keep it for the full period; it may discard sooner. It may never keep it longer.

The mechanism is what makes the system viable. Consider a resolver serving ten thousand clients. A popular name might be requested thousands of times an hour. Without caching, each request would cost three round trips to the hierarchy, which would place an impossible load on the root and top-level domain servers. With caching, the first request costs the full walk and the rest cost a memory lookup.

Caching occurs at several levels simultaneously, and each level applies the same rule with the lifetime it received.

| Level | Implementation | Populated by | Cleared by |
|---|---|---|---|
| Browser | Private host cache in the browser process | The browser's own resolver calls | Browser network settings page |
| Operating system | System resolver cache, for example the Windows DNS client or the systemd resolved service | Answers returned to the stub resolver | The platform flush command |
| Router or gateway | Forwarding cache in the home or office device | Answers returned to LAN clients | Restart of the device or its DNS service |
| Recursive resolver | The main cache, serving an ISP or an enterprise | The iteration the resolver performed | Operator action, or expiry |
| Application runtime | Caches inside language runtimes and connection pools | The application's own lookups | Restart of the process |

Two behaviours follow from the design and both are frequently tested.

First, the lifetime counts down. A record published with a lifetime of 3,600 seconds appears in a cache with 3,600 remaining immediately after the fetch, and with 3,500 remaining a hundred seconds later. Any tool that displays cached data shows the remaining value, not the published value.

Second, a change is not instantaneous. When an address record is replaced, the authoritative server answers with the new value immediately, but every cache that already holds the old value continues to return it until its copy expires. This is why TTL planning exists: an operator who intends to move a service reduces the lifetime to a few minutes a day in advance, performs the move, and then restores a longer lifetime once the old value has drained from caches.

Choosing a lifetime is a trade-off with two ends.

A **long** lifetime reduces query load, reduces latency for repeat lookups, and makes the service resilient to a short outage of the authoritative servers, because caches keep answering. It also makes changes slow and makes a mistaken record persist for hours.

A **short** lifetime makes changes fast and lets the operator react to a failure quickly. It increases load on the authoritative servers and on the resolver, and it removes the protective effect of caching during an outage.

Typical values reflect that trade-off. Delegation records in top-level domains carry lifetimes of a day or two because they change rarely. Ordinary address records commonly carry between five minutes and one hour. Records used for load balancing or failover may carry a minute or less, and some operators use thirty seconds for services that must move fast.

### 2.8 Negative caching

A resolver must be able to remember that a name does not exist, or that a name exists but has no record of the requested type. Without that memory, every request for a misspelled or non-existent name would be re-asked all the way to the authoritative server, and a trivial denial-of-service attack could be built from random names.

Negative caching is formalised in a later standard and works as follows. When an authoritative server answers negatively, it includes the start-of-authority record of its zone in the authority section. That record carries two lifetimes: its own record lifetime, and the final value in its data, historically called the minimum field. The negative cache lifetime is the smaller of the two. Resolvers cache the negative result for that period and answer subsequent identical queries from that cached denial.

Two negative outcomes are distinguished, and the distinction is a favourite examination point.

**Name error**, reported as a response code of three and conventionally called NXDOMAIN, means that the queried name does not exist anywhere in the zone. No type at that name can exist.

**No data**, sometimes called NODATA, is reported as a successful response code with an empty answer section and the zone's start-of-authority record in the authority section. It means the name exists but has no record of the requested type. A domain with only a mail exchanger record and no address record produces no data for an address query.

A server that returns no data for a type is not broken, and a resolver must not treat the two outcomes as the same. A client that asks for a quad-A record and receives no data must conclude that the name exists only over version 4, not that the name is unregistered.

Negative caching has an operational consequence that surprises administrators. If a name is queried before it is created, the denial may be cached for the negative lifetime, and the name will appear not to exist for that period even after the record is published. This is why a new subdomain occasionally appears broken to one office and fine to another, and why lowering the negative lifetime is part of a fast-moving deployment.

### 2.9 Transport behaviour

Ordinary queries travel over UDP on port 53. A single datagram carries the query, and a single datagram carries the response, so there is no handshake, no acknowledgement and no connection state at the server. A lost query is retried by the client after a timeout, with the retry interval widening on successive attempts.

TCP on port 53 is used in three situations, and all three must be named for a complete answer.

A response that exceeds the size the client advertised, or 512 octets in the absence of the extension, is truncated. The server sets the truncation flag, and the client repeats the query over TCP to obtain the whole answer. Responses with long canonical name chains, many mail exchangers or large text records commonly trigger this.

Zone transfers between authoritative servers use TCP, because a full zone may be megabytes and requires reliable, ordered delivery. The classic transfer is a full copy; the incremental form transfers only changes since a known serial number.

Operational policy occasionally requires TCP. Some networks block large UDP responses to avoid fragmentation-based attacks, and some resolvers prefer TCP for its resistance to certain spoofing attempts. A firewall that permits UDP 53 but blocks TCP 53 will therefore appear to work most of the time and fail on exactly the queries that matter most.

Two encrypted transports are now widely deployed. DNS over Transport Layer Security, abbreviated DoT, wraps the ordinary protocol in a TLS session on port 853. DNS over Hypertext Transfer Protocol Secure, abbreviated DoH, carries the same messages inside an HTTPS request on port 443. Both hide the query from observers on the path. Neither proves that the answer is correct, so both are complementary to, not replacements for, signed records.

### 2.10 The security model and its weaknesses

Traditional DNS provides no authentication. A resolver matches a response to its query by the query identifier and by the source and destination addresses and ports, and accepts the first matching response. Every attack and every defence in this area is about how hard it is to produce a matching response, or how to prove that a response is genuine even if it is not the one that was requested.

**Spoofing and cache poisoning.** An attacker who can send packets to a resolver, and who can predict or observe the query identifier and source port, can send a forged response before the genuine one arrives. The forged response is cached for the lifetime of the records it contains, which means every client of that resolver receives the attacker's address. The canonical demonstration of this attack in 2008, by Dan Kaminsky, showed that a weakness in the delegation logic allowed an attacker to repeat guesses efficiently against the same name, turning an improbable guess into a practical attack. The industry response was rapid and is the reason the defences below are now standard.

**The entropy defence.** A 16-bit identifier gives 65,536 possibilities. A resolver that also randomises its source port from the roughly thirty thousand ports available gives a combined space in the order of a billion possibilities per query. An attacker who must guess correctly within the few milliseconds before the genuine answer arrives will fail with overwhelming probability. This defence is cheap and effective, and its presence is why modern resolvers are not trivially poisoned. It is also why 2008 is treated as the dividing line in DNS security history.

**Bailiwick checking.** A resolver must reject records that fall outside the zone of the server that supplied them. If a server authoritative for example.com includes a record for a bank in its response, the resolver must discard it, because that server has no authority over the bank's zone. Without this check, a single compromised delegation could poison a resolver's cache for arbitrary names.

**Case randomisation.** Some resolvers randomise the capitalisation of the query name and require the response to echo the same pattern. Since the name is compared case-insensitively for meaning, the pattern adds entropy without changing semantics. It is a supplementary measure, not a substitute for the two primary ones.

**Signed records.** The Domain Name System Security Extensions, abbreviated DNSSEC, add public-key signatures to records. Each zone publishes a key-signing key and a zone-signing key as key records, and signs every record set with the zone-signing key. The parent publishes a delegation signer record containing a digest of the child's key, which chains authority from the root downwards. A validating resolver follows the chain from a configured trust anchor and can therefore prove that an answer came from the zone owner and was not modified. Denial of existence is signed too, using a mechanism that proves no name exists between two published names.

DNSSEC is important to describe precisely because it is widely misunderstood. It provides **origin authentication and integrity**. It does **not** provide confidentiality: an observer can still read the query and the answer. It also does not prevent denial of service, because an attacker can still drop packets.

**Anycast.** Announcing the same address from many locations does three things at once. It reduces latency by serving from the nearest instance. It spreads load, because the routing system distributes queries across instances. And it absorbs attack traffic, because a flood is distributed across the same instances rather than concentrated on one. This is the primary reason the root service can withstand sustained attack, including the distributed denial of service attacks, abbreviated DDoS, that aim to exhaust a service rather than to falsify its data.

**Amplification and reflection.** A small query can produce a much larger response. An attacker who sends queries with the victim's address as the source causes the responses to be directed at the victim. Defences include limiting response rates per client, refusing to answer queries from addresses that cannot legitimately have sent them by filtering spoofed source addresses at network ingress, and disabling unnecessary services such as unrestricted zone transfer.

| Threat | What the attacker exploits | Primary defences |
|---|---|---|
| Cache poisoning | Trust in the first matching response | Random identifier and source port, bailiwick checks, DNSSEC |
| Spoofed response | Predictable query parameters | The same unpredictability measures, plus case randomisation |
| Reflection and amplification | Small query, large answer | Response rate limiting, ingress source filtering |
| Volumetric attack | Concentration of service in one place | Anycast distribution, over-provisioning |
| On-path observation | Plaintext protocol | Encrypted transports on ports 853 and 443 |
| Registrar or account compromise | Control of the delegation itself | Registry locks, multi-factor authentication, monitoring |

## 3. Methods and Operations

### 3.1 The canonical iterative resolution walk

The following sequence is the reference answer for a question of the form "explain how a name is resolved". It assumes a cold cache at every level and a client that has never contacted the name before. The name is www.example.com and the requested type is A.

Step 1. The application calls the stub resolver. The stub resolver reads its configuration and learns the address of the recursive resolver, for example 192.168.1.1. It builds a query with a randomly chosen 16-bit identifier, sets the recursion-desired flag, and places the question www.example.com, type A, class IN in the question section. It sends the query to the resolver on UDP port 53 and starts a timer.

Step 2. The recursive resolver receives the query and checks its cache. There is no entry for the name and type, and no cached negative entry, so it must iterate. It consults its root hints, a small built-in list of the thirteen root server identities and their addresses, which is the only piece of the hierarchy it must know in advance.

Step 3. The resolver sends an iterative query to a root server, for example 198.41.0.4. The recursion-desired flag is clear, because the resolver is asking the server to answer only from its own knowledge. The root server is authoritative for the root zone and does not know the address of www.example.com, so it returns a referral rather than an answer. The response has an empty answer section, thirteen name server records for com in the authority section, and address records for those servers in the additional section. The authoritative flag is clear, because the root is not authoritative for com.

Step 4. The resolver caches the com name server set, with its lifetime of two days in a typical root zone, and selects one of the com servers, for example 192.5.6.30. It sends the same question to that server.

Step 5. The com server is authoritative for com but not for example.com. It returns a second referral: an empty answer section, the name server records for example.com in the authority section, and glue address records for those servers in the additional section, because their names fall inside the delegated zone. The resolver caches this delegation.

Step 6. The resolver sends the question to one of the example.com authoritative servers, for example 199.43.135.53. This server holds the zone and answers authoritatively. If the zone publishes www as an alias for the apex, the answer contains two records: a canonical name record stating that www.example.com is an alias for example.com, and an address record giving the address of example.com. Both are returned in one response because the target lies inside the same zone, and the authoritative flag is set.

Step 7. The resolver caches both records with their published lifetimes, then sends a response to the stub resolver. That response copies the original identifier from the client's query, has the recursion-available flag set, and contains the same records. It also carries the additional flag indicating that the resolver considers the data authentic if the zone is signed and validation succeeded.

Step 8. The stub resolver hands the address to the application, which opens a connection to that address on the port required by its protocol, for example 443 for secure web traffic. The name has now done its job and plays no further part in the exchange.

Three observations about this walk matter more than the step count.

The resolver performs at most three round trips to the hierarchy, not one per label. It does not query the root for each label of a longer name; it asks for the full name at each level and follows referrals. A name with six labels still costs three round trips, because referrals are made on zone boundaries rather than on labels.

The resolver caches intermediate results, so the second lookup for any name in com skips steps 3 and 4, and the second lookup in example.com skips steps 5 and 6 as well. In steady state almost every query is answered from cache.

If the alias target lies in a different zone, the resolver must repeat the iteration for the target name, because it has no authority to assume that the target's zone will resolve without asking. Chains of aliases therefore multiply the work, which is one reason providers keep chains short.

### 3.2 What each tier caches, and for how long

Caching decisions differ by tier because the data differs in stability.

The resolver caches each name server set it learns, with the lifetime the parent published. Delegation lifetimes are usually a day or two, which means a resolver that has resolved any name in com will usually answer the first step of subsequent lookups from its own cache.

The resolver caches each answer record with that record's lifetime, which for host records is commonly between five minutes and one hour.

The resolver caches negative answers with the negative lifetime derived from the zone's start-of-authority record, and it caches the start-of-authority record itself so that it can answer questions about the zone efficiently.

The stub resolver caches whatever its operating system chooses to keep. On Windows the client service keeps a cache and honours record lifetimes; on Linux the behaviour depends on the resolver library or the local caching daemon in use.

The browser keeps a separate cache with its own policy. Browsers frequently impose a ceiling on how long they will honour a record, so a record published with a one-hour lifetime may be discarded by the browser after a minute. This decoupling is deliberate, and it is why clearing a browser's host cache and flushing the operating system cache are two different operations.

### 3.3 Controlling a query from the command line

The lookup tool used throughout this note allows each part of the protocol to be exercised deliberately. The flags below are the ones worth knowing, because each maps to a concept in the previous section.

| Purpose | Command form | What it demonstrates |
|---|---|---|
| Ask a specific server | dig @192.5.6.30 example.com A | The server named is the one queried |
| Suppress recursion | dig @198.41.0.4 www.example.com +norecurse | Referral behaviour and the delegation chain |
| Perform the iteration yourself | dig +trace example.com A | Every referral, in order |
| Force TCP | dig +tcp example.com A | Port 53 over the reliable transport |
| Request signed data | dig +dnssec example.com A | Signature records and the authenticated-data flag |
| Read only the answer | dig example.com A +noall +answer | The record without the message framing |
| Query a pointer | dig -x 8.8.8.8 | Reverse lookup through the in-addr.arpa tree |
| Set a larger buffer | dig +bufsize=1232 example.com A | The advertised UDP payload size |

The distinction between the first two rows is the one students most often miss. Naming a server changes who is asked; suppressing recursion changes what is being asked of it. A query to a root server with recursion requested will receive a refusal or a referral, never an answer for a name the root does not hold.

### 3.4 Verifying delegation

A delegation can be checked at each level without any special tool, because delegation data is ordinary records.

Ask the top-level domain servers for the name server records of the domain. These are the records the parent publishes, and they are what the world follows.

Ask the authoritative servers for the same name server records. These are the records the child publishes. If the two sets differ, the parent's set wins for the purposes of resolution, and the child's own view of itself is wrong.

Ask for the delegation signer record of the domain. Its presence indicates that the parent has a signed delegation, which is the prerequisite for the chain of trust to continue into the child.

Check that the glue addresses exist and are current. A delegation that names servers whose addresses have changed will send resolvers to machines that no longer answer, which presents as intermittent failure depending on which name server a resolver selects.

### 3.5 Changing a record safely

Record changes should follow a sequence, because caches convert an instantaneous edit into a gradual transition.

Step 1. Inspect the current lifetime of the record and of the delegation above it. The longer of the two governs how long the change takes to be universal.

Step 2. If the lifetime is long, lower it to a small value and wait at least the old lifetime. The wait is essential: caches that already hold the record will keep it for the old period regardless of the new value.

Step 3. Make the change. Verify it by querying the authoritative servers directly, which bypasses every cache.

Step 4. Wait for the new small lifetime to elapse, so that the old value has drained from every cache that could hold it.

Step 5. Restore a longer lifetime if the record is now stable.

Step 6. Verify again through a resolver rather than an authoritative server, which is what ordinary clients use.

### 3.6 Flushing caches at each level

Flushing is a local operation with a specific scope. The commands below are the standard ones for each platform, and each clears only the cache named.

| Platform | Command | Scope |
|---|---|---|
| Windows | ipconfig /flushdns | The operating system resolver cache |
| Windows, PowerShell | Clear-DnsClientCache | The same cache, different interface |
| Linux with systemd-resolved | sudo resolvectl flush-caches | The local caching resolver |
| Linux with a local forwarding daemon | sudo systemctl restart dnsmasq | That daemon's cache |
| macOS | sudo dscacheutil -flushcache and a restart of the responder | The system cache |
| Browser | The browser's internal network page | That browser's host cache |

The commands do not reach the resolver operated by the Internet service provider, and they do not reach a router cache. When a stale answer persists after a flush, the next step is to query a different resolver, which distinguishes a local cache from an upstream one.

### 3.7 A diagnostic procedure

The order below follows the delegation chain outwards, so that each step eliminates a layer.

1. Confirm the name is spelled correctly and is fully qualified where the tool requires it.
2. Query the authoritative servers directly. If they answer correctly, the zone is correct and the fault lies in caching or in the path.
3. Query the parent for the name server records. A mismatch with the child indicates a broken or stale delegation.
4. Query a public resolver. A different answer from your local resolver identifies a stale or wrong cache.
5. Flush the local cache and repeat step 4. A change in behaviour confirms a local cache fault.
6. Check the transport. A query that succeeds over TCP but fails over UDP indicates a size or filtering problem.
7. Only after all of the above, investigate the destination service.

## 4. Worked Implementation from the Notes

### 4.1 Task: observe the full delegation chain in one command

### 4.2 Implementation: trace iteration from the root downwards

Step 1. Ask the tool to start at a root server and follow referrals itself, rather than delegating the work to a resolver.

```bash
dig +trace example.com A
```

Step 2. Read the output in four blocks.

```text
.                       518400  IN      NS      a.root-servers.net.
.                       518400  IN      NS      b.root-servers.net.
.                       518400  IN      NS      c.root-servers.net.
;; Received 239 bytes from 192.168.1.1#53(192.168.1.1) in 11 ms

com.                    172800  IN      NS      a.gtld-servers.net.
com.                    172800  IN      NS      b.gtld-servers.net.
com.                    172800  IN      NS      c.gtld-servers.net.
;; Received 1170 bytes from 198.41.0.4#53(a.root-servers.net) in 94 ms

example.com.            172800  IN      NS      a.iana-servers.net.
example.com.            172800  IN      NS      b.iana-servers.net.
;; Received 692 bytes from 192.5.6.30#53(a.gtld-servers.net) in 106 ms

example.com.            3600    IN      A       93.184.216.34
;; Received 56 bytes from 199.43.135.53#53(a.iana-servers.net) in 121 ms
```

Step 3. Interpret block one. The tool first asks the configured resolver for the root name server names, so that it has a starting point. This block is not part of the iteration; it is bootstrapping. The lifetime of 518,400 seconds is six days, which is normal for root zone data because the root changes rarely.

Step 4. Interpret block two. A root server was asked for example.com and replied with the com delegation. The lifetime of 172,800 seconds is two days, the standard for top-level domain delegations. The response came from a root server, proving that the first hop of the iteration reached the top of the tree.

Step 5. Interpret block three. A com server was asked and replied with the example.com delegation. This referral is the critical one for the owner of a domain: it is the record set that the registry holds on the owner's behalf, and if it is wrong, nothing below it can work.

Step 6. Interpret block four. An authoritative server answered with the address record and the authoritative flag. The lifetime of 3,600 seconds is the value published by the zone owner and is now the ceiling for every cache.

Step 7. Count the cost. Three referrals produced three round trips of roughly 94, 106 and 121 milliseconds, so the cold lookup cost a quarter of a second. A cached lookup costs the resolver nothing beyond a memory read, which quantifies the reason caching exists.

### 4.3 Task: perform the iteration by hand to prove which server controls which fact

### 4.4 Implementation: three queries with recursion suppressed

Step 1. Ask a root server directly, with recursion forbidden.

```bash
dig @198.41.0.4 www.example.com A +norecurse
```

Step 2. Read the response header and authority section.

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34011
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27

;; AUTHORITY SECTION:
com.                    172800  IN      NS      a.gtld-servers.net.
com.                    172800  IN      NS      b.gtld-servers.net.
;; (eleven further name server records omitted for brevity)

;; ADDITIONAL SECTION:
a.gtld-servers.net.     172800  IN      A       192.5.6.30
a.gtld-servers.net.     172800  IN      AAAA    2001:503:a83e::2:30
```

Step 3. Interpret the header. Only the response flag is set: the authoritative flag is absent because the root is not authoritative for the name, the recursion-available flag is absent because the tool did not request recursion, and the answer count is zero. Thirteen authority records and twenty-seven additional records are exactly what a root referral looks like, and the additional section carries glue for both address families.

Step 4. Follow the referral to the top-level domain server.

```bash
dig @192.5.6.30 www.example.com A +norecurse
```

Step 5. Read the second referral.

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40119
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 2, ADDITIONAL: 4

;; AUTHORITY SECTION:
example.com.            172800  IN      NS      a.iana-servers.net.
example.com.            172800  IN      NS      b.iana-servers.net.

;; ADDITIONAL SECTION:
a.iana-servers.net.     172800  IN      A       199.43.135.53
b.iana-servers.net.     172800  IN      A       199.43.134.53
```

Step 6. Interpret. The pattern is identical to the previous step, one level lower: no answer, a delegation in the authority section, and glue in the additional section because the name server names fall inside the delegated zone.

Step 7. Ask the authoritative server.

```bash
dig @199.43.135.53 www.example.com A +norecurse
```

Step 8. Read the final answer.

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51123
;; flags: qr aa; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; ANSWER SECTION:
www.example.com.        3600    IN      CNAME   example.com.
example.com.            3600    IN      A       93.184.216.34
```

Step 9. Interpret. The authoritative flag is now set, the answer count is two, and the authority section is empty because no referral is needed. The first record is an alias and the second is the address of the alias target. Only this server could have answered in this way, which is the operational meaning of authority.

### 4.5 Task: prove that a cached answer decays

### 4.6 Implementation: query twice and compare remaining lifetimes

Step 1. Resolve through the configured resolver and note the lifetime.

```bash
dig example.com A +noall +answer
```

Step 2. A representative first result shows the published value.

```text
example.com.            3600    IN      A       93.184.216.34
```

Step 3. Wait sixty seconds, then query again.

```bash
dig example.com A +noall +answer
```

Step 4. The second result shows a reduced remaining lifetime, because the resolver is serving its cached copy.

```text
example.com.            3540    IN      A       93.184.216.34
```

Step 5. Interpret. A reduction of exactly the elapsed time proves that the answer came from the cache and was not fetched again. The lifetime is a countdown, not a fixed property of the record. When it reaches zero the resolver must ask again, and the value will jump back to the published figure.

Step 6. Confirm the same behaviour in the operating system cache on Windows.

```powershell
ipconfig /displaydns | Select-String -Pattern "example.com" -Context 0,5
```

Step 7. The block shows the same countdown in the system cache, with the record type given numerically and the data shown in a labelled field. Two independent caches, two independent counters, one published lifetime.

### 4.7 Task: build and validate a zone file

### 4.8 Implementation: write the zone and check it before serving it

Step 1. Write the zone for a small domain, with explicit owner names and explicit lifetimes.

```text
example.com.        3600  IN  SOA   ns1.example.com. hostmaster.example.com. (
                              2024110701 ; serial
                              7200       ; refresh
                              3600       ; retry
                              1209600    ; expire
                              300 )      ; negative caching

example.com.        3600  IN  NS    ns1.example.com.
example.com.        3600  IN  NS    ns2.example.com.
example.com.        3600  IN  A     192.0.2.10
example.com.        3600  IN  MX    10 mail1.example.com.
example.com.        3600  IN  TXT   "v=spf1 mx -all"

www.example.com.     300  IN  CNAME example.com.
api.example.com.     600  IN  A     192.0.2.50
api.example.com.     600  IN  AAAA  2001:db8:1::50

ns1.example.com.    3600  IN  A     198.51.100.53
ns2.example.com.    3600  IN  A     198.51.100.54
mail1.example.com.  3600  IN  A     192.0.2.25
```

Step 2. Validate the file with the standard checker before loading it.

```bash
named-checkzone example.com /etc/bind/db.example.com
```

Step 3. Read the result.

```text
zone example.com/IN: loaded serial 2024110701
OK
```

Step 4. Interpret. The checker parses every record, confirms that a start-of-authority record exists at the apex, confirms that at least one name server record exists, confirms that every name ends with a dot where an absolute name is intended, and confirms that the serial number is present. A syntax error in a zone file causes the server to refuse the whole zone rather than serve part of it, which is why validation is done before a reload rather than after.

Step 5. Verify that the alias rule is respected. The zone contains an alias at www and no other record at that name, and the apex carries a start-of-authority record, name server records, an address record, mail records and a text record with no alias among them. Adding an alias at the apex, or adding an address record beside the alias at www, would be rejected by the checker.

Step 6. Verify that mail routing is satisfiable. The mail exchanger target mail1.example.com has an address record inside the same zone. Had the target been an alias, the record would have been syntactically valid but would have violated the routing rule that mail exchangers must resolve to an address.

### 4.9 Task: observe a negative answer and its cache lifetime

### 4.10 Implementation: query a name that does not exist, then a type that does not exist

Step 1. Ask for a name that is not in the zone.

```bash
dig nxdomain.example.com A
```

Step 2. Read the response.

```text
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 10021
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; AUTHORITY SECTION:
example.com.            300     IN      SOA     ns1.example.com. hostmaster.example.com. (
                                                2024110701 7200 3600 1209600 300 )
```

Step 3. Interpret the first case. The response code of three is the definitive statement that the name does not exist. The answer section is empty and the authority section carries the zone's start-of-authority record, which is what allows the resolver to cache the denial. The negative lifetime is the smaller of the record's own lifetime, 300 seconds, and the final value in its data, also 300 seconds.

Step 4. Ask for a type that the name does not have.

```bash
dig example.com AAAA +noall +comment +authority
```

Step 5. Read the response.

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10088
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; AUTHORITY SECTION:
example.com.            299     IN      SOA     ns1.example.com. hostmaster.example.com. (
                                                2024110701 7200 3600 1209600 300 )
```

Step 6. Interpret the second case. The status is a success, not a name error, because the name exists. The answer section is empty because there is no quad-A record at that name. This is the no-data outcome, and the remaining lifetime of 299 seconds on the authority record shows that even a denial is cached, with a counter that has already begun to run down.

Step 7. State the practical difference. An administrator who sees a name error checks whether the name exists at all. An administrator who sees no data checks whether the record type is published. Confusing the two sends troubleshooting in the wrong direction.

### 4.11 Task: confirm that a signed zone validates

### 4.12 Implementation: validate the chain of trust from the trust anchor

Step 1. Query the delegation signer record that the parent publishes for the domain.

```bash
dig example.com DS +noall +answer
```

Step 2. Read the record.

```text
example.com.            86400   IN      DS      370 13 2 BE74359954660069D5C63D200C39F5603827D7DD02B56F120EE9F3A8 6764247C
```

Step 3. Interpret the fields. The four numbers are the key tag, the algorithm, the digest type and then the digest itself, split across two tokens by the presentation format. The presence of this record in the parent proves that the parent vouches for a specific key in the child, which is the link in the chain.

Step 4. Validate the answer with a validating resolver tool.

```bash
delv example.com A
```

Step 5. Read the result.

```text
; fully validated
example.com.            3600 IN A 93.184.216.34
```

Step 6. Interpret. The comment states that the resolver followed the chain from the configured trust anchor, verified the signature on the address record, and verified the denial-free path of delegations in between. Had any signature failed, the tool would report that the answer was not secure and the resolver would return a server failure instead of the data.

Step 7. Note what is not proven. Validation says nothing about whether the address is the intended one, only that the zone owner published it and nobody altered it in transit.

### 4.13 Task: reset the caches on each platform

### 4.14 Implementation: flush, then verify that the cache is empty

Step 1. On Windows, flush from an elevated Command Prompt and read the confirmation.

```powershell
ipconfig /flushdns
```

```text
Windows IP Configuration

Successfully flushed the DNS Resolver Cache.
```

Step 2. Verify that the entry has gone.

```powershell
ipconfig /displaydns | Select-String -Pattern "example.com"
```

Step 3. No match is returned, which confirms the cache was cleared rather than merely refreshed.

Step 4. On a Linux system that uses the standard local resolver, flush and then inspect its statistics.

```bash
sudo resolvectl flush-caches
sudo resolvectl statistics
```

Step 5. The statistics report a cache size of zero, which is the confirmation that the flush took effect.

Step 6. On macOS, flush the directory service cache and restart the responder so that both halves of the system cache are cleared.

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

Step 7. Interpret. The first command empties the cache, and the second signals the daemon that owns it to reload. Neither prints a success message, so verification is by repeating the original failing lookup rather than by reading output.

Step 8. State the scope once more. All three procedures clear the local machine. The resolver at the provider, and the forwarding cache in the router, are unaffected and must expire on their own.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Reading a response without guessing

A DNS response is a small structured document, and every field has one correct reading. Interpreting it properly is a skill that transfers directly to examination answers, because examiners frequently present a response and ask what it proves.

Read the response code first. A code of zero means the question was answered, but the answer may still be empty. A code of three means the name does not exist. A code of two means the server could not complete the work, which is a failure at the server rather than an absence of data. A code of five means the server refused to answer, typically because recursion was requested from a server that does not offer it, or because of an access policy.

Read the flags second. The response flag distinguishes answers from queries. The authoritative flag tells you whether the data came from the zone that owns it. The truncation flag tells you that the response was cut short and that the client should retry over TCP. The recursion-desired flag records the client's request; the recursion-available flag records the server's capability. The authenticated-data flag reports that a validating resolver has proved the data. Reading the flags in that order prevents the most common misinterpretation, which is treating a referral as a failure.

Read the counts third. A response with one question, zero answers, and a thirteen-record authority section is a root referral. A response with one question, zero answers, and a single start-of-authority record in the authority section is a negative answer. A response with two answers, one of them an alias, is a canonical name chain that was resolved inside one zone.

Read the remaining lifetimes last. They tell you how much of the cache period is left, and therefore how long a change will take to be seen by this particular client.

### 5.2 A capability checklist

A student who can perform the following has understood the mechanism rather than memorised the vocabulary.

- Draw or describe the delegation chain for an arbitrary name and identify which server holds which fact.
- Explain, without notes, why the resolver queries the root once per delegation rather than once per label.
- Distinguish recursion from iteration by naming who does the walking in each case, and place each in the resolution sequence.
- Given a zone file, identify any record that violates a constraint of its type.
- Explain what glue is, why it exists, and what would break without it.
- Predict the effect of a lifetime change on cache behaviour over time, including the drain period.
- Distinguish a name error from a no-data answer and describe how each is cached.
- Name the two randomness sources that make poisoning impractical and explain what each contributes.
- Explain which property DNSSEC provides and which two properties it does not.
- Justify the choice of anycast for the root service in terms of latency, load and resilience.

### 5.3 Common errors and how they present

The failures below account for most real incidents and most lost marks, and each has a recognisable signature.

| Error | How it presents | Why it happens |
|---|---|---|
| Alias at the zone apex | Zone rejected, or the apex unreachable | The apex must hold a start-of-authority and name server records |
| Alias beside another record | Zone rejected, or inconsistent answers | An alias excludes every other record at its name |
| Missing glue for an in-zone name server | Intermittent timeouts for the whole domain | The delegation cannot be followed without the address |
| Mail exchanger pointing at an alias | Mail accepted by some senders, rejected by others | Mail routing expects a name with an address record |
| Wrong reverse zone name | Reverse lookups return a name error | Octets were not reversed, or the suffix was mistyped |
| Lifetime raised before a move | The site appears half-migrated for hours | Caches honour the old lifetime regardless of the new value |
| Delegation not updated at the registrar | The domain resolves to the old provider | The parent's records govern, not the child's |
| Serial number not incremented | Secondaries never pick up the change | Transfers are triggered by a serial comparison |
| Relative name without a trailing dot | Records created under the wrong name | The name was interpreted relative to the zone origin |
| Firewall blocking TCP port 53 | Most queries succeed, large answers fail | Truncated responses cannot be retried |

Three of these deserve a sentence more than the table allows.

The alias errors are structural rather than syntactic. A zone containing an alias at the apex may parse, and some servers will load it, but the zone is then internally inconsistent: the apex cannot simultaneously be an alias and the owner of its own authority records. Correct design places the alias below the apex and points it at the apex, or uses a provider feature that synthesises the apex records at query time.

The glue error is the hardest to diagnose because it is invisible from inside the domain. The domain's own servers answer perfectly when asked directly, and the failure only appears when a resolver tries to reach them by following the delegation.

The serial number error is the classic cause of "it works on one name server and not the other". Secondaries transfer only when the serial increases, so an edit that leaves the serial unchanged propagates nowhere.

### 5.4 Interpreting performance and capacity

Latency in DNS is dominated by round trips, not by processing. An authoritative server answers in microseconds; the milliseconds that users feel are the propagation delay to the server and the number of times the hierarchy must be crossed.

Three consequences follow and are worth stating quantitatively.

A cold lookup that crosses three servers costs three round trips. On a path with 100 milliseconds of round-trip latency, that is a third of a second before the application can even start connecting, which is comparable to the time taken to fetch a small page.

A warm lookup costs one round trip to the resolver if that resolver is local, and zero if the operating system has cached the answer. Moving the cache one level closer therefore removes one round trip, which is why browsers keep their own cache in addition to the system cache.

The load on the hierarchy is set by the miss rate, not the query rate. A resolver serving a million queries a day with a ninety-nine per cent cache hit rate sends only ten thousand queries upwards, and this ratio is what allows thirteen root identities to serve the entire Internet. Any change that reduces cache effectiveness, such as artificially short lifetimes, multiplies the load on the top of the tree.

### 5.5 Limits of the architecture

The design is remarkable for its age and reach, and it has well-understood limits that a balanced answer should name.

**No intrinsic authentication.** A response is believed if it matches the query parameters. DNSSEC closes this gap for zones that deploy it, but deployment is incomplete, and a validating resolver can do nothing about an unsigned zone.

**No confidentiality.** Queries and answers are readable on the path in the default configuration. Encrypted transports address this, at the cost of centralising queries at a small number of providers and of making local inspection harder.

**A single trust anchor at the root.** The chain of trust in DNSSEC begins with the root key. Compromise of that key would undermine validation everywhere, which is why its custody is treated as a high-security operation and why the key is rolled with ceremony and public witnessing.

**Cache dependencies.** A mistaken record propagates as fast as caches fill and persists as long as lifetimes allow. The system has no way to recall a record, which is why the change procedure in Section 3 is deliberate.

**Aliasing and the apex conflict.** The rule that an alias cannot sit at the apex is a direct consequence of the record model, and it forces awkward workarounds for services that want a bare domain to redirect. Providers synthesise such records, but the synthesis is an extension rather than part of the base protocol.

**Operational fragility at the edges.** A domain functions only while three independent parties remain correct: the registry's delegation, the registrar's account, and the operator's zone. Failures at any of the three look identical from the outside, which is the practical difficulty of running a name.

### 5.6 Summary

DNS is a distributed, hierarchical, delegated database with a query protocol, and name resolution is the act of reading from it. The name space is a tree in which the root delegates top-level domains, each top-level domain registry delegates registered second-level domains, and each registrant controls everything below. Zones mark the boundaries of authority, and name server records are the mechanism of delegation, supported by glue where a delegation would otherwise be circular.

Resolution proceeds by iteration from the root downwards and by recursion from the client upwards. The stub resolver asks; the recursive resolver walks; the root and top-level domain servers refer; the authoritative server answers. Three round trips suffice regardless of the depth of the name, and caching removes almost all of them in steady state.

Records carry a type and a lifetime. The type determines the semantics and imposes constraints, of which the alias rules and the mail exchanger target rule matter most in practice. The lifetime governs caching, which happens at the browser, the operating system, the router and the resolver, and which converts every change into a gradual transition.

Because the protocol has no intrinsic authentication, its security depends on making forged answers hard to produce and on making genuine ones provable. Random identifiers and source ports supply the first, signed records and the chain of trust supply the second, and anycast supplies the distribution that keeps the service available under attack. The root is thirteen logical identities served by many physical instances, and port 53 carries both of the transports DNS uses.


