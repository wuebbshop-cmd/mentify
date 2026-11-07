## 1. Concept and Use Case

### 1.1 Four layers that must agree before a page appears

A website that answers a request is never the product of one decision. It is the product of four independent arrangements, each maintained by a different tool, and each capable of failing on its own while the other three remain healthy. The first arrangement is **naming**: a human-readable name must be translated into a machine address, and that translation must be under the control of the site owner rather than of an Internet service provider. The second is **transport and identity**: packets must reach a machine that is reachable from the public Internet, and that machine must be able to prove to a browser that it is the genuine holder of the name. The third is **execution**: a server process, a runtime for the application, and enough memory and processor time to answer requests at the rate they arrive. The fourth is **persistence**: a database and a set of files whose loss would be unrecoverable if no copy existed elsewhere.

Deployment is the discipline of making all four arrangements correct and repeatable. Hosting is the commercial market that supplies the second and third arrangements. Security is the set of controls that protects the third and fourth from people who want to read, alter, or destroy them. Disaster recovery is the set of procedures that restores the fourth when prevention fails. The four are taught together because they fail together: a perfectly hardened server behind a lapsed name registration is invisible, and an impeccably registered name pointing at a machine whose database was never copied is still a total loss after a disk failure.

### 1.2 The path of a single request

Understanding what has to be deployed begins with following one request through every hop.

A visitor types a name into a browser. The browser's stub resolver asks a recursive resolver, typically operated by the access provider or by a public service, for the address record of that name. The recursive resolver, if it has nothing cached, walks the delegation chain from the root zone down to the zone that is authoritative for the name, and returns the address together with a time to live that says how long the answer may be reused. The browser opens a Transmission Control Protocol connection to that address on port 443, performs a Transport Layer Security handshake in which the server presents a certificate for the requested name, and only then sends an HTTP request. The web server passes the request to the application runtime, which may query a database, and the response travels back along the same connection.

Every hop in that paragraph corresponds to something that must be configured, paid for, and monitored. The delegation chain depends on the registrar and the nameservers. The connection depends on routing, on a listening socket, and on a firewall rule that permits port 443. The handshake depends on a certificate that must be issued and renewed. The application depends on a runtime version, on file permissions, and on a database account with exactly the rights it needs. The response depends on the database being available and consistent. An operator who can name the layer at which a fault occurred is already most of the way to fixing it.

### 1.3 Why hosting is a market of isolation

Every hosting product on the market is a point on a single axis: how much of the machine is exclusively yours. At one end, many customers share one operating system, one web server process, and one pool of memory; the boundary between customers is a directory and a user account. At the other end, the customer owns the hardware and merely rents space, power, cooling, and connectivity inside somebody else's building.

As the boundary moves outward, price rises and the blast radius of a neighbour's mistake shrinks. On shared hosting, a runaway script belonging to another customer consumes the processor and makes your pages slow, and a vulnerability in a shared component can expose your files. On a virtual private server, the neighbour is confined by a hypervisor, so processor and memory are allocated rather than contested, although the physical disk and network card are still shared. On a dedicated server, the whole machine is yours, and the only shared elements are the network and the building. On a colocated server, you supply the hardware yourself and rent the environment, which gives the greatest control and the greatest responsibility.

The choice is therefore not a matter of prestige. It is a judgement about traffic, about regulatory obligations, about how much administrative work the team can absorb, and about how much a bad neighbour would cost.

### 1.4 Two failure models: adversaries and disasters

Two different kinds of misfortune are being defended against, and confusing them produces bad plans.

The first is deliberate: automated scanning for known vulnerable software, credential stuffing against an administrative login, injection attacks against form handlers, theft of a database through an unpatched plugin, and ransomware that encrypts files and then deletes the copies it can reach. Controls answer this model. Access control limits what an intruder can reach after a foothold. Authentication raises the cost of guessing. Source code protection removes information that would otherwise shorten an attack. A firewall reduces the exposed surface to the ports that must be reachable.

The second is accidental or environmental: a disk that fails, a file deleted by a tired administrator at two in the morning, a bad deployment that drops a table, a provider that goes out of business without warning, a fire or flood that destroys a building, or a region-wide power failure. Controls cannot answer this model, because the event is not an adversary that can be deterred. Only a copy that exists somewhere else answers it, and only a copy that has been restored at least once can be trusted to answer it.

A complete plan therefore has both halves: reduce the probability of loss with controls, and reduce the consequence of loss with backups and a rehearsed recovery procedure.

### 1.5 The vocabulary this topic depends on

**DNS** is the Domain Name System, the distributed database that maps names to addresses and to other records. **TLD** is a top-level domain, the last label of a name such as `com`, `org`, or `uk`. A **registry** operates the authoritative database for one TLD. A **registrar** is a company accredited to sell names inside that database on behalf of customers. The **registrant** is the person or organisation that holds the name. A **nameserver** is a server that answers queries for a zone. **TTL** is time to live, the number of seconds a cached answer may be reused.

**IP** is Internet Protocol, and an IP address is the numeric locator of an interface. **VPS** is a virtual private server, a machine-sized slice of a physical host created by a hypervisor. **TLS** is Transport Layer Security, the protocol that encrypts and authenticates a connection. **SNI** is Server Name Indication, the TLS extension that lets a client state which name it wants before the certificate is chosen. **WAF** is a web application firewall. **PCI DSS** is the Payment Card Industry Data Security Standard.

**RPO** is the recovery point objective, the greatest age of lost data that the business will tolerate. **RTO** is the recovery time objective, the greatest elapsed time from failure to restored service that the business will tolerate. **ACL** is an access control list. **RBAC** is role-based access control. **MFA** is multi-factor authentication.

## 2. Data, Syntax, and Core Concepts

### 2.1 The name space and its syntax

A domain name is a sequence of labels separated by full stops, read from the most specific on the left to the most general on the right, with the root implicitly at the far right. Each label is limited to 63 octets, the whole name to 253 octets in its textual form, and the complete wire encoding to 255 octets. Labels are compared case-insensitively for the ASCII letters, so `Shop.Example.COM` and `shop.example.com` name the same zone, although the original case may be preserved for display.

Only letters, digits, and the hyphen are permitted in a plain label, and a hyphen may not begin or end one. Names outside that repertoire are carried as **IDN**, internationalised domain names, which are converted to an ASCII-compatible encoding called an A-label beginning with `xn--`. The conversion is not cosmetic: the A-label is what appears in the zone, in the certificate, and in the delegation, and a mismatch between the Unicode form a user types and the A-label that was registered produces a name that resolves somewhere else or nowhere.

A name identifies a **zone**, and a zone is an administrative unit, not a machine. One zone may be served by several servers, and one server may host thousands of zones. The **apex** of a zone is the name itself, and the records at the apex are special: the start of authority record and the delegation records live there, and a CNAME may not.

Subdomains are created by the holder of the zone without any further registration. `shop.example.com` and `support.example.com` are separate names within the same zone, and their records are edited at whichever DNS provider hosts the zone. This is why a business can run several services under one registered name without buying anything further, and why a mistake in one subdomain's records does not affect the delegation of the parent.

### 2.2 The registration data model

A registration is a row in a registry database, plus a contract with a registrar. Four parties appear in it, and the distinction between them explains most confusion about what a registrar can and cannot do.

