## 1. Concept and Use Case

### 1.1 What the examiner is actually testing

Every question on this topic is testing one of four things, and recognising which one is being asked determines the shape of the answer.

The first is **mechanism**: can you narrate a resolution from the client to the authoritative server in the correct order, naming the role of each server and the kind of response it returns? This is the most frequently set question and the easiest to lose marks on by skipping a tier or by reversing the direction of recursion and iteration.

The second is **structure**: can you place a name correctly in the hierarchy, distinguish a domain from a zone, and explain how delegation transfers authority? Questions of this kind are usually worth fewer marks each but more marks in total, because they appear as short definition items.

The third is **data**: do you know what each record type means, what its data looks like, and what constraint applies to it? This is where precise phrasing earns marks and vague phrasing does not.

The fourth is **failure and defence**: can you explain why the protocol is attackable and what each defence actually achieves? This question rewards a causal chain rather than a list of acronyms.

A candidate who identifies the category in the first ten seconds of reading the question can plan the answer before writing, which is the single largest source of mark improvement in this topic.

### 1.2 The definition that earns the first marks

A compact definition that scores reliably is: the Domain Name System, abbreviated DNS, is a distributed, hierarchical database, accessed by a query and response protocol, that maps human-readable domain names to the resource records associated with them, most commonly Internet Protocol addresses.

Four components of that sentence carry marks, and each should be present.

"Distributed" states that no single server holds the data, which is the property that allows the system to scale. "Hierarchical" states that the name space is a tree, which is the property that allows delegation. "Database with a query protocol" states that it is data plus an access method, not merely a lookup table. "Resource records, most commonly addresses" states the general case rather than the narrow one, which distinguishes a strong answer from a weak one that says only that DNS converts names to addresses.

A one-mark item usually asks for the expansion of the acronym and a purpose in a sentence. A three-mark item usually wants the definition plus one consequence, for example that names can be changed without changing client software.

### 1.3 Why the topic recurs in every paper

The topic is examined repeatedly because it demonstrates four general principles that the syllabus tests elsewhere, so a question on DNS doubles as a question on those principles.

**Indirection decouples a name from a location.** A service can move without any client being reconfigured, because the binding is looked up at the moment of use. The same principle underlies virtual hosting, content delivery and load balancing.

**Hierarchical delegation bounds the work of any one authority.** A registry does not need to know what a customer does inside their domain, only which servers answer for it. The same principle underlies file system directories and organisational structures.

**Caching with expiry trades freshness for speed.** Every cache in the system holds data with a countdown attached, which is a general pattern for distributed data.

**Trust without authentication is fragile.** The protocol accepts answers that match a query, and every security mechanism added later is an attempt to supply the missing proof. The same reasoning applies to any protocol designed before adversaries were modelled.

An answer that names these principles, even briefly, reads as understanding rather than recall, and examiners reward that distinction where a question carries a discussion mark.

### 1.4 The four question shapes you will meet

Almost every question on this topic can be classified into one of the shapes below. Knowing the shape tells you the structure of the answer before you write a word.

**Shape one: narrate the resolution.** "Describe how the domain name www.example.com is resolved to an Internet Protocol address." Typically eight to twelve marks. The answer is a numbered sequence of servers and responses, with the role of each server named and the direction of the query stated.

**Shape two: compare and define.** "Compare recursive and iterative queries." Or "Distinguish a domain from a zone." Typically four to six marks. The answer is a table or a set of paired sentences, with one mark per genuine difference.

**Shape three: data and constraints.** "Name four record types and state the purpose of each." Or "Explain why a canonical name record cannot be placed at the zone apex." Typically four to eight marks. The answer is precise per item, with the constraint stated as a consequence rather than as a rule to memorise.

**Shape four: failure and defence.** "Explain cache poisoning and describe two defences." Typically six to eight marks. The answer is an attack chain, then a defence per mark with the mechanism stated.

A fifth shape appears occasionally and combines the four: a scenario is described, a symptom is given, and the candidate must diagnose it. That shape is covered by the diagnostic procedure in Section 3 and the trap table in Section 5.

### 1.5 Terminology that must be used exactly

Marks are awarded for the correct term used in the correct place, and marks are lost where a term is used loosely. The following distinctions are the ones that examiners deliberately probe.

A **domain** is a node in the name tree together with everything below it. A **zone** is the portion of the tree for which one set of servers holds authoritative data. Every zone is a domain, but not every domain is a zone, because a delegation creates a boundary.

A **recursive** query asks a server to complete the work. An **iterative** query asks a server for its best answer, which is frequently a referral. The client recurses; the resolver iterates.

An **authoritative** answer comes from a server that holds the zone. A **cached** answer comes from a server that remembers what an authoritative server said. The authoritative flag distinguishes them in a response.

A **referral** is an empty answer with delegation records in the authority section. A **negative answer** is an empty answer with the zone's start-of-authority record in the authority section. Both have zero answers and neither is an error.

