## 1. Concept and Use Case

### 1.1 What the examiner is actually testing

Questions on the World Wide Web and client-server architecture are not asking whether you can define a term. They are asking four separable things, and the mark scheme rewards each of them differently.

First, whether you can **separate the Web from the Internet**. This is the most frequently examined distinction in the topic and the one most often answered carelessly.

Second, whether you can **describe a sequence in order**. The request-response cycle, the rendering pipeline and the evolution from the basic to the interactive model are all sequences, and sequences are marked by named stages rather than by impressionistic description.

Third, whether you can **compare two things on stated criteria**. Browser engines, server platforms, static and dynamic resources, client-side and server-side code: every one of these appears as a comparison question with a fixed number of marks, and every one rewards a criterion-by-criterion structure.

Fourth, whether you can **justify a choice**. Scenario questions give a requirement and expect a recommendation with a reason and a trade-off.

An answer that supplies definitions where a sequence was asked for, or a list where a comparison was asked for, loses marks even when every fact in it is true. The remedy is to recognise the shape of the question before writing.

### 1.2 The definition and the marks it carries

The standard definition is worth learning in a form that can be reproduced under pressure and then unpacked.

The World Wide Web is a system of interlinked documents and resources, identified by Uniform Resource Locators, delivered over the Internet using the Hypertext Transfer Protocol, and rendered by a browser from Hypertext Markup Language.

That sentence contains five markable elements: interlinked resources, unique addressing, the transfer protocol, the underlying network, and the presentation language. A four-mark question asking for a definition will normally credit three or four of them, and a student who writes only "a collection of web pages on the Internet" earns one mark at most.

The technical definition, that the Web is the set of resources and users communicating by HTTP, is worth a further mark when the question asks for a technical rather than a general definition. The broad definition from the World Wide Web Consortium, that the Web is the universe of network-accessible information and an embodiment of human knowledge, is worth a mark only when the question asks for the broad or social definition, and using it where a technical definition was requested can cost time without earning credit.

Three properties are always safe to add because they are always true: the Web is accessed through a browser, it is built on hypertext links, and it is one service among many that run over the Internet.

### 1.3 The evolution, as a sequence of mark-bearing changes

Evolution questions reward a change, a cause and a consequence for each stage. The following four stages cover almost every version of the question.

**Stage one, the basic model.** A client requested a document by identifier, a server returned it as markup, the exchange was stateless, and information flowed only from server to client. The model corresponds to the earliest protocol revision and the first markup version. Its limitation is the mark-earning point: there was no way to send data from the client to the server, no way to state acceptable formats, and no way to return anything except markup.

**Stage two, the interactive model.** The client gained the ability to post a body to the server where the server permits it, the body could be any format from seven-bit text to eight-bit binary, and the client could declare which formats it accepted. A consequence worth a mark is that the protocol became a general envelope able to wrap messages from other protocols, which is what makes a proxy server possible.

**Stage three, computed responses.** Servers gained the ability to run a program at request time, so a response could be built from a database rather than read from a file. The consequence is the virtual document: the same address can return different content for different users, and nothing on disk contains the finished page.

**Stage four, state and asynchrony.** Cookies and tokens allowed a stateless protocol to support sessions; asynchronous scripting allowed part of a page to update without a full reload; encryption became the default; and later protocol versions reduced the cost of many requests by reusing connections and multiplexing streams.

A strong answer names the limitation that each stage removed. A weak answer lists technologies without saying what problem each solved.

### 1.4 The distinction that keeps returning

The Internet is the global network of networks that uses the Internet Protocol for addressing and routing and TCP or UDP for transport. The Web is an application that runs over it, using HTTP, URLs and HTML. The Internet existed from 1969; the Web was proposed in 1989 and the first browser was written in 1990.

Three supporting facts earn marks when a question asks you to justify the distinction. Email, Domain Name System resolution, file transfer and secure remote login all work without the Web. The Web's protocols are layered above Internet transport, so an Internet failure stops the Web while a Web failure leaves the Internet intact. And the Web's naming scheme is imposed on Internet addressing rather than replacing it, since every request ultimately reaches an Internet Protocol address.