| Party | Role | What it controls |
|---|---|---|
| Registry | Operates the authoritative database for one TLD | The zone file, the delegation records, the registry lock |
| Registrar | Accredited reseller with a protocol connection to the registry | The registration record, the billing relationship, the nameserver settings |
| Registrant | The holder of the name | The right to use the name, and the choice of registrar |
| DNS provider | Operates the authoritative nameservers for the zone | Every record inside the zone except the delegation itself |

The registrant does not edit the registry directly. The registrar submits a provisioning command using **EPP**, the Extensible Provisioning Protocol, over a TLS-protected session, and the registry applies it. The protocol carries a small set of objects, principally the domain, the host, and the contact, and each object carries a set of status values that govern what may be done to it. Those status values are the mechanism behind most "the transfer was refused" and "the name is locked" messages, so they are worth knowing precisely.

| EPP status | Set by | Meaning | Practical effect |
|---|---|---|---|
| `ok` | Registry | No prohibitions are active | Any permitted operation may proceed |
| `inactive` | Registry | No nameservers are delegated | The name exists but resolves to nothing |
| `clientTransferProhibited` | Registrar | The registrant asked for a transfer lock | A transfer to another registrar is refused |
| `clientHold` | Registrar | The registrar suspended delegation | The name is removed from the zone |
| `serverHold` | Registry | The registry suspended delegation | The name is removed from the zone |
| `pendingDelete` | Registry | The name is in the deletion pipeline | It will become available after the hold period |
| `redemptionPeriod` | Registry | The name was deleted and may be restored for a fee | Only a restore command revives it |
| `autoRenewPeriod` | Registry | The name renewed automatically after expiry | It still resolves, and may still be recovered |
| `clientUpdateProhibited` | Registrar | Updates are blocked at the registrar | Records cannot be changed until the lock is lifted |

Two of these deserve emphasis. `clientHold` and `serverHold` are the states in which a name that is paid for and correctly configured suddenly stops resolving, usually because a billing check failed or because an abuse report was upheld. The fix is administrative, not technical, and no amount of nameserver editing will help until the hold is lifted. `redemptionPeriod` is the state in which a name that has already been deleted can still be recovered, typically for a fee far larger than the renewal price; after it ends, the name returns to general availability and may be bought by somebody else within minutes.

### 2.3 The delegation chain, exactly

The chain has three links, and each link is a pair of records rather than a single one.

**Link one: the root.** The root zone contains a delegation for every top-level domain. For `example.com` the root zone contains an NS record set naming the servers for `com`, and the response from a root server is a referral: it does not answer the question, it names the next servers to ask. The root is served by thirteen named server identities, operated by different organisations and replicated by anycast across hundreds of locations.

**Link two: the TLD.** The `com` zone, operated by the registry for that TLD, contains a delegation for `example.com`. That delegation is an NS record set, optionally accompanied by a DS record if DNSSEC is in use. Crucially, the `com` zone contains nothing else about the domain: no address, no mail exchanger, no text record. This is the single most misunderstood fact about registration. The registry knows only which servers are authoritative; everything else lives in the child zone.

**Link three: the authoritative zone.** The servers named in the delegation answer with the actual records: the address of the web server, the name of the mail exchanger, the policy records, and the start of authority record that describes the zone's timing.

The delegation must also be reachable. If the nameservers named in the parent are themselves inside the delegated zone, for example `ns1.example.com` for `example.com`, the resolver cannot look up the address of `ns1.example.com` without first reaching `ns1.example.com`. The registry solves this by publishing **glue records**: address records for the nameservers, held in the parent zone purely to break the circularity. Glue is a copy, and a stale copy is a classic cause of an outage after a server migration.

```text
Root zone:
  com.                     IN NS   a.gtld-servers.net.
  com.                     IN NS   b.gtld-servers.net.

com zone (registry):
  example.com.             IN NS   ns1.example-dns.net.
  example.com.             IN NS   ns2.example-dns.net.
  example.com.             IN DS   12345 13 2 49FD...

example.com zone (authoritative):
  example.com.             IN SOA  ns1.example-dns.net. hostmaster.example-dns.net. 2026110701 7200 3600 1209600 300
  example.com.             IN A    203.0.113.10
  www.example.com.         IN A    203.0.113.10
  example.com.             IN MX   10 mail.example.com.
  example.com.             IN TXT  "v=spf1 mx -all"
```

The **SOA** record is the metadata of the zone and deserves separate reading. It carries the primary nameserver, a mailbox-style identifier for the responsible party, a serial number, a refresh interval, a retry interval, an expire interval, and a negative-caching minimum. The serial must increase on every change if secondary servers are to notice the change; the common convention is a date stamp followed by a two-digit revision counter. The negative-caching minimum tells resolvers how long to remember that a name does not exist, which is why a newly created subdomain can appear to be missing for several minutes even after it has been added.

A delegation that points at a server which is not in fact authoritative for the zone is called **lame**. The server answers, but with a refusal or with a referral that leads nowhere, and the resolver reports SERVFAIL rather than NXDOMAIN. The distinction matters diagnostically: NXDOMAIN means the name does not exist, while SERVFAIL means the name may exist but the chain is broken.

### 2.4 How resolution actually proceeds

A recursive resolver performs the walk on the client's behalf, and it caches every answer it receives for the duration of the TTL attached to that answer. The walk is iterative: ask a root server, receive a referral to the TLD servers, ask a TLD server, receive a referral to the authoritative servers, ask an authoritative server, receive the answer.

Several details follow from that design and are frequently examined. Caching means a change to a record is not visible everywhere at once; the old answer survives until its TTL expires, which is why operators lower the TTL well in advance of a planned migration and raise it again afterwards. The **stub resolver** on the client usually caches nothing beyond the operating system's own cache, but that cache can be flushed and is a common cause of "it works on my machine". A **CNAME** at a name terminates the lookup at that name: the resolver restarts the query at the target, and no other record type may coexist with the CNAME at the same owner name, which is why a CNAME cannot be placed at the apex of a zone that also carries mail records.

Negative answers are cached too, using the SOA minimum, and a **DNSSEC**-signed zone adds a chain of signatures from the root downward. The chain is anchored in the DS record at the parent, which is why enabling DNSSEC requires an action at the registrar as well as at the DNS provider, and why an expired signature makes a zone fail validation and become unreachable for validating resolvers.

| Record | Purpose | Notes |
|---|---|---|
| A | Maps a name to an IPv4 address | The commonest record in any zone |
| AAAA | Maps a name to an IPv6 address | Absence does not break IPv4 clients |
| CNAME | Aliases one name to another | Cannot coexist with other data at the owner name |
| NS | Delegates a zone to a set of servers | Present at the parent and at the apex |
| SOA | Describes zone timing and authority | One per zone, at the apex |
| MX | Names mail exchangers with a preference value | Lower preference is tried first |
| TXT | Carries arbitrary text | Used for sender policy, verification, and policy records |
| CAA | Restricts which authorities may issue certificates | Enforced by certificate authorities |

### 2.5 Hosting infrastructure models

Four models dominate the market, and they differ in where the isolation boundary sits.

