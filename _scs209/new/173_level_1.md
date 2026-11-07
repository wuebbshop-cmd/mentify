## 1. Concept and Use Case

### 1.1 Picture a country held together by roads

Imagine a country in which every town is joined to every other town by roads, but no single authority built or owns them all. Some roads are wide motorways carrying thousands of lorries an hour; others are narrow lanes serving a handful of houses. At every junction stands a signpost that tells a driver which road continues in which direction. Local delivery firms collect parcels from houses and hand them to regional depots, the depots pass them to national hauliers, and the hauliers exchange loads with firms from neighbouring countries at border depots. A parcel never travels as one object along one road from end to end. It is packed into a van, unpacked at a depot, sorted, packed into a different lorry with a different label for the next leg, and so on until it reaches the correct street and the correct house number.

That picture is the whole idea behind this topic. The roads are the cables and radio links that carry signals. The signposts at junctions are the devices that decide which way each piece of data continues. The border depots are the meeting points where large carriers hand traffic to one another. The local delivery firm is your Internet Service Provider. The house number is the address that identifies your device. And the parcel that gets repacked at every depot is your data, chopped into small labelled pieces that are forwarded independently and put back together at the far end.

Nothing in that picture requires the roads to know what is inside the parcels. A lorry carrying furniture and a lorry carrying medicine use the same motorway. That single property, that the network carries whatever it is given without caring what it means, explains most of the Internet's behaviour, both the inventiveness it makes possible and the problems it cannot solve by itself.

### 1.2 What the Internet is

The Internet is a worldwide system of interconnected computer networks that all agree to communicate in the same way, so that any device on any of those networks can exchange data with any other. Three parts of that sentence matter, and each part is worth learning on its own because examiners ask about each of them separately.

The first part is that the Internet is a **network of networks**, not one network. No single company owns it or runs it end to end. When you send a message from a laptop in one city to a server in another, the message crosses your home wireless router, your provider's access network, one or more long-distance links owned by other companies, and the destination provider's network. Each of those pieces belongs to a different organisation with its own equipment, staff and failures.

The second part is that the networks all agree on **common rules**. These rules are called protocols. Interconnection works because every participant handles addresses and forwarding in the same manner and transports data in the same manner. Agreement on the rules, not shared ownership, is what turns thousands of separately managed networks into one system that behaves predictably.

The third part is that the Internet is a **general-purpose carrier**. It does not know or care whether it is carrying a web page, an email, a voice call, a video, a game or a software update. The same equipment carries all of them, which is why one connection to your home can support so many different activities at once.

### 1.3 The Internet is not the World Wide Web

This is the confusion that costs beginners the most marks, so it is worth removing immediately. The Internet is the transport system: the cables, the radio links, the routers, the addressing scheme and the rules for moving data. The World Wide Web is one service that runs on top of that transport system. It is the collection of pages you reach with a browser, and it is built on three ideas: a way of naming a page, a protocol for requesting it, and a language for describing it.

The easiest proof that the two are different is age. The Internet began as a research network in 1969. The Web was proposed in 1989 and appeared in the early 1990s, roughly two decades later. For those twenty years email, file transfer, remote login and name lookup all worked perfectly well without a single web page existing. They still work that way today: your phone collects mail, your computer reaches a server through a secure shell, and your machine looks up names, all without a browser being involved.

So the correct sentence to write is that the Web is a service delivered over the Internet, not a synonym for it. If a question asks you to distinguish them, give one sentence for each and then one example of an Internet service that does not use the Web.

### 1.4 What people actually use it for

The list of services has been remarkably stable in shape even as the details changed. The oldest and still largest use is **email**, the sending of written messages to people who are not present so that the message waits for them. The second is **information retrieval**, whether through the Web, through a search engine or through a direct query to a database. The third is **file transfer**, moving a whole document, program or media file from one machine to another. The fourth is **conversation**, which now includes text chat, voice calls and video meetings. The fifth is **remote control**, using a machine somewhere else as though you were sitting in front of it. The sixth is **entertainment**, including streamed video, music and multiplayer games. The seventh, which has grown fastest in recent years, is **machine-to-machine traffic**: software updates, sensors, payment terminals, smart meters and household appliances that report to a server without any person pressing a button.

A useful way to think about that list is that every item is a different answer to the same question, which is what two programs on two distant machines should say to each other in order to get something done. The Internet itself supplies none of those conversations. It supplies the ability to have them.

### 1.5 Why a beginner should care about the architecture

It is tempting to treat the underlying machinery as someone else's problem, because a browser hides it. Three reasons make it worth understanding.

