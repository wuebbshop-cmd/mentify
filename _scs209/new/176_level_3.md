## 1. Concept and Use Case

### 1.1 What this topic is examined on

Questions on this topic are set to find out whether a candidate can do four things: name the parts of a web address and say what each part does; describe the exchange between client and server precisely enough that a programmer could implement it; classify a request by what it is allowed to change; and explain how a protected connection is established and how identity survives a protocol that remembers nothing. Every past-paper variant is a rearrangement of those four demands.

The marks are distributed unevenly. Definitions are cheap and are almost always worth one or two marks each, so they must be given quickly and exactly. Explanations of mechanism carry the middle marks and reward sequence words such as first, then, and only after. Comparisons and justifications carry the highest marks per sentence, because they require a judgement rather than a recollection. A candidate who writes four correct definitions and one well-argued comparison will usually beat one who writes eight definitions and no argument.

### 1.2 The anchor statements worth memorising

These sentences are short enough to learn and precise enough to earn full marks. Each is written so that a marker can tick a specific point.

- A Uniform Resource Identifier is a string that identifies a resource; a Uniform Resource Locator is a URI that identifies a resource by the mechanism for obtaining it.
- The Hypertext Transfer Protocol is an application-layer, stateless, request-response protocol in which the client sends a request message and the server returns a response message.
- HTTP is stateless because the protocol requires each request to be interpretable without reference to any earlier request; the server retains no session context as part of the protocol.
- A method is safe if it does not change the state of the server, and idempotent if repeating it has the same effect as performing it once.
- HTTPS is HTTP carried over a Transport Layer Security channel, which provides confidentiality, integrity, and authentication of the server.
- TLS uses asymmetric cryptography to authenticate the server and to agree a shared secret, and symmetric cryptography to protect the bulk of the data.
- A cookie is a small name-value pair that a server asks a client to store and return on later requests, allowing state to be reconstructed despite a stateless protocol.

### 1.3 The six question patterns

Almost every question in this topic matches one of six patterns, and each has a predictable shape of answer.

**Pattern one: define and distinguish.** "Define URI and URL and state the relationship between them." Two marks for the definitions, one for the containment relationship, one for a correct example. Answers fail when they define a URL and then claim a URI is the same thing.

**Pattern two: identify components.** "Given the address below, identify the scheme, host, port, path, query, and fragment." One mark per component, and a common loss is claiming the fragment is sent to the server.

**Pattern three: describe a process.** "Describe the sequence of events when a browser requests a page over HTTPS." This is marked as a sequence: name lookup, connection, key agreement, certificate validation, request, response, rendering. Marks are awarded for order as well as for content.

**Pattern four: classify and justify.** "State whether each method is safe and idempotent, and explain why the distinction matters." The marks are in the justification: retries, caching, prefetching.

**Pattern five: diagnose.** "A client receives a 403 when it expects a 200. Explain two possible causes and the evidence that would distinguish them." Marks reward a specific check per cause.

**Pattern six: evaluate.** "Discuss the claim that HTTPS makes a web application secure." The highest marks go to the limits: HTTPS protects the channel, not the application; it does not prevent injection, authorisation errors, or a dishonest site.

### 1.4 Where the marks actually sit

| Demand | Typical wording | Marks | Cost per mark |
|---|---|---|---|
| Recall a definition | State, define, name | 1 to 2 | Very low |
| Recall a list | List four components, name three headers | 3 to 4 | Low |
| Describe a sequence | Describe the request-response cycle | 4 to 6 | Medium |
| Classify with reason | State and justify safety and idempotence | 4 to 6 | Medium |
| Compare | Compare GET and POST, or HTTP and HTTPS | 6 to 8 | High |
| Diagnose | Explain the cause of a status code | 4 to 6 | High |
| Evaluate | Discuss, assess, to what extent | 8 to 12 | Highest |

The practical consequence for revision is that definitions should be learned to the point of automaticity, so that the cheap marks are collected in the first minutes of an answer and the remaining time is spent on the expensive ones. An answer that spends ten minutes perfecting a two-mark definition has already lost the question.

### 1.5 The single most useful framing