A **name error** means the name does not exist. **No data** means the name exists but has no record of the requested type. Both are cached, and they are cached differently in interpretation though identically in mechanism.

## 2. Data, Syntax, and Core Concepts

### 2.1 The name space: facts with mark values

The hierarchy has four examinable layers. For each, be able to name an example, say who controls it, and say what it stores.

| Layer | Example | Controlled by | Stores | Typical mark |
|---|---|---|---|---|
| Root | the trailing dot, written as a single dot | Root server operators, coordinated globally | Delegations to every top-level domain | 1 |
| Generic top-level domain, gTLD | com, org, net, app | The registry for that TLD | Delegations to registered domains | 1 |
| Country-code top-level domain, ccTLD | ke, uk, de, jp | The national registry | Delegations, under national policy | 1 |
| Second-level domain | example.com | The registrant, through a registrar | The organisation's records | 2 |
| Subdomain | www.example.com | The registrant alone | Records for one host, service or tenant | 2 |

Four quantitative facts are commonly worth a mark each: a label may be at most 63 octets; a complete name in wire format may be at most 255 octets; comparison is case-insensitive; a trailing dot marks a fully qualified name.

The statement most often required in a two-mark item is that delegation is what allows the name space to grow without a central bottleneck, because authority for a subtree is transferred to its owner, who can then create names without further approval.

### 2.2 The server hierarchy: facts with mark values

| Role | Receives | Returns | Holds | Mark |
|---|---|---|---|---|
| Stub resolver | The application's request | A query to the recursive resolver | No zone data | 1 |
| Recursive resolver | A recursive query | The final answer, after iterating | A cache of everything it learns | 2 |
| Root name server | An iterative query | A referral to the relevant top-level domain | The root zone only | 2 |
| Top-level domain name server | An iterative query | A referral to the authoritative servers | Delegations for its TLD | 2 |
| Authoritative name server | An iterative query | The record, with the authoritative flag | The zone itself | 2 |

Two facts about the root must be stated correctly, because a common wrong answer is heavily penalised.

There are **13 logical root server identities**, named with the letters a to m. Each identity is served by many physical machines in many countries through **anycast**, a routing arrangement in which one address is announced from several locations and each query reaches the nearest. The root is therefore not 13 machines, and any answer implying that is wrong.

The root zone holds **no host addresses for ordinary domains**. It holds delegations, so every uncached lookup begins with a referral rather than an answer.

Two facts about authoritative service are worth a mark each: a zone must publish at least two name server records, and multiple authoritative servers are kept consistent by a serial number in the start-of-authority record, with secondaries transferring the zone when the serial increases.

### 2.3 Record types: the table to memorise

| Type | Purpose | Example data | Constraint that earns an extra mark |
|---|---|---|---|
| A | Maps a name to an Internet Protocol version 4 address | 192.0.2.10 | Several may exist at one name |
| AAAA | Maps a name to an Internet Protocol version 6 address | 2001:db8:1::50 | Independent of the A record |
| CNAME | Declares a name to be an alias for another name | example.com | Cannot coexist with any other record at that name; not permitted at the apex |
| MX | Names the mail servers for a domain, with preference | 10 mail1.example.com | Target must have an address record, not be an alias |
| NS | Names the servers authoritative for a zone | ns1.example.com | Required at every apex; the parent's copy governs |
| PTR | Maps an address back to a name | 10.2.0.192.in-addr.arpa | Lives only in the reverse zones under in-addr.arpa or ip6.arpa |
| TXT | Carries arbitrary text for policy and verification | "v=spf1 mx -all" | Multiple strings are concatenated by consumers |

Three sentence patterns score reliably and should be rehearsed.

For a canonical name: "A CNAME record states that the queried name is an alias, so resolution continues at the target name; because of that redirection, no other record may exist at the alias name, since it could never be reached."

For a mail exchanger: "An MX record gives a preference value and a host name; the lowest preference is tried first, and the target must resolve to an address rather than to an alias, because mail routing does not follow aliases."

For a pointer: "A PTR record answers the reverse question and exists in a separate branch of the name space in which the octets of the address are reversed, so that the most specific part of the address is the leftmost label."

### 2.4 Transport and port facts

| Fact | Value | Why it is examined |
|---|---|---|
| DNS port | 53, for both transports | A frequent one-mark recall item |
| Default transport | UDP on port 53 | No handshake, one datagram each way, retry on timeout |
| Reliable transport | TCP on port 53 | Used for truncated responses and zone transfers |
| Truncation signal | The TC flag in the header | Triggers a retry over TCP |
| Original UDP limit | 512 octets | The reason truncation exists |
| Extended UDP size | Commonly 1,232 octets, up to 4,096 | Avoids fragmentation on typical paths |
| Encrypted transport, TLS | Port 853 | Hides the query, does not authenticate the data |
| Encrypted transport, HTTPS | Port 443 | Same effect, blended with web traffic |

The sentence to write when a question asks about port numbers is: "DNS uses port 53 for both UDP and TCP; UDP carries ordinary queries because a single request and response fit in one datagram, while TCP carries responses that exceed the advertised datagram size and is also used for zone transfers."