The first is **diagnosis**. When a page fails to load, the failure could be at the wireless link, at your router, at your provider, at a name server, at the destination server, or in the page itself. Each of those failures produces a different symptom, and knowing the layers tells you which test to run first instead of restarting everything and hoping.

The second is **purchase decisions**. Advertised connection speeds are one number, but the experience of using a connection depends on several numbers that providers do not advertise prominently. Understanding which number limits which activity stops you paying for capacity you cannot use.

The third is **explanation**. Questions on this topic are almost always of the form "explain why" or "compare and justify". Those are answered from the design of the system, not from a list of product names, so the architecture is the answer.

## 2. Data, Syntax, and Core Concepts

### 2.1 The parts you can touch: transmission lines, routers, backbone hubs

The physical side of the Internet consists of three functional kinds of equipment, and each has a job that can be stated in one sentence.

**Transmission lines** carry the signal from one point to another. They are the twisted copper pairs in telephone cables, the coaxial cable used for television, the strands of glass in fibre-optic cable, and free space itself when the signal is a radio wave. Their properties set the physical limit on everything above them: how much data they can carry, how far the signal travels before it must be boosted, and how easily interference corrupts it.

**Routers** are the junctions. A router keeps a table that says, for each range of destination addresses, which of its connections leads closer to that destination. When a packet arrives, the router reads the destination address, looks it up in the table, and sends the packet out of the chosen connection. It does not know what the packet contains and does not keep a record of the conversation. It forwards and forgets.

**High-bandwidth backbone hubs** are the long-distance links and the meeting points where large networks connect. Historically the backbone was a small number of very fast national links, which is why the word suggests a spine. Today it is a mesh of many providers interconnected at exchange points, where two networks hand traffic directly to each other instead of paying a third company to carry it. Undersea cables are a large part of this layer: most intercontinental traffic crosses an ocean on a glass strand no thicker than a human hair.

| Component | Job | What goes wrong if it fails |
|---|---|---|
| Transmission line | Carries the signal between two points | Only that path is lost; traffic diverts if another path exists |
| Router | Chooses the next hop by destination address | The networks behind it become unreachable |
| Backbone link or exchange point | Joins large networks together | Congestion or a regional partition |

The important beginner point is that a failure rarely takes the whole Internet down. It removes one path, and the routers around it choose another. That resilience was a deliberate design goal, not an accident.

### 2.2 The companies in the middle: providers and their tiers

An **Internet Service Provider**, abbreviated **ISP**, is the organisation that connects a customer to the rest of the Internet. Your ISP is the local delivery firm in the road picture: it collects your traffic, carries it across its own network, and hands it to somebody else who can take it further.

Providers are conventionally described in three tiers, although the boundaries have become blurred by mergers and by providers that operate at more than one level.

A **Tier 1** provider owns or leases enough long-distance capacity to reach every other network in the world without paying anybody for transit. It exchanges traffic with other Tier 1 providers on equal terms, an arrangement called settlement-free peering.

A **Tier 2** provider buys transit from a Tier 1 provider in order to reach the whole world, but peers directly with other Tier 2 providers in places where that saves money.

A **Tier 3** provider buys transit from the tiers above and sells access to end customers, usually within one country or one city.

Two consequences follow, and both are examinable. First, the quality of your connection depends on your provider's peering arrangements as well as on the cable into your house, because congestion usually appears where two networks meet rather than inside either one. Second, a public wireless hotspot, a mobile phone tower and a satellite dish are all still connected to an ISP somewhere; there is no path to the Internet that skips the provider layer.

### 2.3 Six ways of reaching your home

Every access technology answers the same question: how do we carry data across the local loop, the segment between the customer's premises and the provider's nearest equipment? The six that are compared in this topic differ in medium, in capacity, in delay, in reliability and in cost.

**Dial-up** uses the ordinary telephone line and a modem, a device that converts digital data into audible tones and back again. Because it uses speech frequencies, it occupies the line for the whole session: nobody can telephone you while you are connected. The best possible rate is 56 kilobits per second, which is about one thousandth of a modern fibre service, and the connection takes twenty to thirty seconds to establish because a call must be dialled and negotiated.

**DSL**, short for **Digital Subscriber Line**, also uses the telephone pair but sends data at frequencies above those used by speech, so a telephone call and an Internet session can happen at the same time. The common residential form is asymmetric, meaning the download rate is much higher than the upload rate, which suits the way most households use a connection. Typical rates run from a few megabits per second up to tens of megabits per second, falling as the distance from the provider's cabinet increases.