If a question is unfamiliar, reduce it to the four commitments: a name, a message, a method, and a channel. Every question in this topic can be answered by saying which of those four is in play and what the protocol requires of it. A question about caching is a question about the message and its headers. A question about login is a question about the channel plus client-side state. A question about a redirect is a question about the message and the name.

## 2. Data, Syntax, and Core Concepts

### 2.1 Naming: facts that earn marks

A URI has the general form of a scheme, a colon, a hierarchical part, an optional query introduced by a question mark, and an optional fragment introduced by a hash mark. (2 marks for the form, 1 for naming the optional parts.)

A URL is a URI whose scheme implies a mechanism for retrieval, and its practical form is scheme, two slashes, authority, path, optional query, optional fragment. (2 marks.)

A URN is a URI that names a resource persistently without stating where it is held; `urn:isbn:9780132350884` is the standard example. (1 mark for the definition, 1 for the example.)

Default ports are 80 for HTTP and 443 for HTTPS. This is worth one mark whenever a question shows an address without a port and asks where the request goes. (1 mark.)

The fragment is not sent to the server. It is resolved by the client after the response arrives. (1 mark, and a very common trap.)

Component meanings, expressed so that each phrase earns a tick:

| Component | Definition worth a mark | Example |
|---|---|---|
| Scheme | Identifies the protocol to be used | `https` |
| Authority | Identifies the host and optionally the port and user information | `shop.example.com:8443` |
| Host | The domain name or address literal of the server | `shop.example.com` |
| Port | The numbered service endpoint on the host | `8443` |
| Path | The hierarchical name of the resource | `/catalog/items` |
| Query | Parameters supplied to the resource | `category=books&page=2` |
| Fragment | A secondary reference within the resource, handled by the client | `reviews` |

### 2.2 Message format: the marks are in the order

A request has three parts in a fixed order: a request line, a header section, and an optional body. (1 mark for the three parts, 1 for the order.)

The request line is the method, a space, the request target, a space, the protocol version. (2 marks; a candidate who omits the version loses one.)

The response line is the version, a space, the three-digit status code, a space, a reason phrase. (2 marks.)

Headers are one per line as a name, a colon, and a value, and an empty line separates the header section from the body. (2 marks; the empty line is often the mark that decides a pass.)

The body is delimited by Content-Length, by chunked transfer coding, or by closing the connection. (3 marks, one each.)

A complete pair worth being able to reproduce from memory, with every element in its marked position:

