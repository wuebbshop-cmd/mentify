## 1. Concept and Use Case

### 1.1 What the Internet is

The Internet is a global system of interconnected computer networks that communicates using a common family of protocols, chiefly TCP/IP. The definition has three separable parts, and every examination question on this topic turns on one of them.

The first part is that the Internet is a **network of networks**, not a single network. No organisation owns or operates it end to end. A message from a laptop in Nairobi to a server in Frankfurt crosses a home wireless router, an Internet Service Provider's access network, one or more national and international backbone links, and the destination provider's network, each owned and administered separately.

The second part is that the networks agree on a **common protocol family**. Interconnection is possible because every participant speaks IP for addressing and routing, and TCP or UDP for transport. Agreement on these protocols, not physical ownership, is what makes the components one system.

The third part is that the Internet is a **general-purpose carrier**. It does not know whether it is carrying a web page, an email, a voice call, or a video stream. The same packet-forwarding infrastructure serves all of them, which is why a single connection can support so many services.

### 1.2 The distinction students most often get wrong

The Internet and the World Wide Web are not the same thing. The Internet is the transport infrastructure: the physical links, the routers, the addressing scheme, and the protocol family. The World Wide Web is one application that runs on top of it, invented in 1989 and built on HTTP, URLs, and HTML.

The distinction is easy to see from the fact that the Internet predates the Web by roughly two decades, and that email, file transfer, remote login, and domain name resolution are all Internet services that existed before the Web and do not depend on it. A correct examination answer states the relationship as: the Web is a service delivered over the Internet, not a synonym for it.

### 1.3 Why the architecture matters in practice

The design decisions taken in the 1970s and 1980s determine what is easy and what is hard today.

Because the network is deliberately **dumb in the middle and intelligent at the edges**, the routers between two hosts do not need to understand the applications they carry. New applications can be deployed by changing only the endpoint software, without upgrading the intervening infrastructure. This is the property that allowed the Web, and later streaming and video conferencing, to spread without a coordinated rebuild of the network.

Because the network is **best-effort**, IP makes no promise that a packet will arrive, arrive once, or arrive in order. Reliability, when required, is supplied by the endpoints; TCP adds acknowledgements, retransmission, and reordering. This separation is why UDP can be used where low delay matters more than perfect delivery, as in live voice and video.

Because addressing is **hierarchical and globally unique**, any host can be reached by any other host without prior arrangement, which is the property that makes a global market of services possible.

### 1.4 Typical use cases examined in this course

The course uses the Internet as the substrate for the services studied in later topics: electronic mail, file transfer, remote login, the World Wide Web, name resolution, and hosting. A useful framing for revision is that the material moves up the layers. Topic 1 establishes the wires, routers, and addressing. Later topics establish the services and the markup delivered over them.

## 2. Data, Syntax, and Core Concepts

### 2.1 The physical infrastructure

The Internet's physical layer consists of three functional classes of equipment, and the course names them explicitly.

**Transmission lines** carry the signal. They are the copper pairs, coaxial cables, fibre-optic strands, and radio paths between equipment. Their characteristics — capacity, attenuation, susceptibility to interference — set the physical limits on what any higher layer can achieve.

**Routers** are the packet switches at the junctions. A router holds a routing table, examines the destination address of each packet, and forwards the packet out of the interface that the table indicates. Routers do not track applications; they forward packets.

**High-bandwidth backbone hubs** are the long-haul links and the exchange points where major networks interconnect. Historically the backbone was a small number of very fast national links; today it is a mesh of many providers interconnecting at Internet Exchange Points, where they exchange traffic directly instead of paying a third party to carry it.

| Component | Function | Typical failure effect |
|---|---|---|
| Transmission line | Carries the signal between two points | Loss of that path only; routing may reconverge |
| Router | Forwards packets by destination address | Loss of reachability to the networks behind it |
| Backbone link or IXP | Interconnects large networks | Regional congestion or partition |

### 2.2 Internet Service Providers and connection tiers

An Internet Service Provider is the organisation that connects an end customer to the rest of the Internet. Providers are conventionally described in tiers, though the boundaries have blurred.

**Tier 1** providers own or lease global long-haul capacity and reach every other network without paying transit fees; they exchange traffic with peers of similar standing.

