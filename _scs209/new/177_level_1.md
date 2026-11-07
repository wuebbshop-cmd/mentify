## 1. Concept and Use Case

### 1.1 A contacts list for the whole world

Imagine a contacts list so large that it holds an entry for every shop, office and home on the planet, and that the people who answer the phone at those places move to a different building every few months. You would never try to memorise that list. You would memorise names instead — "the bakery on the corner", "Aunt Mary", "the dentist" — and let the list translate the name into whichever number is correct today. You would also accept that the list must be split among many offices, because no single office could keep it current, and you would expect a lookup to take a fraction of a second even though the list is enormous.

That is exactly what the Domain Name System does for computer networks. The Domain Name System, abbreviated DNS, is a worldwide, automatically maintained directory that translates the names people like to type into the numeric addresses that machines need. The name is easy for a person to remember and easy for a business to print on a van. The number is what the network actually understands. DNS is the bridge between the two, and it runs quietly in the background every time you open a web page, send an email, or start a video call.

The comparison people in the industry use most often is that DNS is the telephone directory of the Internet. The comparison is useful but incomplete, and the difference matters later in this note. A printed directory is one book in one place, updated once a year. DNS is a distributed system with millions of cooperating servers, updated constantly, and queried billions of times a day. The book analogy captures the purpose; the rest of this note explains the machinery.

### 1.2 Why machines cannot simply use names

Every device attached to a network needs an address so that other devices can send data to it. On the Internet that address is an Internet Protocol address, where Internet Protocol is abbreviated IP. The older and still dominant form is IP version 4, written as four decimal numbers separated by dots, for example 93.184.216.34. The newer form is IP version 6, written as eight groups of hexadecimal digits, for example 2606:4700:4700::1111. Both are precise, both are unique within their version, and neither is memorable in the way a word is.

Routers forward data by looking at these addresses. A router does not read "example.com" and decide where to send the packet; it reads the destination address in the packet header and consults a table. The address is the only thing the forwarding hardware can act on. So the network layer must be given numbers, even though human communication happens in names.

The obvious workaround is to keep a local list of names and addresses on each machine. Early networks did exactly that, with a single shared text file that every host downloaded. The approach collapsed almost immediately. When one file must describe every host in the world, every change anywhere requires every host to fetch a new copy, the file becomes huge, and one administrator becomes a single point of failure for the entire network. DNS was designed to replace that file with a system that scales: no single copy, no single owner, and no need for anyone to know the whole database.

### 1.3 What DNS actually provides

The service DNS provides is called name resolution. Resolution means taking a name and producing the data associated with it. The most familiar data is an address, but DNS is not limited to addresses, and understanding that early prevents a great deal of confusion later.

- An address record answers the question "which machine serves this name?" and comes in an IP version 4 form and an IP version 6 form.
- A mail record answers the question "which server accepts email for this domain?" This is why mail can be delivered without the sender knowing anything about the recipient's infrastructure.
- A name server record answers the question "which servers are authoritative for this part of the name space?" It is the record that makes delegation possible.
- A canonical name record answers the question "is this name merely another label for a name that already exists?" It creates an alias, so one machine can answer to several names.
- A pointer record answers the reverse question, "which name belongs to this address?" It is used in logs and in some security checks.
- A text record carries arbitrary text, and is used today for email authentication policies and for proving to a service that you control a domain.

Each of these is a resource record: a single entry in the distributed database, with a name, a type, a lifetime and a value. Section 2 covers each type properly.

There is a second service DNS provides that is easy to overlook. Because the name space is hierarchical and delegated, DNS is also the mechanism by which authority over a domain is handed from a parent to a child. The operator of the top-level domain for .com does not store the address of every .com website. It stores, for each registered domain, the names of the servers that do. Delegation is the design decision that makes the system grow without limit, and it is the reason a single organisation can add a million subdomains without asking anyone's permission.

### 1.4 Where you meet DNS in daily life

DNS appears in ordinary situations far more often than most people realise.

When you type a web address into a browser and press Enter, the browser must convert the name into an address before it can open a connection. When you send an email, your mail program asks DNS where to deliver it. When a video app on a phone loads a thumbnail from a content network, that name is resolved too. When a company blocks a gambling site at the network boundary, it often does so by refusing to resolve the name rather than by inspecting traffic. When an Internet service provider, abbreviated ISP, wants to tell you that a domain does not exist, it may answer with a page of advertising instead of an error, which is a DNS behaviour rather than a web behaviour.

