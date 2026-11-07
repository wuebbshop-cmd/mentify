## 1. Concept and Use Case

### 1.1 What questions on this topic actually test

Examination questions on Internet fundamentals are almost never about history or product names. They test four distinct abilities, and every past-style question maps onto one of them. Recognising which ability is being tested tells you the shape of the answer before you write a word.

The first is **recall of a numbered or named fact**: a default port, a layer name, a data-unit name, the altitude of a geostationary satellite, the maximum rate of a dial-up modem. These marks are cheap and are lost through carelessness rather than ignorance. They should be collected first and quickly.

The second is **description of an architecture**: the three classes of physical equipment, the four layers, the two addressing schemes, the three provider tiers. These answers are marked by counting named components and stated functions. A candidate who writes fluent prose naming two components out of three scores two marks, not four.

The third is **comparison on stated axes**. Questions here almost always name the axes: bandwidth, latency, reliability and cost. The marking scheme awards one mark per correct, distinct point of difference, so a labelled table earns more than a paragraph that circles the same idea.

The fourth is **applied reasoning**: given a requirement, choose a technology and justify it; given a symptom, name the layer and the next test. These marks are awarded for the stated link between the fact and the scenario. The fact alone scores nothing here.

### 1.2 The definition that earns full marks

A weak answer says that the Internet is a big network connecting computers. A full-mark answer contains three separable components, and a typical definition question carries three or four marks.

The first component is that the Internet is a **global network of interconnected networks**. The phrase "network of networks" is the one examiners look for, because it carries the idea that no single organisation owns or operates the whole system. A message crosses several separately administered networks, each with its own equipment and staff.

The second component is that the networks are joined by a **common protocol family, chiefly TCP/IP**, short for Transmission Control Protocol and Internet Protocol. Interconnection is possible because every participant agrees on addressing, on forwarding and on transport behaviour. Agreement on protocols, not shared ownership, is what makes the parts behave as one system.

The third component is that the Internet is a **general-purpose carrier of computing resources and services**. It does not know whether it carries a web page, an electronic mail message, a voice call, a file transfer or a software update, and the same forwarding infrastructure serves all of them.

A fourth sentence, worth a mark when the question says "explain", states the consequence: because the network is neutral in the middle and intelligent at the edges, new services can be deployed by changing only the endpoint software, without upgrading the intervening infrastructure.

### 1.3 Where the marks sit

An analysis of the way this topic is marked produces a consistent distribution, and knowing it tells you where to spend your time in the examination room.

| Category of mark | Share of the total | How it is earned |
|---|---|---|
| Naming a component, layer, protocol or port | About 40 per cent | One mark per correct named item, written precisely |
| Describing a sequence or a mechanism | About 30 per cent | Ordered steps, each naming what happens and why |
| Stating a reason, consequence or trade-off | About 20 per cent | A link from a design property to an effect |
| Correct terminology and units | About 10 per cent | Saying megabits per second, round-trip time, geostationary orbit |

The practical implication is that naming comes first because it is fastest, sequence comes second because it is mechanical once memorised, and reasoning comes third because it is what separates a pass from a distinction. A candidate who spends fifteen minutes on a beautiful introduction and then lists six technologies without any axes has spent the time in the wrong place.

### 1.4 The shapes of questions asked

Five question shapes recur. Each has a predictable structure and a predictable marking pattern.

| Shape | Typical wording | What earns the marks |
|---|---|---|
| Define and describe | "Define the Internet and describe the physical infrastructure that supports it" | Three-part definition plus named components with functions |
| Compare and justify | "Compare any four connection technologies on bandwidth, latency, reliability and cost, and recommend one for a stated requirement" | One mark per correct comparison point, one for a justified recommendation |
| Explain the model | "Explain the four layers of TCP/IP and the role of each" | Layer name, protocol, data unit, addressing, one sentence of function |
| Diagnose | "A user reports that web pages are slow but file downloads are fast; explain the likely cause and the tests you would run" | Named layer, named tool, expected output, interpretation |
| Discuss | "Discuss the advantages of the Internet architecture and its impact on society" | Four advantages tied to design properties, plus balanced impacts |

The command word is the instruction. "State" wants a named fact. "Describe" wants a named fact plus its function. "Explain" wants a mechanism in order. "Compare" wants axes and differences. "Discuss" wants both sides and a judgement. Writing a description where a comparison was asked is the most common way to lose half the available marks while writing a great deal.

### 1.5 The scenario bank the questions are built from

Examiners rarely ask for a technology in the abstract. The question is dressed as a situation, and the situation contains the constraint that selects the answer.

A rural clinic has no cable and unreliable electricity, needs to send small records daily and hold occasional video consultations. The constraint is the absence of fixed infrastructure, so the answer is a wireless or satellite link; the video requirement then forces a discussion of delay, which rules out a geostationary system for the consultations if a low-orbit or terrestrial wireless option exists.

A household of four shares one connection and complains that video calls break up at eight in the evening. The constraint is the shared segment and the upstream rate, so the answer discusses contention ratio and a symmetric link rather than headline download speed.

A small business wants to host its own web server on the premises. The constraint is inbound reachability, so the answer must raise network address translation, the public address and the provider's terms, not merely the bandwidth.

A student's laptop reports a name error for every site while a numeric address still works. The constraint is that addressing and routing are healthy, so the answer isolates name resolution and the configured name servers.