| Model | Isolation boundary | Administrative access | Cost band | Performance predictability | Typical use |
|---|---|---|---|---|---|
| Shared | Directory and user account inside one operating system | Control panel only, no root | Lowest | Low; neighbours compete for processor and memory | Brochure sites, small blogs, first deployments |
| Virtual dedicated (VPS) | Hypervisor, with reserved virtual processor and memory | Root inside the guest | Moderate | Moderate; disk and network still shared | Medium business sites, application servers, staging |
| Dedicated | Whole physical machine | Root, out-of-band console, firmware | High | High; no neighbour on the same processor | High-traffic commerce, regulated workloads |
| Colocated | Whole machine inside a rented facility | Root, and physical access by arrangement | High, plus hardware ownership | High, but entirely the customer's responsibility | Large estates, custom hardware, strict compliance |

The shared model's economy comes from multiplexing: one operating system, one web server, one database service, and one patching regime serve hundreds of sites, so the provider's cost per site is small. The same multiplexing is the weakness. A single unpatched component is reachable from every site on the machine, a single runaway script degrades every neighbour, and the provider's kernel and PHP versions are the versions every customer must live with. The isolation is a permission boundary, not a security boundary, which is why a shared plan is unsuitable for card payments without additional controls.

A VPS moves the boundary into the hypervisor. Each guest has its own kernel, its own filesystem, and a reserved share of processor and memory, so a neighbour cannot read your files and cannot starve your processes of the resources that were reserved. What remains shared is the physical disk subsystem and the network uplink, which is why two VPS instances on the same host can still influence each other's disk latency. The trade is that the customer now owns the operating system: patching, firewall configuration, and certificate renewal become their work, or the work of a managed-service agreement.

A dedicated server removes the neighbour entirely and gives the provider's remote hands as a backup for hardware faults. Colocation goes one step further and makes the hardware the customer's property, which is attractive when the workload needs a specific processor, a hardware security module, or a large storage array that no rental plan offers. It is also the model in which a failed disk is the customer's problem to notice and to replace.

### 2.6 Server resource allocations and what they mean

Hosting plans are sold on four numbers, and each has a precise meaning that differs from the marketing gloss.

**Disk space** is the capacity of the storage visible to the site, measured in gigabytes. It must hold the application files, the uploaded media, the database files, the logs, and the temporary space used during a backup or an upgrade. A small site with text and a few images fits comfortably in a gigabyte; a site with video needs orders of magnitude more, and a database that grows without pruning will eventually fill any allocation. The allocation matters less than the growth path: a plan that cannot be expanded forces a migration under pressure.

**Monthly traffic**, also called bandwidth or transfer, is the volume of data leaving the server in a billing month. Providers meter it in one of two ways. A **cap** allows a fixed volume and either suspends the site and charges an overage when it is exceeded, or throttles it. A **burst** arrangement bills on the ninety-fifth percentile of sampled five-minute rates, discarding the top five per cent of samples, which rewards a site with short peaks and punishes sustained throughput. The two are not comparable, and a plan described only as "unmetered" usually means a port speed limit rather than an unlimited volume.

**Processing speed** is the least honest of the four. On shared hosting, the customer is buying a share of a processor that is not stated, and the only reliable evidence is the measured response time of other sites on the same provider. On a VPS or dedicated plan the allocation is stated as a number of virtual processors and a quantity of memory, and the meaningful additional figure is the input and output operations per second available from the storage, because a database workload is usually limited by disk latency rather than by processor cycles. Memory matters more than processor count for a typical content site, since the database cache and the application's working set determine whether a request is served from memory or from disk.

**Uptime** is expressed as a percentage of a period and is a contractual promise rather than a measurement. The arithmetic is worth memorising, because an examiner will expect the conversion.

| Availability | Downtime per year | Downtime per month |
|---|---|---|
| 99 per cent | about 3 days 15 hours | about 7 hours 18 minutes |
| 99.5 per cent | about 1 day 20 hours | about 3 hours 39 minutes |
| 99.9 per cent | about 8 hours 46 minutes | about 43 minutes 50 seconds |
| 99.95 per cent | about 4 hours 23 minutes | about 21 minutes 55 seconds |
| 99.99 per cent | about 52 minutes 36 seconds | about 4 minutes 23 seconds |

Three qualifications belong in any serious answer. First, a service level agreement normally excludes scheduled maintenance and events outside the provider's control, so the credited figure and the experienced figure differ. Second, compensation is usually a credit against future bills rather than a payment for lost revenue, so the remedy does not restore the loss. Third, the availability of the server is not the availability of the site: a healthy machine behind an expired certificate, a broken deployment, or a failed database is down from the visitor's point of view, and only end-to-end monitoring measures that.

### 2.7 E-commerce hosting prerequisites

A commerce site adds three requirements to an ordinary one, and each has a precise technical form.

**Transport encryption.** Payment details and session identifiers must not cross the network in the clear, so the site must present a valid certificate and redirect every plain request to the encrypted scheme. The certificate must match the name the visitor used, must be within its validity period, and must chain to a root that the client trusts; a missing intermediate certificate produces a warning in some browsers and a hard failure in some clients. **HSTS**, the Strict-Transport-Security response header, instructs the browser to refuse the plain scheme for a defined period and can be extended to subdomains and pinned with preloading, but it is difficult to withdraw and should be introduced with a short lifetime first.

The **dedicated IP address** question is where many answers go wrong by repeating an obsolete rule. Historically, TLS required a separate address for each certificate, because the server had to choose the certificate before it could see which name the client wanted. The **SNI** extension, sent in the first message of the handshake, carries the requested name in the clear, so a server can select the correct certificate from many on a single address. SNI is supported by every current browser and by current command-line clients, so a dedicated address is not strictly required. It is still requested in practice for two reasons: some legacy clients, including very old mobile browsers and some embedded devices, do not send SNI and would receive the default certificate, which produces a name mismatch; and some payment gateways and acquirers list a fixed outbound or inbound address as part of their onboarding. The correct answer states both halves: not technically necessary for modern clients, still operationally common.

**A payment gateway.** The gateway is the service that authorises a card transaction with the acquiring bank and returns an outcome. Integration takes one of three shapes, and the shape determines the compliance burden.

| Integration model | Card data reaches your server | Typical validation level | Trade-off |
|---|---|---|---|
| Hosted payment page | No; the visitor is redirected or framed by the gateway | The lightest self-assessment questionnaire | Least control over appearance, fastest to deploy |
| Direct post or hosted fields | No; the fields are rendered by the gateway inside your page | Light, provided no data touches your code | Better appearance, small scripting obligation |
| Server-to-server interface | Yes, transiently | The heaviest questionnaire, with network segmentation | Full control, greatest responsibility |

Whatever the shape, the server must treat the gateway's notifications as untrusted input. A callback that says a payment succeeded is only evidence if its signature verifies against a shared secret and the raw request body, and the amount and currency in the notification must be compared with the order record before the order is marked paid. The database write that marks the order and the write that records the ledger entry belong in one transaction, so that a crash between them cannot leave a paid order with no record of payment.

**A database.** Commerce needs a store that supports transactions with atomicity, consistency, isolation, and durability, because an order is a set of related writes that must all happen or none. The isolation level decides which concurrency anomalies are possible: a low level permits a reader to see a value that a concurrent writer later rolls back, while a high level prevents that at the cost of blocking or retries. Whatever the level, the application must use accounts with the least privilege required, so that the account serving public pages cannot alter the schema, and it must use parameterised statements so that a value supplied by a visitor cannot become part of the statement text.

### 2.8 Security controls and what each one actually defends against

Security is not a product to be installed but a set of controls, each answering a specific failure. The mapping is the part examiners reward.