**Cable** uses the coaxial cable of a television network. Nominal rates are high, often far above DSL, but the cable segment is shared among the households attached to it, so the rate each household achieves drops when neighbours are busy. This sharing is described by a contention ratio.

**Wireless** access uses radio, either a mobile network or a fixed link to an antenna on a mast. It needs no cable to the premises, which makes it the practical choice where copper and glass are absent, but its quality varies with distance, with obstacles such as walls and trees, and with the number of users on the same cell.

**Satellite** access places a link between a dish at the premises and a transponder in orbit. Its distinguishing feature is delay. A satellite in geostationary orbit sits about 35,800 kilometres above the equator, so a signal travelling up and back covers nearly 72,000 kilometres even before it goes anywhere useful, which produces a round-trip delay of roughly half a second. Constellations in low earth orbit, only a few hundred kilometres up, reduce that delay to a few tens of milliseconds, at the cost of a much larger and more expensive system.

**Fibre optics** carries data as pulses of light along a strand of glass. It offers the highest capacity, the lowest loss over distance, and complete immunity to electrical interference. It is the medium used for new backbone links and increasingly for the connection into the home.

| Technology | Medium | Typical download | Typical round-trip delay | Reliability | Relative cost |
|---|---|---|---|---|---|
| Dial-up | Telephone copper pair | Up to 56 kilobits per second | 150 to 200 milliseconds | Poor, and exclusive of voice calls | Lowest |
| DSL | Telephone copper pair, higher frequencies | A few to tens of megabits per second | 20 to 40 milliseconds | Good | Low to medium |
| Cable | Coaxial television cable | Tens to hundreds of megabits per second | 10 to 25 milliseconds | Good, but shared segment slows at peak | Medium |
| Wireless | Radio, mobile or fixed | A few to hundreds of megabits per second | 20 to 60 milliseconds | Variable with distance and load | Medium |
| Satellite | Radio to an orbiting transponder | Tens of megabits per second | About 500 milliseconds in geostationary orbit | Weather sensitive | High |
| Fibre | Glass strand, light | Hundreds of megabits to several gigabits per second | 2 to 15 milliseconds | Highest | Medium to high to install |

The pattern in that table is the one worth remembering: as you go down the list you generally trade cost and availability against capacity and delay, and no single row wins on all four measures at once.

### 2.4 The rules that hold it all together: protocols

A **protocol** is an agreed set of rules for exchanging data. It is not advice; it is a contract precise enough that two programs written by strangers in different countries can work together without meeting. Protocols are published as documents called **Requests for Comments**, abbreviated **RFC**, and the RFC number is the definitive citation for a protocol's behaviour.

The Internet's foundation is the **TCP/IP** suite, short for **Transmission Control Protocol / Internet Protocol**. The name names two of its most important members, but the suite contains many more. The Internet Protocol handles addresses and forwarding. The Transmission Control Protocol handles reliable delivery of a stream of bytes. The **User Datagram Protocol**, abbreviated **UDP**, provides a lighter, faster service with no delivery guarantees.

Rules are needed for a simple reason. If one computer numbers bytes from zero and another numbers them from one, the file arrives corrupted. If one machine expects the length of a message first and the other sends it last, nothing can be parsed. Multiply that by thousands of independent manufacturers and you have the reason the Internet converged on a small number of written agreements rather than letting each vendor invent its own conventions.

### 2.5 The four layers

The TCP/IP suite is described as four layers. A layer is a division of labour: each layer offers a service to the layer above it and relies on the service of the layer below. Keeping them separate is what lets a new application appear without changing the cables, and a faster cable appear without changing the applications.

| Layer | What it does | Examples | What identifies the endpoint |
|---|---|---|---|
| Application | Provides the service the user asked for | Web, email, file transfer, name lookup | A name or a URL |
| Transport | Delivers data to the right program on the host | TCP and UDP | A port number |
| Internet | Moves packets between networks | IP version 4 and IP version 6 | An IP address |
| Link | Moves frames across one physical link | Ethernet, Wi-Fi, dial-up framing | A hardware address |

The table repays a second look, because it contains the single most examined idea in the topic: three different kinds of address, each doing a different job. At the top the identifier is a name, or a **URL**, short for **Uniform Resource Locator**, which is the full textual address of a resource including the scheme, the host and the path. Below that, an **IP address** identifies a machine across the whole Internet and is what routers use. A **hardware address**, also called a **Media Access Control address** or **MAC address**, identifies a network card on one local link and is used only within that link. A **port number** identifies which program on the machine should receive the data. That is how a single machine can be a web server, a mail server and a name server at the same time without confusion.

