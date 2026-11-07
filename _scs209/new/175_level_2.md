## 1. Concept and Use Case

### 1.1 The Web, stated precisely

The World Wide Web is an information space in which resources are named by Uniform Resource Identifiers, described and connected by hypertext, and transferred between programs using the Hypertext Transfer Protocol over the Internet. Four commitments are packed into that sentence, and each one is separately examinable.

The first is **naming**: every resource has an identifier that is unique within the space and that encodes enough information for a client to act on it. The second is **linking**: the description of a resource can contain references to other resources, and following a reference is a first-class operation rather than an afterthought. The third is **transfer by a common protocol**: the request and the response have a fixed syntax, so any client can talk to any server without prior agreement. The fourth is **dependence on the Internet**: the Web supplies no links, no routing and no addressing of its own; it borrows the Internet Protocol suite and adds an application layer on top.

A narrower definition, the one used when the Web is treated as a technical system rather than a body of content, is that the Web is the set of resources and users that communicate using HTTP. A broader definition, adopted by the World Wide Web Consortium, describes it as the universe of network-accessible information and an embodiment of human knowledge. The narrow definition is the one that supports engineering statements; the broad one is the one that supports statements about publishing and society. A strong answer names both and says which is which.

### 1.2 The distinction that carries marks

The Internet is a packet-switched network of networks that uses the Internet Protocol for addressing and routing, and the Transmission Control Protocol or the User Datagram Protocol for transport. The Web is an application that runs over that network. The distinction is not pedantic: electronic mail, the Domain Name System, secure remote login over the Secure Shell, and file transfer all operate over the Internet without the Web, and all predate it.

Three pieces of evidence settle the question. The Internet was operational in 1969 and the Web was proposed in 1989. The Web's own protocols are layered on top of Internet transport, so a failure of the lower layer stops the Web while the reverse is not true. And the Web's address space is a naming scheme imposed on the Internet's addressing, not a replacement for it, since every web request ultimately reaches an Internet Protocol address.

### 1.3 Architectural evolution

The evolution of the Web is best told as the accumulation of four capabilities on top of one original model, because each capability removed a specific limitation rather than changing the design.

**The basic model.** The original arrangement had a client, a server, an identifier, a protocol and a markup language, and information flowed in one direction only. The client requested a document by name; the server returned it as Hypertext Markup Language; the connection was stateless; the protocol carried no metadata beyond what was needed to find the document. This corresponds to the earliest protocol revision, which knew only a request for a document and a response containing it, and to the first version of the markup language. Its limitations were severe and easy to enumerate: no way to send data from client to server, no way for a client to state which formats it could accept, no way to express the type of the returned body, and no way to carry anything except markup.

**Identifiers.** The naming layer was formalised into a family. A Uniform Resource Identifier is the general concept: any string that names a resource. A Uniform Resource Locator is a URI that identifies a resource by its access mechanism, which is why a URL can be resolved by a client that knows nothing about the resource. A Uniform Resource Name is intended to be a persistent identifier independent of location, and a Uniform Resource Citation was proposed as attribute-value metadata about a resource. In practice the Web runs on URLs, and the persistent naming problem that URNs were meant to solve has been addressed commercially by permanent redirects rather than by a new naming scheme.

**The protocol layer.** HTTP was specified as a stateless presentation-layer protocol modelled on the Multipurpose Internet Mail Extensions, usually shortened to MIME: a set of headers, optionally followed by a body in any format the client can accept, with the client declaring its capabilities through accept headers. Because the protocol could wrap messages belonging to other protocols inside its own headers, it became a general envelope, which is the technical basis of the proxy server. The protocol was placed on top of TCP, whose three-way handshake establishes a reliable byte stream, at the cost of a round trip before any request can be sent.

**The markup layer.** HTML was defined as an application of the Standard Generalized Markup Language, an international standard for defining document types. The original definition was a Document Type Definition on top of an SGML parser, and it grew into a richer definition able to express tables, images and forms, and eventually into the current standard with a parsing algorithm specified in detail so that all engines produce the same tree from the same bytes. The essential point for architecture is that markup is the only thing the server is obliged to send, and even that obligation is weak: a server may store data in any format and generate the markup at request time, which is the origin of the virtual document.

**The interactive model.** The addition that turned the Web into a platform was bidirectional transfer. The client can post a body to the server where the server permits it, the body may be any format from seven-bit text to eight-bit binary, and the transfer may use any protocol the Web supports, with HTTP acting as the carrier because it can encapsulate the others. From that single change came forms, searches, uploads, sessions, and eventually the application architectures that dominate current practice.

**Later additions.** Server-side program execution, first through the Common Gateway Interface, allowed a response to be computed. Cookies allowed state to be carried across stateless requests. Asynchronous JavaScript allowed a page to exchange data without a full reload. Persistent connections, request pipelining, header compression and multiplexing reduced the cost of many small requests, and encryption became effectively universal. None of these altered the underlying request-response contract.

### 1.4 What the client-server split buys, and what it costs