A supplier must send a 4 gigabyte archive overnight. The constraint is capacity within a time window, so the answer computes the required sustained rate and then compares technologies on that basis rather than on peak figures.

## 2. Data, Syntax, and Core Concepts

### 2.1 High-yield facts and the marks they carry

The following facts appear most often. Learn them as a set, because each is worth one or two marks on its own and together they cover most short-answer papers.

| Fact | Typical marks |
|---|---|
| The Internet is a global network of networks using a common protocol family | 1 to 2 |
| The World Wide Web is one application on the Internet, not a synonym | 2 |
| Physical infrastructure has transmission lines, routers and high-bandwidth backbone hubs | 3 |
| An ISP is the organisation connecting a customer to the rest of the Internet | 1 |
| Providers are described as Tier 1, Tier 2 and Tier 3 | 3 |
| Six access technologies: dial-up, DSL, cable, wireless, satellite, fibre | 6 |
| The TCP/IP model has four layers: application, transport, internet, link | 4 |
| The data unit at each layer is message, segment or datagram, packet, frame | 4 |
| Addressing is by name, port number, IP address and hardware address | 4 |
| A geostationary satellite imposes about 500 milliseconds of round-trip delay | 2 |
| Dial-up peaks at 56 kilobits per second and occupies the telephone line | 2 |
| Fibre carries light, has the lowest loss and is immune to electrical interference | 2 |
| Bandwidth and latency are independent quantities | 2 |
| HTTP is port 80 and HTTPS is port 443 | 2 |

### 2.2 The physical infrastructure, stated the way it is marked

Three functional classes of equipment carry the Internet, and each has a one-sentence definition worth a mark.

**Transmission lines** carry the signal between two points. They are twisted copper pairs, coaxial cable, fibre-optic strands and radio paths. Their capacity, attenuation and susceptibility to interference set the physical limit on every layer above.

**Routers** are the packet switches at junctions. A router holds a routing table, reads the destination address of each arriving packet, selects the matching entry and forwards the packet out of the corresponding interface. It does not track applications or conversations.

**High-bandwidth backbone hubs** are the long-haul links and the interconnection points where major networks exchange traffic. The historical backbone was a small number of very fast national links. The modern equivalent is a mesh of providers meeting at Internet Exchange Points, abbreviated IXP, where they exchange traffic directly rather than paying a third party to carry it. Submarine cables form a large part of this long-haul capacity.

| Component | Function | Failure effect |
|---|---|---|
| Transmission line | Carries the signal between two points | Loss of that path only; traffic may reconverge |
| Router | Forwards packets by destination address | Loss of reachability to the networks behind it |
| Backbone link or exchange point | Interconnects large networks | Regional congestion or partition |

A strong answer adds the reason this arrangement is resilient. Because forwarding decisions are made independently at each router from a local table, the failure of one link is absorbed by the routers adjacent to it. No central controller has to issue new instructions, so recovery is automatic and local.

### 2.3 Providers and connection tiers

An **Internet Service Provider**, abbreviated **ISP**, is the organisation that connects an end customer to the rest of the Internet, and earns a mark for that definition alone. Two further points commonly earn a mark each: the ISP carries the customer's traffic across its own network before handing it to another provider, and every access path, including a public wireless hotspot and a mobile tower, still terminates at an ISP.

| Tier | What it owns or buys | How it reaches the rest of the world | Typical customer |
|---|---|---|---|
| Tier 1 | Global long-haul capacity | Settlement-free peering with other Tier 1 networks | Tier 2 providers |
| Tier 2 | Regional or national network | Buys transit from Tier 1, peers with other Tier 2 providers | Tier 3 providers, large enterprises |
| Tier 3 | Local access network | Buys transit from the tiers above | End customers |

The examinable consequence is that connection quality depends on peering as well as on the local access technology. Congestion typically arises where two networks exchange traffic, which is why a connection can be excellent to one destination and poor to another at the same moment.

### 2.4 Six access technologies, compared on the four examinable axes

Each technology is a different answer to the same question: how is data carried across the local loop, the segment between the customer's premises and the provider's nearest equipment?

**Dial-up** modulates digital data into audible tones over the ordinary telephone pair. It occupies the line for the whole session, so a telephone call and a session cannot coexist. The maximum rate is 56 kilobits per second, achieved only on a clean line, and connection setup takes twenty to thirty seconds.

**DSL**, short for **Digital Subscriber Line**, also uses the telephone pair but transmits at frequencies above the speech band, so voice and data coexist. Residential service is normally asymmetric, with a much higher downstream rate, which matches browsing behaviour. Rate falls with distance from the provider's cabinet because higher frequencies attenuate faster in copper.

**Cable** uses the coaxial cable of a television network with a cable modem. The nominal rate is high, but the segment is shared among the households attached to it, so achieved throughput falls at peak times. This sharing is quantified as a contention ratio.

**Wireless** access uses radio, either a cellular network or a fixed link to an antenna. It requires no cabling to the premises, which makes it the practical choice where copper and glass are absent, but quality depends on distance, on obstacles and on the number of users sharing the cell.

**Satellite** access links the premises to an orbiting transponder. A geostationary satellite at about 35,800 kilometres altitude produces a round-trip propagation delay of roughly 500 milliseconds, because the signal travels up and back before it goes anywhere useful. Low-earth-orbit constellations at a few hundred kilometres reduce that delay to tens of milliseconds at much greater system cost.