The four layers are often compared with the seven-layer **Open Systems Interconnection** model, abbreviated **OSI**, which divides the same work more finely. The OSI model is a useful teaching reference and appears in many textbooks, but the working Internet is built on TCP/IP, so an answer that mixes the two frameworks loses marks for inconsistency. Choose one and stay with it.

### 2.6 Addresses, packets and the journey of a message

An **IPv4 address**, meaning Internet Protocol version 4 address, is a 32-bit number written as four decimal numbers separated by dots, such as 196.201.1.9. Part of it names the network and part names the host within that network, and the split is given by the subnet mask. When the destination lies inside the sender's own network, the sender delivers directly. When it lies outside, the sender hands the packet to its default gateway, which is the first router on the way out.

Three ranges of IPv4 addresses are reserved for private use and are never routed across the public Internet: 10.0.0.0 to 10.255.255.255, 172.16.0.0 to 172.31.255.255, and 192.168.0.0 to 192.168.255.255. Every device on a typical home network therefore holds a private address, and the router performs **Network Address Translation**, abbreviated **NAT**, so that all of them share the single public address the provider assigned. NAT rewrites the source address of outgoing packets and remembers which internal device each reply belongs to.

**IPv6**, Internet Protocol version 6, uses 128-bit addresses written as eight groups of four hexadecimal digits. The enormous address space removes the need for translation, because every device can hold an address that is unique and routable across the whole Internet. Both versions currently run side by side.

Data does not travel as one continuous stream. It is divided into **packets**, each carrying a header with the source and destination addresses, a sequence of numbers identifying its place in the stream, and a limited lifetime. Each packet is forwarded independently and may take a different route from its neighbours. The receiving end reassembles them in order, which is the job TCP performs. This design is called **packet switching**, and it is why a single link can serve thousands of conversations: no capacity is reserved for a conversation that is silent.

Port numbers complete the addressing picture. A short table of the ones that recur in this material is worth memorising, because they are free marks in any question that mentions a service.

| Service | Port | What it is for |
|---|---|---|
| File Transfer Protocol, FTP | 20 and 21 | Moving files; 21 carries commands, 20 carries data in active mode |
| Secure Shell, SSH | 22 | Encrypted remote login |
| Telnet | 23 | Unencrypted remote login |
| Simple Mail Transfer Protocol, SMTP | 25 | Sending mail between servers |
| Domain Name System, DNS | 53 | Turning names into addresses |
| Hypertext Transfer Protocol, HTTP | 80 | Requesting web pages in clear text |
| Post Office Protocol version 3, POP3 | 110 | Downloading mail to one device |
| Internet Message Access Protocol, IMAP | 143 | Keeping mail synchronised across devices |
| Hypertext Transfer Protocol Secure, HTTPS | 443 | Web pages protected by encryption |

### 2.7 The numbers used to judge a connection

Providers advertise one number, but six quantities together describe how a connection actually behaves. Learning what each one limits is what turns a comparison question into a confident answer.

**Bandwidth** is the maximum rate at which data can be carried, usually quoted in megabits per second. It sets how long a large transfer takes. **Throughput** is the rate actually achieved, which is always lower because of overheads, contention and protocol behaviour.

**Latency** is the delay between sending something and receiving a response, usually measured as a round trip in milliseconds. It sets how quickly a single small request can be answered, whatever the bandwidth.

**Jitter** is the variation in that delay from one packet to the next. A large jitter value breaks speech and video even when bandwidth is plentiful, because the receiving software cannot play out packets at a steady rate.

**Packet loss** is the proportion of packets that never arrive. A small loss is hidden by retransmission for file transfer but is audible in a voice call.

**Reliability** is the stability of the service over time, usually expressed as an uptime percentage. Ninety-nine per cent sounds impressive until you notice that it allows almost four days of outage a year.

**Contention ratio** is the number of customers sharing a nominal capacity. A shared cable segment or a mobile cell is contended, which is why the advertised rate is a peak and not a promise.

The distinction between bandwidth and latency is the one beginners blur most often, and Section 5 returns to it with two everyday comparisons.

## 3. Methods and Operations

### 3.1 What happens when you open a page

The sequence is short enough to memorise and it is the backbone of every "describe what happens" question. It also shows why so many separate things can go wrong.