The counterpart distinction, between the Web and a browser, is worth one mark in a definition question: the Web is the information space and the protocols; the browser is a client program that requests and renders it.

### 1.5 The shapes of questions asked

Five stems recur, and each has a predictable structure.

**"Define X and explain how it differs from Y."** Divide the answer into a definition, the distinction, and evidence. Two or three marks for each part.

**"Describe the sequence of events when a URL is entered."** Marked by named stages in the correct order, usually six to eight marks.

**"Compare A and B."** Marked by paired criteria, not by unpaired descriptions. A table or a criterion-by-criterion paragraph is safest.

**"Explain how the server distinguishes static from dynamic resources, giving evidence."** Marked for the mechanism and for the evidence, with the evidence often carrying the higher marks because it separates a memorised answer from an understood one.

**"A company needs X. Recommend a server platform and justify your choice."** Marked for a recommendation, two or three justified criteria, and an acknowledged trade-off.

The command words matter. Define means state precisely. Describe means give the stages or features in order. Explain means give a reason for each statement. Compare means give similarities and differences on stated criteria. Justify means give evidence for a choice. Evaluate means give both sides and reach a judgement.

## 2. Data, Syntax, and Core Concepts

### 2.1 The high-yield fact table

The following facts carry marks in almost every paper, and the third column indicates the scale of question in which each typically appears.

| Fact | Detail worth writing | Typical marks |
|---|---|---|
| Definition of the Web | Interlinked resources, uniquely addressed, transferred by HTTP, rendered from HTML | 2 to 4 |
| Internet versus Web | Network versus application; Internet from 1969, Web proposed 1989 | 2 to 3 |
| Inventor and origin | Tim Berners-Lee, CERN, 1989 proposal, first browser written in 1990 | 1 to 2 |
| Three components of the basic model | Client, server, and the identifier plus protocol and markup that join them | 3 |
| Purpose of a URI | To specify a syntax for encoding names and addresses of resources and how they are accessed | 1 to 2 |
| URL, URN, URC | Locator by access mechanism, persistent name, citation metadata | 2 to 3 |
| HTTP characteristics | Stateless, request-response, text-based, headers plus optional body, runs over TCP | 3 to 4 |
| Default ports | HTTP 80, HTTPS 443, FTP 20 and 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143, IMAPS 993, POP3S 995 | 2 to 4 |
| Status classes | 1 informational, 2 success, 3 redirection, 4 client error, 5 server error | 2 to 3 |
| HTML lineage | Application of SGML, defined as a document type definition, extended to tables, images and forms | 1 to 2 |
| Interactive model additions | Client can post data; any body format; accept headers; other protocols encapsulated | 3 |
| Hypertext by whom | Hypertext named in the 1960s; the concept predates the Web by decades | 1 |
| Browser subsystems | User interface, browser engine, rendering engine, networking, script engine, UI backend, storage | 4 to 6 |
| Rendering engines | Chrome and Edge Blink, Firefox Gecko, Safari WebKit, Opera Blink | 2 to 4 |
| Static versus dynamic | Stored bytes versus computed at request time | 2 to 4 |
| Server products | Apache, IIS, Nginx, Sun Java System, with one distinguishing feature each | 4 |
| Client-side versus server-side | Visibility, trust, latency, capability | 2 to 4 |

### 2.2 Acronyms that must be expanded on first use

Marks are lost for using an abbreviation without expansion, and the loss is easy to avoid. World Wide Web (WWW). Hypertext Transfer Protocol (HTTP). Hypertext Transfer Protocol Secure (HTTPS). Hypertext Markup Language (HTML). Uniform Resource Identifier (URI), Uniform Resource Locator (URL), Uniform Resource Name (URN). Domain Name System (DNS). Internet Protocol (IP). Transmission Control Protocol (TCP). Transport Layer Security (TLS). Cascading Style Sheets (CSS). Document Object Model (DOM). Common Gateway Interface (CGI). Multipurpose Internet Mail Extensions (MIME). Internet Information Services (IIS). JavaScript is a name, not an acronym, and must not be expanded.