**Fibre optics** carries data as pulses of light in a glass strand. It offers the highest capacity, the lowest attenuation over distance and immunity to electromagnetic interference. Capacity is raised by changing the equipment at each end rather than by replacing the cable, which is why fibre is the medium of choice for new backbone and access build-out.

| Technology | Bandwidth | Latency | Reliability | Cost |
|---|---|---|---|---|
| Dial-up | Up to 56 kilobits per second | High, 150 to 200 milliseconds | Poor; exclusive use of the line | Lowest monthly, but metered call time in some markets |
| DSL | A few to tens of megabits per second, asymmetric | 20 to 40 milliseconds | Good; distance dependent | Low to medium |
| Cable | Tens to hundreds of megabits per second, shared | 10 to 25 milliseconds | Good, but peak-hour contention | Medium |
| Wireless | A few to hundreds of megabits per second, load dependent | 20 to 60 milliseconds | Variable with distance and interference | Medium |
| Satellite | Tens of megabits per second | About 500 milliseconds geostationary; tens of milliseconds low orbit | Weather sensitive | High |
| Fibre | Hundreds of megabits to several gigabits per second | 2 to 15 milliseconds | Highest; immune to electrical interference | Medium to high to install, low to run |

Three sentences convert that table into marks. Fibre wins on bandwidth, latency and reliability but costs most to install. Cable offers high bandwidth at medium cost but shares capacity, so it degrades at peak. Satellite is the only option where no terrestrial infrastructure exists, and its delay, not its rate, is what limits its suitability for interactive work.

### 2.5 The TCP/IP suite and the four-layer model

The suite is described as four layers. Each layer provides a service to the layer above and uses the service of the layer below, and each has a name, protocols, a data unit and an addressing scheme. All four columns are examinable and each is normally worth a mark.

| Layer | Principal protocols | Data unit | Addressing |
|---|---|---|---|
| Application | HTTP, HTTPS, DNS, SMTP, FTP, SSH, IMAP, POP3 | Message | Names, URLs, service names |
| Transport | TCP, UDP | Segment for TCP, datagram for UDP | Port number |
| Internet | IP version 4, IP version 6, ICMP | Packet | IP address |
| Link, also called network access | Ethernet, Wi-Fi, PPP, optical framing | Frame | Hardware or MAC address |

The value of the model is that it localises change. A new application protocol requires no change to IP. A new link technology requires no change to TCP. This is the structural form of the principle that the network is simple in the middle and intelligent at the edges.

Three addressing schemes appear in that table and must never be conflated. An **IP address** identifies an interface globally and is used by routers to forward packets between networks. A **MAC address**, short for Media Access Control address, identifies an interface on a single link and is used only within that link. A **port number** identifies a process on a host, which is how one address can serve a web server, a mail server and a name server simultaneously.

The four layers are frequently confused with the seven-layer **Open Systems Interconnection** reference model, abbreviated OSI. The OSI model subdivides the same work more finely and is a legitimate teaching reference, but the working Internet is built on TCP/IP. An answer that names seven layers and then claims TCP sits at layer four of that stack, without distinguishing the two models, reads as inconsistent and loses the terminology mark.

### 2.6 Encapsulation, the mechanism that makes layering real

When an application sends data, each layer adds its own header. The application message becomes a transport segment with a transport header in front. The segment becomes an IP packet with an IP header in front. The packet becomes a frame with a link header in front and a trailer behind. At the receiving end each layer removes its own header and passes the remainder upward.

Two facts follow, and both earn marks. First, the IP addresses in the header do not change from source to destination, while the link-layer addresses change at every hop. This is precisely what allows the system to be a network of independent networks: each link can use its own technology and its own hardware addressing, because the global decision is carried unchanged inside. Second, an error at one layer is often reported as a symptom at a higher one, because the higher layer simply never receives the data it expected. That is why diagnosis proceeds layer by layer.

### 2.7 Addressing facts that questions assume

An IPv4 address is a 32-bit number written as four decimal octets separated by dots, for example 196.201.1.9. The network portion and host portion are separated by the subnet mask. A host whose destination is inside its own subnet delivers directly; a host whose destination is outside sends to its default gateway.

Three ranges are reserved for private use and are never routed on the public Internet: 10.0.0.0 to 10.255.255.255, 172.16.0.0 to 172.31.255.255, and 192.168.0.0 to 192.168.255.255. Every device on a home network therefore holds a private address, and the router performs **Network Address Translation**, abbreviated **NAT**, so that all of them share the single public address assigned by the provider. NAT rewrites the source address of outgoing packets and remembers which internal host each reply belongs to.

Two consequences are commonly examined. NAT conserves public IPv4 addresses and incidentally blocks unsolicited inbound connections, which is a security benefit and a barrier to hosting a server on the premises. IPv6, with 128-bit addresses written as eight groups of four hexadecimal digits, removes the need for translation because every device can hold a globally routable address. During the transition both versions run on the same infrastructure, which is why name records exist in both A form for IPv4 and AAAA form for IPv6.

### 2.8 Ports and services, with the correct defaults

Port numbers are the transport layer's addressing scheme, and misquoting one is an avoidable loss. The following table is the complete set this topic requires.

| Service | Protocol | Default port |
|---|---|---|
| File Transfer Protocol | FTP | 20 for data in active mode and 21 for control |
| Secure Shell | SSH | 22 |
| Telnet | Telnet | 23 |
| Simple Mail Transfer Protocol | SMTP | 25 |
| Domain Name System | DNS | 53 |
| Hypertext Transfer Protocol | HTTP | 80 |
| Post Office Protocol version 3 | POP3 | 110 |
| Internet Message Access Protocol | IMAP | 143 |
| Hypertext Transfer Protocol Secure | HTTPS | 443 |