The split concentrates presentation in the client and authority in the server. That yields four durable benefits: independent evolution of the two sides, because they only share a protocol; horizontal scaling of the server side, because stateless requests can be answered by any member of a pool; caching at many points, because a response can be reused without contacting the origin; and a clear security boundary, because the data and rules that must not be disclosed never leave the server.

The costs are equally concrete. Every interaction that needs the server pays a round trip, which is bounded below by the speed of light in fibre and above by queueing. State must be reconstructed on every request or carried explicitly, which adds moving parts. The server must be reachable continuously and must be provisioned for peak load. And because the client is under the user's control, the server must treat every request as potentially hostile.

### 1.5 Typical use cases

The architecture supports four broad classes of use, and distinguishing them clarifies which parts of the model are under strain. Publishing, where the same content is served to everyone and caching is easy. Transactional services, where each request depends on identity and state and caching must be restricted. Media distribution, where bodies are large and range requests matter. And system integration, where the client is another program rather than a person and the response is data rather than presentation.

## 2. Data, Syntax, and Core Concepts

### 2.1 Identifier syntax and resolution

A URL has the general form scheme, colon, two slashes, authority, path, optional query and optional fragment. Each component has a defined role and a defined set of legal characters.

The **scheme** selects the protocol handler. `http` implies port 80 and no encryption; `https` means HTTP carried over Transport Layer Security, usually written TLS, and implies port 443. The **authority** contains an optional user information part, a host and an optional port. The **path** is a sequence of segments separated by slashes, and it is interpreted by the server, not by the protocol. The **query** begins with a question mark and is a sequence of name-value pairs separated by ampersands. The **fragment** begins with a hash and is never transmitted.

Resolution of a relative reference is defined algorithmically. Given a base address and a relative reference, the client merges the paths, removes dot segments, and produces an absolute address. This is why a page at `/shop/items/list.html` containing `href="../index.html"` resolves to `/shop/index.html`, and why a page moved to a different directory breaks its relative links while its absolute links continue to work.

Percent-encoding handles characters that are not legal in a component. A space becomes `%20`, and a reserved character that must appear literally is encoded so that it is not mistaken for a delimiter. This matters because a query string is not a free-text field: it is a structured component whose delimiters must be respected.

### 2.2 Message syntax

An HTTP message is a sequence of bytes with a rigid shape. A request begins with a request line, then zero or more header fields, then a blank line, then an optional body.

```http
POST /orders HTTP/1.1
Host: shop.example
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Accept: text/html,application/xhtml+xml
Accept-Encoding: gzip, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Connection: keep-alive

item=beans&qty=2&grind=medium&ship=yes
```

The request line has three parts separated by single spaces: the method, the request target and the protocol version. The `Host` header is mandatory in the current version and is what makes name-based virtual hosting possible. `Content-Length` delimits the body, and its presence is what tells the server how many bytes to read after the blank line. The body here is form-encoded, which is one of three common encodings, the others being multipart for file uploads and JSON for programmatic clients.

A response has the same shape with a status line instead of a request line.

```http
HTTP/1.1 201 Created
Date: Fri, 07 Nov 2026 09:21:44 GMT
Server: nginx/1.24.0
Content-Type: application/json
Content-Length: 64
Location: /orders/8842
Cache-Control: no-store

{"id": 8842, "status": "accepted", "item": "beans", "quantity": 2}
```

The status line carries a three-digit code and a reason phrase that is informative only; clients must act on the code. The `Location` header is meaningful for a created resource and for redirects. `Cache-Control: no-store` instructs every cache not to retain the response, which is the correct instruction for an order confirmation.

Header field names are case-insensitive; field values are not. Field order is not significant except for fields that may appear repeatedly. Line endings are carriage return followed by line feed, which is one of the few places where the protocol is unforgiving.

### 2.3 Methods, status classes and the headers that carry meaning

The method states the intent. `GET` retrieves a representation and must not change server state. `HEAD` retrieves the headers a `GET` would produce, without the body, and is the correct way to test a resource cheaply. `POST` submits data for processing, may change state, and is not safely repeatable. `PUT` replaces a resource at a known address. `PATCH` applies a partial modification. `DELETE` removes a resource. `OPTIONS` asks which methods and capabilities a resource supports.

The status code states the outcome in classes. Informational codes beginning with 1 mean the request was received and processing continues. Success codes beginning with 2 mean the request was understood, accepted and processed. Redirection codes beginning with 3 mean further action is needed, usually at another address. Client error codes beginning with 4 mean the request was malformed, unauthorised or aimed at something that does not exist. Server error codes beginning with 5 mean a syntactically valid request could not be fulfilled because of a fault on the server side.

| Code | Meaning | Typical cause in practice |
|---|---|---|
| 200 | OK | Normal successful retrieval |
| 201 | Created | A POST produced a new resource, with its address in Location |
| 301 | Moved Permanently | The resource has a new canonical address |
| 304 | Not Modified | The client's cached copy is still valid |
| 400 | Bad Request | Malformed syntax, such as a missing Host header |
| 403 | Forbidden | The server understood but refuses, often a permission problem |
| 404 | Not Found | No resource maps to the path |
| 405 | Method Not Allowed | The path exists but not for this method |
| 500 | Internal Server Error | A program failed while building the response |
| 502 | Bad Gateway | A proxy could not obtain a valid response from the upstream server |
| 503 | Service Unavailable | Overload or maintenance, often with Retry-After |