```http
GET /catalog/items HTTP/1.1
Host: shop.example.com
Accept: text/html
```

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 18432
```

The first block is a request: method, target, and version on one line, then headers. The second is a response: version, code, and reason phrase on one line, then headers describing the body. Neither block shows the empty line or the body, which is exactly the omission that loses marks when a candidate reproduces only these lines.

| Fact | Marks | Why it is asked |
|---|---|---|
| Request line order | 2 | Tests whether the candidate has seen a real message |
| Status line order | 2 | Same, and tests status-code position |
| Empty line terminator | 1 to 2 | Distinguishes memorised prose from understanding |
| Host is mandatory in HTTP/1.1 | 1 | Explains virtual hosting |
| Content-Length or chunked or close | 3 | Tests framing and security awareness |

### 2.3 Methods: the highest-frequency table in the topic

| Method | Purpose | Safe | Idempotent | Success code |
|---|---|---|---|---|
| GET | Retrieve a representation | Yes | Yes | 200 |
| HEAD | Retrieve headers only | Yes | Yes | 200 |
| POST | Submit data for processing | No | No | 201 |
| PUT | Replace the resource at a known address | No | Yes | 200 or 204 |
| DELETE | Remove the resource | No | Yes | 204 |
| OPTIONS | Discover supported methods | Yes | Yes | 200 or 204 |
| TRACE | Echo the request for diagnosis | Yes | Yes | 200 |

Three sentences convert this table into marks. Safety is about changing state, so `GET`, `HEAD`, `OPTIONS`, and `TRACE` are safe while `PUT` and `DELETE` change state and are therefore not safe. Idempotence is about repetition, so `PUT` and `DELETE` are idempotent because repeating them reaches the same end state. `POST` is the only method in the list that is neither safe nor idempotent, which is why a browser warns before resubmitting a form. (1 mark per classification, 1 to 2 for the reason.)

### 2.4 Status codes: thirteen codes carry most of the marks

| Code | Reason phrase | Meaning worth a mark |
|---|---|---|
| 200 | OK | The request succeeded and the body is the representation |
| 201 | Created | A new resource exists and Location names it |
| 204 | No Content | Success with no body to return |
| 301 | Moved Permanently | The resource has a new permanent address |
| 302 | Found | Temporary redirect; the method may be changed to GET |
| 304 | Not Modified | The client's cached copy is still valid; no body |
| 400 | Bad Request | The request is malformed or invalid |
| 401 | Unauthorized | Authentication is required or has failed |
| 403 | Forbidden | Authenticated but not permitted |
| 404 | Not Found | No resource exists at that address |
| 405 | Method Not Allowed | The resource exists but not for that method |
| 500 | Internal Server Error | An unexpected failure inside the application |
| 502 | Bad Gateway | An upstream server returned an invalid response |
| 503 | Service Unavailable | Temporarily unable to handle the request |

The five classes are worth one mark each when asked, and the definitions must be phrased as protocol meanings rather than as moods: 1xx informational, 2xx success, 3xx redirection requiring further action, 4xx client error, 5xx server error.

Two mandatory companions are examined repeatedly. A 401 must carry a WWW-Authenticate header naming the scheme, and a 405 must carry an Allow header listing the permitted methods. (1 mark each.)

### 2.5 Headers: seven that are named in the syllabus

| Header | Direction | Question it answers | Mark-bearing detail |
|---|---|---|---|
| Host | Request | Which site is wanted | Mandatory in HTTP/1.1; enables virtual hosting |
| User-Agent | Request | Which client is asking | Identifies browser and version; forgeable |
| Accept | Request | Which media types are acceptable | Comma list, optional q-values |
| Content-Type | Both | What the body contains | Media type plus optional charset |
| Authorization | Request | Who the client is | Scheme name plus credentials, for example Basic or Bearer |
| Cache-Control | Both | Who may store and for how long | no-store, no-cache, max-age, private, public |
| Set-Cookie | Response | State to remember | Attributes govern scope and protection |

A single sentence per header is enough for one mark, provided the sentence states the function rather than restating the name. "Content-Type tells the receiver the media type of the body, such as text/html with a charset parameter" earns the mark; "Content-Type is the type of the content" does not.

### 2.6 HTTPS: the marks are in the sequence and the split

The four facts that appear in nearly every marking scheme are these.

HTTPS is HTTP carried over TLS on port 443 by default. (1 mark.)

TLS provides confidentiality, integrity, and authentication of the server. (3 marks, one each.)

Asymmetric cryptography is used during the handshake to authenticate the server and to agree a session key; symmetric cryptography then protects the application data because it is far faster. (3 marks: one for asymmetric use, one for symmetric use, one for the performance reason.)

The server proves its identity with a certificate issued by a certificate authority and validated by the client against a trusted root. (3 marks: certificate, authority, chain.)

The handshake sequence, in the order a marker expects for TLS 1.2:

1. Client sends ClientHello with supported versions, a random value, cipher suites, and the server name.
2. Server responds with ServerHello, its random value, the chosen cipher suite, and its certificate chain.
3. Server sends its ephemeral key share and a signature proving possession of the certificate's private key.
4. Client sends its own key share; both derive the same shared secret.
5. Both send Finished messages proving the keys agree.
6. Application data follows under the negotiated symmetric cipher.

For TLS 1.3 the marker accepts a shorter sequence: ClientHello with key share, ServerHello with key share, encrypted certificate and signature, Finished, then data. The name of the version matters less than the presence of the four logical stages: hello, key agreement, authentication, finished.

### 2.7 Cookies: attributes and the attack each blocks

| Attribute | Effect | Attack or problem addressed |
|---|---|---|
| Domain | Extends the cookie to subdomains of the stated domain | Prevents one site writing cookies for another |
| Path | Restricts the cookie to a path prefix | Reduces exposure to unrelated endpoints |
| Expires or Max-Age | Sets lifetime; Max-Age wins if both are present | Bounds the window in which a stolen value works |
| Secure | Sends only over HTTPS | Stops the value being read on a plain connection |
| HttpOnly | Hides the cookie from page scripts | Reduces session theft through cross-site scripting |
| SameSite | Restricts cross-site sending; Strict, Lax, or None | Reduces cross-site request forgery |

Three sentences earn marks. Without Domain the cookie is host-only, which is the safer default. SameSite equal to None must be accompanied by Secure. A cookie with no Expires and no Max-Age is a session cookie that the browser discards when the session ends.

### 2.8 Persistence and version facts

HTTP/1.0 closed the connection after each response unless the client requested keep-alive; HTTP/1.1 keeps it open by default and closes when either side sends `Connection: close`. (2 marks.)

Persistence removes a transport handshake and a key agreement per resource, which matters most on high-latency links. (2 marks.)

HTTP/2 multiplexes several requests over one connection and compresses headers, removing application-level head-of-line blocking. HTTP/3 runs over a datagram-based transport so that loss on one stream does not stall others. (1 mark each if asked.)

### 2.9 The trap table

| Statement a candidate may write | Verdict | Correct position |
|---|---|---|
| HTTPS is a separate protocol unrelated to HTTP | Wrong | HTTPS is HTTP carried inside a TLS channel |
| A URL and a URI are identical | Wrong | A URL is one kind of URI; a URN is another |
| The fragment is sent to the server | Wrong | The client strips it before sending |
| Default port for HTTPS is 8080 | Wrong | 443 for HTTPS, 80 for HTTP |
| GET changes data because it can submit a form | Wrong | A GET may carry a query but must not change state |
| PUT is safe because it is idempotent | Wrong | PUT changes state, so it is not safe; it is idempotent |
| POST is idempotent because the same data is sent | Wrong | A repeat may create a second resource |
| DELETE is not idempotent because the second call returns 404 | Wrong | Idempotence concerns the resulting state, not the code |
| 401 means the user is logged in but not allowed | Wrong | That is 403; 401 means authentication is missing or failed |
| 404 means the server is down | Wrong | The server answered; the resource is absent |
| 304 means an error | Wrong | It means the cached copy is still valid |
| 301 and 302 differ only in wording | Wrong | 301 is permanent; 302 is temporary |
| 302 preserves the original method | Wrong | 307 and 308 preserve it; 301 and 302 may not |
| Cookies are programs stored on the client | Wrong | A cookie is a name-value string with attributes |
| HttpOnly encrypts the cookie | Wrong | It prevents script access; Secure restricts it to HTTPS |
| TLS encrypts the whole session with RSA | Wrong | RSA or another asymmetric method is used only in the handshake |
| The certificate contains the session key | Wrong | It binds a name to a public key; session keys are derived |
| A padlock proves the site is trustworthy | Wrong | It proves channel protection and name validation only |
| HTTP is stateful because logins persist | Wrong | Sessions are reconstructed from cookies on each request |
| Content-Length and Transfer-Encoding may both be trusted | Wrong | The combination is ambiguous and must be rejected |

## 3. Methods and Operations

### 3.1 How to open any answer in this topic

1. Give the definition in one sentence, using the expanded acronym the first time.
2. Give the smallest concrete example, ideally an address or a message line.
3. Name the mechanism that makes it work.
4. State the consequence or the trade-off.

Four sentences, four marks in most schemes, and the rest of the answer then has a spine to hang on. Candidates who begin with a story about the internet lose the first mark and usually the second.

### 3.2 Structuring a describe-the-cycle answer

1. The client parses the address into scheme, host, port, path, query, and fragment.
2. The client resolves the host through the domain name system, using a cached answer if one is valid.
3. The client opens a transport connection to the host and port.
4. For HTTPS the client performs the TLS handshake before any request is sent.
5. The client sends a request message consisting of a request line, headers, an empty line, and an optional body.
6. The server interprets the method and target, performs the action, and returns a response message consisting of a status line, headers, an empty line, and an optional body.
7. The client acts on the status code: it renders a body, follows a redirect, retries, or reports an error.
8. The connection may be reused for further requests, or closed.

Each numbered line is a mark in a six-mark question, which is why the sequence must not be compressed into "the browser sends a request and gets a response".

### 3.3 Structuring a methods answer

1. State the method's purpose in one clause.
2. State whether it is safe, with the reason: whether it changes server state.
3. State whether it is idempotent, with the reason: whether repetition changes the outcome.
4. State the success status code and, where relevant, the mandatory header.
5. Give one operational consequence: caching, retry, prefetch, or form resubmission.

A five-line treatment per method covers a comparison question comfortably. For a ten-mark question comparing four methods, twenty lines is the right length, and the marks are concentrated in steps two, three, and five.

### 3.4 Structuring a status-code answer

1. Name the family and its meaning first, because the family is worth a mark on its own.
2. Name the specific code and its precise meaning.
3. Say whose fault it is and what the recipient should do next.
4. Name any mandatory companion header.
5. Distinguish it from the neighbour it is most often confused with.

Step five is where strong candidates separate themselves. A 401 answer that contrasts itself with 403, or a 502 answer that contrasts itself with 504, reads as understanding rather than recall.

### 3.5 Structuring an HTTPS answer

1. State that HTTPS is HTTP over TLS, with 443 as the default port.
2. List the three properties: confidentiality, integrity, server authentication.
3. Describe the handshake in order, naming the hello exchange, the key agreement, the certificate and signature, and the finished messages.
4. State the split between asymmetric and symmetric use, and justify it on cost.
5. Describe certificate validation as a chain from the leaf through intermediates to a trusted root, including name and date checks.
6. State at least one limitation, for example that HTTPS protects the channel and not the application.

Step six is the mark that distinguishes an evaluation from a description, and it is the one most often omitted.

### 3.6 Structuring a cookie answer

1. Define a cookie as a name-value pair with attributes, set by a Set-Cookie response header and returned in a Cookie request header.
2. Explain why it exists: the protocol is stateless, so identity must be carried by the client.
3. Name the scope attributes, Domain and Path.
4. Name the protection attributes, Secure, HttpOnly, and SameSite, and give the attack each addresses.
5. Name the lifetime attributes, Expires and Max-Age, and the difference between a session cookie and a persistent one.
6. State one limitation, for example that a cookie is sent with every matching request and is therefore a privacy exposure, or that deleting the client copy does not end the session unless the server invalidates it.

### 3.7 Quoting evidence in an answer

A short verified observation strengthens a description and is worth a mark where the question says "illustrate" or "with reference to an example". Three are enough for the whole topic.

A header-only request shows the status line and the response headers without a body, which is the cheapest way to demonstrate that the status line precedes everything else. A verbose request shows the connection being reused and the negotiated cipher, which demonstrates persistence and TLS in one output. A chain printout shows the leaf, the intermediate, and the root, which demonstrates the trust hierarchy concretely.

### 3.8 Managing the arithmetic of round trips

Questions sometimes ask how many round trips a sequence costs. The safe general statements, in words rather than notation, are these: a transport handshake costs one round trip before data can flow; a TLS 1.3 handshake costs one round trip, and a TLS 1.2 full handshake costs two; a resumed TLS 1.3 session can send data in the first flight, which is why it is described as zero round trip for the resumption case. A persistent connection amortises those costs over every subsequent request on it. Stating the count in words, with the reason for each, is what earns the mark; a bare number with no reason usually earns nothing.

## 4. Worked Implementation from the Notes

### 4.1 Task: produce the evidence a good answer quotes

### 4.2 Implementation: one command, three facts

Step 1. Request headers only from a secure address.

```bash
curl -I https://shop.example.com/catalog/items
```

Step 2. Read representative output.

```http
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:15:22 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 18432
Cache-Control: public, max-age=300
ETag: "7d3f9a1c-4800"
```

Step 3. Extract the three facts worth quoting. The status line shows the version, the code, and the reason phrase in that order. The Content-Type header shows a media type with a charset parameter, which is the pattern an answer should reproduce. The ETag header shows the validator that makes a conditional request possible.

Step 4. Note what the command proves beyond its content: the request used the HEAD method, so no body was transferred, which is why the response stops after the headers.

### 4.3 Task: show that a redirect changes the address, not the method contract

### 4.4 Implementation: read the location header

Step 1. Ask for the old address.

```bash
curl -i https://shop.example.com/catalogue
```

Step 2. A representative first line and header are `HTTP/1.1 301 Moved Permanently` and `Location: https://shop.example.com/catalog`. The pair is the whole mechanism: the code states the permanence and the header states the destination.