| Control | Defends against | What failure looks like without it |
|---|---|---|
| Least-privilege accounts | Privilege escalation after a compromise | A stolen web account can rewrite every file on the host |
| Strong authentication with MFA | Credential stuffing and password reuse | A leaked password from another site opens the administrative panel |
| Key-based SSH with password login disabled | Automated guessing against the shell | Thousands of login attempts per day, one of which succeeds |
| Hashing with a salted, slow algorithm | Offline cracking after a database theft | The whole user table is reversed in hours |
| Source code protection | Reconnaissance and code theft | Debug output, backups, and repository directories served as files |
| Stateful packet filter | Unrequested inbound connections | Database and cache ports reachable from the Internet |
| Web application firewall | Known injection and scanning patterns | Automated exploit traffic reaches the application |
| File integrity monitoring | Undetected modification of code | A backdoor survives for months in an unused file |
| Security headers | Content injection and framing attacks | Script from another origin executes in the visitor's session |
| Segmented network | Lateral movement from a compromised front end | The web server can reach the database with administrative rights |

**Access control** answers the question of who may do what. A discretionary model lets an owner grant rights; a mandatory model imposes labels that owners cannot override; a role-based model assigns permissions to roles and roles to people, which is the practical choice for a business because it makes review possible. Whatever the model, two rules apply: the default must be denial, and every grant must be reviewed, because permissions accumulate and are almost never removed.

**Authentication** answers the question of who is there. Three factor classes exist: something known, something held, and something inherent. Two factors from different classes constitute multi-factor authentication; two passwords do not. Passwords must be stored as salted hashes produced by a deliberately slow function such as Argon2id or bcrypt, never by a fast general-purpose hash and never in a form that can be reversed. Sessions must be bound to an unguessable identifier, marked HttpOnly and Secure, rotated at login, and destroyed at logout.

**Source code protection** is often reduced to "hide the code", but the real objective is to deny an attacker the information that shortens the path to a compromise. Concrete measures are: disable verbose error display in production and log details to a file that is not served; remove version banners from server responses; never leave a repository directory, an editor swap file, a database dump, or an environment file inside the document root; keep credentials in environment variables or a secrets store rather than in code; and never serve a directory listing. None of these makes the code secret in principle, but together they remove the accidental disclosures that turn a scanner into an intrusion.

**A firewall** is a filter on traffic, and the kinds differ in how much state they keep. A stateless packet filter examines each packet in isolation against rules about addresses, ports, and flags. A stateful firewall records the connections it has permitted and admits the returning traffic without a rule for it, which is what makes a default-deny inbound policy practical. An application-layer firewall parses the request itself and can reject a pattern that a packet filter cannot see; the common open-source form is a rule set attached to the web server, and the commercial form is a managed reverse proxy. A host-based firewall protects one machine; a network firewall protects a segment. The correct posture is default deny inbound, explicit permits only for ports that must be public, and restricted outbound traffic so that a compromised application cannot easily reach its controller.

### 2.9 The three backup strategies and exactly how they differ

A backup strategy is defined by one question: against what reference point is the change measured?

A **full backup** copies every selected file or every database object, regardless of whether it has changed. It is self-contained: it can be restored alone. It is also the largest and the slowest, and it places the greatest load on the source system.

A **differential backup** copies every file that has changed since the most recent full backup. It is measured against the full, not against the previous differential, so each successive differential contains everything changed since that full and therefore grows with each day that passes. Restoring requires the full and the most recent differential only.

An **incremental backup** copies every file that has changed since the most recent backup of any kind. It is measured against the previous run, so each set is small and quick, and it never grows while the schedule continues. Restoring requires the full and then every incremental in the order they were taken, because each set contains only the delta from its immediate predecessor.

| Property | Full | Differential | Incremental |
|---|---|---|---|
| Reference point | None; everything is copied | The last full | The last backup of any type |
| Size of each set | Largest | Grows until the next full | Smallest |
| Time to create | Longest | Moderate and rising | Shortest |
| Sets needed to restore | One | Two | The full plus every incremental |
| Restore time | Moderate | Moderate | Longest, because every set is applied |
| Risk in the chain | None | The single differential must be intact | Any missing set breaks the restore beyond that point |
| Typical schedule | Weekly | Daily, with a weekly full | Hourly or daily, with a weekly full |

The trade is therefore between the cost of creating backups and the cost of restoring them. Incremental sets are cheap to make and expensive to restore; differential sets are the reverse; a full set is expensive at both ends but has no chain to break. Real policies combine them, which is why the term **synthetic full** exists: a provider periodically assembles a new full image from the existing full plus its incrementals, so that the chain is shortened without another complete read of the source.

Two further distinctions prevent common mistakes. A **snapshot** taken by a storage system is not automatically a backup: if it lives on the same array as the data and is deleted with it, it protects against logical error but not against the loss of the array. A **replica** is not a backup either: replication copies a deletion or an encryption as faithfully as it copies a legitimate change, which is why ransomware that reaches a primary database also reaches its synchronous standby. A copy is only a backup when it is independent, retained, and restorable.

### 2.10 Recovery objectives and backup policy

Two numbers govern every design decision, and they are set by the business rather than by the technologist.

The **recovery point objective** is the greatest amount of data, measured in time, that the business will accept losing. A daily backup at two in the morning gives an RPO of up to twenty-four hours, because a failure at one in the morning loses almost a full day. The objective dictates the frequency: an RPO of fifteen minutes requires transaction log shipping or continuous archiving, not a nightly dump.

The **recovery time objective** is the greatest elapsed time from failure to restored service. It dictates the restore method: a full restore from object storage may take hours, a warm standby may take minutes, and a hot site with synchronous replication may take seconds. The two objectives are independent, and a plan that satisfies one may fail the other; a nightly full backup meets a one-hour RPO only if the failure happens just after the job finishes.

Around those two numbers a policy is built from four further decisions. **Retention** defines how many sets are kept and for how long, usually in a grandfather-father-son rotation that keeps dailies for a fortnight, weeklies for a quarter, and monthlies for a year or more. **Location** follows the rule of three copies on two media with one off-site, extended in current practice by one copy offline or immutable and zero errors found on verification. **Immutability** matters because ransomware routinely deletes or encrypts reachable backups; object storage with a retention lock, or a tape on a shelf, is the answer. **Encryption** protects the copies in transit and at rest, and the key must be held separately from the backup, or the encryption protects nothing against an attacker who takes both.
## 3. Methods and Operations

### 3.1 The registration workflow, step by step

Registration looks like a shopping transaction but is really a sequence of checks on a shared namespace. Following the sequence makes clear why each step exists.

Step 1. **Decide the name and the extension.** The extension is chosen for the audience rather than for search ranking: a country code places the business in a jurisdiction, a generic extension signals the kind of organisation, and a sponsored extension may carry eligibility rules that must be satisfied and may later be audited. A name should be short, unambiguous when spoken aloud, free of hyphens where possible, and free of trademarks held by others.

Step 2. **Check availability at the authoritative source.** A registrar's search box is convenient but is a query against its own stock and the registry; the authoritative answer is the registry's response to a create attempt, because availability can change between the search and the purchase. A name that is registered but expired may be in the redemption period, in which case it is not available at the ordinary price.

Step 3. **Choose a registrar and read the renewal terms.** Accreditation means the registrar has a provisioning agreement with the registry. The price that matters is the renewal price, not the first-year promotion, and the terms that matter are the transfer policy, the grace period after expiry, and whether the registration record is published with privacy protection.