Several headers deserve names because they explain behaviour that otherwise looks mysterious. `Content-Type` states the media type and, for text, the character encoding. `Content-Length` gives the body size in bytes; when it is absent and the body is streamed, the response uses chunked transfer encoding. `Cache-Control` states freshness rules. `ETag` gives an opaque validator for a specific version of the representation. `Last-Modified` gives a time-based validator. `If-None-Match` and `If-Modified-Since` let the client ask whether its copy is still valid, which is how a 304 is produced. `Set-Cookie` hands state to the client. `Location` names another address. `Vary` tells caches which request headers change the response.

### 2.4 Hypertext, hypermedia and non-linear navigation

Hypertext is a data model in which documents are nodes and references are directed edges. The model is deliberately graph-like rather than tree-like: there is no root, no required order, and no guarantee that any two nodes are reachable from one another. Hypermedia extends the model to nodes that contain media other than text.

The practical consequences follow from the graph. Because navigation is associative, a reader can enter at any node, which means every node must be intelligible without assuming a starting point. Because links are cheap to create and expensive to maintain, link integrity decays, which is why the 404 response is a normal outcome rather than an exceptional one. Because there is no canonical sequence, orientation aids such as navigation bars, breadcrumbs and consistent headings are not decoration but a response to a structural property of the medium. And because a link can point anywhere, the Web has no notion of a document boundary, so authorship and provenance become difficult to establish, which is the structural root of many contemporary problems in information quality.

Link classification matters for implementation. Internal links keep the reader inside the site and can be validated at build time. External links leave it and cannot. Relative links survive relocation of the site; absolute links do not need to. Fragment links address a position inside a document and are resolved locally. Links that carry query parameters create distinct cacheable representations, which has consequences for caching and for duplicate content.

### 2.5 The browser as a system of components

The browser is conventionally decomposed into seven subsystems, and the decomposition is examinable because each subsystem has a distinct failure mode.

The **user interface** provides the address bar, navigation controls, tabs, bookmarks, history views, download manager and settings. It is the only component the user interacts with directly, and it is not standardised, which is why browsers differ so much in appearance.

The **browser engine** is the coordinator. It accepts high-level commands such as navigate, reload, stop and back; it manages the session history and the mapping between history entries and documents; it decides when a navigation may be served from cache; it applies policy such as blocking mixed content; and it drives the rendering engine by supplying it with content and telling it when to lay out and paint. It also owns the tab model and the process model, which in modern browsers means deciding which renderer process handles which origin.

The **rendering engine** converts markup and style into a render tree and then into pixels. Its internal pipeline is parse, style, layout, paint and composite. It knows nothing about history, bookmarks or the address bar; it receives a document and a viewport and produces a surface.

The **networking subsystem** implements HTTP, manages connection pools, performs name resolution, negotiates TLS, applies byte-range requests and consults the HTTP cache. It is the only component that talks to the network.

The **JavaScript engine** parses and executes scripts and provides the object graph that scripts manipulate. Its performance characteristics differ substantially between products.

The **user interface backend** draws standard widgets using the host operating system's facilities.

The **storage subsystem** persists data: the HTTP cache, cookies, local and session storage, indexed databases, the cache storage used by service workers, saved credentials and history.

### 2.6 Browser engine and rendering engine are not synonyms

The two terms are often used interchangeably in casual writing, and the confusion causes wrong answers because the components have different responsibilities and different names.

The **rendering engine** is the layout and painting component. Its inputs are a document and a style description; its output is what appears in the viewport. When people say that Chrome uses Blink, Firefox uses Gecko and Safari uses WebKit, they are naming rendering engines.

The **browser engine** is the layer above it. It loads a document in response to a navigation, arranges for the rendering engine to be instantiated or reused for that content, maintains history, coordinates the loading of subresources, applies content policy, and dispatches events between the user interface and the page. In some texts the phrase browser engine is used loosely to mean the rendering engine, which is precisely why a careful answer defines the term before using it.

The distinction has visible consequences. Two browsers may share a rendering engine and still differ in history behaviour, tab isolation, back-forward cache semantics or security policy, because those are browser-engine responsibilities. Conversely, a browser may change its browser engine architecture, as Edge did when it moved to Chromium, without that being described as a change of rendering engine alone.

### 2.7 The rendering engines and the browsers built on them

Three engines account for essentially all current use, and the mapping to browsers and script engines is fixed knowledge.

| Engine | Owner | Script engine | Browsers using it | Notes |
|---|---|---|---|---|
| Blink | Chromium project, Google-led | V8 | Chrome, Edge, Opera, Brave, Samsung Internet | Forked from WebKit in 2013; the largest share of the market |
| Gecko | Mozilla | SpiderMonkey | Firefox, Thunderbird | Independent codebase with its own layout and style implementation |
| WebKit | Apple | JavaScriptCore | Safari, all browsers on iOS and iPadOS | Forked from KHTML; the only permitted engine on Apple mobile platforms |
| EdgeHTML | Microsoft | Chakra | Legacy Edge only, before 2020 | Retired in favour of Chromium |
| Presto | Opera Software | Carakan | Opera before 2013 | Retired in favour of Blink |