Step 3. Compare with a temporary move, where the code is 302 and the client is expected to keep using the original address. The distinction is what a search engine uses when deciding whether to transfer ranking.

Step 4. State the consequence for an exam answer: the code carries the permanence and the header carries the destination, and an answer that gives only one of the two is incomplete.

### 4.5 Task: answer a question on the request-response cycle and statelessness

### 4.6 Implementation: complete model answer, eight marks

Question: Describe the HTTP request-response cycle and explain why HTTP is described as stateless. (8 marks)

1. The client parses the address into scheme, host, port, path, and query, and discards the fragment because it is never transmitted. (1 mark)
2. The client resolves the host name to an address and opens a transport connection to the port, using 80 for http and 443 for https. (1 mark)
3. For HTTPS the client completes the TLS handshake before any request is sent, so that the message is protected. (1 mark)
4. The client sends a request message: a request line naming the method, target, and version; header fields including a mandatory Host; an empty line; and an optional body. (2 marks)
5. The server interprets the method and target and returns a response message: a status line naming the version, code, and reason phrase; headers describing the body; an empty line; and an optional body. (2 marks)
6. HTTP is stateless because each request must be interpretable without reference to earlier requests, so the server retains no protocol-level context between them; this allows any server instance to handle any request, and continuity such as a login must be reconstructed from cookies or tokens sent with every request. (1 mark)