**Tier 2** providers buy transit from Tier 1 networks for global reach but peer with other Tier 2 networks to reduce cost.

**Tier 3** providers buy transit from the tiers above and serve end customers, often within a single city or region.

The practical consequence for a customer is that the quality of a connection depends not only on the access technology at the customer's premises but also on the provider's peering arrangements, because congestion typically arises where networks exchange traffic, not inside any single network.

### 2.3 Connection media and access technologies

The course compares six access technologies. Each is a different answer to the question of how to carry data over the local loop, the segment from the customer's premises to the provider.

**Dial-up** uses the ordinary telephone line and a modem that converts digital data into audible tones. It occupies the line for the duration of the call, offers roughly 56 kbps at best, and requires a call setup delay of many seconds before any data moves.

**DSL (Digital Subscriber Line)** also uses the telephone pair but exploits frequencies above those used by voice, so the line can carry data and a telephone call simultaneously. Asymmetric DSL, the common residential form, gives more downstream than upstream capacity, which matches typical browsing behaviour.

**Cable** uses the coaxial cable of a cable television network. Capacity is shared among the subscribers on the same segment, so throughput falls during peak periods, although the nominal rate is high.

**Wireless** access uses radio, either a provider's cellular network or a fixed wireless link. It requires no cabling to the premises, which makes it the practical choice where copper and fibre are absent, but it is more sensitive to interference and to distance from the access point.

**Satellite** access places a link between the premises and an orbiting transponder. Its distinguishing characteristic is delay: a geostationary satellite at roughly 35,800 km altitude imposes a round-trip propagation delay of about 500 ms, which is noticeable in conversation and disruptive in interactive protocols. Low-earth-orbit constellations reduce that delay substantially at much greater cost.

**Fibre optics** carries data as pulses of light in a glass strand. It offers the highest capacity and the lowest attenuation, is immune to electromagnetic interference, and does not degrade with distance in the way copper does, which is why it is the medium of choice for new backbone and access build-out.

### 2.4 The TCP/IP layered model

The TCP/IP suite is described as four layers. Each layer provides a service to the layer above and uses the service of the layer below.

| Layer | Principal protocols | Unit of data | Addressing used |
|---|---|---|---|
| Application | HTTP, DNS, SMTP, FTP, SSH | Message | Names and URLs |
| Transport | TCP, UDP | Segment (TCP), datagram (UDP) | Port number |
| Internet | IP (IPv4, IPv6) | Packet | IP address |
| Link (Network access) | Ethernet, Wi-Fi, PPP | Frame | MAC address |

The value of the model is that it localises change. A new application protocol requires no change to IP. A new link technology, such as a faster optical standard, requires no change to TCP. This is the same "intelligent edges, dumb middle" principle in structural form.

Two addressing schemes appear in the table and must not be confused. An **IP address** identifies an interface globally and is used by routers to forward packets across networks. A **MAC address** identifies an interface on a single link and is used only within that link. A **port number** identifies a process on the host, which is how a single IP address can serve a web server, a mail server, and a name server at the same time.

### 2.7 TCP and UDP, the two transport services

The transport layer offers two distinct services, and the choice between them is a design decision rather than a matter of preference.

TCP provides a reliable, ordered, connection-oriented stream. It establishes a connection with a three-way handshake, numbers every byte, acknowledges what has been received, retransmits what has not, reorders what arrives out of sequence, and applies flow control so a fast sender cannot overwhelm a slow receiver. It also interprets loss as a signal of congestion and reduces its sending rate accordingly. The cost of these guarantees is delay: a lost segment must be noticed and resent, and the application receives nothing until the gap is filled. This is the correct choice for the web, email, and file transfer, where every byte matters and a short wait is acceptable.

UDP provides an unreliable, unordered, connectionless datagram service. It adds port numbers and a checksum and nothing else. Nothing is acknowledged, nothing is retransmitted, nothing is reordered, and there is no congestion response. The gain is that a datagram is delivered immediately with no waiting for anything else. This is the correct choice for live voice and video, where a late packet is worthless and waiting for it is worse than losing it, and for DNS queries, where the request and the answer each fit in one datagram and the application implements its own retry.

The examination point is that unreliability in UDP is a deliberate trade, not a shortcoming. A student who writes that TCP is better than UDP has answered the wrong question; the right answer states the requirement and then justifies the choice.