Two facts in that table are frequently examined and frequently missed. The first is that Edge is no longer built on a Microsoft engine; the current product is Chromium-based, so it renders with Blink and executes with V8. The second is that every browser on iOS uses WebKit regardless of its name, because the platform does not permit third-party rendering engines, so a claim that Chrome on an iPhone uses Blink is wrong.

The practical significance is compatibility. Because Blink dominates, sites are usually developed and tested against it first, which produces a feedback loop in which other engines are more likely to be the ones that break. Standards conformance reduces but does not eliminate the divergence, since each engine has its own bug history and its own schedule for implementing new features.

### 2.8 Where a browser keeps data

Persistence is part of the architecture, not an implementation detail, because it determines what a site can do without contacting the server and what survives a restart.

| Storage | Lifetime | Typical size | Sent to the server | Controlled by |
|---|---|---|---|---|
| HTTP cache | Until expiry or eviction | Large, bounded by quota | No | Response headers such as Cache-Control and ETag |
| Cookie | Set expiry, otherwise session | Small, a few kilobytes each | Yes, on every matching request | Set-Cookie and the browser's policy |
| Session storage | Until the tab closes | A few megabytes | No | Page scripts, same origin only |
| Local storage | Until deleted | A few megabytes per origin | No | Page scripts, same origin only |
| Indexed database | Until deleted | Large, quota-managed | No | Page scripts, same origin only |
| Cache storage | Until deleted | Large | No | Service worker code |

The rules that make this safe are the same-origin policy and its extensions. An origin is the combination of scheme, host and port, and storage is partitioned by origin, so a script on one origin cannot read another origin's storage directly. Cookies are the exception in the other direction: they are transmitted automatically with matching requests, which is why they are the classic vehicle for session identity and the classic target for cross-site attacks.

### 2.9 Web server architecture

A web server is a program with five internal responsibilities, and the way it implements each one distinguishes the products.

**Listening and accepting.** The server binds a socket to an address and port, marks it listening, and repeatedly accepts connections. The accept loop is the outermost structure of the program.

**Connection handling.** This is the major architectural fork. A process-per-connection model is simple and isolated but expensive at high concurrency. A thread-pool model amortises the cost of process creation but bounds concurrency by thread count and memory. An event-driven model uses a small number of workers with non-blocking I/O and a readiness notification mechanism, so a single worker can hold many thousands of connections. Apache supports all three through its multi-processing modules; Nginx is event-driven by design.

**Request parsing and routing.** The server reads the request line and headers, enforces limits on their size, validates the Host header, and routes the request to a handler. Routing may be by filesystem path, by pattern matching on the path, by host name for virtual hosting, or by a rewrite rule that transforms the path before it is interpreted.

**Resource resolution.** For a static request the route ends at a file. The server maps the path into the document root, normalises it to prevent traversal outside that root, checks permissions, determines the media type from the extension or a configured mapping, and prepares a response with validators. For a dynamic request the route ends at an interface: a FastCGI socket, an application server port, a servlet container, a WebSocket endpoint or an embedded interpreter.

**Response construction and logging.** The server assembles the status line and headers, may compress the body, may add cache and security headers, and writes the response. It appends an entry to the access log, usually in a common format that records the client address, identity, authenticated user, timestamp, request line, status, byte count, referrer and user agent.

Two further responsibilities are common in production. **Virtual hosting** lets one address and port serve many sites, distinguished by the Host header in name-based hosting or by the local address in address-based hosting. **Reverse proxying** lets the server forward a request to another program and relay the answer, which is how a modern deployment puts a fast static file server and TLS terminator in front of one or more application processes.

### 2.10 Static and dynamic handling

Static handling is a read-and-copy operation with metadata. The server resolves the path to a file, obtains its size and modification time, computes or looks up an entity tag, checks the client's conditional headers, and either returns 304 with no body or streams the file with the appropriate content type. Because the content is fixed, the response can carry strong validators and long freshness lifetimes.

Dynamic handling is a delegation. The server resolves the path to a handler, passes the request metadata and body to it, waits for or streams the result, and returns whatever the handler produced. The handler may consult a database, apply business rules, render a template and set its own headers. Because the content is produced per request, validators are either absent or computed from the inputs, and freshness is usually set to no-cache or a very short lifetime.

The difference is visible in the protocol trace, and an answer that asserts the difference without citing evidence is weak. Static responses typically carry `Last-Modified`, a stable `Content-Length` and a long `Cache-Control`. Dynamic responses typically carry `Cache-Control: no-store` or a private directive, may omit `Content-Length` when streaming, often set a cookie, and often vary with the request body or with a session header. A second request for the same static resource produces the same bytes; a second request for a dynamic resource may not.

The intermediate case is worth naming. A page can be generated once and then cached as a file, which is static generation; or generated per request but cached in memory for a short period, which is dynamic with a cache in front. Both are common, and neither changes the underlying distinction between a stored representation and a computed one.