Two clarifications prevent common errors. First, FTP uses two ports, and the pair is 20 and 21, not 21 and 22; port 22 belongs to SSH. Second, HTTPS is 443 and IMAP is 143; transposing those two digits turns a correct answer into a wrong one.

### 2.9 The numbers worth memorising

| Quantity | Value | Where it is used |
|---|---|---|
| Maximum dial-up rate | 56 kilobits per second | Comparison of access technologies |
| Geostationary altitude | About 35,800 kilometres | Explaining satellite delay |
| Geostationary round-trip delay | About 500 milliseconds | Justifying rejection of satellite for interactive work |
| Speed of light in fibre | About 200,000 kilometres per second | Converting measured delay into a path length |
| IPv4 address length | 32 bits | Addressing questions |
| IPv6 address length | 128 bits | Addressing questions |
| Bits in a byte | Eight | Converting megabits per second to megabytes per second |
| Typical wired round-trip time in a city | 5 to 20 milliseconds | Interpreting a ping result |
| Typical intercontinental round-trip time | 80 to 150 milliseconds | Interpreting a ping result |

## 3. Methods and Operations

### 3.1 The command inventory, and what each command can prove

Diagnostic questions are marked on the choice of test and on the interpretation, not on remembering exotic options. Six commands cover the whole topic.

| Command | What it proves | What it cannot prove |
|---|---|---|
| `ping` | Reachability and round-trip time to an address | Bandwidth, or that a service is running |
| `tracert` on Windows or `traceroute` elsewhere | The sequence of routers and where delay is added | The cause of loss at any single hop |
| `nslookup` | Whether a name resolves and to which address | Whether the resolved host serves the service |
| `curl -I` | That the application answers, and with which status code | The end-to-end experience in a browser |
| `Get-NetIPConfiguration` | Local address, gateway and name servers | Whether the path beyond the gateway works |
| `Get-NetTCPConnection` | Which ports the local host is listening on | Whether a remote host is reachable |

Two interpretation rules carry marks. A failed echo request does not prove a host is down, because firewalls commonly suppress the protocol used by `ping`. And loss reported at one hop only, which disappears at later hops, indicates that a router is rate-limiting its own error messages rather than dropping user traffic.

### 3.2 A diagnostic procedure that maps symptoms to layers

Diagnosis is marked as a sequence, so it is worth having a fixed order. Test from the inside outwards, so that each test eliminates one layer.

| Symptom | Likely layer | Next command | What a positive result rules out |
|---|---|---|---|
| No connection at all, no local address | Link | `Get-NetIPConfiguration` | Nothing yet; the local link is the fault |
| Gateway does not answer | Link or local router | `ping` the gateway address | The provider and everything beyond |
| Numeric address fails but the gateway answers | Internet | `ping 8.8.8.8` | The local link and the router |
| Numeric address works but names fail | Application, name resolution | `nslookup` a known name | Addressing and routing |
| Name resolves but no page appears | Transport or application | `curl -I` the address | Name resolution |
| Page appears but is slow | Capacity or contention | Repeat a transfer at different times | A total outage |
| Some sites fast, others slow | Peering or the far server | Trace to both destinations | Your own access link |

The value of the table in an answer is that it converts a vague instruction such as "check the connection" into a named test with a stated expectation. Examiners award the expectation as much as the command.

### 3.3 Building an answer: definition, mechanism, consequence

Almost every explanation mark can be earned with a three-move structure, which is worth practising until it is automatic.

Move one is the **definition**: name the thing precisely, in one sentence, using the terminology of the topic. "A router is a packet switch that forwards by destination address" is a definition.

Move two is the **mechanism**: say what it does, in order, naming the parts. "It reads the destination address of each packet, looks the address up in its routing table, selects the most specific matching entry, and forwards the packet out of the corresponding interface."

Move three is the **consequence**: say why it matters. "Because decisions are local, no central controller is needed, which is why the network survives the failure of individual links."

Three moves, three likely marks. A candidate who writes only move one has written a glossary entry, not an answer.

### 3.4 Building a comparison answer

Comparison questions are marked point by point against the axes in the question. Use the axes as headings and never merge them.

1. Draw a table with one row per technology and one column per named axis.
2. Fill each cell with a comparative statement, not an adjective. "About 500 milliseconds, dominated by propagation" is a point; "slow" is not.
3. Add a short paragraph after the table naming the two clearest separations, for example that fibre and cable differ mainly in shared capacity, while satellite differs mainly in delay.
4. Answer the recommendation explicitly, and tie it to the requirement in the question rather than to a general preference.
5. State one disadvantage of the recommended option, because a recommendation with no acknowledged cost reads as unsupported.

### 3.5 The trap table

The following errors account for most lost marks in this topic. Each row states the trap, why it costs marks, and the correct statement to write instead.