Marking note: step four and step five each carry two marks because each must have both the correct order and the empty-line terminator. A candidate who writes "the browser sends a request and the server replies" earns one mark at most.

### 4.7 Task: answer a question comparing methods

### 4.8 Implementation: complete model answer, ten marks

Question: Compare GET, POST, PUT, and DELETE with reference to safety and idempotence, and state the success status code for each. (10 marks)

1. A method is safe when it does not change the state of the server, and idempotent when repeating it has the same effect on server state as performing it once. (2 marks)
2. GET retrieves a representation; it is safe and idempotent; a successful read returns 200 with the representation in the body. (2 marks)
3. POST submits data for processing; it is neither safe nor idempotent, because repeating it may create a second resource; a successful creation returns 201 with a Location header naming the new resource. (2 marks)
4. PUT replaces the resource at a known address; it is not safe because it changes state, but it is idempotent because the same replacement applied twice leaves the same content; success returns 200 with the new representation or 204 with none. (2 marks)
5. DELETE removes the resource; it is not safe but it is idempotent, because after the first removal the resource is absent and further removals leave it absent; success returns 204, and a repeat may return 404 without breaking idempotence. (1 mark)
6. The distinction matters operationally: a client or intermediary may retry an idempotent request automatically, may cache and prefetch a safe GET, and must not silently repeat a POST, which is why browsers warn before resubmitting a form and why APIs add idempotency keys. (1 mark)