### 2.5 Header fields worth naming

A question that asks you to describe the message format needs the header fields that carry meaning, not all twelve octets.

| Field | Meaning | One-line significance |
|---|---|---|
| Identifier | 16-bit value chosen by the client and echoed by the server | The primary defence against a mismatched reply |
| QR | Query or response | Distinguishes the two directions |
| AA | Authoritative answer | Separates an authoritative answer from a cached one |
| TC | Truncated | Requests a retry over TCP |
| RD | Recursion desired | Set by the client to ask for the full job |
| RA | Recursion available | Set by a resolver, absent at root and authoritative servers |
| AD | Authenticated data | Set when signature validation succeeded |
| RCODE | Result code | Zero success, two server failure, three name error, five refused |

The four sections carry the payload: the question repeats what was asked, the answer holds records that answer it, the authority holds records describing the zone, and the additional section holds records expected to be useful next, chiefly glue.

### 2.6 Caching: layers, lifetimes and negative entries

| Level | Typical holder | Governed by | Cleared by |
|---|---|---|---|
| Browser | The browser process | Its own policy, often capped below the record lifetime | The browser's network page |
| Operating system | The system resolver cache | The record lifetime | The platform flush command |
| Router | The gateway device | The record lifetime | Restart of the device or its service |
| Resolver | The provider or enterprise resolver | The record lifetime | Operator action or expiry |

The examinable statements about caching are these.

A record's time to live, abbreviated TTL, is the maximum period for which a cache may keep it. The value counts down in the cache and is displayed as the remaining value, not the published value. A cache may discard sooner but may never retain longer.

Negative answers are cached too. The negative lifetime is the smaller of the start-of-authority record's own lifetime and the final value in that record's data. This is why a name queried before it is created can appear not to exist for a period afterwards.

A long lifetime reduces load and makes the service resilient to a brief authoritative outage, but delays changes. A short lifetime makes changes fast but increases load and removes that resilience. The standard migration procedure is to lower the lifetime, wait for the old value to drain, change the record, then restore the lifetime.

### 2.7 Security: threats, mechanisms and marks

| Threat | Mechanism the attacker uses | Defence | What the defence achieves | Mark |
|---|---|---|---|---|
| Cache poisoning | A forged response accepted before the genuine one | Random identifier plus random source port | Makes guessing both values impractical | 2 |
| Spoofing | A response pretending to come from the queried server | The same unpredictability, plus case randomisation | Raises the cost of a matching forgery | 1 |
| Poisoning through a delegation | Data outside the server's authority accepted | Bailiwick checking | Rejects records the server had no right to supply | 2 |
| Tampering with genuine data | Modification in transit or at a compromised server | Signed records with a chain of trust | Origin authentication and integrity | 3 |
| Reflection and amplification | Many spoofed queries producing large answers to a victim | Response rate limiting and ingress filtering of spoofed sources | Reduces the amplification factor and the supply of forged sources | 2 |
| Volumetric flooding | Concentrated attack on one address | Anycast across many instances | Distributes the flood and keeps the service answering | 2 |
| Observation of queries | Reading plaintext traffic | Encryption on port 853 or 443 | Confidentiality of the query, not authenticity of the answer | 2 |

The single most examinable sentence in this area is that signed records provide origin authentication and integrity but **not** confidentiality and **not** availability. A candidate who adds that sentence to an answer almost always gains the final discussion mark.

A distributed denial of service attack, abbreviated DDoS, is different in aim from the others: it does not try to falsify data but to make the service unavailable by exhausting it from many sources. Its defences are therefore distribution and rate limiting rather than cryptography, which is why anycast appears in the same table as signed records.

### 2.8 Numbers worth carrying into the exam

| Number | What it is | Where it earns a mark |
|---|---|---|
| 53 | DNS port for UDP and TCP | Port recall |
| 13 | Logical root server identities, a to m | Root structure |
| 63 | Maximum octets in one label | Name syntax |
| 255 | Maximum octets in a complete name | Name syntax |
| 512 | Original UDP payload limit | Truncation |
| 1,232 | Recommended modern UDP payload size | EDNS buffer |
| 65,536 | Number of possible 16-bit identifiers | Entropy defence |
| 65,535 | Highest valid port number, source of port entropy | Entropy defence |
| 853 and 443 | Encrypted transports for query privacy | Security |
| 0, 2, 3, 5 | Success, server failure, name error, refused | Response codes |

### 2.9 A zone fragment to be able to read

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

Four things to say about this zone if a question presents one.

The start-of-authority record identifies the primary server and the responsible mailbox, carries the version number that secondaries compare, and sets the negative caching ceiling of 300 seconds in its final field.

The apex carries authority records, an address record, mail records and a text record, and deliberately carries no alias, because an alias at the apex would conflict with the authority records.

The alias at www points at the apex, is the only record at that name, and has a shorter lifetime than the apex because web names change more often.