| Trap | Why it loses marks | Correct statement |
|---|---|---|
| Treating the Web as the Internet | Collapses two examinable concepts into one | The Web is one application on the Internet; email, DNS and FTP are Internet services that do not need it |
| Saying the Internet is owned by nobody, therefore unmanaged | Overstates the case and contradicts the existence of standards | No single owner, but standards bodies publish the protocols and providers manage their own networks |
| Listing only cables when asked for physical infrastructure | The question asks for three classes of equipment | Transmission lines, routers and high-bandwidth backbone hubs, each with a function |
| Describing an ISP as a search engine or a website | Confuses the access provider with a service | An ISP is the organisation that connects a customer to the rest of the Internet |
| Claiming satellite is unsuitable because it is slow | Delay, not rate, is the constraint | Satellite capacity can be adequate; propagation delay of about 500 milliseconds defeats interactive use |
| Saying DSL and dial-up are the same because both use the telephone line | Misses the frequency-division distinction | DSL uses frequencies above the speech band, so voice and data coexist; dial-up occupies the line |
| Naming four layers but six data units | The data unit must match the layer | Message, segment or datagram, packet, frame for application, transport, internet and link |
| Confusing an IP address with a MAC address | Two different scopes are being merged | IP is global and unchanged across the journey; MAC is per link and changes at each hop |
| Claiming a failed ping proves the host is down | Ignores deliberate suppression of echo requests | Firewalls commonly suppress ICMP, so test the actual service before concluding |
| Reading one hop's reported loss as a fault | Misreads router error-message rate limiting | Loss that disappears at later hops is not user-traffic loss |
| Equating bandwidth with speed | Latency is left unexplained | Bandwidth limits bulk transfer; latency limits how quickly one request is answered |
| Quoting FTP as port 21 only, or as 21 and 22 | Wrong pair | FTP uses 20 for data in active mode and 21 for control; 22 is SSH |
| Transposing HTTPS 443 and IMAP 143 | One digit error, one lost mark | HTTPS is 443, IMAP is 143 |
| Mixing the OSI seven-layer model with TCP/IP | Inconsistent framework | State which model you are using and stay with it |
| Asserting UDP is defective because it is unreliable | Misreads a deliberate design choice | UDP omits guarantees so that real-time traffic need not wait for retransmission |
| Recommending fibre without acknowledging cost | Unsupported recommendation | Fibre wins on all technical axes but costs most to install and is not always available |

### 3.6 Reading command output in an answer

Marks for interpretation are awarded for naming the signal and then explaining it. The following table is the vocabulary to use.

| Observation | What it indicates | What to write |
|---|---|---|
| Four replies, zero loss, steady times | Healthy path with little jitter | The path is delivering packets and the delay is stable |
| Replies but widely varying times | Congestion or a wireless link | Jitter is high, which will affect real-time traffic |
| No replies from a name but replies from a numeric address | Name resolution failure | Addressing and routing are healthy; the resolver is at fault |
| A large step in delay between two hops | A long-haul link, not a fault | The step reflects propagation over distance |
| Loss at one hop that vanishes later | Router rate limiting of error messages | Not evidence of user-traffic loss |
| A status code beginning with 4 | Client-side request problem | The server is reachable and refused the specific request |
| A status code beginning with 5 | Server-side failure | The path and the service are reachable but the application failed |
| A local address in a private range plus a different public address | Translation in use | The router holds the public address and rewrites source addresses |

## 4. Worked Implementation from the Notes

### 4.1 Task: an eight-mark answer defining the Internet and describing its infrastructure

### 4.2 Implementation: build the answer in marked steps

Step 1. Open with the three-part definition. Do not begin with history.

"The Internet is a global network of interconnected computer networks that communicates using a common family of protocols, chiefly TCP/IP. It is a network of networks: no single organisation owns or operates it end to end. It is a general-purpose carrier, in that the same infrastructure carries web pages, electronic mail, voice and file transfer without distinguishing between them."

Marking point: one mark for "network of networks", one mark for the common protocol family, one mark for general-purpose carriage. A candidate who writes only "a global network of computers" earns none of the three, because none of the distinguishing properties is present.

Step 2. Name the first class of physical equipment with its function.

"Transmission lines carry the signal between two points. They include twisted copper pairs, coaxial cable, fibre-optic strands and radio paths. Their capacity and their loss over distance set the physical limit on everything above them."

Marking point: one mark for naming transmission lines, one for stating that they carry the signal and that their characteristics bound performance.

Step 3. Name the second class.

"Routers are the packet switches at junctions. Each router holds a routing table, reads the destination address of an arriving packet, selects the matching entry and forwards the packet out of the corresponding interface. A router does not inspect the application payload and does not retain per-conversation state."

Marking point: one mark for naming routers, one for the forwarding-by-destination-address function.

Step 4. Name the third class.

"High-bandwidth backbone links and the exchange points where major networks meet provide long-haul capacity between regions. Historically this was a small number of very fast national links; today it is a mesh of providers interconnecting at Internet Exchange Points, together with submarine cables that carry most intercontinental traffic."

Marking point: one mark for backbone links or hubs, one for identifying them as the interconnection layer between large networks.

Step 5. Explain why the three cooperate rather than merely coexist.

"Because each router decides independently from a local table, and because the destination address in the packet header is unchanged while the link-layer address is rewritten at every hop, the three classes of equipment compose into one system without a central controller."

Marking point: one mark for stating that the address unchanged across the journey and the hardware address per hop is what permits independent networks to interoperate. This is the sentence that turns a list into an explanation, and it is the sentence most candidates omit.

Step 6. Close with the consequence that the question implies.

"The result is resilience through redundancy and application neutrality, which is why a new service can be deployed without changing the intervening infrastructure."