### 2.11 Server platforms compared

The four platforms occupy different niches, and the comparison is a standard examination table.

| Platform | Vendor and licence | Operating systems | Connection model | Configuration and extension | Dynamic integration |
|---|---|---|---|---|---|
| Apache HTTP Server | Apache Software Foundation, open source | Linux, Unix, Windows, macOS, FreeBSD | Process or thread pools via multi-processing modules, including an event module | Text configuration files plus per-directory `.htaccess`; large module library | Modules for embedded interpreters, FastCGI, reverse proxy to application servers |
| Microsoft IIS | Microsoft, bundled with Windows Server | Windows | Thread-based worker processes organised into application pools | Graphical console and XML configuration files | Native integration with Microsoft application platforms; FastCGI for others |
| Nginx | Open source, BSD-style licence | Linux, Unix, Windows, macOS | Event-driven workers with non-blocking I/O | Declarative configuration with server and location blocks | Reverse proxy and FastCGI to separate application processes |
| Sun Java System Web Server | Oracle, formerly Sun, free but not open source | Windows, Linux, several Unix variants | Process-based with configurable pools | Administrative console and configuration files | Java platform technologies, plus interfaces for other languages |

Three comparative judgements follow from the table. Apache offers the widest configurability and the largest ecosystem, at the cost of memory per connection under older process models. Nginx offers the best behaviour under very high concurrency and is usually deployed as a front end rather than as an application host. IIS offers the tightest integration with Windows and Microsoft's application stack. The Sun product is aimed at organisations already committed to the Java platform and to medium or large sites.

### 2.12 Client-side execution versus server-side processing

The Web has two execution environments, and almost every design decision in a modern application is a decision about which one does a piece of work.

**Client-side execution** means code is delivered as part of the response and runs in the browser. The markup and style sheets are interpreted by the rendering engine, and scripts are executed by the script engine, which has access to the document tree, to storage, to the network through the fetch interface, and to a large set of browser capabilities. Client-side code can respond to an event in milliseconds because no round trip is required, it can continue working while the network is unavailable if the data is already present, and it offloads computation from the server to the user's device. Its constraints are equally definite: it is fully visible to the user, it can be modified, it runs under the same-origin policy so it cannot read another origin's data, it cannot be trusted with secrets, and its performance depends on the device.

**Server-side processing** means code runs before the response leaves the server, inside a handler reached through an interface such as FastCGI, a servlet container or a reverse-proxied application process. It has access to databases, the file system, internal services, credentials and the authoritative copy of every business rule. Its output is the only thing the client receives, so its logic and its data remain hidden. Its constraints are latency, because every interaction that needs it costs a round trip, and capacity, because every concurrent user consumes server resources.

The boundary between the two is a trust boundary, and this is the part that is most often examined. Anything supplied by the client, including anything validated by client-side code, must be treated as untrusted. A rule enforced only in the browser is not enforced at all, because the browser belongs to the user. A secret embedded in client-side code is published, because the code is delivered. Conversely, a server that repeats every check is not being redundant; it is placing the check where it can be relied upon.

The boundary is also a performance boundary. Rendering a page on the server and sending finished markup produces a fast first paint and content that can be cached by an intermediary. Rendering in the browser produces a smaller initial response and richer interaction after the code has loaded. The two are often combined, with the server sending markup that is already populated and the client taking over afterwards, which is why the same application can be described as both server-rendered and client-rendered.

Evidence of the boundary is easy to obtain. The document source shows all client-side code that was delivered, because it is part of the response. It never shows server-side code, only that code's output. A page whose source contains a full data set that the interface merely filters is doing the filtering on the client; a page whose source contains an empty container and a script that requests data is doing the work on the server or at an interface in between.

## 3. Methods and Operations

### 3.1 The request-response cycle, step by step

The following sequence is the canonical description, and each step is a place where a real system can fail.

1. **Intent.** The user activates a link or submits an address. The user interface hands the navigation to the browser engine as a command with a target address and a disposition such as same tab or new tab.
2. **Address parsing.** The browser engine parses the address into scheme, host, port, path, query and fragment, and rejects or repairs malformed input. A bare host name is completed with a default scheme, which is why typing a name and pressing enter usually produces an HTTPS request.
3. **Policy checks.** The browser applies its security policy: it may upgrade the scheme, block a mixed-content request, or refuse a navigation to a scheme with no registered handler.
4. **Cache lookup.** The networking subsystem checks the HTTP cache for a fresh response matching the request method and the varying headers. A fresh hit ends the network part of the cycle.
5. **Name resolution.** The host is resolved to an address. The browser checks its own cache, then the operating system's resolver cache, then asks a recursive resolver, which may consult root, top-level-domain and authoritative servers in turn. The result is an address record, and for dual-stack hosts both an IPv4 and an IPv6 record may be returned with a preference order.
6. **Transport connection.** A TCP connection is established with a three-way handshake: the client sends a synchronise segment, the server replies with synchronise-acknowledge, and the client completes with acknowledge. The connection is identified by the four-tuple of client address, client port, server address and server port.
7. **Security negotiation.** For HTTPS, a TLS handshake follows. In current versions the client sends a hello containing supported versions, cipher suites and a key share; the server responds with its choice, its certificate chain and its own key share; both derive session keys; and encrypted application data begins. The certificate is validated against the requested host name and a trusted authority.
8. **Request transmission.** The client writes the request line, the headers including `Host`, and the body if any. The `Host` header is what allows one address to serve many sites.
9. **Server admission and parsing.** The server accepts the connection, reads the request under limits on header size and body size, validates the syntax, and identifies the virtual host from the Host header.
10. **Routing and authorisation.** A handler is selected. Access control, authentication and rate limiting may be applied. For a static path the handler is the file system; for a dynamic path it is an application process.
11. **Response generation.** The handler produces a status, headers and a body. The server may compress the body, add validators, and apply cache directives.
12. **Response transmission and completion.** The response is written, the connection is either kept alive for reuse or closed according to the protocol version and the `Connection` header, and the transaction is logged.
13. **Rendering.** For an HTML response the browser parses the markup into a document tree, discovers subresources, requests them in parallel subject to per-host connection limits, parses style, computes layout, paints and composites. Scripts may block parsing unless marked to load asynchronously or defer.