DNS is also implicated in a large share of network troubleshooting. A connection that fails immediately, with a message about the server not being found, is usually a naming failure rather than a routing failure. A site that loads for everyone else but not for you, while the address still pings, is often a stale cached entry on your own machine. A new website that is invisible to some visitors for a day is usually a lifetime value that was set too high before the move. Each of these is covered in Section 5.

### 1.5 What happens in the second after you press Enter

Because DNS hides itself so well, it helps to hold one simple picture of the sequence. The detail comes later; the shape is what matters now.

1. Your computer checks its own short-term memory, called a cache, for the name. If the answer is there and has not expired, the lookup is finished immediately.
2. If it is not there, your computer asks a helper server — usually one run by your ISP, your router, or a public provider — to find the answer on your behalf.
3. That helper, called a recursive resolver, may already know the answer from its own cache. If not, it asks a series of servers in order: first a root server, then a server for the top-level domain, then the server that actually holds the records for the domain.
4. The answer comes back to the helper, which passes it to your computer and remembers it for a while so the next request is instant.

The whole exchange usually completes in tens of milliseconds, which is why nobody notices it. It is also why a fault in DNS feels like the whole Internet is broken: every application depends on that first step succeeding.

### 1.6 What DNS is not

Several everyday beliefs about DNS are wrong, and clearing them up now saves confusion later.

DNS is not a website and does not hold web pages. It holds small records, mostly addresses, and nothing else. A web page is delivered by a web server that DNS merely helped you locate.

DNS is not the same thing as registering a domain name. Registration is a commercial and administrative act: you pay a registrar for the right to use a name, and the registrar tells the registry to publish your name servers. DNS is the technical machinery that then answers queries. You can own a domain and still have broken DNS if the records are wrong, and you can operate DNS servers for a name you do not own — which is exactly what a hosting company does on your behalf.

DNS is not a search engine. If you type a partial or misspelled name, DNS does not guess what you meant. It answers that the name does not exist, and any helpful suggestion you see comes from the browser or from an ISP that has chosen to interfere.

DNS is not encrypted by default. Traditional queries travel in plain text, which means a network operator or anyone able to watch the path can see which names you look up. Encrypted variants exist and are described later, but they are not the default behaviour of the protocol.

## 2. Data, Syntax, and Core Concepts

### 2.1 Names are read from right to left

A domain name such as www.books.example.com looks like a single string, but it is really a path through a tree, and the tree is read from the right-hand end backwards. The rightmost label is the most general part of the name; each label to the left is more specific.

The name ends, in its complete form, with a dot that is usually omitted. That final dot represents the root of the tree, the single starting point for every name in the system. A name written with the trailing dot is called a fully qualified domain name, abbreviated FQDN, and it is unambiguous. A name written without it is relative to whatever starting point the local configuration supplies, which is why a missing trailing dot in a configuration file causes so many mistakes.

Reading www.books.example.com from the right:

- the root, represented by the trailing dot, is the top of the tree;
- com is a top-level domain;
- example is a second-level domain, the part a business registers;
- books is a subdomain created by the owner of example.com;
- www is a further subdomain, and in this case the specific host that serves the website.

Each of these pieces is called a label. A label may be up to 63 characters long, and the complete name in its wire form may be up to 255 characters.

### 2.2 The layers of the name space

The hierarchy has four layers that you need to be able to name in an examination.

The **root domain** is the top of the tree. It is served by a set of root name servers, and its only job is to know which servers are responsible for each top-level domain. The root zone contains no website addresses at all. It contains pointers, and those pointers are the beginning of every lookup that is not already cached.

**Top-level domains** sit directly beneath the root. There are two families you must know. A generic top-level domain, abbreviated gTLD, is a category defined by purpose or by commercial policy: .com, .org, .net, .info and the many newer ones such as .app and .dev belong here. A country-code top-level domain, abbreviated ccTLD, is a two-letter code assigned to a country or territory: .ke for Kenya, .uk for the United Kingdom, .de for Germany, .jp for Japan. Sponsored top-level domains such as .edu, .gov and .mil are restricted to particular communities and are usually grouped with the generic family in introductory material.

**Second-level domains** are the names that organisations and individuals register: example.com, example.org, example.co.ke. Registration happens through an accredited registrar, and the registry for the top-level domain records which name servers are authoritative for the new domain. This is the layer at which a business owns something.