### 2.3 Engines and browsers: the table to memorise

The most reliable two marks in the topic are the engine pairings, and they are also the easiest to get wrong under pressure.

| Browser | Rendering engine | Script engine | Platform note |
|---|---|---|---|
| Google Chrome | Blink | V8 | Blink forked from WebKit in 2013 |
| Microsoft Edge | Blink | V8 | Chromium-based since 2020; previously EdgeHTML with Chakra |
| Mozilla Firefox | Gecko | SpiderMonkey | Independent engine, not derived from WebKit |
| Apple Safari | WebKit | JavaScriptCore | The only engine permitted on iOS and iPadOS |
| Opera | Blink | V8 | Used Presto until 2013 |

Two failure modes are so common that they should be rehearsed. Writing that Edge uses EdgeHTML describes a product that has not existed since 2020. Writing that Chrome on iOS uses Blink contradicts the platform rule that every iOS browser uses WebKit.

### 2.4 Hypertext, hypermedia and non-linear navigation

Hypertext is a data model in which documents are nodes and references are directed edges, so the structure is a graph rather than a sequence. Hypermedia applies the same model to nodes containing images, sound or video rather than only text. Both terms carry marks when defined with the graph idea, and neither is worth full marks when defined only as "text with links".

The consequences of the graph are examinable because they explain features of real sites that otherwise look arbitrary. Because a reader may enter at any node, every document must be intelligible without assuming a starting point, which is why pages repeat context in headings and summaries. Because there is no canonical order, orientation aids such as navigation bars, breadcrumbs and consistent layout are a response to the structure rather than decoration. Because any node may link to any other, the boundary of a document is not defined by the medium, which complicates questions of authorship and provenance. Because links decay, a 404 response is a normal outcome rather than an exceptional one.

Link types are worth one mark when named together. An internal link stays inside the site and can be validated at build time. An external link leaves it and cannot. A relative link resolves against the address of the current page and survives relocation of the site; an absolute link does not need to. A fragment link addresses a position inside a document and is resolved by the browser without being sent to the server. A mail link starts an electronic mail message rather than a retrieval.

Advantages of non-linear navigation are usually worth two marks: retrieval by association, the ability to follow a reference immediately, and multiple routes to the same material for readers with different backgrounds. Disadvantages are worth two more: disorientation, often described as being lost in hyperspace, the loss of a guaranteed narrative order, and the maintenance burden of link integrity.

### 2.5 Message anatomy

A request and a response have the same three-part shape: a start line, header fields, and an optional body after a blank line.

```http
GET /catalogue/books.html HTTP/1.1
Host: library.example
User-Agent: Mozilla/5.0 (X11; Linux x86_64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-GB,en
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 10:02:18 GMT
Server: Apache/2.4.58 (Debian)
Content-Type: text/html; charset=UTF-8
Content-Length: 512
Last-Modified: Wed, 05 Nov 2026 14:11:09 GMT
ETag: "200-62f1ab3c4d880"
Cache-Control: max-age=3600
```

Four header facts earn marks in their own right. `Host` is mandatory and enables name-based virtual hosting. `Content-Type` tells the browser how to interpret the body and takes precedence over any guessing. `Content-Length` delimits the body. `Last-Modified` and `ETag` are validators that allow a client to revalidate instead of re-downloading, which is what produces a 304 response with no body.

### 2.6 Ports and status codes

| Port | Service | Port | Service |
|---|---|---|---|
| 20 and 21 | File Transfer Protocol, data and control | 80 | HTTP |
| 22 | Secure Shell | 110 | Post Office Protocol version 3 |
| 23 | Telnet | 143 | Internet Message Access Protocol |
| 25 | Simple Mail Transfer Protocol | 443 | HTTPS |
| 53 | Domain Name System | 993 | IMAP over TLS |
| 67 and 68 | Dynamic Host Configuration Protocol | 995 | POP3 over TLS |