The cycle clarifies three facts that are often stated vaguely. Latency is dominated by round trips, not by bandwidth, for small resources. Caching can remove steps four to twelve entirely. And the number of distinct resources determines how many times steps eight to twelve execute, which is why bundling and reuse of connections matter.

### 3.2 Comparing connection-handling models

A process-per-connection server isolates faults completely, because a crash affects one request, but each process costs address space and a context switch. A thread-pool server amortises creation but must bound the pool, so a slow client can occupy a thread and reduce capacity for others, which is the classic denial-of-service pattern. An event-driven server registers interest in readiness and multiplexes many connections in one thread, so slow clients consume a small state object rather than a thread.

The trade-off is complexity: event-driven code must never block, and any blocking call stalls every connection handled by that worker. This is why event-driven servers usually delegate dynamic work to separate processes rather than executing it inline.

### 3.3 Mapping a path to a handler

A defensible method proceeds in a fixed order. Normalise the path, resolving dot segments and percent-encoding, and reject any result that escapes the document root. Match the longest configured prefix or regular expression. Apply rewrite rules in the defined order, and stop when a rule is marked terminal. If the result names a directory, apply the configured index file. If the result names an existing file, choose static handling. Otherwise, if a dynamic route matches, delegate. Otherwise, return 404.

Two rules prevent most incidents. Never trust a path before normalisation, because traversal sequences are the oldest web server attack. And define the precedence between static files and dynamic handlers explicitly, because a dynamic handler that shadows an upload directory can serve user-supplied code as if it were content.

### 3.4 Choosing caching policy

Three questions decide the instruction. Is the representation identical for every user? If yes, it may be public and long-lived. Does it depend on identity? If yes, it must be private or non-storable. Is it acceptable to show a slightly stale copy? If yes, a short freshness lifetime with revalidation is better than no caching at all.

The mechanism of revalidation is worth stating precisely. The server supplies a validator, either an entity tag or a modification time. The client stores it with the response. On a later request the client sends `If-None-Match` or `If-Modified-Since`. The server compares and, if the representation is unchanged, answers 304 with no body. The client then reuses its stored copy and updates its metadata. This is the single largest saving available in a typical site, because it removes the body from the exchange while preserving correctness.

### 3.5 Selecting a server platform

Selection follows from requirements rather than preference. Establish the operating system standard, because IIS is Windows-only and the others are portable. Establish the application platform, because integration with a Java or Microsoft stack constrains the choice. Establish the concurrency profile, because a site that must hold tens of thousands of idle connections favours an event-driven server. Establish the operational skill available, because a server that nobody on the team can debug is a liability. Then compare, and state the trade-off explicitly rather than declaring a winner.

### 3.6 Partitioning work between client and server

A defensible partition is reached by asking five questions in order and recording the answer to each.

Is the data secret? If yes, it stays on the server, because anything sent to a browser is published. Is the rule authoritative? If yes, it is enforced on the server, even when a duplicate check exists in the browser for speed. Must the response be immediate? If yes, the interaction belongs in the browser, because a round trip is perceptible. Can the work be done without the network at all? If yes, doing it in the browser reduces load and improves resilience. Does the answer need to be cacheable by an intermediary? If yes, producing it on the server and marking it public is simpler than reconstructing it in every client.

Two anti-patterns are worth naming because they appear in examination scenarios. The first is **trusting the browser**, which occurs when a price, a permission or a validation rule exists only in client-side code; the correct answer states that the server must repeat the check. The second is **over-serialising**, which occurs when every keystroke triggers a request; the correct answer is to batch, debounce or perform the work locally.

The partition has a visible consequence in the protocol trace. Work done in the browser produces one response that is larger and contains the code, followed by no further requests for that interaction. Work done on the server produces several responses, each small, each carrying a new representation. Counting requests is therefore a practical way to see where the work is happening.

## 4. Worked Implementation from the Notes

### 4.1 Task: serve one site with Apache and one with Nginx, distinguishing static from dynamic handling in each