Step 4. **Supply the registrant record accurately.** The registry requires a registrant name, an organisation where applicable, a postal address, and a reachable administrative and technical record. Accuracy is a contractual obligation, and an unreachable registrant record is the reason many names are lost at renewal. Where a privacy service is used, the service's records are published in place of the registrant's, but the registrar still holds the real ones and the registrant remains responsible for their accuracy.

Step 5. **Place the order and complete validation.** Some extensions require documentary evidence of eligibility, and some jurisdictions require local presence. Until validation completes, the name may exist in a pending state without delegation.

Step 6. **The registrar submits the create command.** The registrar sends an EPP create for the domain object, naming the initial nameservers and the registrant records. The registry either accepts and returns a transaction identifier or refuses with a result code that states the reason, for example that the name is already registered or that a required contact object is missing.

Step 7. **The registry writes the delegation.** The name appears in the TLD zone with the NS record set supplied, and only then does it begin to resolve. Between the create and the appearance of the delegation there is a short interval during which the name is registered but not yet visible.

Step 8. **Publish the zone at the DNS provider.** The authoritative servers must already hold the zone, or must create it on first query, with at least the apex address records, the mail exchanger, and the policy records. The delegation and the zone are configured in two different places, and this is where most new sites go wrong: the nameservers are correct at the registrar, but the zone at the provider is empty, so every query returns NXDOMAIN.

Step 9. **Verify from outside.** A query against the authoritative server proves that the zone is correct; a query through a recursive resolver proves that the delegation is visible. Both are necessary, and the second lags the first by the TTL of the parent's NS record.

Step 10. **Apply the locks and the renewal policy.** A transfer lock prevents an attacker who obtains the registrar credentials from moving the name; registry lock, where offered, requires out-of-band confirmation for any change; automatic renewal with a stored payment method prevents the commonest cause of a lost name, which is a lapsed card.

### 3.2 Changing delegation without an outage

Nameservers are changed at the registrar, and the change is a single EPP update, but the timing requires planning because the parent's NS record set is cached for its own TTL.

The safe procedure is to lower the TTL on the existing NS record set to a small value, typically five minutes, at least one old TTL period before the change; to create the zone at the new provider with every record copied and verified, including the mail records and any verification text records; to test the new servers directly by querying them by address rather than through a resolver; to make the change at the registrar; and to wait for the old TTL to expire before removing the old zone. The order matters because the two providers must both be able to answer during the overlap. Removing the old zone first produces a window in which queries reach servers that no longer hold the data.

A common variation is to keep the registrar's own nameservers and change only the records inside the zone. That avoids the delegation change entirely and takes effect within the record TTL, which is why registrars that bundle DNS service are popular for small sites. The trade is that the registrar's DNS service becomes a dependency for the whole estate, including mail.

### 3.3 Choosing and provisioning a host

Selection begins from measurements rather than from adjectives. Three estimates are enough to narrow the market.

The first is storage: the size of the application and its dependencies, plus the current database, plus the growth of uploads over the intended lifetime, plus room for logs and for a temporary copy during upgrades and backups. A site whose database is 4 GB today and grows by 1 GB a month needs a plan that will hold roughly 16 GB by the end of a year, not a plan that holds 5 GB.

The second is transfer: the average page weight multiplied by the monthly page views, plus the same for media that is downloaded rather than viewed. A page averaging 1.5 MB viewed 40,000 times a month consumes about 60 GB, which already exceeds a small shared plan's allowance once the media and the API traffic are added. This is the figure that most often forces an upgrade.

The third is concurrency: the number of simultaneous requests at the busiest minute, multiplied by the average time each request holds a worker. A site that serves ten requests per second with each taking a fifth of a second needs two workers at steady state and several times that for a burst; a plan that permits a small fixed number of concurrent entry processes will queue the rest.

Once the model is chosen, provisioning is a fixed sequence: install the operating system at a supported version, create a non-root administrative account with a key, disable password authentication for the shell, apply all updates, set the time zone and the clock synchronisation, configure the host name, add a default-deny packet filter with only the public ports open, install the runtime and the database from the distribution's packages, create a per-site account and a per-site database account with restricted rights, and only then deploy the application. Each step is small and each is easier to do at the beginning than to retrofit. The order also matters: hardening before the application is deployed means the application never runs in a permissive environment.

### 3.4 Issuing and installing a certificate

Certificate issuance has three inputs: a name to be certified, proof that the applicant controls that name, and a signature from an authority the client trusts. The proof is the interesting part.

**HTTP-01** places a token at a well-known path on port 80 and asks the authority to fetch it. It is simple, works with any web server, and fails if port 80 is closed or if the name resolves elsewhere. **DNS-01** places a token in a text record under a dedicated name and asks the authority to query it. It works when port 80 is unavailable, and it is the only method that can certify a wildcard, because a wildcard covers names that do not exist and therefore cannot answer an HTTP challenge. **TLS-ALPN-01** performs the proof inside a special TLS handshake on port 443.

Renewal is where operational discipline shows. A certificate that is issued manually will eventually be forgotten, and the failure appears as a browser warning or as a hard failure in an application that verifies the chain. Automation renews well before expiry, reloads the server gracefully, and alerts on failure. The renewal window should be judged against the certificate lifetime: a ninety-day certificate renewed at sixty days leaves a month of retries, while a one-year certificate renewed at thirty days leaves a month as well but concentrates the risk.

Installation is a server configuration problem, and the two decisions are protocol versions and cipher policy. Only TLS 1.2 and TLS 1.3 should be enabled, with a cipher list that prefers forward secrecy, and the certificate file must contain the server certificate followed by the intermediate chain. A missing intermediate is the single commonest cause of "it works in one browser and not another", because some clients cache intermediates and others do not.

### 3.5 Hardening the running host

Hardening is a checklist of removals and restrictions, applied in a fixed order.

Remove what is not needed: unused packages, sample applications, default accounts, and any service that listens on a public interface without a reason. Restrict what remains: the shell accepts keys only, the administrative account is not root, the database listens on the loopback interface unless a separate host must reach it, and the application runs as an unprivileged user whose home directory is not inside the document root.

Set file permissions by intention rather than by convenience. Application files are owned by the deployment account and readable by the web server, uploaded media is writable only by the account that must write it, configuration files containing credentials are readable only by their owner, and no directory inside the document root is executable or listable. A permission of full access for everyone is not a shortcut but a permanent vulnerability.

Then apply the application-level controls: parameterised statements for every query, output encoding for every value rendered into a page, a content security policy that names the origins allowed to supply script, and a web application firewall rule set in front of the application. These defend against classes of input that the operating system cannot distinguish from legitimate traffic.

Finally, arrange to notice change. File integrity monitoring over the application directory, a log of authentication successes and failures shipped off the host, and an alert on a new listening socket together catch the moment a compromise becomes visible rather than months later.

### 3.6 Constructing the backup jobs

A backup job has five parameters: what is selected, how it is captured consistently, where it is written, how it is verified, and when it is forgotten.

Selection is by explicit list rather than by exclusion, because exclusion lists silently miss new directories. Consistency is the hard part for a database: copying the files of a running database produces a set that is torn across transactions and will not open cleanly. The supported method is the database's own dump utility, run in a mode that takes a consistent snapshot, or a filesystem snapshot taken after the database has been quiesced.