Status codes are examined as classes and as individual meanings. A 200 means success. A 201 means a resource was created. A 301 means a permanent move and may be cached indefinitely. A 302 means a temporary move. A 304 means the client's copy is still valid and no body follows. A 400 means the request was malformed. A 401 means authentication is required. A 403 means the server refuses. A 404 means no resource matches. A 405 means the method is not allowed for that resource. A 500 means the server failed while processing. A 502 means a proxy received an invalid response from upstream. A 503 means the service is unavailable.

### 2.7 Static and dynamic resources

A static resource is stored as it will be transmitted. The server resolves the path to a file, reads it and sends the bytes unchanged. A dynamic resource is produced at request time by a program that consults data outside the file system and builds the response.

The evidence that distinguishes them is more valuable in an examination than the definition, because it cannot be memorised without understanding.

| Evidence | Static | Dynamic |
|---|---|---|
| Last-Modified header | Usually present | Usually absent |
| Entity tag | Stable across requests | Absent or varies with inputs |
| Content-Length | Constant | May be absent if streamed |
| Cache-Control | Often public with a long lifetime | Often no-store or private |
| Body on repeat request | Identical | May differ |
| Extra headers | None | Application headers such as X-Powered-By, Set-Cookie |
| Response time pattern | Consistently short | Varies with the work performed |

A single sentence that earns full marks: a static response carries the modification time and byte range of a stored file, whereas a dynamic response carries no such validators because no stored representation exists.

### 2.8 Server platforms

| Platform | Licence and vendor | Operating systems | Distinguishing feature |
|---|---|---|---|
| Apache HTTP Server | Open source, Apache Software Foundation | Almost all, including Windows and Unix | Modular, per-directory `.htaccess`, widest ecosystem |
| Microsoft IIS | Bundled with Windows Server, Microsoft | Windows only | Tight operating system integration and graphical administration |
| Nginx | Open source, BSD-style | Unix-like systems and Windows | Event-driven, high concurrency, strong reverse proxy |
| Sun Java System Web Server | Free but closed source, Sun then Oracle | Windows, Linux, Unix | Java platform integration for medium and large sites |

Two extra facts often carry a mark. Apache historically served the largest share of web server machines. Nginx is commonly deployed in front of application servers rather than as the application host itself.

### 2.9 Client-side and server-side execution

| Criterion | Client-side | Server-side |
|---|---|---|
| Where the code runs | In the user's browser | On the web server |
| Visibility to the user | Fully visible and modifiable | Hidden from the user |
| Trust | None; can be bypassed | Authoritative |
| Access to data | Only what was sent to the browser | Databases, files and internal services |
| Latency | Immediate, no round trip | One round trip per interaction |
| Load placed on | The user's device | The server |
| Typical uses | Validation for convenience, interface behaviour, animation | Authentication, business rules, data access, page generation |
| Evidence in a page | Visible in the page source | Only the output appears in the source |

The examinable conclusion is that client-side code improves responsiveness and server-side code enforces correctness, so a secure system repeats its validation on the server.

### 2.10 How a web server handles a request

A web server has five responsibilities, and a four-mark question on server functionality is usually marked one per responsibility with the fifth as a bonus.

It **listens and accepts**: a socket is bound to an address and port, marked listening, and incoming connections are accepted. It **parses**: the request line gives the method and target, the headers give the Host and the client's preferences, and the body is read under a size limit. It **routes and authorises**: the path is normalised, long enough to prevent traversal outside the document root, then matched against virtual hosts, rewrite rules, static paths and dynamic handlers, with access control applied before anything is returned. It **resolves or delegates**: a static request ends at a file, a dynamic request ends at a program reached through an interface such as FastCGI or a reverse proxy. It **responds and records**: the status line and headers are written, the body may be compressed, and an entry is appended to the access log.

The connection model is worth a mark on its own. A process per connection isolates faults at the cost of memory. A bounded thread pool amortises creation costs but caps concurrency. An event-driven model multiplexes many connections in a few workers and therefore handles high concurrency efficiently, which is the design reason Nginx is placed in front of application servers.