Marking note: the most frequently lost mark is the last one. The classification alone is recall; the operational consequence is understanding.

### 4.9 Task: answer a question on HTTPS and certificates

### 4.10 Implementation: complete model answer, ten marks

Question: Explain how HTTPS uses both asymmetric and symmetric encryption, and describe the role of certificates in establishing trust. (10 marks)

1. HTTPS is HTTP carried over a Transport Layer Security channel, using port 443 by default, and it provides confidentiality, integrity, and authentication of the server. (2 marks)
2. The client sends a ClientHello with the versions, cipher suites, and key share it supports, and names the site it wants so that a shared server can select the right certificate. (1 mark)
3. The server replies with a ServerHello containing its key share and the chosen cipher suite, and sends its certificate chain. (1 mark)
4. Both sides derive the same shared secret from the ephemeral key exchange, so the secret is never transmitted; the server also signs the handshake with the private key matching its certificate, proving it holds that key. (2 marks)
5. Each side sends a Finished message that is a keyed hash over the transcript, proving that both derived identical keys, after which application data is protected by an authenticated symmetric cipher such as AES-GCM. (1 mark)
6. Asymmetric cryptography is used only for authentication and key agreement because it is computationally expensive and can encrypt only a small block, whereas symmetric cryptography is used for bulk data because it is orders of magnitude faster and provides integrity together with confidentiality. (1 mark)
7. The certificate is a signed statement binding a domain name to a public key, issued by a certificate authority; the client builds a chain from the leaf through intermediates to a root it already trusts, verifies each signature, checks the validity dates and the permitted uses, and matches the requested host name against the subject alternative names. (2 marks)