### 2.8 Encapsulation, the mechanism that makes layering work

When an application sends data, each layer adds its own header. The application message becomes a TCP segment with a TCP header in front; the segment becomes an IP packet with an IP header in front; the packet becomes a frame with a link header in front and a trailer behind. At the receiving end each layer removes its own header and hands the remainder upward.

This is the concrete meaning of layering. It also explains a practical diagnostic fact used in Section 5: an error at one layer is often reported as a symptom at a higher one, because the higher layer simply never receives the data it expected.

### 2.6 Addressing essentials that later topics assume

An IPv4 address is a 32-bit number written as four decimal octets separated by dots, for example 196.201.1.9. Part of the address identifies the network and part identifies the host within it, and the split is given by the subnet mask. A host whose destination lies within its own subnet sends directly; a host whose destination lies outside sends to its default gateway, which is the mechanism Section 4.6 demonstrates.

Three ranges are reserved for private use and are never routed on the public Internet: 10.0.0.0 to 10.255.255.255, 172.16.0.0 to 172.31.255.255, and 192.168.0.0 to 192.168.255.255. Every device on a home network therefore typically holds a private address, and the router performs network address translation so that all of them share the single public address assigned by the provider. This is why a trace such as the one in Section 4.4 begins with a private address and only becomes public further along the path.

IPv6 addresses are 128 bits and are written as eight groups of four hexadecimal digits. The far larger address space removes the need for translation between private and public addressing, and it permits every device to hold a globally routable address. During the long transition both protocols run on the same infrastructure, which is why name records exist in both A form for IPv4 and AAAA form for IPv6.

## 3. Methods and Operations

### 3.1 How a packet actually reaches a distant host

The forwarding process can be stated as a sequence, which is the form expected in an examination answer.

1. The application hands data to TCP, which segments it and attaches a header containing source and destination port numbers.
2. IP attaches its own header, containing the source and destination IP addresses.
3. The link layer determines the hardware address of the next hop and frames the packet for transmission on that link.
4. Each router on the path removes the link framing, examines the destination IP address, consults its routing table, selects the next hop, and reframes the packet for the next link.
5. The destination host reassembles the data and passes it up the layers, where TCP reorders and acknowledges, and the application receives the message.

The important idea is that the IP addresses in the header do not change from source to destination, while the link-layer addresses change at every hop. This is exactly what allows the network to be a network of independent networks.

### 3.2 Measuring reachability and path

Three tools are used throughout the course. Each operates at a different level, and knowing which level explains what its output can and cannot show.

`ping` tests reachability and round-trip time using ICMP echo requests. It is fast and simple, but many hosts and firewalls deliberately suppress ICMP, so a non-response does not prove that a host is down.

`traceroute` (or `tracert` on Windows) reveals the path by sending packets with progressively increasing time-to-live values; each router that decrements the counter to zero returns an error message, exposing its address.

`mtr` combines both, repeatedly probing each hop to build a loss and latency profile along the path.

### 3.3 Assessing a connection against its claims

A provider's advertised rate is a peak figure under favourable conditions. To assess a connection the following measurements are relevant, and they are independent of one another.

- **Bandwidth** is the maximum data rate the access link can sustain. It limits bulk transfer time.
- **Latency** is the one-way or round-trip delay between endpoints. It limits how quickly a request can be answered, regardless of bandwidth.
- **Jitter** is variation in latency, which matters for real-time traffic.
- **Reliability** is the stability of the service over time, usually expressed as a percentage of uptime and as a packet loss rate.
- **Contention ratio** is the number of subscribers sharing a nominal capacity, which explains why a shared cable segment slows at peak hours.

### 3.4 Method for selecting an access technology

A defensible choice follows from the requirement rather than from the headline speed.

1. Establish the dominant traffic profile: bulk download, interactive browsing, real-time voice and video, or machine-to-machine telemetry.
2. Establish the latency budget. Interactive voice needs delay kept low and jitter bounded; bulk file transfer is comparatively insensitive to delay.
3. Establish the geography and the available infrastructure. Where fibre is present it is almost always preferable; where it is absent, fixed wireless is usually the practical compromise.
4. Establish the reliability requirement and the acceptable cost per month.
5. Compare the candidates against the requirement, stating the trade-off rather than asserting a single winner.

### 3.6 Assessing whether a connection suits a workload