Two further capabilities are commonly credited. Name-based virtual hosting serves several sites from one address by reading the Host header. Reverse proxying forwards a request to another program and relays the answer, which is how a fast static file server and TLS terminator is combined with an application server.

## 3. Methods and Operations

### 3.1 Method for a sequence question

Sequence questions are marked by stage names in the correct order. Write them as numbered steps, name the component responsible for each, and add one clause of purpose.

A reliable six-stage skeleton covers most versions. The address is parsed. The name is resolved to an address by DNS. A TCP connection is opened with a three-way handshake. For HTTPS, TLS negotiates encryption and validates the certificate. The request is sent with a method, a path, a Host header and accept headers. The server routes the request to a file or a program and returns a status, headers and a body. The browser parses the markup, requests subresources, and renders.

If the question specifies "when a page with images loads", add the subresource step explicitly and note that each resource is a separate request. If it specifies "when a form is submitted", change the method to POST, add the body, and note that the response may be a redirect.

### 3.2 Method for a browser architecture question

Divide the browser into its subsystems and give each one a function and a failure symptom. Six subsystems are usually enough for full marks: user interface, browser engine, rendering engine, networking, script engine and storage.

Then state the distinction that most answers miss. The browser engine coordinates navigation, history, loading and policy; the rendering engine converts markup and style into a laid-out and painted page. Naming Blink, Gecko or WebKit answers "which rendering engine", not "which browser engine", and a question that asks for both will not credit the same word twice.

Finish with the engine mapping and one sentence on why it matters: differing engines implement the same standards separately, so a page can render differently, and testing must therefore cover more than one engine.

### 3.3 Method for a comparison question

Choose three or four criteria before writing and apply them to both items in the same order. For servers, the productive criteria are licence and cost, platform support, connection model and concurrency, configuration style, and dynamic-content integration. For static versus dynamic, the productive criteria are storage, generation, caching, validators, and cost per request. For client-side versus server-side, they are location, trust, latency, data access and load.

Never write one paragraph about the first item and one about the second. Marks are awarded for paired statements, and paired statements also make the trade-off obvious, which is usually worth a final mark.

### 3.4 Method for an evidence question

Evidence questions ask how you would tell two things apart, and they reward tool output. State the tool, state what it reveals, and state what would differ between the two cases.

For static versus dynamic the strongest single piece of evidence is a headers-only request, because the presence of a modification time and an entity tag proves that a stored file exists. The second strongest is two requests separated in time, where an unchanged file yields identical bytes and a generated page may not. The third is the server configuration, where a rewrite to a file and a proxy to an application are visibly different constructs.

### 3.5 Configuration evidence you can quote

An Apache virtual host establishes name-based hosting and a document root.

```apache
<VirtualHost *:80>
    ServerName library.example
    DocumentRoot "/srv/library/public"
    ErrorLog "/var/log/apache2/library-error.log"
    CustomLog "/var/log/apache2/library-access.log" combined
</VirtualHost>
```