Marking note: step six is the answer to "why both", and it must name cost and capacity. Step seven must mention the chain and the name check; a candidate who says only "the certificate proves the site is safe" earns nothing.

### 4.11 Task: answer a question on cookies and statelessness

### 4.12 Implementation: complete model answer, eight marks

Question: Explain how cookies allow a stateless protocol to support a login session, and describe three attributes that make a session cookie secure. (8 marks)

1. A cookie is a small name-value pair that a server sends in a Set-Cookie response header and that the client stores and returns in a Cookie request header on later matching requests. (2 marks)
2. Because HTTP retains no state between requests, the server cannot recognise a returning client by the connection; instead it issues an unguessable session identifier as a cookie value and stores the associated state on the server, keyed by that identifier. (2 marks)
3. Each later request carries the identifier, the server looks it up, and identity is reconstructed; without the cookie the same request returns 401, which demonstrates that the protocol itself carried no identity. (1 mark)
4. Secure restricts the cookie to HTTPS, so the identifier is never exposed on a plain connection. (1 mark)
5. HttpOnly hides the cookie from page scripts, so a cross-site scripting flaw cannot read and exfiltrate the session identifier. (1 mark)
6. SameSite equal to Lax, or Strict where cross-site navigation is unnecessary, stops the cookie being attached to cross-site requests, which blunts cross-site request forgery; a value of None must be combined with Secure. (1 mark)

Marking note: step two must mention both halves, the client-side identifier and the server-side record. A candidate who says the cookie "stores the user's login" has misunderstood, because the cookie stores only an opaque reference.

### 4.13 Task: answer a diagnostic question

### 4.14 Implementation: complete model answer, six marks

Question: A client that successfully logged in yesterday now receives 401 from every protected endpoint, while public pages still return 200. Explain three plausible causes and the evidence that would distinguish them. (6 marks)

1. The session expired, because the cookie was issued with a bounded Max-Age or the server-side record reached its own expiry; the evidence is a Set-Cookie header at login carrying a short Max-Age and no newer Set-Cookie afterwards. (2 marks)
2. The cookie is not being sent, because its Domain, Path, or SameSite attribute excludes the endpoint, or because it is marked Secure and the client is using a plain connection; the evidence is the absence of a Cookie header on the failing request while the browser's stored cookie list still shows the value. (2 marks)
3. The session was invalidated on the server, for example by a restart with in-memory sessions, a logout in another tab, or a credential change; the evidence is that a fresh login restores access immediately and the old identifier no longer resolves to a record. (2 marks)

Marking note: each cause earns one mark and the evidence earns one. Naming a cause without a discriminating observation earns half credit at most, because the question asks how the causes would be distinguished.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Revision checklist

Work through this list and tick only what you can do aloud, without notes, in under a minute each.