Destination must be a different failure domain from the source. A second directory on the same disk is not a backup; a second machine in the same rack protects against a disk failure but not against a fire; object storage in another region protects against both and is the practical default. Verification should be automatic: a checksum recorded with each set, a manifest of the file count and total size, and a periodic restore into a scratch environment.

Forgetting is a policy, not an afterthought. Retention is expressed as a schedule with a defined number of hourly, daily, weekly, and monthly sets, and the deletion job must be tested as carefully as the creation job, because a retention rule with an off-by-one error deletes the set that was needed.

### 3.7 The restore runbook

A restore is a procedure performed under pressure, so it must be written down before it is needed and rehearsed while nothing is wrong.

The runbook states, in order: how to declare an incident and who may authorise a restore; how to stop writes to the affected system so that the restored copy is not immediately overwritten; how to identify the target recovery point from the incident time; which sets must be applied and in what order; how to verify the restored data against the manifest and against business invariants such as the count of orders in the last hour; how to repoint traffic to the restored system; and how to reconcile any transactions that arrived after the recovery point, which is the step most often omitted and the one that determines whether customers see a duplicated or a missing order.

The runbook also records the measured time of the last rehearsal. An RTO that has never been measured is an aspiration, not an objective.

### 3.8 Monitoring, drills, and the record of what happened

Four monitors cover the failures that matter. A name monitor queries the authoritative servers for the apex address and the mail exchanger. A transport monitor connects and completes a handshake, and reports the days remaining on the certificate. An application monitor requests a page that exercises the database and checks for a known marker in the response. A backup monitor checks that the most recent set exists, that its checksum matches, and that its size is within the expected band, because a backup job that quietly produced a truncated file is worse than one that failed loudly.

Drills turn a plan into a capability. A quarterly restore of one database into a scratch environment proves the procedure; an annual full exercise that restores the whole estate and repoints a staging name proves the runbook; a tabletop discussion of a lost provider proves the decision-making. Each drill is recorded with the time taken and the problems found, and the runbook is amended afterwards.

## 4. Worked Implementation from the Notes

### 4.1 Task: trace the delegation chain for a name that is about to be deployed

### 4.2 Implementation: query each link explicitly

Step 1. Ask the local resolver what it knows. The first query establishes the baseline: whether the name resolves at all for this machine.

```bash
dig +short example.com A
```

Observed output:

```text
203.0.113.10
```

The answer proves only that some resolver returned an address. It says nothing about which server is authoritative, so it cannot distinguish a stale cached answer from a fresh one.

Step 2. Query the authoritative servers directly, bypassing caches.

```bash
dig +short example.com NS
```

Observed output:

```text
ns1.example-dns.net.
ns2.example-dns.net.
```

Step 3. Ask one of those servers for the same record and check the flags in the response.

```bash
dig @ns1.example-dns.net example.com A
```

Observed output:

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41287
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; ANSWER SECTION:
example.com.            300     IN      A       203.0.113.10
```

The `aa` flag means authoritative answer: this server holds the zone. The TTL of 300 means the answer may be cached for five minutes. A reply from this server without `aa` would indicate a misconfiguration, because the delegation names it as authoritative.

Step 4. Walk the chain from the root to see the referrals, which is what proves the delegation rather than merely the zone contents.

```bash
dig +trace example.com A
```

Observed output, condensed to the delegation lines:

```text
.                       518400  IN      NS      a.root-servers.net.
com.                    172800  IN      NS      a.gtld-servers.net.
example.com.            172800  IN      NS      ns1.example-dns.net.
example.com.            172800  IN      NS      ns2.example-dns.net.
example.com.            300     IN      A       203.0.113.10
```

Step 5. Interpret the result. The TTL of the delegation, 172800 seconds or two days, belongs to the parent zone and is not the TTL that governs ordinary answers. Lowering the record TTL at the DNS provider therefore does not shorten the time a delegation change takes to become visible; only the parent-side NS TTL does that. This is exactly why a migration plan lowers the NS TTL at the registrar a full old-TTL period in advance.

### 4.3 Task: serve two names from one address with SNI

### 4.4 Implementation: one listener, two certificates, verified with a name-aware client

Step 1. Obtain two certificates, one for each name, and place the full chain with each.

```bash
sudo certbot certonly --webroot -w /var/www/html -d shop.example.com
sudo certbot certonly --webroot -w /var/www/html -d www.example.com
```

Each invocation completes an HTTP-01 challenge by writing a token under the web root and asking the authority to fetch it. The certificate is written to a directory named after the first requested name.

Step 2. Configure a single listener with two server blocks, each naming its own certificate. The server chooses the block by the name the client sends in the handshake.

```nginx
server {
    listen 443 ssl;
    server_name shop.example.com;

    ssl_certificate     /etc/letsencrypt/live/shop.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/shop.example.com/privkey.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;
    ssl_session_cache   shared:SSL:10m;
    resolver            1.1.1.1 valid=300s;
    resolver_timeout    5s;
    ssl_stapling        on;
    ssl_stapling_verify on;

    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Content-Type-Options "nosniff" always;

    root  /var/www/shop;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
}

server {
    listen 443 ssl;
    server_name www.example.com;

    ssl_certificate     /etc/letsencrypt/live/www.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.example.com/privkey.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    return 301 https://shop.example.com$request_uri;
}
```

Step 3. Test the configuration and reload without dropping connections.

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Observed output:

```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Step 4. Prove that name selection works by asking for each name explicitly and reading the certificate subject.

```bash
echo | openssl s_client -connect 203.0.113.10:443 -servername shop.example.com 2>/dev/null | openssl x509 -noout -subject -dates
```

Observed output:

```text
subject=CN = shop.example.com
notBefore=Nov  1 09:12:00 2026 GMT
notAfter=Jan 30 09:11:59 2027 GMT
```

Repeating the command with `-servername www.example.com` returns the other subject. The address never changed, which is the demonstration: two certificates are served from one address because the client stated the name, and the dedicated address is not needed for this to work.

Step 5. Verify the application sees the right host and that plain requests are redirected.

```bash
curl -I http://shop.example.com/
```

Observed output:

```text
HTTP/1.1 301 Moved Permanently
Server: nginx
Location: https://shop.example.com/
```

A 301 rather than a 302 is correct here because the canonical scheme is permanent; a temporary code would invite clients to retry the plain scheme.

### 4.5 Task: run a full-plus-differential schedule with a written policy

### 4.6 Implementation: one script, one policy file, one verification step

Step 1. State the policy in a machine-readable file so that the schedule is reviewable rather than buried in a crontab.

```yaml
backup_policy:
  name: shop-daily
  source:
    database: shop
    files: /var/www/shop
    config: /etc/nginx
  schedule:
    full: "Sun 02:00"
    differential: "Mon-Sat 02:00"
    transaction_log: "continuous"
  retention:
    daily: 14
    weekly: 8
    monthly: 12
  objectives:
    rpo_minutes: 15
    rto_minutes: 120
  destination:
    primary: /srv/backup
    offsite: s3://shop-backups-eu
    immutable_days: 30
  verification:
    checksum: sha256
    restore_test: quarterly
```

Step 2. Write the job so that the difference between the two set types is explicit. The full copies everything and records a marker; the differential copies only what changed since that marker.