Marking point: one mark for a stated consequence linked to the description. Total available: eight marks, all earned, because each component is named and each function is stated in one sentence.

Step 7. Check the answer against the command word. The question said "describe", so each component needed its function, not merely its name. If the question had said "state", the three names alone would have sufficed and the extra prose would have cost time rather than earned marks.

### 4.3 Task: a ten-mark comparison answer with a justified recommendation

### 4.4 Implementation: answer in table form, then justify in prose

Step 1. State the requirement in the answer's first line, so the recommendation has an anchor.

"The clinic has no cable infrastructure, needs to transfer small records daily and intends occasional video consultations."

Marking point: one mark for restating the constraint. It looks trivial and it is frequently omitted, which leaves the later recommendation unsupported.

Step 2. Compare on the four named axes in a table.

| Technology | Bandwidth | Latency | Reliability | Cost |
|---|---|---|---|---|
| Dial-up | Up to 56 kilobits per second | 150 to 200 milliseconds | Poor; occupies the telephone line | Lowest |
| DSL | A few to tens of megabits per second | 20 to 40 milliseconds | Good, but distance limited | Low to medium |
| Satellite, geostationary | Tens of megabits per second | About 500 milliseconds | Weather sensitive | High |
| Fibre | Hundreds of megabits to several gigabits per second | 2 to 15 milliseconds | Highest | High to install, low to run |

Marking point: one mark per correct, distinct cell comparison, up to six marks. Marks are awarded for comparative content, so a cell reading "fast" earns nothing while "hundreds of megabits per second" earns the mark.

Step 3. Add the two separations that the table does not make obvious.

"The decisive difference between cable and fibre is shared capacity: a cable segment is contended among its households, whereas a fibre point-to-point link is not. The decisive difference between satellite and the terrestrial options is delay, not rate, because the geostationary round trip of about 500 milliseconds is set by physics and cannot be improved by adding capacity."

Marking point: one mark for identifying contention as the cable limitation, one mark for identifying propagation delay rather than bandwidth as the satellite limitation.

Step 4. Recommend, with the reason attached.

"For the records transfer, a low-orbit satellite link is adequate because a daily batch tolerates delay. For the video consultations, delay must be bounded, so terrestrial wireless or fibre is required; if only geostationary satellite is available, the consultations should be scheduled by voice instead, because a 500 millisecond round trip makes conversational video unpleasant."

Marking point: one mark for a recommendation matched to the stated requirement, one mark for acknowledging the alternative and its cost. Ten marks in total.

Step 5. Check that no claim is left as an adjective. Every comparative statement in the answer names a quantity or a mechanism, which is what the marking scheme rewards.

### 4.5 Task: a six-mark answer on the layered model with command evidence

### 4.6 Implementation: state the model, then demonstrate it on a real host

Step 1. Present the four layers with all four attributes, because the marking scheme counts each column.

"The TCP/IP suite has four layers. The application layer carries HTTP, DNS, SMTP and FTP and exchanges messages addressed by name. The transport layer carries TCP and UDP, exchanges segments or datagrams, and addresses them by port number. The internet layer carries IP and exchanges packets addressed by IP address. The link layer carries Ethernet or Wi-Fi and exchanges frames addressed by hardware address."

Marking point: one mark per layer for which the layer, protocol, data unit and address are all correct. A layer with a correct name and a wrong data unit earns nothing for that layer.

Step 2. Demonstrate the internet and link layers on a host.

```powershell
Get-NetIPConfiguration
```

```text
InterfaceAlias       : Wi-Fi
InterfaceIndex       : 12
InterfaceDescription : Intel(R) Wireless-AC 9560 160MHz
NetProfile           : HomeNet
IPv4Address          : 192.168.1.24
IPv4DefaultGateway   : 192.168.1.1
DNSServer            : 192.168.1.1
```

Marking point: one mark for interpreting the output correctly, namely that 192.168.1.24 is a private address, that 192.168.1.1 is the first-hop router, and that the name server is a separate configured service.

Step 3. Demonstrate the transport layer on the same host.

```powershell
Get-NetTCPConnection -State Listen | Select-Object -First 6 LocalAddress, LocalPort, OwningProcess
```

```text
LocalAddress LocalPort OwningProcess
------------ --------- -------------
0.0.0.0             80          4120
0.0.0.0            443          4120
127.0.0.1           53          2140
0.0.0.0           3000          8812
```

Marking point: one mark for explaining that a single address serves several services distinguished only by port number, which is the observable form of transport-layer addressing.

Step 4. State the encapsulation mechanism in one sentence, because it is the part that explains why the model is useful.

"Each layer prepends its own header, so an application message becomes a transport segment, then an IP packet, then a link frame; the receiving host strips one header per layer on the way up, which is why a fault at one layer appears as a missing input at the next."

Marking point: one mark for the ordered encapsulation and decapsulation description.

### 4.7 Task: an eight-mark diagnosis of a slow connection

### 4.8 Implementation: run the tests in layer order and interpret each result

Step 1. Restate the symptom precisely and note what it already excludes.

"Pages are slow while large downloads complete quickly. Because bulk transfer is satisfactory, capacity is not the limiting factor, so the fault lies in delay, in name resolution or in per-request overhead rather than in bandwidth."

Marking point: one mark for excluding bandwidth from the evidence already given. This is the reasoning mark that most candidates miss.

Step 2. Measure delay to the gateway and to a public address.

```powershell
ping -n 4 192.168.1.1
ping -n 4 8.8.8.8
```