The mail exchanger target has an address record in the same zone, so mail routing can complete; note also that ns1 and ns2 are inside the delegated zone, so the parent must publish glue for them.

## 3. Methods and Operations

### 3.1 The ten-mark narration skeleton

A "describe the resolution" question is marked against a list, and the list is predictable. The skeleton below is the order in which to write, because it matches the order of events and never puts a server before the step that reaches it.

1. State that the client is an application that requires an address, and that the operating system's stub resolver issues the first query.
2. State that the stub resolver sends the query to a configured recursive resolver, with the recursion-desired flag set, over UDP port 53.
3. State that the resolver checks its cache first, and that a hit ends the process immediately.
4. State that on a miss the resolver consults its root hints and queries a root server iteratively.
5. State that the root server returns a referral, not an answer, containing the name server records of the relevant top-level domain.
6. State that the resolver repeats the query to a top-level domain server, which returns a referral to the authoritative servers of the registered domain.
7. State that the resolver repeats the query to an authoritative server, which returns the record with the authoritative flag set.
8. State that the resolver caches each record with its lifetime, and returns the answer to the stub resolver.
9. State that the application now connects to the address on its own port, and that the name plays no further part.
10. Add one sentence on cost, for example that three round trips are needed on a cold lookup and none on a cached one.

Ten marks usually map to ten of these, with the referral-versus-answer distinction carrying two of them and the direction of recursion and iteration carrying two more.

The two errors that lose the most marks are stating that the client queries the root server directly, and stating that the resolver sends recursive queries to the root. Neither is correct: the client recurses only to its resolver, and the resolver iterates to the hierarchy.

### 3.2 The comparison skeleton

Comparison questions are marked per genuine difference, so each point must contain both sides rather than describing one side twice.

For recursive against iterative, the reliable five points are these.

Who performs the work: the server in a recursive query, the client in an iterative query.

What may be returned: a final answer or an error in the recursive case, a final answer or a referral in the iterative case.

Where each occurs in a real resolution: recursion between the stub resolver and the resolver, iteration between the resolver and the hierarchy.

Which flag carries it: the recursion-desired flag in the query, and the recursion-available flag in the response.

What it costs: the recursive party bears the round trips and the cache, the iterative party bears only the cost of one exchange.

Add a conclusion sentence for the final mark: the arrangement exists because clients are numerous and simple while resolvers are few and capable, so the expensive work is concentrated where it can be cached and shared.

### 3.3 The security skeleton

A security answer scores when it is written as a chain of cause and effect, in four moves.

Move one, the design property: the protocol matches a response to a query by identifier, addresses and ports, and accepts the first match, because it was designed for a trusting network.

Move two, the exploit: an attacker who can predict or observe those values sends a forged answer before the genuine one, and the resolver caches it for the record's lifetime, so every client of that resolver receives the attacker's address.

Move three, the consequence: the user sees the correct name in the address bar while the traffic goes elsewhere, which is why cache poisoning is more dangerous than a simple redirect.

Move four, the defence, one mark each, each stated with its mechanism: random identifier and source port make prediction impractical; bailiwick checking rejects data outside the server's authority; signed records with a chain of trust let the resolver verify origin and integrity; anycast distributes load so that flooding cannot concentrate on one instance; source filtering at network ingress removes the spoofed queries that amplification depends on.

Close with the limitation sentence: signed records do not provide confidentiality, so encryption on a separate port is required for privacy, and they do not provide availability, so distribution is required for resilience.

### 3.4 The diagnostic skeleton

Scenario questions ask what is wrong and what to check. Answer in order of elimination, and name the observation that discriminates in each step.

Query the authoritative server directly. If it answers correctly, the zone data is sound and the fault is in caching or in the path.

Query the parent for the name server records. If they disagree with the child, the delegation is stale and the world is following records the owner no longer intends.

Query a different resolver. A different answer identifies a stale or poisoned cache rather than a broken zone.

Flush the local cache and repeat. A change confirms a local cache fault.

Repeat the query over TCP. Success over TCP after failure over UDP identifies truncation blocked by filtering.

Only then examine the destination service, because a naming failure says nothing about whether a server is running.

### 3.5 Commands that are safe to quote in an answer

| Aim | Command | What the marker wants you to say |
|---|---|---|
| Resolve a name | dig example.com A | Shows the answer section and the response code |
| Trace the hierarchy | dig +trace example.com | Shows each referral in order |
| Suppress recursion | dig @198.41.0.4 example.com +norecurse | Produces a referral rather than an answer |
| Query a specific server | dig @192.5.6.30 example.com A | Bypasses local caches |
| Read mail records | dig example.com MX | Shows preference and target |
| Reverse lookup | dig -x 8.8.8.8 | Shows the in-addr.arpa branch |
| Force TCP | dig +tcp example.com | Demonstrates the second transport |
| Validate signatures | delv example.com A | Reports fully validated |
| Inspect the cache | ipconfig /displaydns | Shows remaining lifetimes |
| Flush the cache | ipconfig /flushdns | Windows, administrator prompt |
| Flush on Linux | sudo resolvectl flush-caches | Local resolver cache |
| Flush on macOS | sudo dscacheutil -flushcache | System cache |