1. You type a name, or click a link that contains one. The browser needs an address, not a name.
2. The computer asks a name server to translate the name into an address. The request goes out on port 53, and the answer comes back in a fraction of a second if the name is already cached somewhere nearby.
3. The browser opens a connection to the server on port 443 for a secure page, or port 80 for a plain one. For a secure page an encrypted session is negotiated before any content is requested.
4. The browser sends a request that names the page it wants, together with a description of what it can accept.
5. The server answers with a status code and, if the answer is a success, the content. A status code beginning with 2 means success, one beginning with 3 means a redirect, one beginning with 4 means the client asked for something unavailable, and one beginning with 5 means the server failed.
6. The browser reads the content, discovers that it refers to images, style sheets and scripts, and requests each of those in turn. This is why one page produces dozens of requests.
7. The browser assembles everything and draws the page.

Steps 1 and 2 are name resolution, steps 3 and 4 are connection setup and request, step 5 is the response, and steps 6 and 7 are rendering. A fault in any one of them produces the same user-visible symptom, a page that does not appear, which is exactly why the tests in Section 3.3 exist.

### 3.2 How a packet finds its way

A packet leaves your computer with a destination address in its header. Your machine compares that address with its own network and mask. If the destination is local, the packet is sent directly to the destination's hardware address. If it is not local, the packet is sent to the default gateway, which is your router.

The router repeats the same decision on a larger scale. It reads the destination address, finds the most specific entry in its routing table that matches, and forwards the packet out of the corresponding interface. The next router does the same, and so on. Because the destination address never changes, every router on the path is making a consistent decision about the same final destination.

Each packet also carries a small counter called the **time to live**, abbreviated **TTL**. Every router that handles the packet reduces the counter by one, and a router that receives a packet whose counter has reached zero discards it and reports the fact back to the sender. The counter exists to stop a packet circling forever if routing tables are inconsistent, and it is also the mechanism that makes route tracing possible, as Section 4.2 shows.

Two properties of this method are worth stating explicitly. First, because each router decides independently, a change in one link is absorbed by the routers nearest to it; no central controller has to issue new instructions. Second, because decisions are made per packet, two packets of the same conversation can take different routes and arrive out of order, which is why the transport layer has to reassemble them.

### 3.3 Testing your own connection, in the right order

When something does not work, the useful approach is to test from the inside outwards, so that each test eliminates one layer.

Start with the local link. Can the machine reach its own gateway? If not, the fault is in the wireless connection, the cable, or the router itself. If the gateway answers, the local network is healthy.

Next, test a numeric address on the public Internet rather than a name. Success proves that addressing, routing and the provider's network are working. Failure at this stage, after the gateway answered, points at the provider or at the path beyond it.

Next, test a name. Success with the numeric address and failure with the name isolates the fault to name resolution, which usually means the name servers configured on the machine are unreachable or wrong.

Next, test a service rather than a host. A web server that answers a ping may still refuse a request on port 443, so a request to the actual service is a different test from a reachability test.

Finally, test throughput. Speed tests measure capacity, and they must be run more than once, at different times, because a single result describes a moment rather than a service.

### 3.4 Choosing a connection for a stated need

A defensible choice starts from the requirement and works towards the technology, never the other way round.

1. Decide what kind of traffic dominates. Large downloads and backups are limited by bandwidth. Browsing, voice and gaming are limited by latency and jitter.
2. Decide whether the connection must be symmetric. A video meeting needs a good upload rate, while ordinary browsing does not.
3. Establish what infrastructure exists at the location. Where fibre is available it is almost always the best answer; where it is not, fixed wireless is the usual compromise.
4. Establish how much outage is tolerable. A business that sells online needs a backup path; a household may not.
5. Compare monthly cost against the requirement, and state the trade-off rather than declaring a single winner.

The mark in such a question is usually awarded for the reasoning, not for the product name. "Fibre, because the site needs a symmetric link for video calls and fibre is the only technology available there that provides one" is a complete answer. "Fibre is the fastest" is not, because it does not engage with the requirement.

### 3.5 Reading the numbers on a plan

Advertised rates are quoted in megabits per second, where one megabit is one million bits. File sizes are usually quoted in megabytes, where one megabyte is eight times as many bits. Confusing the two makes a connection look eight times worse or better than it is, and it is the single most common arithmetic error in this topic.

The conversion to remember is that a rate in megabits per second divided by eight gives a rate in megabytes per second. A 100 megabits per second line therefore transfers at most about 12.5 megabytes per second in ideal conditions, so a 1 gigabyte file needs roughly 80 seconds at best. Real transfers take longer because of protocol overhead, server limits, disk speed and contention.

Two further cautions apply. A provider's figure is usually a peak achieved on a test server inside its own network, which says little about a server on another continent. And an upstream limit can dominate: a household with a fast download and a slow upload will still struggle to send a large file or to run a video meeting.