- Expand URI, URL, URN, HTTP, HTTPS, TLS, SSL, DNS, and CA correctly.
- Write the general form of a URI and name all six components.
- Break a given address into components and state which parts reach the server.
- State the two default ports and what each scheme implies.
- Write a request line and a status line in the correct order.
- State the three parts of a message and the role of the empty line.
- Name the three ways a body is delimited.
- Define safe and idempotent, and classify all seven methods.
- Give the five status classes with their meanings.
- Give the meaning of 200, 201, 204, 301, 302, 304, 400, 401, 403, 404, 405, 500, 502, and 503.
- Name the mandatory companion header for 401 and for 405.
- Explain the role of Host, User-Agent, Accept, Content-Type, Authorization, Cache-Control, and Set-Cookie.
- Describe the TLS 1.3 handshake in four stages and the TLS 1.2 handshake in six.
- Explain why asymmetric cryptography is confined to the handshake.
- Describe certificate validation as an ordered chain check, including the name check.
- Name six cookie attributes and the attack each addresses.
- Explain persistence, the cost it saves, and the problem it introduces.
- State three limitations of HTTPS as a security control.

### 5.2 Time strategy

A three-hour paper with six questions gives thirty minutes each, and a two-hour paper with four questions gives thirty minutes each. In either case the internal split should be roughly one minute of writing per mark, plus two minutes of planning.

For a ten-mark question, spend two minutes writing a four-word plan in the margin: name, message, method, channel. Then twelve minutes of writing, and one minute re-reading for the mandatory details: the empty line, the port numbers, the companion headers, and the word "idempotent" spelled correctly. For a four-mark question, spend forty seconds on the plan and four minutes writing, and do not exceed five minutes, because the cheap marks on the next question are worth more than a perfect sentence here.

Two timing errors cost more than any content error. The first is spending fifteen minutes on a two-mark definition, which is unrecoverable because the later questions are the expensive ones. The second is answering a "discuss" question with a list, which takes as long as an argument and earns about half the marks. If a question says discuss or evaluate, one third of the answer must be limitation or trade-off.

### 5.3 How marks are lost, in order of frequency

1. **No explicit classification.** The question asks whether a method is safe and idempotent, and the answer describes what the method does instead. State the classification as a sentence before explaining it.
2. **Missing companion header.** A 401 answer without a WWW-Authenticate mention, or a 405 without Allow, loses a mark that takes six words to secure.
3. **Reversed ports.** HTTPS is 443 and HTTP is 80. A reversal inside an otherwise good answer is read as carelessness and often costs two marks, because the answer is then internally inconsistent.
4. **Confusing authentication with authorisation.** 401 is authentication; 403 is authorisation. Say "who you are" and "what you may do" explicitly.
5. **Describing idempotence as safety.** Repetition is not the same as no change; PUT repeats idempotently and still changes state.
6. **Claiming the fragment is transmitted.** It is not. Say that the client strips it and resolves it locally.
7. **Describing TLS as symmetric throughout, or asymmetric throughout.** The split is the point of the question.
8. **Omitting the limitation.** Evaluation marks require a limit, and HTTPS always has one: it protects the channel, not the application, and a padlock is not a character reference.
9. **Giving a bare number for a round-trip question.** State the handshake, state what it costs, and state what persistence saves.
10. **Ignoring the verb in the question.** "Describe" wants sequence, "compare" wants two sides and a criterion, "evaluate" wants a judgement with support. A candidate who describes when asked to evaluate has answered a different question.

### 5.4 Interpretation habits that raise the grade

Read the status code before the payload, because a friendly error page may arrive with a failure code and a page that looks correct may have arrived with a redirect that changed the address. Read the request line before the headers, because the method and target decide the entire meaning of the message. Read the mandatory headers before the optional ones, because Host, Content-Type, Location, Allow, and WWW-Authenticate are where marking schemes put their points.

When a question supplies an exchange, count the parts of the message before interpreting it: one request line or status line, a header block, one empty line, and a body. Most supplied extracts in examinations are missing exactly one element, and the question usually asks which.

### 5.5 The last five facts to revise before entering the room

HTTP is stateless, and sessions are reconstructed from cookies on every request. The default ports are 80 and 443. GET and HEAD are safe and idempotent; PUT and DELETE are idempotent but not safe; POST is neither. TLS uses asymmetric cryptography to authenticate and agree a key, then symmetric cryptography for the data. A certificate binds a name to a public key and is validated through a chain to a trusted root, including a check that the requested name appears in the certificate.