The following table converts a stated requirement into the quantity that actually constrains it. It is the form of answer expected when a question supplies a scenario and asks for a recommendation.

| Workload | Quantity that limits it | Why | Typical acceptable figure |
|---|---|---|---|
| Reading email and news | Latency | Requests are small and frequent | Under 150 ms round trip |
| Bulk file download | Bandwidth | Transfer time falls directly as capacity rises | Several Mbps sustained |
| Video conference | Jitter and upload capacity | Delay variation breaks speech | Under 30 ms jitter, symmetric link |
| Online gaming | Latency and loss | State updates must arrive promptly | Under 60 ms, under 1 per cent loss |
| Nightly off-site backup | Bandwidth during the window | The job must finish before the window closes | Sustained capacity, not peak |
| Home server access | Public address and upstream capacity | Inbound connections must be routable | Public IPv4 or IPv6, upstream headroom |

The pattern worth internalising is that interactive work is limited by delay and bulk work is limited by capacity, so a provider's headline rate answers only the second question.

### 3.7 Method for reading a connection's real performance

A single speed test is not evidence. A defensible assessment takes repeated measurements at different times of day, separates download from upload, records latency alongside throughput, and notes the test server used, because a measurement against a nearby server says little about the path to a distant one.

### 3.8 Why the first request to a site is slower than the second

Name resolution sits between the application and every connection, and it explains a pattern that otherwise looks like inconsistency. When a name is not already cached, the stub resolver on the host asks a recursive resolver, which may in turn consult a root server, then the server for the top-level domain, then the authoritative server for the zone. That is up to four round trips before the first packet of the actual conversation is sent.

Each of those round trips costs latency, not bandwidth. On a 20 ms link the lookup adds perhaps 80 ms and is barely noticeable; on a 500 ms satellite link it adds about two seconds before anything visible happens. The resolver then caches the answer for the duration of the record's time to live, which is why the second visit to the same site starts immediately and why a site can appear to "warm up".

This is also why content delivery networks place copies of content near users rather than only at the origin. Shortening the path reduces the number of round trips that must complete before data flows, which is the only way to improve perceived responsiveness once bandwidth is already sufficient.

## 4. Worked Implementation from the Notes

### 4.1 Task: confirm basic connectivity and measure round-trip time

### 4.2 Implementation: use ping against a public resolver, then interpret

Step 1. Send a small, fixed number of echo requests so the result is repeatable.

```bash
ping -c 4 8.8.8.8
```

Step 2. Read the output. A representative result is shown below; the exact figures depend on the network.

```text
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=18.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=19.1 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=117 time=18.7 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=117 time=18.9 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 18.4/18.8/19.1/0.3 ms
```

Step 3. Interpret each figure. Zero per cent loss shows the path is currently delivering packets. The average round-trip time of 18.8 ms shows how far away the destination is in time, not in distance. The small deviation of 0.3 ms shows a stable path with little jitter, which is what a wired access link typically produces and what a congested wireless link typically does not.

Step 4. Note what the test does not show. It says nothing about bandwidth; a connection can have low latency and low capacity simultaneously, as a satellite link with a small allocation demonstrates.

### 4.3 Task: expose the path a packet takes

### 4.4 Implementation: trace the route and identify network boundaries

Step 1. Run a trace with a bounded number of hops.

```bash
traceroute -m 12 example.com
```

Step 2. Read a representative trace.

```text
traceroute to example.com (93.184.216.34), 12 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  1.204 ms  1.118 ms  1.093 ms
 2  10.20.0.1 (10.20.0.1)  9.442 ms  9.301 ms  9.276 ms
 3  ae12.acc1.nairobi.example.net (196.201.1.9)  14.882 ms  14.701 ms  14.655 ms
 4  xe-0-0-1.core1.lon1.example.net (195.66.224.20)  96.113 ms  96.002 ms  95.884 ms
 5  93.184.216.34 (93.184.216.34)  97.221 ms  97.004 ms  96.912 ms
```

Step 3. Identify the boundaries. Hop 1 is the local router, a private address. Hop 2 is the provider's first aggregation device. Hop 3 is the provider's access concentrator, named accordingly and carrying a public address. Hop 4 is a core router in a different country, and the jump from roughly 15 ms to roughly 96 ms is the transit delay across that long-haul link.