```text
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=214ms TTL=117
Reply from 8.8.8.8: bytes=32 time=382ms TTL=117
Reply from 8.8.8.8: bytes=32 time=511ms TTL=117
Reply from 8.8.8.8: bytes=32 time=289ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 214ms, Maximum = 511ms, Average = 349ms
```

Marking point: one mark for reading the measurements correctly. Zero loss shows packets are delivered; the wide spread from 214 to 511 milliseconds is jitter of nearly 300 milliseconds, which is consistent with a congested or interference-affected wireless link rather than with a long path.

Step 3. Trace the path to locate where the delay is introduced.

```powershell
tracert -h 8 8.8.8.8
```

```text
Tracing route to 8.8.8.8 over a maximum of 8 hops

  1   180 ms   240 ms   196 ms  192.168.1.1
  2   195 ms   263 ms   221 ms  10.20.0.1
  3   212 ms   389 ms   247 ms  196.201.1.9
  4   220 ms   401 ms   255 ms  195.66.224.20
  5   231 ms   377 ms   268 ms  8.8.8.8

Trace complete.
```

Marking point: one mark for the decisive observation, which is that the delay is already present at hop 1, the local router. Delay that appears before the provider's network cannot be caused by the provider or by the far server.

Step 4. Test the application layer, to separate delay from service failure.

```bash
curl -I https://example.com
```

```text
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Connection: close
```

Marking point: one mark for concluding that the service is healthy, since a 200 response proves name resolution, connection setup, the encrypted session and the server application all worked.

Step 5. Name the cause, the layer and the remedy.

"The fault is at the link layer, on the wireless link between the client and its own router, evidenced by 180 to 240 milliseconds of delay at the first hop and by jitter approaching 300 milliseconds. The remedy is to move the client closer to the access point, change the radio channel to avoid interference, or connect by cable; increasing the subscribed bandwidth would not help, because the measurements show that capacity is already sufficient."

Marking point: one mark for naming the link layer, one mark for the remedy, one mark for stating why a bandwidth upgrade would not help. Eight marks total.

Step 6. Check the answer's logic for the trap this scenario is built around. The tempting answer is "the connection is too slow, upgrade the plan", and it is wrong, because the evidence for capacity was never in doubt.

### 4.9 Task: a ten-mark discussion of architectural advantages and societal impact

### 4.10 Implementation: tie every claim to a design property

Step 1. State the four design properties that generate all the advantages. Naming them first gives the answer a spine.

"The architecture has four properties that generate its advantages: open interconnection through published protocols, neutrality towards the traffic carried, redundancy through adaptive routing, and layering with defined interfaces."

Marking point: one mark for each property named, up to four.

Step 2. Convert each property into one advantage with a consequence.

"Open interconnection lowers the barrier to entry, so a small organisation can reach a global audience without negotiating with every intervening network. Application neutrality allows a new service to be deployed by the two endpoints alone, which is why the Web, streaming and conferencing spread without an infrastructure rebuild. Redundancy means a cut cable causes congestion rather than a national outage. Layering allows a fault to be localised to a link, a route or an application, which makes systematic diagnosis possible."

Marking point: one mark for each advantage that names both the property and its consequence, up to four.

Step 3. Present the societal benefits and costs as two sides of the same properties.

"Lower publishing costs widened access to education, health information and markets, and enabled remote work and distributed collaboration. The same openness permits fraud and abuse that no central authority can inspect. Neutrality produced rapid innovation and also concentrated attention in a few platforms. Universal reach reproduced existing inequalities as a digital divide between those with affordable access and those without. Layering distributed responsibility, so each operator can legitimately claim that a fault lies at another layer, which slows the resolution of cross-network problems."

Marking point: one mark for a benefit, one mark for a cost, and one mark for explicitly connecting a cost to the same property that produced a benefit. That last mark is what distinguishes a discussion from two unrelated lists.

Step 4. Close with a judgement, because "discuss" requires one.

"The balance is not accidental. The Internet is efficient precisely because it does not try to police content, guarantee quality or equalise access, so those goals must be pursued by other means, at the endpoints, by providers and by policy, rather than by the network itself."

Marking point: one mark for a defensible judgement that follows from the preceding points rather than contradicting them.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Rewrite drill: seven sentences that lose marks

Each of the following is a sentence students actually write. The correction on the right is what the marking scheme rewards.

| Weak sentence | Corrected sentence | Mark at stake |
|---|---|---|
| "The Internet is the same as the World Wide Web." | "The World Wide Web is one application that runs over the Internet, alongside email, name resolution and file transfer." | 2 |
| "The Internet is fast because it uses fibre." | "Fibre has the highest capacity and lowest attenuation, which raises the ceiling on achievable bandwidth, but end-to-end speed also depends on contention, delay and the far server." | 2 |
| "Satellite is slower so it is useless." | "Satellite capacity can be adequate, but the propagation delay of about 500 milliseconds in geostationary orbit makes it unsuitable for interactive work." | 2 |
| "A router sends data to the right computer." | "A router reads the destination address of each packet, matches it against the most specific entry in its routing table, and forwards the packet out of the corresponding interface." | 1 to 2 |
| "TCP/IP has seven layers." | "The working Internet uses the four-layer TCP/IP model; the seven-layer OSI model is a separate reference framework." | 2 |
| "Ping failed, so the server is down." | "Echo requests may be suppressed by a firewall, so a failure does not establish that the host is down; a request to the actual service is required." | 2 |
| "Bandwidth is the speed of the connection." | "Bandwidth is the maximum data rate; latency is the delay before a response begins; they are independent and limit different activities." | 2 |