Two further Windows forms appear in marking schemes: `nslookup example.com` for a simple interactive query, and `nslookup -type=MX example.com` for a type-specific query. Both are acceptable where the question does not require flag-level detail.

### 3.6 Phrasing that earns marks

Examiners award marks for causal statements, not for lists of nouns. The following substitutions are worth making deliberately.

Instead of "the resolver asks the root, then the TLD, then the authoritative", write "the resolver iterates from the root downwards, following a referral at each level until an authoritative server answers".

Instead of "DNS is like a phone book", write "DNS provides indirection between a name and an address, so the address can change without any client being reconfigured".

Instead of "TTL is how long it is cached", write "the time to live is the maximum period for which any cache may retain the record; caches count it down and must re-query when it reaches zero".

Instead of "DNSSEC makes DNS secure", write "signed records provide origin authentication and integrity through a chain of trust from the root, but provide neither confidentiality nor availability".

Instead of "anycast makes it fast", write "anycast announces one address from many locations, so queries reach the nearest instance, load is spread, and a flood is distributed across instances".

## 4. Worked Implementation from the Notes

### 4.1 Task: model answer for a ten-mark resolution question

### 4.2 Implementation: full narration with per-step marking points

**Question.** Describe how a client resolves the domain name www.example.com to an Internet Protocol address. (10 marks)

**Step 1. State the starting point.** The client application requires an address, so the operating system's stub resolver issues a query for the name www.example.com of type A in class IN. [1 mark]

**Step 2. Identify the first destination and the flags.** The stub resolver sends the query to its configured recursive resolver over UDP port 53, with the recursion-desired flag set, which asks the server to complete the work rather than merely to refer. [1 mark]

**Step 3. State the cache check.** The resolver examines its cache. A valid cached entry would end the process here; on a miss the resolver begins to iterate. [1 mark]

**Step 4. Reach the root.** The resolver consults its root hints and queries a root server iteratively, because the root holds no host records and can only refer. [1 mark]

**Step 5. Describe the first referral precisely.** The root returns a response with no answer, the name server records for com in the authority section, and glue addresses in the additional section. The authoritative flag is clear. [2 marks]

**Step 6. Reach the top-level domain server, and note the caching of the delegation.** The resolver queries a com server with the same question and receives a second referral, this time naming the authoritative servers for example.com, again with glue because those names lie inside the delegated zone. The delegation is cached with its lifetime. [1 mark]

**Step 7. Reach the authoritative server.** The resolver queries an authoritative server for example.com. That server holds the zone and returns either the address record directly or an alias followed by the address of the alias target, with the authoritative flag set. [2 marks]

**Step 8. Return and cache.** The resolver caches every record with its published lifetime, builds a response that copies the client's identifier and sets the recursion-available flag, and returns it to the stub resolver. [1 mark]

**Total: 10 marks.**

The narrative is verifiable with a single command, which is worth quoting if the question invites evidence.

```bash
dig +trace www.example.com A
```

```text
.                       518400  IN      NS      a.root-servers.net.
;; Received 239 bytes from 192.168.1.1#53(192.168.1.1) in 11 ms

com.                    172800  IN      NS      a.gtld-servers.net.
;; Received 1170 bytes from 198.41.0.4#53(a.root-servers.net) in 94 ms

example.com.            172800  IN      NS      a.iana-servers.net.
;; Received 692 bytes from 192.5.6.30#53(a.gtld-servers.net) in 106 ms

www.example.com.        3600    IN      CNAME   example.com.
example.com.            3600    IN      A       93.184.216.34
;; Received 101 bytes from 199.43.135.53#53(a.iana-servers.net) in 121 ms
```

**Why this answer scores full marks.** It names every tier in the correct order, it distinguishes a referral from an answer at each step, it identifies which party recurses and which party iterates, it gives the port and transport, and it accounts for the alias in the final answer. It also states the cache check at the point where the process could have terminated, which is the sentence weaker answers omit.

### 4.3 Task: model answer for a comparison question

### 4.4 Implementation: paired differences with a concluding judgement

**Question.** Compare recursive and iterative DNS queries. (6 marks)

**Step 1. Define both.** A recursive query requests a complete answer and obliges the server to obtain it. An iterative query requests the server's own best answer, which may be a referral to a server that can answer. [1 mark]

**Step 2. State who performs the work.** In the recursive case the server performs the work; in the iterative case the client performs it by following referrals. [1 mark]

**Step 3. State the possible responses.** A recursive query returns the requested record, a definitive negative answer, or an error. An iterative query returns a record, a negative answer, or a referral, and a referral is not a failure. [1 mark]

**Step 4. Place each in a real resolution.** Recursion occurs between the stub resolver and the recursive resolver. Iteration occurs between the recursive resolver and each tier of the hierarchy in turn. [1 mark]