### 4.2 Implementation: configure virtual hosts, add a rewrite, proxy a dynamic path, then verify with header-level evidence

Step 1. Create the document root and a minimal page that the server can return byte for byte.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Karibu Coffee</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Karibu Coffee</h1>
    <p>Roasted in Nakuru, shipped on Mondays.</p>
  </header>
  <main>
    <p><a href="/beans">See this week's lots</a></p>
  </main>
</body>
</html>
```

The page requests `/beans`, which will later be answered by a program rather than a file. Nothing in the markup distinguishes the two cases; only the server's routing does.

Step 2. Configure Apache to serve the site by name, with a rewrite that maps an attractive address onto a real file.

```apache
<VirtualHost *:80>
    ServerName karibu.example
    ServerAlias www.karibu.example
    DocumentRoot "/srv/karibu/public"

    <Directory "/srv/karibu/public">
        Options FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog "/var/log/apache2/karibu-error.log"
    CustomLog "/var/log/apache2/karibu-access.log" combined
</VirtualHost>
```

The `ServerName` and `ServerAlias` directives are what make name-based virtual hosting work: Apache compares the Host header against these values to choose the virtual host, so several sites can share one address. `AllowOverride All` permits per-directory configuration, which the next step uses.

Step 3. Add a per-directory rewrite so that `/lots` resolves to a stored file without the visitor seeing the file name.

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^lots/?$ /lots.html [L]
</IfModule>
```

The condition means "only if the requested name is not already a file", which prevents the rule from shadowing a later dynamic route with the same name. The rule is terminal because of the `L` flag, so no later rule is considered. This is static handling reached through a rewritten path: the response body still comes from a file, and the response will therefore carry `Last-Modified` and `ETag` headers.

Step 4. Delegate a dynamic path to a program running on a local port.

```apache
<VirtualHost *:80>
    ServerName karibu.example
    ProxyPreserveHost On
    ProxyPass "/beans" "http://127.0.0.1:9001/beans"
    ProxyPassReverse "/beans" "http://127.0.0.1:9001/beans"
</VirtualHost>
```

`ProxyPass` forwards matching requests to the upstream process and `ProxyPassReverse` rewrites redirect headers coming back so that the client is sent to the public address rather than the internal one. Apache is now acting as a reverse proxy, which is the standard way to combine a general-purpose web server with an application server.

Step 5. Rebuild the same site in Nginx, using a server block and a location that matches by prefix.

```nginx
server {
    listen 80;
    server_name karibu.example www.karibu.example;

    root /srv/karibu/public;
    index index.html;

    location / {
        try_files /index.html =404;
    }

    location /beans {
        proxy_pass http://127.0.0.1:9001;
        proxy_set_header Host karibu.example;
        proxy_set_header X-Forwarded-For 127.0.0.1;
    }

    location ~* \.(css|js|png|jpg|svg)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

Three Nginx behaviours are visible here. `try_files` is the idiomatic way to select a static file and fall back. `proxy_pass` inside a location implements the same delegation as Apache's `ProxyPass`. The regular-expression location matches by file extension and applies a seven-day freshness lifetime, which is the correct policy for content-hashed static assets and the wrong policy for HTML.

Step 6. Verify the static path with a headers-only request.

```bash
curl -I http://karibu.example/lots.html
```

```text
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:31:12 GMT
Server: Apache/2.4.58 (Unix)
Last-Modified: Thu, 06 Nov 2026 18:22:05 GMT
ETag: "1a4-62f0c1d9e7b40"
Accept-Ranges: bytes
Content-Length: 420
Content-Type: text/html
```

The presence of `Last-Modified`, a stable `ETag` and `Accept-Ranges` is conclusive evidence of static handling: the server can only report the modification time and byte ranges of a file that exists. The `Content-Length` matches the file size on disk.

Step 7. Verify that revalidation works, which is the mechanism that saves bandwidth.

```bash
curl -I -H 'If-None-Match: "1a4-62f0c1d9e7b40"' http://karibu.example/lots.html
```

```text
HTTP/1.1 304 Not Modified
Date: Fri, 07 Nov 2026 09:31:20 GMT
Server: Apache/2.4.58 (Unix)
ETag: "1a4-62f0c1d9e7b40"
```

The status changed to 304 and no body was sent, which is the correct behaviour when the client's stored validator still matches. The `Content-Length` header is absent because there is no body. This exchange is the concrete demonstration of why validators exist.

Step 8. Verify the dynamic path and compare the evidence.

```bash
curl -i http://karibu.example/beans
```

```text
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:31:35 GMT
Server: Apache/2.4.58 (Unix)
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 118
Cache-Control: no-store
Vary: Accept-Encoding