**Subdomains** are everything the owner creates below the second level: www.example.com, shop.example.com, mail.example.com, and deeper names such as dev.api.example.com. Subdomains are created by the domain owner alone. No registry, no registrar and no central authority needs to be informed, which is why a single domain can support an unlimited number of services.

| Layer | Example | Who controls it | What it contributes |
|---|---|---|---|
| Root | the trailing dot | Root server operators | Points to each top-level domain |
| Top-level domain | com, org, ke, uk | Registry for that TLD | Points to the name servers of each registered domain |
| Second-level domain | example.com | The registrant, through a registrar | Holds the organisation's records |
| Subdomain | www.example.com, shop.example.com | The registrant alone | Holds records for one service or host |

A domain and a zone are not the same thing, although the words are often used loosely. A zone is the portion of the name space for which one set of name servers holds authoritative data. When the owner of example.com delegates shop.example.com to a different set of name servers, a new zone begins at that point. Until such a delegation is made, every subdomain sits inside the parent zone.

### 2.3 The servers that cooperate in a lookup

Four roles appear in every resolution, and confusing them is the most common source of lost marks in this topic.

The **stub resolver** is the small piece of software inside your own computer that asks the first question. It does not search the hierarchy itself; it forwards the request to a configured server and waits. On a typical laptop the stub resolver is part of the operating system.

The **recursive resolver** is the workhorse. It receives the question from the stub resolver and takes responsibility for producing a complete answer, doing as much work as necessary. It may already have the answer cached. If not, it walks the hierarchy itself, asking one server after another, and finally returns the answer and stores it for the period the record allows.

The **root name servers** answer the first step of that walk. They are asked "who is responsible for .com?" and reply with the names of the .com name servers. There are 13 logical root server identities, named with the letters a through m, but each identity is served by many separate machines in different countries using a technique called anycast, in which the same address is announced from many locations and each query reaches the nearest one. Thirteen identities therefore do not mean thirteen physical computers; the real count of instances is in the thousands.

The **top-level domain name servers** answer the second step: "who is responsible for example.com?" They reply with the names of the servers that the domain owner, or the hosting company acting for the owner, has configured.

The **authoritative name servers** hold the actual records for the domain. They are authoritative in the sense that their answer is the final word: they are configured by the domain owner, they do not guess, and they do not consult other servers to answer a query about their own zone. If a name does not exist inside their zone, they say so definitively.

| Role | Typical operator | Question it answers |
|---|---|---|
| Stub resolver | Your operating system | Where do I send this question? |
| Recursive resolver | ISP, router, or public provider | What is the final answer, however much work it takes? |
| Root name server | Independent root server operators | Which servers handle this top-level domain? |
| Top-level domain name server | The TLD registry | Which servers handle this registered domain? |
| Authoritative name server | The domain owner or their host | What are the records for this name? |

### 2.4 Resource record types and what each is for

A resource record is one entry in the database. Every record has the same five parts: the name it belongs to, its type, its class, its lifetime, and its value. The class is almost always IN, meaning Internet. The lifetime is explained in the next subsection. The type is what determines how the value is interpreted.

| Type | Stands for | Plain-English purpose | Example value |
|---|---|---|---|
| A | Address | Gives the IP version 4 address of a host | 192.0.2.10 |
| AAAA | Address, four times A | Gives the IP version 6 address of a host | 2001:db8::10 |
| CNAME | Canonical Name | Makes one name an alias for another name | www.example.com points to example.com |
| MX | Mail Exchanger | Names the mail servers for a domain, with a preference number | 10 mail1.example.com |
| NS | Name Server | Names the servers authoritative for a zone | ns1.example.com |
| PTR | Pointer | Maps an address back to a name | 34.216.184.93.in-addr.arpa points to example.com |
| TXT | Text | Carries arbitrary text, such as an email policy | "v=spf1 mx -all" |

Three details about these types cause most beginner errors.

An A record and an AAAA record are separate records with the same name. A domain with both can be reached over either version of the protocol, and the two do not conflict. The name AAAA is pronounced "quad A" because it is four times as long as an A record, which is a fair description of the address it holds.

A CNAME record cannot coexist with any other record of the same name, and it cannot be placed at the top of a zone. The reason is that a canonical name tells the resolver "stop looking here, look there instead", and any other record at that name would then be unreachable. For the same reason, a mail exchanger must point at a name that has an address record, not at a name that is only an alias.