```bash
#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M)"
KIND="${1:-differential}"
ROOT="/srv/backup"
MARKER="$ROOT/.last_full"
DEST="$ROOT/$KIND/$STAMP"

mkdir -p "$DEST"

if [ "$KIND" = "full" ]; then
    tar --create --gzip --file "$DEST/files.tar.gz" -C /var/www shop
    mysqldump --single-transaction --routines --triggers --events \
        --databases shop > "$DEST/shop.sql"
    date -u +%Y-%m-%dT%H:%M:%SZ > "$MARKER"
elif [ "$KIND" = "differential" ]; then
    tar --create --gzip --file "$DEST/files.tar.gz" \
        --newer-mtime="$(cat "$MARKER")" -C /var/www shop
    mysqldump --single-transaction --routines --triggers --events \
        --databases shop > "$DEST/shop.sql"
else
    echo "usage: $0 full|differential" >&2
    exit 64
fi

sha256sum "$DEST"/* > "$DEST/SHA256SUMS"
rsync -a --delete "$DEST" "backup@offsite.example.net:/srv/shop/$KIND/"
```

Step 3. Explain the critical lines. `--single-transaction` makes the dump consistent without locking the tables, which is what allows the site to keep serving during the job. `--newer-mtime` with the timestamp of the last full is what makes the file archive differential rather than incremental: the reference point is the full, so the archive grows each day until the next full replaces the marker. The database component is deliberately a complete logical dump in both kinds of set, because a dump is a script of statements with no partial form; the finer recovery point that a short objective demands comes from archiving the transaction log separately, not from a smaller dump. The checksum file is written after the data and copied with it, so a truncated archive is detected at restore time rather than assumed good.

Step 4. Schedule the two kinds, and confirm that the jobs are actually running.

```bash
crontab -l
```

Observed output:

```text
0 2 * * 0  /usr/local/bin/site-backup full
0 2 * * 1-6 /usr/local/bin/site-backup differential
```

Step 5. Verify the newest set independently of the job's own exit status.

```bash
ls -1 /srv/backup/differential | tail -n 3
sha256sum -c /srv/backup/differential/20261106-0200/SHA256SUMS
```

Observed output:

```text
20261104-0200
20261105-0200
20261106-0200
shop.sql: OK
files.tar.gz: OK
```

The second command is the one that matters: an exit status of zero from the backup job proves only that the commands ran, while a checksum comparison proves that the bytes on the destination are the bytes that were written.

### 4.7 Task: restore to a stated point and prove the result

### 4.8 Implementation: apply the sets in dependency order

Consider a week in which a full was taken on Sunday at 02:00 and differentials on Monday through Saturday at 02:00. The site is corrupted on Friday at 17:40, and the target recovery point is Friday at 02:00, immediately before the last good set, so the sets required are the full from Sunday and the differential from Friday morning, because the file archive in that differential contains everything changed since the Sunday full.

Step 1. Identify the sets from the manifest and stop writes.

```text
Recovery point requested : 2026-11-06 02:00 UTC
Full set                 : 2026-11-01 02:00  (files 4.1 GB, database 1.2 GB)
Differential set         : 2026-11-06 02:00  (files 380 MB, database 1.2 GB)
Sets required            : 2  -> full then differential
```

Step 2. Restore the full first, because the differential contains only changes and cannot be applied to an empty target.

```bash
tar --extract --gzip --file /srv/backup/full/20261101-0200/files.tar.gz -C /var/www
mysql < /srv/backup/full/20261101-0200/shop.sql
```

Step 3. Apply the differential over the restored full. The file archive layers over the extracted tree, and the Friday dump loads as a complete replacement for the Sunday dump, because a logical dump recreates its databases rather than appending to them.

```bash
tar --extract --gzip --file /srv/backup/differential/20261106-0200/files.tar.gz -C /var/www
mysql < /srv/backup/differential/20261106-0200/shop.sql
```

Step 4. Explain why two sets suffice here and would not suffice under an incremental schedule. Under the differential schedule every file archive after Sunday is measured against Sunday, so the newest one already contains Monday through Friday. Under an incremental schedule the sets would be measured against each other, and the restore would need Sunday's full plus Monday, Tuesday, Wednesday, Thursday, and Friday in that order, because Friday's set contains only Thursday night's changes. Applying them out of order, or skipping one, produces a database that opens but is missing a day's orders.

Step 5. Verify against business invariants rather than against a row count alone.

```sql
SELECT COUNT(*) AS orders_today
FROM orders
WHERE created_at >= '2026-11-05 00:00:00'
  AND created_at <  '2026-11-06 02:00:00';

SELECT MAX(id) AS last_order_id, MAX(created_at) AS last_order_at
FROM orders;
```

Observed output:

```text
orders_today
------------
412

last_order_id  last_order_at
-------------  -------------------
90417          2026-11-06 01:58:44
```

The maximum timestamp sits just before the backup window, which is what a correct restore of a set taken at 02:00 should show. A maximum timestamp of 17:39 on Friday would mean the restore had somehow included data past the recovery point and should be investigated before traffic is restored.

### 4.9 Task: accept a payment notification without trusting it

### 4.10 Implementation: verify the signature, then commit in one transaction

Step 1. Receive the raw body before any parsing, because the signature covers the exact bytes.

```python
import hashlib
import hmac
import json


def verify(raw_body: bytes, header_signature: str, secret: bytes) -> bool:
    expected = hmac.new(secret, raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header_signature)
```

Step 2. Explain the two defensive details. The comparison uses a constant-time function so that the time taken does not reveal how much of the guess was correct. The body is the raw bytes, not a re-serialised object, because a JSON round trip may reorder keys or change spacing and the digest would no longer match.

Step 3. Apply the state change and the ledger entry inside one transaction, after checking the amount against the stored order.

```sql
BEGIN;

SELECT id, total_cents, currency, status
FROM orders
WHERE reference = 'ORD-2026-1106-0042'
FOR UPDATE;

UPDATE orders
SET status = 'paid', paid_at = NOW()
WHERE reference = 'ORD-2026-1106-0042'
  AND status = 'pending';

INSERT INTO payments (order_reference, gateway_reference, amount_cents, currency, received_at)
VALUES ('ORD-2026-1106-0042', 'GW-88213', 12999, 'EUR', NOW());

COMMIT;
```

Step 4. Explain the correctness argument. The row lock prevents two concurrent notifications for the same order from both seeing a pending status. The `status = 'pending'` predicate makes the update idempotent: a duplicate delivery updates nothing, so the order is not paid twice. The insert and the update commit together, so a crash between them cannot leave a paid order with no payment record. Rejecting a notification whose amount or currency differs from the stored order is the control that stops a small-amount test payment from marking a large order as settled.

### 4.11 Task: reduce the exposed surface of the host

### 4.12 Implementation: keys only, default deny, then measure

Step 1. Restrict the shell to key authentication and to a named administrative account.

```ini
# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AllowUsers deploy
MaxAuthTries 3
ClientAliveInterval 300
```

Step 2. Reload and confirm the effective configuration rather than the file.

```bash
sudo sshd -t
sudo systemctl reload ssh
sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication|allowusers'
```

Observed output:

```text
permitrootlogin no
passwordauthentication no
allowusers deploy
```