### 3.6 Keeping the connection safe and usable

The security of a home or small-office connection rests on a small number of practices, all of which follow from how the architecture works.

Change the administrator password on the router before connecting it to anything. Default passwords are published, and a router with a default password is an open door on the inside of your network.

Use the strongest wireless encryption the equipment supports, which today means the standards known as WPA2 or WPA3, short for **Wi-Fi Protected Access**. Older schemes can be broken in minutes by anyone within range.

Keep the router's software updated. The router is a small computer exposed to the Internet, and its firmware is the part most often left unpatched.

Separate guests and untrusted devices onto a guest network, so that a compromised appliance cannot reach the computers that hold your work.

Remember that NAT is not a firewall. It blocks unsolicited inbound connections as a side effect of how it works, but it does nothing about outbound traffic or about a device that initiates the connection itself.

## 4. Worked Implementation from the Notes

### 4.1 Task: prove the line is working and measure how long a reply takes

### 4.2 Implementation: send four echo requests to a public address

Step 1. Ask the operating system to send four echo requests to a stable public address. Four is enough to show a pattern and few enough to be quick.

```powershell
ping -n 4 8.8.8.8
```

Step 2. Read the output. A representative result on a working domestic connection is shown below; the exact times depend on your own path.

```text
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=18ms TTL=117
Reply from 8.8.8.8: bytes=32 time=19ms TTL=117
Reply from 8.8.8.8: bytes=32 time=18ms TTL=117
Reply from 8.8.8.8: bytes=32 time=21ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 18ms, Maximum = 21ms, Average = 19ms
```

Step 3. Interpret each figure. Four replies out of four shows that a path exists and is currently delivering packets. The average of 19 milliseconds is the round-trip time, so a one-way trip is roughly half of that. The spread from 18 to 21 milliseconds is small, which means the delay is steady and the connection would be comfortable for voice traffic. A TTL of 117 tells you that the reply crossed eleven routers if the destination started its counter at 128, which is typical for this service.

Step 4. State what the test does not prove. It says nothing about bandwidth: a satellite link with a huge capacity would show a much larger time. It also does not prove that any particular service is available, because a host can answer an echo request while refusing a connection on port 443.

### 4.3 Task: show the path a packet takes across the world

### 4.4 Implementation: trace the route with a bounded hop count

Step 1. Trace the route, limiting the number of hops so that the command finishes even if the destination is unreachable.

```powershell
tracert -h 12 8.8.8.8
```

Step 2. Read a representative trace from a domestic fibre connection.

```text
Tracing route to 8.8.8.8 over a maximum of 12 hops

  1     1 ms     1 ms     1 ms  192.168.1.1
  2     8 ms     9 ms     8 ms  10.20.0.1
  3    14 ms    15 ms    14 ms  196.201.1.9
  4    96 ms    96 ms    95 ms  195.66.224.20
  5    97 ms    97 ms    96 ms  8.8.8.8

Trace complete.
```

Step 3. Identify each boundary. Hop 1 is the router in the building, holding a private address. Hop 2 is the provider's first aggregation device, also private. Hop 3 is the provider's access concentrator, now carrying a public address. Hop 4 is a router in another country, and the jump from about 15 to about 96 milliseconds is the time taken to cross that long-distance link. Hop 5 is the destination.

Step 4. Explain why the large jump is not a fault. Light in glass travels at roughly two-thirds of its speed in a vacuum, about 200,000 kilometres per second, so a 96 millisecond round trip implies a path of tens of thousands of kilometres. That is simply the distance involved. A genuine fault would show as continuing loss at one hop that persists at every hop after it.

### 4.5 Task: discover the address your machine holds and the address the world sees

### 4.6 Implementation: compare the private and public addresses

Step 1. Display the local configuration, including the address and the gateway.

```powershell
Get-NetIPConfiguration
```

Step 2. A representative result looks like this.

```text
InterfaceAlias       : Wi-Fi
InterfaceIndex       : 12
InterfaceDescription : Intel(R) Wireless-AC 9560 160MHz
NetProfile           : HomeNet
IPv4Address          : 192.168.1.24
IPv4DefaultGateway   : 192.168.1.1
DNSServer            : 192.168.1.1
```

Step 3. Note that 192.168.1.24 lies inside one of the three private ranges, so it cannot be reached from the public Internet. The gateway 192.168.1.1 is the first router on every outgoing path, which is exactly hop 1 in the trace above.

Step 4. Ask an external service what address your traffic appears to come from.

```bash
curl -s https://api.ipify.org
```