An NS record appears at the top of every zone and is the record that a parent uses to delegate. If the NS records published by the parent disagree with those published inside the child zone, the parent's copy is what the rest of the world follows, which is why a delegation can appear correct locally and broken globally.

### 2.5 Time to live and the idea of caching

Every record carries a number called its time to live, abbreviated TTL, measured in seconds. The number means: you may keep this answer in memory for this long, and after that you must ask again. A TTL of 3600 means one hour; a TTL of 300 means five minutes.

Caching is what makes DNS fast enough to be invisible. Without it, every page load would trigger a full walk from a root server downwards, and root servers would melt under the load. With it, a resolver that has just answered a query for a popular name can answer the next thousand queries from memory in microseconds.

Caching happens at several levels, and each level has its own memory and its own rules.

| Level | Where it lives | Typical lifetime | How to clear it |
|---|---|---|---|
| Browser | Inside the browser process | A minute or less | Browser's own network settings page |
| Operating system | The system resolver cache | Governed by record TTL | The operating system's flush command |
| Router | The home or office gateway | Governed by record TTL | Reboot, or restart the router's DNS service |
| Recursive resolver | The ISP or public resolver | Governed by record TTL | Not under your control |

The consequence of caching is a trade-off you must be able to describe. A long TTL reduces load and speeds up repeated lookups, but it means a change takes hours to become visible everywhere. A short TTL makes changes visible quickly but increases load on the authoritative servers. Administrators usually keep TTLs long during quiet periods and shorten them deliberately a day or two before a planned move.

One further kind of caching explains a confusing experience. A resolver also remembers that a name does not exist, or that it exists without a particular kind of record. This is called negative caching, and its period is short, usually a few minutes. The effect is that a name created a moment ago can appear not to exist for a little while, because somebody looked it up just before it was created and the "does not exist" answer was remembered.

### 2.6 The port that DNS uses

DNS uses port 53 for both of its transport protocols. That single sentence answers a frequent examination question. Queries and responses normally travel over the User Datagram Protocol, abbreviated UDP, because a single question and a single answer fit comfortably in one small datagram, and because UDP avoids the delay of setting up a connection. When an answer is too large for a UDP datagram, or when a transfer of a whole zone is required, DNS switches to the Transmission Control Protocol, abbreviated TCP, which is reliable and connection-oriented.

So port 53 appears twice in the same service: once for UDP and once for TCP. A firewall rule that permits only UDP 53 will appear to work for most queries and then fail mysteriously for large responses, which is a real and common operational fault.

### 2.7 Who runs what

Three kinds of organisation share responsibility for the name space.

The root is coordinated by the Internet Corporation for Assigned Names and Numbers, and operated in practice by a group of independent organisations that each run one of the thirteen root server identities.

Each top-level domain is run by a registry, which maintains the database of registered names and publishes the delegation records that point to each domain's name servers.

Registrars are the commercial interface: they sell registrations, collect the registrant's details, and pass the name server information to the registry. A hosting company may act as registrar, as DNS provider, or as both, and knowing which role is failing is the first step in diagnosing a broken domain.

## 3. Methods and Operations

### 3.1 Two ways to ask: recursive and iterative

There are two styles of question in DNS, and the difference is easiest to see as a difference in who does the walking.

An **iterative** query is a question asked of a server that will not do the work for you. You ask a root server "what is the address of www.example.com?" and it replies, in effect, "I do not know, but the servers for .com are over there; go and ask them." You then ask a .com server and receive "I do not know, but the servers for example.com are over there." You finally ask the authoritative server and receive the address. Each server gives you the best answer it has, which is often a referral rather than a final answer.

A **recursive** query is a question asked of a server that promises to finish the job. You ask the recursive resolver "what is the address of www.example.com?" and it returns the address. How many other servers it had to ask is its own business. If it cannot produce an answer, it returns an error rather than a referral.

In practice both styles appear in every lookup, and that is the point most beginners miss. Your computer sends a recursive query to its resolver. The resolver then sends iterative queries to the root, the top-level domain servers, and the authoritative servers in turn. So the recursion is at the top of the chain and the iteration is at the bottom. A common wrong answer states that the resolver sends recursive queries to the root server; it does not, because root servers refuse to do that work.