**Step 5. Name the protocol signals.** The recursion-desired flag in the query asks for recursive service, and the recursion-available flag in the response reports that the server offers it. A root or authoritative server sets neither. [1 mark]

**Step 6. Draw the design conclusion.** Concentrating iteration in a few resolvers allows the results to be cached and shared among many clients, which is why the architecture scales; if every client iterated, the root would receive a query for every lookup in the world. [1 mark]

**Total: 6 marks.**

**Why this answer scores full marks.** Each point contains both sides, so no mark is spent describing one side twice, and the last point supplies the reason the arrangement exists rather than merely restating it.

### 4.5 Task: model answer for a security question

### 4.6 Implementation: attack chain followed by mechanism-level defences

**Question.** Explain how a DNS cache poisoning attack works and describe three defences against it. (8 marks)

**Step 1. State the design property that is exploited.** Traditional DNS matches a response to a query by the 16-bit identifier, the source and destination addresses, and the port numbers, and accepts the first response that matches. The protocol has no intrinsic authentication. [1 mark]

**Step 2. Describe the injection.** An attacker who can send packets to the resolver, and who can predict or observe those values, sends a forged response that appears to answer the resolver's outstanding question, arriving before the genuine response. [1 mark]

**Step 3. Describe the persistence.** The resolver caches the forged records for their published lifetime, so every client that asks that resolver during that period receives the attacker's address. [1 mark]

**Step 4. State the consequence for the user.** The user types the correct name, the address bar shows the correct name, and the connection goes to the attacker, so there is no visible sign of compromise. [1 mark]

**Step 5. Defence one, unpredictability.** The resolver randomises both the 16-bit identifier, giving 65,536 possibilities, and the source port, giving tens of thousands more, so the combined space exceeds a billion values per query and an attacker must guess within a few milliseconds. [1 mark]

**Step 6. Defence two, bailiwick checking.** The resolver rejects any record that falls outside the zone of the server that supplied it, so a compromised or malicious delegation cannot introduce records for unrelated names. [1 mark]

**Step 7. Defence three, signed records.** With the Domain Name System Security Extensions, each zone signs its record sets and the parent publishes a digest of the child's key, forming a chain of trust from the root; a validating resolver can therefore prove origin and integrity, and reports failure rather than accepting altered data. [2 marks]

**Total: 8 marks.**

**Why this answer scores full marks.** It separates the design weakness from the exploit and from the persistence, which is what the three description marks reward, and each defence is stated with the mechanism that makes it work rather than as a name.

### 4.7 Task: model answer for a record-type question

### 4.8 Implementation: precise semantics plus a constraint explained as a consequence

**Question.** Name four DNS record types, state the purpose of each, and explain why a canonical name record cannot be placed at the zone apex. (8 marks)

**Step 1. Address record.** An A record maps an owner name to one Internet Protocol version 4 address; several may exist at one name, which provides a simple form of distribution. [1 mark]

**Step 2. Mail exchanger record.** An MX record gives a preference value and the name of a host that accepts mail for the domain; the lowest preference is tried first, and the target must resolve to an address rather than to an alias. [1 mark]

**Step 3. Name server record.** An NS record names a server authoritative for a zone; every apex must publish at least two, and the copy published by the parent is the one the world follows when it descends the tree. [1 mark]

**Step 4. Pointer record.** A PTR record maps an address back to a name and exists only in the reverse zones under in-addr.arpa or ip6.arpa, where the address components are written in reverse order. [1 mark]

**Step 5. Alternative fourth type if preferred.** A quad-A record maps a name to an Internet Protocol version 6 address and is independent of any address record at the same name, so a dual-stack host publishes both. A text record carries arbitrary strings used for sender policy and domain verification. [1 mark]

**Step 6. State the alias rule.** A canonical name record declares that the queried name is an alias and that resolution continues at the target name. [1 mark]

**Step 7. Explain the exclusion.** Because every query for the alias name is redirected, no other record at that name could ever be reached, so a canonical name may not coexist with any other record. [1 mark]

**Step 8. Apply it to the apex.** The apex must carry a start-of-authority record and at least two name server records; placing an alias there would contradict the exclusion rule, so the apex is never an alias and the standard pattern is an address record at the apex with an alias below it. [1 mark]

**Total: 8 marks.**

The pattern being described appears directly in a zone file, which is worth quoting if the question supplies one or invites an example.

```text
example.com.        3600  IN  A     192.0.2.10
www.example.com.     300  IN  CNAME example.com.
```

**Why this answer scores full marks.** Each type is given with its data shape and one consequence, and the constraint is derived from the redirection behaviour rather than asserted as a rule, which is what the final two marks reward.

### 4.9 Task: model answer for a caching and troubleshooting question

### 4.10 Implementation: mechanism, then procedure, then evidence

**Question.** Explain how DNS caching reduces load on the hierarchy, and describe how the cache would be cleared on Windows and on Linux. (6 marks)