Step 3. Apply a default-deny inbound policy with only the public service ports permitted.

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```

Observed output:

```text
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
```

Step 4. Confirm that nothing else is listening, since a firewall rule cannot protect a service that is bound to the public interface by accident.

```bash
sudo ss -tulpn
```

Observed output:

```text
Netid State  Local Address:Port   Process
tcp   LISTEN 0.0.0.0:22           sshd
tcp   LISTEN 0.0.0.0:80           nginx
tcp   LISTEN 0.0.0.0:443          nginx
tcp   LISTEN 127.0.0.1:3306       mysqld
```

Step 5. Interpret the result. The database listens only on the loopback address, so a packet arriving from the Internet cannot reach it even if a firewall rule were later loosened by mistake. That is defence in depth: two independent controls, either of which would be sufficient, which is the property to state in an answer rather than counting rules.
## 5. Testing, Interpretation, and Common Errors

### 5.1 Tests of understanding

- Trace one request from the browser's first query to the application's response, naming the record and the server involved at each hop.
- Explain why the registry zone contains only the delegation and the child zone contains everything else, and what breaks if the two are configured by different teams.
- Distinguish `clientHold` from `clientTransferProhibited` in terms of what a visitor experiences and what an administrator must do.
- State the four hosting models and identify the isolation boundary of each in one word.
- Convert an uptime figure of 99.95 per cent into annual downtime and explain why the experienced figure is usually worse than the contractual one.
- Explain why a dedicated address is not required for TLS with SNI, and give two reasons it is still requested.
- Name three integration models for a payment gateway and say which one removes card data from the merchant's compliance scope.
- Match five security controls to the specific failure each prevents, without using the word "hacker".
- Define full, differential, and incremental backups in terms of their reference points, then state the sets required to restore each.
- Given a full on Sunday and differentials on Monday to Saturday, list the sets needed to recover Friday's state and explain why the answer differs under an incremental schedule.
- Distinguish an RPO from an RTO and give one design change that improves each.
- Explain why a synchronous replica is not a backup.

### 5.2 Interpreting evidence correctly

Evidence has a hierarchy, and the weaker forms are constantly mistaken for the stronger. An exit status of zero from a backup job proves that the commands completed, not that the archive is usable; only a checksum comparison, and then a restore, proves usability. A successful name lookup proves that some resolver returned an answer, not that the delegation is correct; only a query against the authoritative server with the `aa` flag set proves that. A green monitor proves that one URL returned a successful status, not that the database behind it is consistent; a monitor that requests a page exercising a query and checking a known value proves much more.

The same discipline applies to certificates. A browser padlock proves that the certificate chains to a trusted root and matches the name; it does not prove that the organisation is trustworthy, and it does not prove that the site is free of vulnerabilities. A certificate expiry warning proves that the automated renewal did not run, which is an operational failure rather than a security one, although the visitors experience it as both.

Timing evidence needs care as well. A restore that took ninety minutes in a drill is the only defensible basis for an RTO, because the figure includes the time to notice, to decide, to find the sets, and to verify. A plan that quotes the time taken by the copy command alone is quoting the smallest component of the outage.

### 5.3 Symptom to cause

| Symptom | Likely cause | Check |
|---|---|---|
| Name resolves for some users and not others | Delegation recently changed, old TTL still cached | Query the authoritative servers directly and compare with the resolver |
| NXDOMAIN from every resolver | Zone missing at the provider, or wrong zone published | Query the authoritative server by address for the apex |
| SERVFAIL instead of NXDOMAIN | Lame delegation, or DNSSEC validation failure | Check the NS set, then check the DS record and the signature dates |
| Name stopped resolving without any change | Registry or registrar hold applied | Read the domain status in the registration record |
| Browser warns about a name mismatch | Certificate issued for another name, or SNI not sent by the client | Read the certificate subject and the requested name |
| Padlock appears in one browser and not another | Intermediate certificate missing from the chain | Fetch the chain with a client and count the certificates |
| Site loads over HTTP but not HTTPS | Listener not configured for 443, or packet filter blocks it | Test the port, then read the server configuration |
| Payment notification arrives but the order stays pending | Signature verification rejecting a re-serialised body | Compare the digest over the raw bytes |
| Order marked paid twice | Update not guarded by a status predicate | Inspect the statement and the transaction boundary |
| Site slow at peak but idle otherwise | Worker or connection limit reached | Measure concurrent requests and queue depth |
| Backup job succeeds but restore fails | Torn database copy or truncated archive | Restore into a scratch instance and open the dump |
| Backup sets missing for the last three nights | Retention rule deleting more than intended | List the destination and read the deletion job |
| Whole site lost after a provider failure | Copies stored only inside the provider's account | Check that at least one copy is in a different account and region |
| Restored data is a day older than expected | Recovery point not aligned with the stated RPO | Compare the backup window with the failure time |

### 5.4 Common errors in rigorous answers

- **Treating the registrar as the DNS host.** The registrar controls the delegation; the DNS provider controls the records inside the zone. An answer that merges them cannot explain why a correct nameserver change still yields NXDOMAIN.
- **Saying DNS propagates.** Records do not propagate; they are cached for a TTL. The word suggests a push, and it hides the fact that the delay is bounded by a number that can be read and lowered in advance.
- **Quoting a single availability figure without its period.** "99.99 per cent" means nothing until it is expressed per year or per month, and the conversion is a standard examination task.
- **Claiming a dedicated address is required for TLS.** SNI removed that requirement for modern clients; the honest answer states the legacy and commercial reasons the address is still requested.
- **Describing shared hosting as secure because each customer has a login.** A user account is a permission boundary inside one kernel, not an isolation boundary between kernels.
- **Confusing differential with incremental.** The differential is measured against the last full and grows; the incremental is measured against the last backup of any kind and does not. Every restore question turns on this distinction.
- **Saying a full backup is unnecessary if incrementals are frequent.** Without a full there is nothing to apply the deltas to, and without periodic new fulls the chain becomes long enough that the restore time breaches the RTO.
- **Treating replication as a backup.** Replication reproduces deletion and encryption as faithfully as it reproduces legitimate change.
- **Assuming a firewall makes an application secure.** A firewall filters addresses and ports; an injection attack arrives on an open port and is indistinguishable from legitimate traffic without request inspection.
- **Believing HTTPS protects data at rest.** TLS protects the connection. The database, the backups, and the logs each need their own protection.
- **Storing hashed passwords with a fast hash.** Speed is the defect: a general-purpose digest allows billions of guesses per second on commodity hardware.
- **Describing a restore without naming the order of sets.** The order is the substance of the answer; a list of set types without a sequence earns little credit.
- **Forgetting that the backup itself must be protected.** A readable backup of a customer database is a second copy of the breach, and a deletable backup is no defence against ransomware.

### 5.5 Trade-offs to state in a conclusion

Every choice in this topic buys one property by spending another, and a conclusion that names the exchange is stronger than a list of features. Shared hosting buys cost and spends isolation; a VPS buys isolation and spends administrative effort; a dedicated machine buys predictability and spends money; colocation buys control and spends responsibility for hardware.

SNI buys address economy and spends compatibility with clients that predate it, which is why the dedicated address survives as a commercial requirement rather than a technical one. A hosted payment page buys the smallest compliance scope and spends control over the checkout experience; a server-to-server integration buys control and spends the heaviest validation burden. A web application firewall buys protection against known patterns and spends latency and the risk of blocking legitimate input.

Full backups buy independence and spend time and storage; differential backups buy a short restore and spend growing daily volume; incremental backups buy cheap creation and spend a long, fragile chain. A short RPO buys tolerance of loss and spends continuous log shipping; a short RTO buys fast recovery and spends the cost of a warm or hot standby. The defensible conclusion states the business requirement first, chooses the mechanism that meets it, and says plainly what the choice costs.