| Feature | Recursive query | Iterative query |
|---|---|---|
| Who does the walking | The server that receives the question | The client that asks |
| Typical user | A stub resolver asking its resolver | A resolver asking the hierarchy |
| Possible response | Final answer or error | Final answer, or a referral to another server |
| Work performed | All of it, if not cached | Only the part this server knows |

### 3.2 Reading a lookup with dig

The standard tool for inspecting DNS on Linux and macOS is called dig, short for domain information groper. It is the tool examiners most often expect, because its output is explicit about every part of the answer.

The parts of the output that matter, in order, are the status line, the flags, the answer section, and the authority section. The status line reports whether the query succeeded. The flags report whether recursion was requested and available, and whether the answer came from an authoritative server. The answer section lists the records that answer the question, each with a remaining time to live that counts down while the record sits in a cache. The authority section, present when there is no direct answer, usually carries the records that describe the zone, which is how a negative answer is cached.

### 3.3 Reading a lookup with nslookup

The older and simpler tool is nslookup, which is available on Windows, Linux and macOS. It prints less, and the smaller output is sometimes easier to read.

```bash
nslookup example.com
```

A representative result looks like this.

```text
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
Name:   example.com
Address: 93.184.216.34
```

The first two lines name the server that was asked and give its address and port, which again shows port 53. The phrase "non-authoritative answer" is the important part: it means the server answered from its cache rather than from the zone itself, so the answer is a remembered copy. If you ask the authoritative server directly, that phrase disappears.

To ask for a specific record type, the tool takes a type option.

```bash
nslookup -type=MX gmail.com
```

```text
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
gmail.com       mail exchanger = 5 gmail-smtp-in.l.google.com.
```

The output shows the preference value and the mail host, which are the two parts of a mail exchanger record.

### 3.4 Looking at your own cache

Your operating system keeps a cache, and you can look inside it. On Windows the command is `ipconfig /displaydns`. It prints one block per remembered entry, showing the name, the type, the remaining time to live, and the data. Reading it teaches two things quickly: that a name may have several records at once, and that entries visibly expire.

Seeing entries expire is the clearest demonstration that time to live is a real countdown rather than a number in a textbook. Run the command, note the remaining time on a record, wait a minute, and run it again. The number falls.

### 3.5 Clearing a cache

Sometimes the cache is the problem: the site moved, and your machine is still going to the old address. Clearing the cache forces a fresh lookup.

| System | Command | Notes |
|---|---|---|
| Windows | ipconfig /flushdns | Run in an administrator Command Prompt |
| Windows, PowerShell | Clear-DnsClientCache | Same effect, PowerShell style |
| Linux with systemd-resolved | sudo resolvectl flush-caches | Must be run with elevated rights |
| macOS | sudo dscacheutil -flushcache | Usually paired with a restart of the responder |

Two points are worth stating exactly. First, flushing your own cache does not flush the cache of your ISP's resolver. If the stale answer lives there, you must wait for its time to live to expire, or ask a different resolver. Second, flushing is not the same as clearing a browser's history or its web cache; those are separate stores holding different things.

### 3.6 Choosing which resolver to ask

By default your computer asks whichever resolver it was given when it joined the network, normally through the router. You can override that and ask any resolver you like, which is useful both for testing and for privacy.

Public resolvers are run by large providers and are reachable at memorable addresses, for example 8.8.8.8 and 1.1.1.1. Using one can be faster than a poorly maintained local resolver, and it can bypass an ISP that redirects failed lookups to an advertising page. The trade-off is that the public resolver now sees every name you look up, so the choice is a privacy decision as much as a performance one.

You can also ask a specific resolver for a single query without changing any settings. Every lookup tool accepts a server parameter, so you can compare what two resolvers say about the same name — which is the fastest way to prove that a stale cache is the culprit.

### 3.7 Asking for something other than an address

Addresses are only one kind of answer. To check where email for a domain should go, ask for its mail exchanger records. To see which servers are authoritative, ask for name server records. To check the reverse mapping of an address, ask for a pointer record, which the tool performs with a special reverse flag. To read a text record, ask for the text type.

Knowing which type to ask for is half of practical DNS work. A domain can have a perfectly correct address record and still fail to receive email because its mail exchanger record is missing, and no amount of testing web pages will reveal that.

## 4. Worked Implementation from the Notes

### 4.1 Task: resolve a name and read every part of the answer

### 4.2 Implementation: a single A record query with dig