**Step 1. State what is cached.** A resolver caches every record it obtains, with the lifetime published by the authoritative server, and also caches negative answers for the negative lifetime derived from the start-of-authority record. [1 mark]

**Step 2. State the hierarchy of caches.** Copies are held in the browser, in the operating system, in the router and in the resolver, each honouring the same lifetime, so an answer is served from the level closest to the asker. [1 mark]

**Step 3. Quantify the effect.** A cold lookup costs three round trips, one to each tier; a cached lookup costs a memory read, so a resolver serving a million queries with a high hit rate sends only a small fraction upwards. [1 mark]

**Step 4. State the trade-off.** A long lifetime reduces load and masks a brief outage of the authoritative servers but delays changes, which is why lifetimes are lowered before a planned move and the old value is allowed to drain. [1 mark]

**Step 5. Give the Windows procedure.** Run an elevated Command Prompt and issue the flush command; the confirmation reports that the resolver cache was flushed. [1 mark]

```powershell
ipconfig /flushdns
```

```text
Windows IP Configuration

Successfully flushed the DNS Resolver Cache.
```

**Step 6. Give the Linux procedure and state its scope.** On a system using the standard local resolver, flush with elevated rights and confirm with the statistics output; note that neither command affects the resolver at the provider, whose cache must expire on its own. [1 mark]

```bash
sudo resolvectl flush-caches
sudo resolvectl statistics
```

**Total: 6 marks.**

**Why this answer scores full marks.** It gives the mechanism, then the quantity, then the trade-off, and it closes with the scope limitation that most answers omit: a local flush cannot fix an upstream stale entry.

## 5. Testing, Interpretation, and Common Errors

### 5.1 The trap table

Every entry below is a statement that candidates write in examinations, followed by the correct statement and the reason the error is attractive. Read the left column and recite the middle column until the correction is automatic.

| Tempting but wrong statement | Correct statement | Why the trap works |
|---|---|---|
| There are thirteen root servers, so there are thirteen machines | There are thirteen logical root server identities, each served by many anycast instances worldwide, numbering well over a thousand machines | The lettering a to m looks like a fixed inventory |
| The client queries the root server directly | The client asks its recursive resolver, which iterates to the root | The whole chain is described as one lookup, so the asker and the worker merge |
| The resolver sends recursive queries to the root | The resolver sends iterative queries to the root and receives a referral | The resolver is recursive on behalf of the client, which tempts a transfer of the label |
| A referral means the server has failed | A referral is a correct response that points to the next tier | It has no answer, so it looks like a failure |
| NXDOMAIN and no data are the same | NXDOMAIN means the name does not exist; no data means it exists without that record type | Both produce an empty answer section |
| DNS returns the address of a website | DNS returns records, of which an address record is the most common | Most taught examples are web addresses |
| CNAME and A records can share a name | A canonical name excludes every other record at that name | Aliases and addresses are both "names", so they seem combinable |
| CNAME may be used at the apex | It may not, because the apex must carry authority records | The bare domain is the name most people want to alias |
| MX records contain addresses | They contain a preference value and a host name | The host name looks like it must resolve already |
| TTL is how long the record exists | TTL is the maximum period a cache may retain it; the record exists until it is changed | "Time to live" sounds like the record's own lifetime |
| Flushing the cache fixes the problem everywhere | A flush clears one local cache; resolver and router caches must expire separately | The symptom disappears on the tester's machine, which seems conclusive |
| DNSSEC encrypts DNS | DNSSEC signs records and provides origin authentication and integrity, not confidentiality | "Security extensions" suggests encryption |
| DNS uses port 53 over UDP only | DNS uses port 53 for both UDP and TCP | Almost every example query is a small one over UDP |
| Anycast means load balancing | Anycast means one address announced from several locations, with routing selecting the nearest | The traffic distribution resembles load balancing |
| A short TTL is always better | A short TTL speeds up change and increases load; the right value matches the record's volatility | Short TTLs are the recommended fix for stale records |
| Reverse lookup proves identity | A pointer record is optional, owner-controlled and may disagree with the forward record | Reverse lookups feel like a verification step |

Two additional traps concern wording rather than fact.

Writing "the DNS server" without qualification loses marks in any question worth more than two, because it conflates four distinct roles. Write "recursive resolver", "root server", "top-level domain server" or "authoritative server" as appropriate.

Writing "domain" where "zone" is meant loses marks in delegation questions. A zone is what a set of servers is authoritative for; a domain is a node in the tree.

### 5.2 Reading output accurately under time pressure

Three quick readings extract almost everything a question asks about a captured response.

Read the response code. Zero is success, which does not guarantee an answer. Two is server failure, which indicates a fault rather than an absence. Three is a name error. Five is a refusal, which often means recursion was requested of a server that does not offer it.

Read the flags. The authoritative flag separates a server that owns the data from one that merely remembers it. The truncation flag says the response was cut short and the client should retry over TCP. The authenticated-data flag says a validating resolver proved the data.