Step 4. Draw the correct conclusion. The large step in latency is a property of distance and the speed of light in fibre, not a fault. A fault would appear as sustained loss at one hop that persists at every subsequent hop.

### 4.5 Task: verify the layered model from the command line

### 4.6 Implementation: inspect addresses at each layer

Step 1. Display the link-layer and internet-layer configuration of the local host.

```powershell
Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address, IPv4DefaultGateway
```

Step 2. Observe that the output reports both an IP address and a gateway. The gateway is the first-hop router from Section 4.4, and it is the address to which the host sends every packet whose destination lies outside its own subnet.

Step 3. Confirm the transport layer by listing listening ports.

```powershell
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess
```

Step 4. Interpret. Each listed port is a process waiting for connections. Port 80 or 443 indicates a web server, 53 indicates a name server, 25 indicates a mail server. This is the concrete demonstration that a single IP address serves many applications simultaneously, distinguished only by port number.

### 4.7 Task: contrast a high-latency link with a low-latency link

### 4.8 Implementation: measure, then compare against the theoretical delay

Step 1. Measure round-trip time to a nearby and to a distant host.

```bash
ping -c 4 196.201.1.9
ping -c 4 195.66.224.20
```

Step 2. Record representative results: roughly 15 ms locally and roughly 96 ms intercontinentally.

Step 3. Explain the difference physically. Light in fibre travels at about two-thirds of its vacuum speed, roughly 200,000 km per second. A round trip of 96 ms therefore implies a path of about 19,200 km, which is consistent with an intercontinental route that is not a straight line. The local figure of 15 ms implies roughly 3,000 km of path at most, consistent with a national route that includes queuing delay at each hop.

Step 4. State the design consequence. Because latency is bounded by physics, no amount of extra bandwidth removes it. Applications that need low delay must be placed near their users, which is the reason content delivery networks exist.

### 4.9 Task: prove that network address translation is in use

### 4.10 Implementation: compare the local address with the public address

Step 1. Read the address the operating system holds.

```powershell
(Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.PrefixOrigin -ne 'WellKnown' }).IPAddress
```

Step 2. A representative answer is 192.168.1.24, which falls inside the reserved private range.

Step 3. Ask an external service what address the rest of the Internet sees.

```bash
curl -s https://api.ipify.org
```

Step 4. A representative answer is 41.90.64.17, which is a public address and is different from the local one.

Step 5. Interpret the discrepancy. The difference is conclusive evidence that translation is happening at the boundary: the router holds the public address and rewrites the source address of outgoing packets, then remembers which internal host each reply belongs to. This also explains why an unsolicited connection from outside cannot reach the internal host, which is a security benefit and a barrier to running a server at home.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to test an understanding of this topic

A student who can do the following has understood the material.

- State the three components of the definition of the Internet and give an example of each.
- Distinguish the Internet from the World Wide Web without hesitation, and give two services that exist without the Web.
- Name the four TCP/IP layers, the protocol at each, and the addressing scheme each uses.
- Explain why the IP addresses in a packet header do not change while the link addresses do.
- Compare the six access technologies on bandwidth, latency, reliability, and cost, and justify a choice for a stated requirement.
- Read a `ping` and a `traceroute` output and say what each figure does and does not prove.

### 5.2 Interpretation: what the numbers actually mean

Bandwidth and latency answer different questions and are not interchangeable. A link with high bandwidth and high latency transfers a large file quickly once it starts, but still takes a long time to begin, because the first response must make the round trip. A link with low bandwidth and low latency feels responsive for small requests but transfers large files slowly. Statements such as "the connection is fast" without specifying which quantity is meant are therefore not answers.

Packet loss is a third, separate quantity. A path can have plenty of bandwidth, low latency, and still be unusable for voice if it loses two per cent of packets. Retransmission conceals loss for bulk transfer but cannot conceal it for real-time traffic, because the retransmitted data arrives too late to be useful.

### 5.3 Limits of the infrastructure

The architecture has known limitations that are worth stating precisely, because examination questions on "advantages and societal impacts" reward balance.

Address exhaustion in IPv4 drove the development and deployment of IPv6 and, as an interim measure, network address translation. Best-effort delivery means that quality of service must be engineered rather than assumed. The absence of a single authority makes coordination of security difficult, which is why vulnerabilities are patched at endpoints rather than in the network. And because the network is a commons, congestion is a shared problem requiring either cooperation or pricing to manage.