Step 1. Ask for the address record of a documentation domain. The domain example.com is reserved for examples, so it is safe to use in notes.

```bash
dig example.com A
```

Step 2. Read a representative answer.

```text
; <<>> DiG 9.18.24 <<>> example.com A
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41287
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            3600    IN      A       93.184.216.34

;; Query time: 14 msec
;; SERVER: 192.168.1.1#53(192.168.1.1) (UDP)
;; WHEN: Mon Nov 03 09:14:22 EAT 2025
;; MSG SIZE  rcvd: 56
```

Step 3. Interpret the status line. The value NOERROR means the name exists and the answer was produced. The identifier is a small number chosen by the client; the client checks that the reply carries the same number, which is the simplest defence against a forged reply.

Step 4. Interpret the flags. The flag qr marks the message as a response rather than a query. The flag rd records that recursion was desired, which is what our computer asked for. The flag ra records that recursion is available, which means the server we asked is a resolver willing to do the walking. Had the flag aa been present instead, the answer would have come directly from an authoritative server.

Step 5. Interpret the answer section. The name is shown with a trailing dot because this is the fully qualified form. The number 3600 is the remaining time to live in seconds, and it will decline on subsequent queries while the entry sits in a cache. The class IN means Internet. The type A and the value 93.184.216.34 complete the record.

Step 6. Interpret the server line. The query went to 192.168.1.1 on port 53 over UDP, which is the local router acting as a forwarding resolver. This single line demonstrates three facts at once: DNS uses port 53, it normally uses UDP, and the machine you ask is usually not the machine that holds the record.

### 4.3 Task: watch the entire hierarchy being walked

### 4.4 Implementation: trace the lookups with the trace option

Step 1. Ask dig to perform the walk itself instead of asking a resolver to do it.

```bash
dig +trace example.com A
```

Step 2. Read a representative trace. The output is long, so the essential lines are shown.

```text
.                       518400  IN      NS      a.root-servers.net.
.                       518400  IN      NS      b.root-servers.net.
;; Received 239 bytes from 192.168.1.1#53(192.168.1.1) in 12 ms

com.                    172800  IN      NS      a.gtld-servers.net.
com.                    172800  IN      NS      b.gtld-servers.net.
;; Received 1170 bytes from 198.41.0.4#53(a.root-servers.net) in 96 ms

example.com.            172800  IN      NS      a.iana-servers.net.
example.com.            172800  IN      NS      b.iana-servers.net.
;; Received 692 bytes from 192.5.6.30#53(a.gtld-servers.net) in 108 ms

example.com.            3600    IN      A       93.184.216.34
;; Received 56 bytes from 199.43.135.53#53(a.iana-servers.net) in 124 ms
```

Step 3. Identify each stage. The first block is the root zone's own name server records, fetched so that the tool knows where to start. The second block is the referral from a root server to the .com servers. The third block is the referral from a .com server to the servers for example.com. The final block is the answer from an authoritative server.

Step 4. Note the timing. Each referral costs a round trip, so a cold lookup costs three round trips before any answer arrives. That is precisely why caching matters: a resolver with the answer cached spends zero round trips.

Step 5. Note the lifetimes. The root's own records carry a very long lifetime, the delegation records carry two days, and the final address carries one hour. Long lifetimes high in the tree are safe because delegations change rarely; shorter lifetimes at the leaf let owners make changes.

### 4.5 Task: check where email for a domain is delivered

### 4.6 Implementation: query the mail exchanger records

Step 1. Ask for the mail records of a domain that publishes them.

```bash
dig gmail.com MX +noall +answer
```

Step 2. Read the answer.

```text
gmail.com.              2231    IN      MX      5 gmail-smtp-in.l.google.com.
```

Step 3. Interpret. The number 5 is a preference value: when a domain has several mail exchangers, senders try the lowest number first and use the others only if it fails. The remainder of the record is a host name, not an address, so a further lookup is needed to reach it. This two-step structure is deliberate, because it lets the mail provider move the machine without republishing every domain's records.

### 4.7 Task: prove that a name is only an alias

### 4.8 Implementation: follow a canonical name

Step 1. Query a name that is published as an alias.

```bash
dig www.github.com A +noall +answer
```

Step 2. Read the chain.

```text
www.github.com.         3600    IN      CNAME   github.com.
github.com.             60      IN      A       140.82.121.4
```