Read the section that is populated. Records in the answer section answer the question. Delegation records in the authority section mean the server is referring downwards. A single start-of-authority record in the authority section means the answer is negative. Address records in the additional section are glue.

A worked reading, of the kind a question may present: a response with response code zero, no authoritative flag, zero answers, thirteen authority records for com and twenty-seven additional records, is a root referral for a name somewhere in com. Saying that in one sentence earns every mark available on such an item.

### 5.3 Ten self-test items with model answers

1. On which port and transports does DNS operate? Port 53, UDP for ordinary queries and TCP for truncated responses and zone transfers.
2. How many root server identities exist and how are they served? Thirteen identities lettered a to m, each served by many anycast instances.
3. What does a root server return for an ordinary name? A referral containing the name server records of the relevant top-level domain, with no answer.
4. What flag marks an authoritative response, and which servers set it? The authoritative-answer flag, set by servers holding the zone, not by resolvers or by root and top-level domain servers.
5. What is the difference between a domain and a zone? A zone is the part of the tree for which one set of servers holds authoritative data; a domain is a node in the tree.
6. Why must a mail exchanger target not be an alias? Mail routing expects a name with an address record; an alias redirects resolution, which the routing rules do not require a sender to follow.
7. How is a negative answer cached? With the smaller of the start-of-authority record's own lifetime and the final value in that record's data.
8. What two values are randomised to defeat forged responses? The 16-bit query identifier and the source port.
9. What does anycast achieve for the root service? Lower latency, distributed load, and resilience under flooding, because one address is served from many locations.
10. What does DNSSEC not provide? Confidentiality and availability; encryption and distribution provide those.

### 5.4 Revision checklist

Work through the list and tick only what you can state aloud without notes. An unticked item is a revision task, not a reading task.

- Expand DNS and give a definition containing distributed, hierarchical, database and resource records.
- Name the four layers of the name space and give an example and an owner for each.
- State the label and name length limits, and explain the meaning of a trailing dot.
- Distinguish a domain from a zone and describe what creates a zone cut.
- Name all five server roles and the question each answers.
- Explain why the root holds no host addresses.
- State the root server identity count and explain anycast in one sentence.
- Explain why glue records are required and what fails without them.
- Narrate a cold resolution in the correct order, in ten steps or fewer.
- State which party recurses and which iterates, and where each appears.
- Distinguish a referral from a negative answer by the section that is populated.
- Define the seven record types with their data shape and one constraint each.
- Explain the alias exclusion rule and its consequence at the apex.
- Explain the start-of-authority fields that matter: serial, refresh, retry, expire, negative ceiling.
- Define time to live as a maximum caching period and describe the countdown.
- Name the four cache levels and what each saves.
- State the negative caching lifetime rule and distinguish name error from no data.
- Give the flush procedures for Windows, Linux and macOS, and state their scope.
- Explain cache poisoning as a four-move chain and give three defences with mechanisms.
- State precisely what signed records do and do not provide.
- Give the port for each transport and the reason TCP is needed.
- Quote four commands that demonstrate resolution, tracing, reverse lookup and cache flushing.

### 5.5 Time strategy in the examination

Assume roughly one mark per minute for structured questions, and plan the paper against that rate.

**First five minutes: read and classify.** Read every question and label each one with its shape: narration, comparison, data, or failure and defence. Mark the ones you can answer completely. Classification prevents the commonest time loss, which is writing a narration where a comparison was asked.

**Next phase: answer in mark order, cheapest first.** Short recall items are completed in a few minutes each and bank marks. A ten-mark narration is written with the skeleton from Section 3, one numbered step per mark, and should take twelve minutes at most. Never begin with the longest question.

**Within each answer, count the marks before writing.** A six-mark comparison needs six distinct points, not nine sentences exploring three. A ten-mark narration needs the full chain, so allocates two marks to the referral-versus-answer distinction and two to the recursion and iteration direction, because those are the discriminating points.

**Leave eight to ten minutes for the check.** Re-read each answer against the trap table and confirm four things: that no server is described as doing another server's job, that every referral is called a referral, that the port is given as 53 for both transports, and that the root is described as thirteen identities served by many instances.

**If time runs short, write the skeleton, not the prose.** A numbered list of ten correct steps earns nearly all the marks of a polished paragraph, whereas a polished paragraph covering four steps earns four marks.

### 5.6 The final ten-minute check

Three questions catch almost every avoidable loss.

Did I answer the question that was asked? A question that says "compare" wants differences, not a description of each in turn. A question that says "explain why" wants a cause, not a definition.

Did I use the precise term at each step? Resolver, root server, top-level domain server and authoritative server are four different roles, and each deserves its own name.

Did I include the qualifying sentence that shows understanding? For caching, that the local flush does not touch upstream caches. For security, that signed records do not encrypt. For the root, that thirteen identities are served by many anycast instances. For records, that an alias excludes every other record at its name.

A candidate who answers all three questions affirmatively before leaving has protected more marks than any last-minute addition is likely to earn.