### 5.4 Common errors and how to avoid them

- **Treating the Web as the Internet.** The Web is one application among many. Email, DNS, SSH, and FTP all run over the Internet without the Web.
- **Confusing an IP address with a MAC address.** The IP address is used across networks by routers; the MAC address is used only within one link, and it changes at every hop.
- **Believing that a failed `ping` proves a host is down.** Firewalls commonly suppress ICMP. Use a TCP-based check to a known port before drawing that conclusion.
- **Reading a single hop's reported loss as a fault.** If the loss disappears at later hops, the router was merely rate-limiting its own error replies, not dropping user traffic.
- **Confusing bandwidth with latency.** They are independent, and neither substitutes for the other.
- **Assuming the advertised rate is the achieved rate.** Contention, distance, and peering all intervene.
- **Confusing the four-layer TCP/IP model with the seven-layer OSI model.** The course uses TCP/IP; the OSI model is a teaching reference, and mixing the two in an answer loses marks.
- **Forgetting that UDP is unreliable by design.** Its lack of guarantees is a feature for low-latency traffic, not a defect.

### 5.6 Architectural advantages and societal impacts

The advantages of the architecture are best stated as consequences of specific design choices rather than as a list of benefits.

**Open interconnection.** Because any network can join by adopting the protocol family, entry cost is low and competition is possible at every level, from the local provider to the content provider. The result is that a small organisation can reach a global audience without negotiating with every intervening network.

**Application neutrality.** Because the network does not inspect or interpret the payload, innovation happens at the edges. A new service can be deployed by two parties who agree on a protocol, without permission from the network operators. This is the reason the Web, streaming, and video conferencing all arrived without a coordinated infrastructure upgrade.

**Resilience through redundancy.** Because routing adapts to the failure of individual links, the loss of any one path usually degrades rather than severs communication. This was an explicit design goal and it remains the reason a cable cut causes congestion rather than a national outage.

**Fault isolation through layering.** Because each layer has a defined interface, a fault can be localised. A physical break is diagnosed at the link layer, a routing problem at the internet layer, and an application failure at the top, which makes systematic troubleshooting possible rather than guesswork.

The societal impacts follow from the same properties, and a balanced answer names both sides.

On the positive side, the Internet has lowered the cost of publishing to near zero, which has widened access to education, health information, and markets. It has enabled remote work, distributed collaboration, and financial services that do not require physical branches. It has allowed small enterprises in regions with limited physical infrastructure to sell nationally and internationally. It has also changed how public services are delivered, from tax filing to examination results.

On the negative side, the same openness that permits innovation permits abuse. Because there is no central authority, harmful content and fraud are policed by platforms and states rather than by the network itself. Concentrated platform power has emerged, since a few services intermediate a large share of traffic. Unequal access, both in availability and in cost, reproduces existing inequalities, which is the substance of the digital divide. Security is an ongoing cost, borne by endpoints and their operators, because the network cannot be trusted to filter. And the physical footprint is substantial: data centres and access networks consume significant electricity and water, which turns a nominally weightless technology into an environmental consideration.

A useful way to hold both sides together in an examination answer is to trace each impact back to the design property that produced it. Open interconnection produced both low barriers to entry and the difficulty of policing abuse. Application neutrality produced rapid innovation and also the concentration of attention in a small number of platforms. Redundancy produced resilience and also the expectation of continuous availability, which makes any outage disruptive. Layering produced systematic diagnosis and also a division of responsibility in which each operator can legitimately claim that the fault lies in another layer. Stated this way, the impacts are not a separate list to be memorised; they are the same four properties seen from the side of society rather than from the side of engineering.

### 5.7 A procedure for any question in this topic

1. Identify whether the question is about infrastructure, protocol layering, access technology, or performance measurement, because each has a different expected shape of answer.
2. For an infrastructure question, name the component and its function rather than describing it vaguely.
3. For a layering question, state the layer, the protocol, the data unit, and the addressing used.
4. For an access-technology question, compare on the four axes and then justify one choice against a stated requirement.
5. For a measurement question, state what the tool tests, what its output shows, and what it cannot show.
6. Close with the trade-off. A balanced statement of cost against capability is what distinguishes a strong answer from a list.