Step 3. Interpret. The first record says that www.github.com is not a host at all; it is another label for github.com, and the resolver must continue at that name. The second record supplies the address. The client receives both records so that it does not have to ask again.

Step 4. State the design benefit. One alias record lets a provider rename a service without asking customers to change anything, and it lets a single address record serve many names.

### 4.9 Task: look up the name that belongs to an address

### 4.10 Implementation: a reverse pointer query

Step 1. Ask for the pointer record of a well-known public resolver address using the reverse flag.

```bash
dig -x 8.8.8.8 +noall +answer
```

Step 2. Read the answer.

```text
8.8.8.8.in-addr.arpa.   43187   IN      PTR     dns.google.
```

Step 3. Interpret. The tool reversed the four parts of the address and appended the special suffix in-addr.arpa, because reverse lookups live in a separate branch of the name tree. The answer is a name, not an address. The long lifetime is normal: the mapping from an address to a name changes rarely.

Step 4. Note the limitation. A missing pointer record proves nothing, because publishing one is optional. Never treat the absence of a reverse record as evidence of wrongdoing, and never treat its presence as proof of identity, because the owner of an address controls what it says.

### 4.11 Task: clear a stale cache on Windows and confirm the effect

### 4.12 Implementation: inspect, flush, and re-resolve

Step 1. Look at what the machine currently remembers about a name.

```powershell
ipconfig /displaydns | Select-String -Pattern "example.com" -Context 0,4
```

Step 2. Read a representative excerpt.

```text
    example.com
    ----------------------------------------
    Record Name . . . . . : example.com
    Record Type . . . . . : 1
    Time To Live  . . . . : 3401
    Data Length . . . . . : 4
    Section . . . . . . . : Answer
    A (Host) Record . . . : 93.184.216.34
```

Step 3. Note what the excerpt proves. The record type 1 is the numeric code for an address record. The time to live of 3401 seconds is lower than the 3600 originally published, which shows the countdown in progress. The data is the address.

Step 4. Flush the cache from an administrator Command Prompt.

```powershell
ipconfig /flushdns
```

Step 5. Read the confirmation.

```text
Windows IP Configuration

Successfully flushed the DNS Resolver Cache.
```

Step 6. Re-run the display command and observe that the entry has gone. The next lookup for the name will go to the network again, which is the intended outcome when a site has moved.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to tell whether a lookup succeeded

The status line of a DNS answer tells you most of what you need, if you know the three words that appear there.

NOERROR means the query was understood and answered. It does **not** mean the answer contained an address. A query for a name that exists but has no record of the requested type also returns NOERROR with an empty answer section, and to a beginner that looks like a success. Read the answer section, not just the status.

NXDOMAIN means the name does not exist at all. It is a definitive statement from an authoritative server, not a network failure. If you see NXDOMAIN for a name you believe you registered, the usual cause is either a typo or records that were never published.

SERVFAIL means the server could not complete the job. Unlike NXDOMAIN, this is a failure rather than an answer: an authoritative server may be unreachable, a delegation may be broken, or a security check may have rejected the data. SERVFAIL is the status that most often indicates a genuine fault rather than a typo.

A fourth outcome is common in practice and does not appear in the status line at all: no reply. The tool reports a timeout. That points at a firewall, a blocked port, or a server that is down, and it is a transport problem rather than a naming problem.

### 5.2 Beginner misconceptions

The following beliefs are common, understandable, and wrong. Each one costs marks in an examination and time in real troubleshooting.

- **"DNS is the same as the domain name."** A domain name is an entry in a registry. DNS is the system of servers and records that answers questions about that name. You can own a name and have no working DNS.
- **"There is one central DNS server."** There is no central server. The design is deliberately distributed: root servers, top-level domain servers, authoritative servers and resolvers all hold different pieces.
- **"There are thirteen root servers, so there are thirteen machines."** There are thirteen logical identities, each of which is served by many machines in many countries through anycast. The physical count runs into the thousands.
- **"A failed lookup proves the site is down."** A failure at the naming stage says nothing about the web server. Test the address directly before drawing that conclusion.
- **"Flushing my cache fixes everyone."** It fixes your machine only. Resolvers and routers keep their own caches, and those must expire or be flushed separately.
- **"A short time to live is always better."** Short lifetimes make changes visible quickly and multiply the query load. The right value depends on how often the record changes.
- **"A CNAME record and an A record can sit on the same name."** They cannot. A canonical name excludes every other record at that name, and it cannot be used at the top of a zone.
- **"Mail records contain addresses."** A mail exchanger record contains a host name and a preference number. The address is a separate record.
- **"The reverse lookup is guaranteed to work."** It is optional. Many addresses have no pointer record at all, and the absence proves nothing.
- **"DNS resolves names to web pages."** It resolves names to records. Most records are addresses, and a web page is fetched afterwards over a separate protocol.
- **"Encrypted DNS makes the answer trustworthy."** Encryption hides the conversation from observers. It does not prove that the answer is correct; that requires a separate signing system.
- **"Changing the record works immediately."** It works immediately for anyone who asks a server that has no cached copy. Everyone else keeps the old answer until the lifetime expires.