Step 5. A representative answer is 41.90.64.17, which is a public address and is different from the local one. The difference proves that translation is happening: your router holds the public address and rewrites the source of outgoing packets, remembering which internal device each reply belongs to. This is also why a device inside the network cannot normally be reached from outside without an explicit forwarding rule.

### 4.7 Task: see which services your own machine is offering

### 4.8 Implementation: list listening ports and match them to services

Step 1. List the ports on which programs are waiting for connections, and show the first few.

```powershell
Get-NetTCPConnection -State Listen | Select-Object -First 8 LocalAddress, LocalPort, OwningProcess
```

Step 2. A representative result is shown below.

```text
LocalAddress LocalPort OwningProcess
------------ --------- -------------
0.0.0.0             80          4120
0.0.0.0            443          4120
127.0.0.1           53          2140
0.0.0.0           3000          8812
0.0.0.0           5357             4
```

Step 3. Interpret the table. Port 80 and port 443 belong to the same process, which is a local web server serving both plain and encrypted pages. Port 53 is a name resolver listening only on the loopback address, so it serves this machine and nothing else. Port 3000 is a development server. The owning process numbers tell you which program to investigate if a port should not be open.

Step 4. Note the demonstration value. A single machine with a single address is serving several services at once, and port numbers are the only thing distinguishing them. That is the concrete form of the transport layer's addressing scheme, and it is also a security lesson: anything listening on 0.0.0.0 is reachable from the network, while anything on 127.0.0.1 is not.

### 4.9 Task: confirm that a web service answers and how quickly

### 4.10 Implementation: request only the headers and read the status

Step 1. Request the headers of a page without downloading the body.

```bash
curl -I https://example.com
```

Step 2. A representative response is shown below.

```text
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Connection: close
```

Step 3. Interpret the response. The first line contains the protocol version, the status code and a short reason phrase. A 200 means the request succeeded, so name resolution, connection setup, the encrypted session and the server application all worked. The content type tells the browser to render the body as a page, and the length tells it how much to expect.

Step 4. Compare this with a ping. A ping proves the host is reachable; this proves the service is reachable, the certificate is acceptable, and the application is responding. When a browser says a site is unavailable but a ping succeeds, a request of this kind distinguishes a dead application from a broken network.

## 5. Testing, Interpretation, and Common Errors

### 5.1 A self-test you can run in five minutes

You have understood this topic if you can do all of the following without notes.

State the three parts of the definition of the Internet and give one example of each. Say what the World Wide Web is and name two Internet services that do not need it. Name the three kinds of physical equipment and the function of each. Explain what an ISP is and what distinguishes the three provider tiers. Name six access technologies and one advantage and one disadvantage of each. Name the four layers, the protocol at each, and the addressing scheme each uses. Explain why an IP address stays the same across the journey while a hardware address changes at every hop. Read a ping output and a trace output and say what each figure does and does not prove. Explain the difference between bandwidth and latency with an example. State four advantages of the architecture and two social problems it creates.

If any of those produces hesitation, that is the section to revisit, not the whole topic.

### 5.2 Two everyday comparisons for the numbers

The first comparison is a road. Bandwidth is the number of lanes; latency is the length of the road. Widening a road does not make it shorter, so adding capacity never removes delay. A very wide road that is very long still takes a long time for one car to arrive, even though it can deliver a huge convoy in the same period.

The second comparison is a delivery of bricks. Latency is how long the first brick takes to arrive; bandwidth is how many bricks arrive per minute after that. If you need one brick urgently, the first figure decides. If you need a lorry load, the second decides. This is why a satellite link with generous capacity still feels sluggish when you click a link, while a modest fibre link feels instant.

A third quantity deserves its own image. Packet loss is like a postal service that occasionally loses an envelope. For a letter, you can post it again, and a file transfer does exactly that. For a live conversation, posting it again is pointless because the moment has passed. That is the reason a connection can be excellent for downloads and unusable for calls at the same time.

### 5.3 Beginner misconceptions, with the correction