The exercise is worth repeating aloud, because the corrected sentence is longer and more precise than the weak one, and candidates under time pressure tend to revert to the shorter form.

### 5.2 Interpreting evidence under time pressure

Three habits produce better interpretation marks than any amount of extra reading.

First, always separate what a test **proves** from what it merely **suggests**. A successful ping proves reachability at that moment on that path. It does not prove that the service is running, that the path will remain stable, or that capacity is adequate.

Second, always convert a measurement into a cause. A round-trip time of 96 milliseconds is a number; a round-trip time of 96 milliseconds implying a path of roughly 19,000 kilometres at 200,000 kilometres per second is an explanation. The arithmetic is not required in full, but the order of magnitude is what earns the reasoning mark.

Third, always check whether the evidence is local or remote. Delay present at the first hop cannot be caused by the provider. Loss that appears at one hop and vanishes later is not user-traffic loss. A name failure with a numeric success is a resolver problem. These three checks resolve most diagnostic questions on their own.

### 5.3 Revision checklist

Work through the list and mark anything you cannot state without notes. The list is ordered by how frequently each item is examined.

- Define the Internet in three components: network of networks, common protocol family, general-purpose carrier.
- Distinguish the Internet from the World Wide Web and give two services that do not use the Web.
- Name the three classes of physical infrastructure and one function for each.
- Explain the difference between transmission lines, routers and backbone exchange points in terms of failure effect.
- Define an ISP and distinguish Tier 1, Tier 2 and Tier 3 providers.
- Name the six access technologies in order from lowest to highest capacity.
- Give the maximum rate of dial-up and explain why it occupies the telephone line.
- Explain how DSL coexists with voice traffic.
- Explain why cable throughput falls at peak times, using the term contention ratio.
- State the geostationary altitude and the resulting round-trip delay.
- State why fibre is immune to electrical interference and how its capacity is upgraded.
- Name the four TCP/IP layers with protocols, data units and addressing.
- Define encapsulation and state which addresses change at each hop.
- Recall the private IPv4 ranges and the purpose of network address translation.
- Recall the nine default ports in the port table without hesitation.
- Explain the difference between bandwidth, latency, jitter and packet loss.
- Describe what `ping`, `tracert`, `nslookup` and `curl -I` each prove and cannot prove.
- State four architectural advantages and connect each to a design property.
- State three societal costs and connect each to the same design property.
- Name the limits: IPv4 exhaustion, best-effort delivery, absent central authority, shared congestion.

### 5.4 Time strategy

The marks for this topic are dense and the answers are short, so time discipline matters more than length.

| Exam length | Marks | Minutes per mark | Suggested split |
|---|---|---|---|
| 1 hour | 40 | About 1.5 | 35 minutes writing, 10 minutes planning across all questions, 15 minutes checking |
| 2 hours | 70 | About 1.7 | 25 minutes on definitions and short answers, 60 minutes on comparisons and explanations, 35 minutes on the discussion question |
| 3 hours | 100 | About 1.8 | 30 minutes on short answers, 90 minutes on structured questions, 40 minutes on the extended answer, 20 minutes checking |

Four rules govern the use of that time. Answer the naming questions first, because they are the fastest marks and they build confidence. Spend no more than one minute of planning per ten marks. Write comparisons as tables, which is faster to produce and easier to mark than prose. And reserve the last few minutes to check every port number and every unit, because those are the errors most easily caught and most easily avoided.

### 5.5 The last-minute sheet

The following ten lines are the minimum needed to attempt any question on this topic.

- Internet equals network of networks plus common protocols plus general-purpose carriage.
- Web equals one application; email, DNS, FTP and SSH do not need it.
- Infrastructure equals transmission lines, routers, backbone links and exchange points.
- ISP equals access provider; tiers one, two and three describe reach and peering.
- Six access technologies: dial-up, DSL, cable, wireless, satellite, fibre.
- Four layers: application, transport, internet, link; message, segment, packet, frame.
- Addresses: name, port, IP, hardware; IP constant across the journey, hardware per hop.
- Delay: about 500 milliseconds geostationary, 20 to 40 milliseconds DSL, 2 to 15 milliseconds fibre.
- Ports: FTP 20 and 21, SSH 22, Telnet 23, SMTP 25, DNS 53, HTTP 80, POP3 110, IMAP 143, HTTPS 443.
- Advantages from four properties; costs from the same four properties.

### 5.6 Phrase bank for full-mark sentences

Certain constructions recur in model answers because they carry a mechanism and a consequence at once.

For definitions: "It is a network of networks, joined by a common protocol family, carrying any service without distinction."

For functions: "It reads the destination address, selects the most specific matching entry in its routing table, and forwards the packet out of the corresponding interface."

For comparisons: "The decisive difference is delay rather than rate, because the round trip is set by propagation distance and cannot be improved by adding capacity."

For diagnosis: "The delay is already present at the first hop, so the fault lies on the local link rather than in the provider's network."

For discussion: "The same property that produces the benefit also produces the cost, which is why the trade-off cannot be removed by design."

Each of those sentences is worth roughly two marks on its own, because each names a mechanism and states its consequence. Learning five or six such constructions is more efficient than memorising whole model answers, since they can be recombined to fit whatever the question asks.