{"week":"2026-W45","lots":[{"name":"Nyeri Karindundu","process":"washed"},{"name":"Embu Gichathaini","process":"natural"}]}
```

Four differences from the static response are diagnostic. There is no `Last-Modified` and no `ETag`, because no stored representation exists to validate. The cache directive forbids storage, because the answer may change and is not public. The `X-Powered-By` header was added by the application, not the server, which shows that the response passed through a second program. And the body is data rather than markup, because the handler chose its own content type.

Step 9. Read the access log to see both transactions recorded in the same way.

```text
203.0.113.44 - - [07/Nov/2026:09:31:12 +0300] "HEAD /lots.html HTTP/1.1" 200 - "-" "curl/8.4.0"
203.0.113.44 - - [07/Nov/2026:09:31:20 +0300] "HEAD /lots.html HTTP/1.1" 304 - "-" "curl/8.4.0"
203.0.113.44 - - [07/Nov/2026:09:31:35 +0300] "GET /beans HTTP/1.1" 200 118 "-" "curl/8.4.0"
```

The log cannot tell you which responses were static and which were dynamic, because the log records the transaction, not the mechanism. This is an important limit: the log tells you what happened at the protocol level, and the headers tell you how the server produced it.

The conclusion follows directly from the last two exchanges. Static handling is file resolution plus metadata, evidenced by validators and a stable length. Dynamic handling is delegation plus computation, evidenced by absent validators, restrictive cache directives and application-added headers. A reverse proxy makes both appear on the same address, so the mechanism must be inferred from the response rather than from the address.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Testing an implementation

A deployment of this kind is tested at four levels. First, resolve the name and confirm it points at the intended address. Second, open a connection to the port and confirm the server answers at all. Third, request a known static file and confirm the status, type and validators. Fourth, request a known dynamic path and confirm that the response is produced by the intended handler, which is usually visible through an application-specific header or a distinctive body.

Each level isolates a class of fault. A name that resolves wrongly makes every later test meaningless. A closed port produces connection refusals that look like application errors. A missing static file produces 404 responses that are often mistaken for routing failures. A misrouted dynamic path produces 200 responses with the wrong content, which is the most dangerous failure of all because it looks like success.

### 5.2 Interpreting headers correctly

A 200 with the wrong `Content-Type` renders as text in the browser, because the browser follows the header rather than sniffing if the header is authoritative. A 304 with an unexpected body violates the protocol and usually indicates a proxy that is rewriting responses. A `Cache-Control: public` on a personalised response is a security defect, because a shared cache may then store one user's data and serve it to another. A `Vary` header that omits the header actually used to select the representation causes caches to serve the wrong variant. A response with neither `Content-Length` nor chunked encoding is malformed and will hang until the connection closes.

The general principle is that headers are the contract and the body is the payload. Reading the headers first explains most surprises.

### 5.3 Common errors

- **Saying that Edge uses EdgeHTML.** Current Edge is Chromium-based and therefore uses Blink with V8; EdgeHTML was retired in 2020.
- **Saying that Chrome on iOS uses Blink.** Every browser on iOS and iPadOS uses WebKit, because the platform permits no other engine.
- **Confusing the browser engine with the rendering engine.** The rendering engine lays out and paints; the browser engine coordinates navigation, history and loading.
- **Treating a URL as a file path.** The path is interpreted by the server, which may map it to a file, to a program, or to nothing at all.
- **Assuming that a static file is always faster than a dynamic page.** A cached dynamic page served from memory can beat a static file read from a slow disk.
- **Assuming that a dynamic page cannot be cached.** Dynamic responses can carry validators and freshness instructions; the handler decides.
- **Believing that a 301 and a 302 are interchangeable.** A permanent redirect may be cached indefinitely by clients and search engines; a temporary one should not be.
- **Believing that keeping the connection open is always better.** Under HTTP/1.1 a reused connection serialises requests unless the client opens several; multiplexing in later protocol versions removes that limit.
- **Confusing state with session.** The protocol is stateless; sessions are an application construct layered on top of it.
- **Assuming that a rewrite rule that works locally will work in production.** Rule order, module availability and the presence of an existing file all change the outcome.
- **Forgetting that `.htaccess` is read on every request.** Per-directory configuration is convenient and costs performance; production sites usually move the directives into the main configuration.
- **Reading a server log as proof of mechanism.** The log records the transaction; only the response headers reveal how the body was produced.

### 5.4 Limits and edge cases

Three edge cases deserve a sentence each because they are frequently examined. A response may be **partially** static: a page generated from a template and then cached to disk, which produces validators and looks static at the protocol level. A response may be **streamed**, in which case the length is unknown when the headers are written and chunked encoding is used. And a response may be **negotiated**, in which case the same address yields different representations depending on accept headers, language or encoding, and the `Vary` header is mandatory for correctness.

### 5.5 A diagnostic procedure

Start from the symptom and move one layer at a time. If nothing appears, test name resolution, then the port, then the protocol. If the wrong content appears, read the response headers and compare the content type, the validators and the cache directives against expectation. If the right content appears intermittently, suspect caching, a load-balanced pool with inconsistent state, or a rewritten path that matches only sometimes. If a page renders but behaves incorrectly, inspect the document source rather than the rendered result, because the difference between them is exactly the work done by client-side code.

Record what each test proved and what it did not. A headers-only request proves what the server claims about a resource; it does not prove that the browser will use it. A successful request from the command line proves the server works; it does not prove that the browser's security policy will allow it. Holding those distinctions is what separates a confident answer from a lucky one.