### 5.3 A sensible troubleshooting order

When a name will not resolve, work from the closest layer outwards rather than guessing. The order below reflects where faults actually occur most often.

1. Check the spelling and the exact name. A single missing letter produces a perfectly correct NXDOMAIN.
2. Check whether other names resolve. If nothing resolves, the fault is the local network or the configured resolver, not the domain.
3. Ask a different resolver for the same name. If the answer differs, you have found a stale or poisoned cache.
4. Ask the authoritative server directly, which you can do by naming it in the lookup. If it answers correctly, the domain is fine and the fault is in caching.
5. Check the parent delegation by querying the top-level domain servers. If the delegation points at the wrong servers, nothing downstream can work.
6. Flush the local cache and repeat. If that fixes it, the fault was a stale local entry.
7. Only then suspect the destination: a firewall, a broken server, or a service that is genuinely down.

The value of the order is that each step eliminates a whole class of cause, so a diagnosis is reached in a few commands instead of a long experiment.

### 5.4 What the caching layers teach about design

The four cache levels are not redundancy for its own sake. Each one exists because the cost of asking a remote server is paid far too often otherwise.

The browser cache saves the cost of a system call for the many names a single page references. The operating system cache saves the cost of a network round trip for every application on the machine. The router cache saves the cost of a trip to the ISP for every device in the home. The resolver cache saves the cost of walking the hierarchy for every customer of that provider. Remove any one of them and the system still works, but it becomes slower and the servers above it become overloaded.

The design principle is worth stating in one sentence: put a copy of the answer as close to the asker as possible, and attach an expiry date so the copy cannot live forever. That principle appears again in content delivery networks, in web proxy caches, and in almost every large-scale system you will meet later in this course.

### 5.5 Security in plain terms

Three attacks are worth knowing at this level, because each one exploits a property that is otherwise a strength.

**Cache poisoning** exploits trust. A resolver accepts the first plausible answer it receives for a question it asked, and remembers it. If an attacker can slip a forged answer in ahead of the real one, the resolver will hand that wrong address to everyone who asks for the lifetime of the record. The defence is to make a forged answer hard to produce: the resolver chooses an unpredictable query identifier and an unpredictable source port, so the attacker must guess both. Signing the data, through the system known as the Domain Name System Security Extensions, abbreviated DNSSEC, goes further and lets the resolver verify that the answer really came from the zone owner.

**Spoofing** is the general form of the same trick: sending a reply that pretends to come from a server you are not. The same two random values defend against it.

**Distributed denial of service**, abbreviated DDoS, exploits the fact that a small query can produce a much larger answer. An attacker who can send queries that appear to come from a victim's address can make many servers send large answers to that victim. The defences are to spread the service across many locations with anycast, so no single site absorbs the whole flood, and to refuse to answer queries from addresses that could not legitimately have sent them.

None of these attacks requires the attacker to break encryption. That is why the defences are described in terms of unpredictability, verification and distribution rather than secrecy.

### 5.6 Key takeaways

DNS translates names into the data that networks need, chiefly addresses, and it does so through a hierarchy that no single organisation owns. A name is read from the right, through the root, a top-level domain, a registered domain and any subdomains the owner creates. Four server roles cooperate: the stub resolver that asks, the recursive resolver that does the work, the hierarchy of root and top-level domain servers that refer, and the authoritative servers that answer. Recursion happens at the top of the chain and iteration at the bottom. Records carry a type and a lifetime, and the lifetime is what makes caching possible and change slow. Port 53 carries both UDP and TCP. The same properties that make the system fast — trust in the first answer and copies held everywhere — are what the attacks exploit, and the defences are unpredictability, verification and distribution.