- **"The Internet and the World Wide Web are the same thing."** The Internet is the transport system. The Web is one service on it. Email and name lookup predate the Web and do not need it.
- **"The Internet is owned by one company or one government."** It is a network of networks owned by thousands of organisations. Coordination comes from shared protocols and from bodies that publish standards, not from ownership.
- **"Data travels as one continuous stream."** It is divided into packets that may take different routes and arrive out of order.
- **"A faster connection means a lower delay."** Bandwidth and latency are independent. Buying more capacity does not shorten a path.
- **"The number on the plan is the speed you get."** It is a peak on a favourable test. Contention, distance and the far server all reduce it.
- **"Megabits and megabytes are the same."** One byte is eight bits, so a rate quoted in megabits per second is eight times larger than the same rate quoted in megabytes per second.
- **"A failed ping proves the site is down."** Many hosts deliberately ignore echo requests. Test the actual service before concluding anything.
- **"The IP address is the same as the hardware address."** The IP address is used across networks and stays the same for the journey. The hardware address is used within one link only and changes at each hop.
- **"A private address such as 192.168.1.24 is your address on the Internet."** It is your address inside your own network. The public address belongs to the router, which translates between the two.
- **"Wi-Fi and the Internet are the same thing."** Wi-Fi is the wireless link between your device and your router. The Internet begins beyond the router, and the router reaches it through a provider.
- **"Satellite Internet is fast, so it is good for gaming."** Its capacity may be high, but its delay of roughly half a second makes interactive play unpleasant. Low-orbit systems reduce the delay and cost much more.
- **"Fibre is fast purely because the glass is new."** Fibre is fast because light suffers very little loss and is immune to electrical interference, so capacity can be raised by changing the equipment at each end rather than by replacing the cable.
- **"Dial-up and DSL are the same because both use the telephone line."** Dial-up converts data to audible tones and occupies the line; DSL uses frequencies above speech and leaves the line usable for calls.
- **"Encryption makes a connection slower, so it should be avoided."** The delay added by modern encryption is small compared with the risk of sending passwords in clear text.

### 5.4 Why the architecture is an advantage

The advantages are best understood as consequences of four design decisions, because that framing turns a list into an explanation.

**Open interconnection.** Any network can join by adopting the published protocols. The barrier to entry is low, competition is possible at every level, and a small organisation can reach a global audience without negotiating with every network in between.

**Application neutrality.** The network does not inspect or interpret what it carries. New services can therefore be deployed by the two parties involved, without permission from the operators in the middle. This is why the Web, streaming and conferencing arrived without a coordinated rebuild.

**Redundancy.** Routing adapts to the failure of individual links and routers. A cut cable causes congestion and slower paths rather than a national outage.

**Layering.** Each layer has a defined job and a defined interface, so a fault can be localised. A broken cable is a link-layer problem, a wrong route is an internet-layer problem, and a rejected password is an application-layer problem. Systematic diagnosis depends on this separation.

### 5.5 What it has done to society

The social effects follow from the same properties, and a fair answer names both directions.

On the positive side, the cost of publishing has fallen to almost nothing, so a school, a clinic or a small business can reach the same audience as a large institution. Education and health information are available to people who cannot travel. Work can be done remotely, which widens the pool of jobs available to someone outside a capital city. Small enterprises can sell nationally and internationally without a chain of physical shops. Public services can be delivered online, and families can stay in contact across distances that would once have meant letters.

On the negative side, the same openness that permits innovation permits fraud and abuse, because there is no central authority able to inspect everything. A small number of platforms intermediate a large share of attention and commerce, which concentrates power. Unequal access, in both availability and cost, reproduces and sometimes widens existing inequalities, and this is what the phrase **digital divide** describes. Security is an ongoing cost carried by the endpoints, because the network cannot be trusted to filter. And the physical footprint is real: data centres and access networks consume significant electricity and water.

The balanced sentence to write is that each benefit and each harm come from the same property. Openness produces both low barriers to entry and the difficulty of policing abuse. Neutrality produces both rapid innovation and the concentration of attention. Redundancy produces both resilience and an expectation of perpetual availability that makes any outage feel like a crisis.

### 5.6 The limits worth naming

Four limits complete the picture and are frequently worth a mark each.

IPv4 ran out of unallocated addresses, which is why translation is universal and why IPv6 exists. Best-effort delivery means that delay and loss are not guaranteed to be controlled, so real-time quality must be engineered rather than assumed. The absence of a single authority makes security coordination difficult, so vulnerabilities are patched at the endpoints rather than prevented in the network. And congestion is a shared problem, because each user acting alone has no reason to slow down, which means management requires either cooperation or pricing.

### 5.7 A checklist for any question in this topic

1. Decide which of the four areas the question belongs to: infrastructure, layering, access technology, or measurement.
2. For infrastructure, name the component and its function in one sentence each.
3. For layering, give the layer, the protocol, the data unit and the addressing.
4. For access technology, compare on bandwidth, latency, reliability and cost, then justify one choice against the stated requirement.
5. For measurement, say what the tool tests, what the output shows, and what it cannot show.
6. End with the trade-off, because a stated trade-off is what separates a description from an argument.