A per-directory rule shows a static rewrite, with the condition preventing the rule from shadowing an existing file.

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^catalogue/?$ /catalogue.html [L]
</IfModule>
```

An Nginx server block shows the same intent in a different configuration language, with a static location and a proxied dynamic location.

```nginx
server {
    listen 80;
    server_name library.example;
    root /srv/library/public;
    index index.html;

    location / {
        try_files /index.html =404;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:9000/;
        proxy_set_header Host library.example;
    }

    location ~* \.(css|js|png|jpg)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

Being able to write one of these from memory converts a vague answer about "configuration files" into a specific one, and specific answers read as understanding.

## 4. Worked Implementation from the Notes

### 4.1 Task: a ten-mark answer describing what happens when a user enters an address

### 4.2 Implementation: a numbered answer with the marking points identified

Question: describe the sequence of events that occurs when a user types an address into a browser and presses enter, ending with the page displayed on screen. Ten marks.

Step 1. The browser parses the address into scheme, host, port, path and fragment. **Marking point:** correct identification of the components, one mark, available for naming the scheme and host at minimum.

Step 2. The browser checks its own cache for a fresh copy of the resource. **Marking point:** one mark for stating that a valid cached copy avoids all network activity.

Step 3. The host name is resolved to an Internet Protocol address using the Domain Name System. **Marking point:** one mark for naming DNS and stating its function; the resolver chain from browser cache to operating system to recursive resolver to authoritative server should still be described, because it demonstrates depth.

Step 4. A Transmission Control Protocol connection is established using a three-way handshake. **Marking point:** one mark for the handshake and for naming the correct port, 80 for HTTP or 443 for HTTPS.

Step 5. For HTTPS, a Transport Layer Security handshake negotiates encryption and the server presents a certificate that the browser validates against the requested host name. **Marking point:** one mark for encryption negotiation and certificate validation.

Step 6. The browser sends an HTTP request containing a method such as GET, the path, a mandatory Host header, and headers declaring acceptable formats. **Marking point:** one mark for the request line and for explaining the Host header's role in virtual hosting.

Step 7. The server selects a virtual host from the Host header, maps the path to a file or a program, and builds a response with a status code, headers and a body. **Marking point:** one mark for routing to a static file or a dynamic handler.

Step 8. The browser receives the response, parses the markup into a document tree, requests each additional resource such as a style sheet or an image, computes layout, and paints the page. **Marking point:** one mark for stating that each subresource is a separate request, and one for the render pipeline from parse to paint.

Step 9. The connection may be kept alive for reuse, the response may be cached according to its headers, and the browser updates its history. **Marking point:** one mark available for connection reuse or for cache behaviour.

Nine steps carry ten marks; the rendering step is worth two because it covers two distinct events. The pattern to notice is that the marks are distributed across stages, so a candidate who writes a long paragraph about DNS and nothing about rendering can score at most three.

### 4.3 Task: an eight-mark answer on browser architecture and engine comparison

### 4.4 Implementation: a structured answer with the marking points identified

Question: describe the main components of a web browser and explain why the same page may appear differently in different browsers. Eight marks.

Step 1. Name the user interface and state its function: address bar, navigation controls, tabs and settings, everything except the page content itself. **Marking point:** one mark.

Step 2. Name the browser engine and state its function: it coordinates navigation, manages history and loading, and passes content to the rendering engine. **Marking point:** one mark, and this is the component most often omitted.

Step 3. Name the rendering engine and state its function: it parses markup and style, computes layout, paints and composites. **Marking point:** one mark.

Step 4. Name the networking and scripting subsystems: HTTP and TLS handling, and the JavaScript engine. **Marking point:** one mark for both, provided their functions are distinguished.

Step 5. Name local storage and state at least two of its forms, such as the HTTP cache, cookies, local storage or an indexed database. **Marking point:** one mark.

Step 6. Give the engine mapping: Chrome and Edge use Blink, Firefox uses Gecko, Safari uses WebKit, Opera uses Blink. **Marking point:** two marks for four correct pairings; one mark for two or three.

Step 7. Explain the divergence: each engine implements the standards independently, with separate bug histories and separate release schedules, so a feature may be interpreted differently, and platform restrictions such as the WebKit requirement on iOS add a further difference. **Marking point:** one mark for the explanation, and this is the mark that distinguishes a described architecture from an understood one.

Step 8. Add the practical consequence: sites must be tested across engines, commonly by testing one Blink browser, Gecko and WebKit. This carries no separate mark but strengthens the explanation and protects the final mark.

### 4.5 Task: a ten-mark answer distinguishing static from dynamic handling and recommending a platform

### 4.6 Implementation: a two-part answer with the marking points identified

Question: a college hosts a prospectus that changes twice a year and an application portal that shows each applicant their own status. Explain how the web server distinguishes static from dynamic resources, giving evidence, and recommend a server platform. Ten marks.

Step 1. Define the two cases precisely. Static content is stored and transmitted unchanged; dynamic content is generated at request time by a program that consults data outside the file system. **Marking point:** two marks, one for each definition.

Step 2. Describe the static mechanism. The server maps the path into the document root, checks permissions, determines the type from the extension, and streams the file with validators. **Marking point:** one mark for path mapping and one for validators.

Step 3. Describe the dynamic mechanism. The server routes the request to a handler through an interface such as FastCGI or a reverse proxy, the handler consults a database and renders a response, and the server relays it. **Marking point:** one mark for delegation, one for the handler setting its own headers.

Step 4. Give the evidence. A static response carries Last-Modified and a stable ETag and may be cached publicly; a dynamic response usually carries neither, sets Cache-Control to no-store or private, and may add application headers or a cookie. **Marking point:** two marks for evidence, which is where most candidates lose marks by asserting the difference without demonstrating it.

Step 5. Apply the distinction to the scenario. The prospectus is static and should be cached with a long lifetime and revalidated by validator, because it changes twice a year. The portal is dynamic and must not be stored by shared caches, because the content is specific to one applicant. **Marking point:** one mark for applying the distinction correctly to both resources.

Step 6. Recommend a platform with justified criteria. Nginx as the front end for static files, TLS termination and caching, with the portal served by a separate application process reverse-proxied behind it. **Marking point:** one mark for the recommendation with a justified criterion, and a statement of the trade-off, such as managing two processes or losing per-directory configuration, strengthens the answer.

The answer scores full marks because it contains two definitions, two mechanisms, evidence, an application and a justified recommendation. A candidate who writes only definitions and a recommendation would score three.

### 4.7 A sixth-mark answer pattern for client-side versus server-side

Question: explain why a registration form should be validated in both the browser and the server. Six marks.

Step 1. State that browser validation runs immediately and gives feedback without a round trip, which improves the experience. **Marking point:** one mark.

Step 2. State that browser code is delivered to the user and can be read, modified or bypassed entirely by sending a crafted request. **Marking point:** two marks, one for visibility and one for bypass.

Step 3. State that server validation runs on infrastructure the user does not control and is therefore authoritative. **Marking point:** one mark.

Step 4. State that server validation protects the data store and any business rule, such as uniqueness of a username or a minimum age. **Marking point:** one mark.

Step 5. Conclude that the two are complementary rather than alternatives: the browser copy is for speed, the server copy is for correctness, and the server must never assume the browser check ran. **Marking point:** one mark.

## 5. Testing, Interpretation, and Common Errors

### 5.1 The trap table

Every entry here is a statement that sounds right and scores zero. Reading the table before an examination is more efficient than rereading notes, because these are the errors that survive ordinary revision.

| Trap | Why it is wrong | Correct statement |
|---|---|---|
| The Web and the Internet are the same | The Web is one application among many on the Internet | The Internet is the transport network; the Web is a service that uses it |
| Edge uses EdgeHTML | Edge moved to Chromium in 2020 | Current Edge uses Blink with V8 |
| Chrome on iPhone uses Blink | Apple permits only WebKit on iOS and iPadOS | Every iOS browser renders with WebKit |
| Browser engine means rendering engine | They are different layers with different duties | The browser engine coordinates; the rendering engine lays out and paints |
| Opera uses Presto | Presto was abandoned in 2013 | Opera uses Blink |
| A URL is a file path | The server interprets the path and may map it to a program | A path is a request target, not necessarily a file |
| HTTP keeps you logged in | HTTP is stateless | Sessions are created by cookies or tokens sent with each request |
| The fragment is sent to the server | The browser strips it before sending | Fragments are resolved locally after the document arrives |
| HTTPS hides the host name | The host appears in connection setup and in the certificate | HTTPS protects path and body, not the identity of the server contacted |
| Static is always faster | A cached dynamic page can be served from memory | Static is simpler to cache; speed depends on the path taken |
| Dynamic cannot be cached | Handlers can set validators and freshness | Dynamic responses may be cached privately or revalidated |
| A 301 and a 302 are equivalent | One is permanent and cacheable, the other temporary | Choose 301 only when the move is permanent |
| A 404 means the server is down | A 404 is a successful exchange with a negative verdict | A 404 means no resource matched the path |
| A 500 is the client's fault | The 5 class denotes server-side failure | The server failed while processing a valid request |
| `Host` is optional | It is mandatory in the current protocol version | `Host` selects the virtual host |
| `.htaccess` is free | It is read on every request in the directory tree | Production sites move directives into the main configuration |
| Client-side validation is security | The user controls the browser | Server-side validation is the control |
| Apache is the fastest under high concurrency | Its strength is flexibility, not event-driven concurrency | Nginx's event-driven model scales better with many connections |
| A rewrite rule always wins | Rule order and file-existence conditions change the outcome | State order and conditions explicitly |
| The page is one file | A page is assembled from many requests | Count resources, not pages, when reasoning about latency |

### 5.2 The revision checklist

Work through this list and mark each item only when you can produce the answer from memory in under two minutes.

- The four-part definition of the Web, and the technical definition, and the World Wide Web Consortium definition.
- Three services that use the Internet without the Web.
- The five elements of the basic model and the three additions of the interactive model, each with the limitation it removed.
- The full anatomy of a URL, including which parts reach the server.
- The difference between a URI, a URL and a URN.
- Four properties of HTTP: stateless, request-response, text-based, layered on TCP.
- The complete request-response cycle in eight or nine ordered stages.
- The seven browser subsystems and one function for each.
- The browser engine versus rendering engine distinction, stated in one sentence.
- The engine mapping for Chrome, Firefox, Safari, Edge and Opera, plus the iOS rule.
- Five forms of browser storage and which of them are transmitted to the server.
- Apache, IIS, Nginx and Sun Java System, each with licence, platform and one distinguishing feature.
- Static versus dynamic handling, with four pieces of distinguishing evidence.
- Client-side versus server-side code, compared on five criteria.
- The default ports for HTTP, HTTPS, FTP, SSH, Telnet, SMTP, DNS, POP3 and IMAP.
- The five status classes and the meanings of 200, 301, 304, 403, 404 and 500.
- One configuration snippet for a virtual host and one for a proxied dynamic path.

Anything you cannot produce from memory should be written out by hand once, because writing forces the sequence into order in a way that reading does not.

### 5.3 Time strategy for the examination

Allocate by marks, not by question order. A ten-mark question deserves roughly twelve minutes in a ninety-minute paper, and a four-mark definition deserves five. If the paper offers a choice, choose the question whose parts you can answer completely rather than the one with the most attractive first part.

Spend the first ninety seconds of a long answer planning the stages as a numbered list in the margin. The list becomes the skeleton, prevents repetition, and guarantees that the sequence is in order before prose obscures it.

Write the definition first, in one sentence, even when the question does not explicitly ask for one. It anchors the answer and it is almost always worth a mark.

Where a question asks for a comparison, draw the criteria as a table before writing prose. If time runs short, the table still earns paired marks.

Where a question asks for evidence, name the tool and the header. "A headers-only request shows Last-Modified and a stable entity tag, which is only possible for a stored file" is worth more than a paragraph of description.

Leave two minutes at the end to check three things: that every acronym is expanded on first use, that no answer describes a product as it existed before a change you know about, and that no question has been answered twice while another is blank.

### 5.4 Interpreting your own practice answers

After a practice question, mark your answer against the marking points rather than against a model answer. Three questions expose most weaknesses. Did I give a mechanism or only a definition? Did I pair every comparison statement, or did I describe the two items separately? Did I supply evidence, or did I assert the conclusion?

An answer that scores six out of ten usually has all the content and none of the structure. The remedy is not more facts but a skeleton: numbered stages for sequences, paired criteria for comparisons, a mechanism plus evidence for explanations, and a recommendation plus trade-off for scenarios.

### 5.5 The last five minutes

Read the question again and check that the answer matches its command word. Define, describe, explain, compare and justify are not interchangeable, and a well-written answer to the wrong command word loses marks quietly. Then check the engine table, because it is the single most commonly reversed fact in the topic, and confirm that you have not written that Edge uses EdgeHTML or that Chrome on iOS uses Blink. Those two errors appear in more scripts than any others, and both are avoidable with one deliberate check.