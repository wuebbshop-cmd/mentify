## 1. Concept and Use Case

### 1.1 The problem the protocol solves

The World Wide Web is a system of documents that point at one another. To make such a system work across millions of independently operated machines, three questions must be answered in a way that any client and any server can agree on without prior arrangement. First, how is a document named so that the name can be transmitted, compared, stored in a bookmark, and resolved by a machine that has never seen it before? Second, what exactly does a client say when it wants a document, and what exactly does a server say when it answers? Third, how can that conversation be protected from a network that is assumed hostile?

The answers are the subject of this topic. Uniform Resource Identifiers supply the naming scheme. The Hypertext Transfer Protocol supplies the conversation. Transport Layer Security supplies the protection, and HTTP carried inside it is HTTPS. The three fit together because each was designed as a general mechanism rather than as a solution to one site's needs: a URI can name anything, HTTP can carry any representation of anything, and TLS can protect any byte stream.

### 1.2 Four commitments that explain most of the protocol

Almost every rule examined in this topic follows from four design commitments, and an answer that names the commitment before the rule is always stronger than one that lists rules.

**Statelessness.** The server keeps no memory of previous requests as part of the protocol. Each request must carry everything needed to interpret it. The benefit is that any server instance can handle any request from any client, which is what makes load balancing, horizontal scaling, and restarting a server mid-traffic possible. The cost is that continuity must be reconstructed at a higher level, using cookies, tokens, or server-side session stores.

**A uniform interface.** Every resource is manipulated through the same small set of methods applied to the same kind of identifier. There is no per-resource vocabulary of verbs. The benefit is that generic software — browsers, caches, proxies, crawlers, monitoring agents — can act on resources it has never seen. The cost is that some operations fit the vocabulary awkwardly, which is why `POST` is used as a general-purpose escape hatch.

**Self-describing messages.** Each message carries metadata sufficient to interpret it: the media type of the body, its length or framing, its encoding, its cacheability, and the credentials attached. A receiver never has to guess.

**Layering.** Proxies, gateways, and caches may sit between client and server and participate in the conversation without either end knowing how many intermediaries exist, provided they obey the same rules about headers and hop-by-hop behaviour.

### 1.3 The use cases that follow

Content retrieval is the original use case: a browser asks for a document, the server returns a representation. Form submission is the second: the client sends data in a body and the server acts on it. Programmatic interfaces are the third: a client application exchanges structured data such as JSON rather than pages, using the same methods and status codes over the same protocol. Redirects and canonicalisation are the fourth: a server tells clients and search engines that a resource has moved, permanently or temporarily. Caching and content delivery are the fifth: headers let a response be reused by browsers and shared caches, which is why the web is affordable at global scale. Session management is the sixth: cookies restore identity on top of a stateless protocol, which is what makes a login possible.

### 1.4 The threat model that motivates HTTPS

An HTTP message crosses many networks that the two endpoints do not control: a wireless access point, an Internet Service Provider's access and core network, transit providers, and any middlebox that inspects traffic. On that path an attacker may read the bytes passively, modify them actively, or impersonate the server by answering in its place.

HTTPS addresses all three. Confidentiality prevents reading. Integrity prevents undetected modification. Authentication prevents impersonation, because the client accepts the connection only after the server proves possession of a private key corresponding to a certificate that a trusted authority issued for that exact name. The three properties are independent: a system that encrypts without authenticating is defeated by a machine in the middle that simply relays and reads, which is why the certificate check is not an optional extra.

## 2. Data, Syntax, and Core Concepts

### 2.1 Uniform Resource Identifier syntax

A URI is defined by a grammar with six components. Written in the notation of the specification, the general form is a scheme, a colon, a hierarchical part, an optional query introduced by a question mark, and an optional fragment introduced by a hash mark.

```text
  https://shop.example.com:8443/catalog/items?category=books&page=2#reviews
  scheme  authority          path            query                    fragment
```

The hierarchical part either begins with two slashes and an authority, or begins directly with a path. Inside the authority, an optional user information part precedes an at sign, then the host, then an optional colon and port. For web addresses the authority is present and the user information part is absent in practice.

| Component | Grammar role | Notes |
|---|---|---|
| Scheme | Selects the protocol | Case insensitive; `https` implies port 443 |
| Authority | Names the host and service | May include user information and port |
| Host | Registered name or address literal | Resolved through the Domain Name System |
| Port | Decimal number | Defaults to 80 for http, 443 for https |
| Path | Hierarchical resource name | Empty path is equivalent to `/` for http |
| Query | Non-hierarchical parameters | Begins at the first question mark |
| Fragment | Secondary reference within the resource | Client-side only; never transmitted |

Two rules about the fragment matter in practice. It is stripped before transmission, so a server never sees it and cannot use it to decide what to return. It is also excluded from the comparison that determines whether two addresses identify the same resource for caching purposes, which is why two links that differ only after the hash can share one cached response.

### 2.2 Percent-encoding, normalisation, and equivalence

The character repertoire of a URI is restricted to a defined set. Unreserved characters are letters, digits, hyphen, full stop, underscore, and tilde, and they may appear literally. Reserved characters carry syntactic meaning and appear literally only in their grammatical position. Every other character, and any reserved character used as data, is written as a percent sign followed by the two hexadecimal digits of its byte.

Normalisation reduces variation that has no meaning. The scheme and host are case insensitive, so `HTTPS://SHOP.EXAMPLE.COM/` and `https://shop.example.com/` are equivalent. An empty path is equivalent to a single slash for these schemes. A port equal to the default may be omitted. Percent-encoded unreserved characters may be decoded, because decoding them cannot change the meaning of the address. Case in the path, by contrast, may be significant, since servers on case-sensitive filesystems distinguish `/Catalog` from `/catalog`.

These rules explain a class of security bug. If a filter checks a decoded form and the server interprets an encoded form, an attacker can place a sequence that the filter misses and the server honours. Normalising once, at the boundary, and rejecting anything ambiguous is the defence.

### 2.3 Forms of the request target

The second token of the request line is the request target, and it takes four forms.

The origin form is the ordinary one: absolute path plus optional query, for example `/catalog/items?page=2`. It omits scheme, host, and port, because the Host header supplies them.

The absolute form includes the full address and is used when a client sends a request to a proxy, because the proxy must know which origin server to contact.

The authority form is a host and port only, used with the `CONNECT` method to ask a proxy to open a tunnel, which is how HTTPS is carried through an intercepting proxy.

The asterisk form is a single asterisk, used with `OPTIONS` to ask about the server as a whole rather than one resource.

### 2.4 The exact request message format

An HTTP/1.1 request is a sequence of octets with a rigid structure. The first line is the request line, terminated by a carriage return and a line feed. Next come zero or more header field lines, each terminated the same way. A single empty line, which is one carriage return and one line feed, ends the header section. The message body, if any, follows and is delimited by rules given below.

```text
request-line   = method SP request-target SP HTTP-version CRLF
header-field   = field-name ":" OWS field-value OWS CRLF
```

The method is case sensitive and is `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `OPTIONS`, or `TRACE` among those examined here. The version reads `HTTP/1.1`. Field names are case insensitive, but convention and most examples use the capitalised forms. Optional whitespace around the value is stripped.

```http
GET /catalog/items?category=books&page=2 HTTP/1.1
Host: shop.example.com:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9
Accept-Language: en-GB,en;q=0.8
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

In HTTP/1.1 the Host field is mandatory and must appear exactly once. It is what allows a single address and port to serve many sites: the server reads the field and selects the correct virtual host. A request without it is malformed, and a server should answer with 400 Bad Request.

### 2.5 The exact response message format

A response begins with a status line whose three tokens are the version, the three-digit status code, and an optional reason phrase. The reason phrase exists for human readers and carries no protocol meaning; a client must decide on the code alone.

```text
status-line    = HTTP-version SP status-code SP reason-phrase CRLF
```

```http
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:15:22 GMT
Server: nginx/1.24.0
Content-Type: text/html; charset=UTF-8
Content-Length: 18432
Cache-Control: public, max-age=300
ETag: "7d3f9a1c-4800"
Last-Modified: Thu, 06 Nov 2026 18:02:11 GMT
Vary: Accept-Encoding

<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Books</title></head>
<body><h1>Books</h1></body>
</html>
```

Status codes are grouped by first digit. The class determines the meaning of the remaining digits and the client's appropriate reaction.

| Class | Meaning | Individual codes that matter |
|---|---|---|
| 1xx | Informational; the request was received and processing continues | 100 Continue, 101 Switching Protocols |
| 2xx | Success; the request was understood, accepted, and acted on | 200 OK, 201 Created, 204 No Content, 206 Partial Content |
| 3xx | Redirection; further action is required to complete the request | 301, 302, 303, 304, 307, 308 |
| 4xx | Client error; the request is invalid or cannot be fulfilled as sent | 400, 401, 403, 404, 405, 409, 415, 429 |
| 5xx | Server error; the server failed while handling a valid request | 500, 501, 502, 503, 504 |

The distinction inside the two hundreds is semantic, not cosmetic. A 200 means the request succeeded and the body is the representation. A 201 means a resource was created and the Location header carries its address. A 204 means the request succeeded and there is deliberately no body, which is the correct answer to a successful delete or an update with nothing to return. A 206 means the body is a byte range, and the Content-Range header says which range, which is how resumable downloads work.

Inside the three hundreds, the difference between 301 and 302 is one of permanence, and the difference between 302 and 307 is one of method preservation. A 301 or 302 may be rewritten to a `GET` by some clients when the original request was a `POST`; 307 and 308 forbid that and require the method and body to be replayed unchanged. A 303 instructs the client to fetch another resource with `GET`, which is the standard pattern after a form submission. A 304 carries no body and means the client's cached copy is still valid.

Inside the four hundreds, the codes that reward memorisation are 400 for a malformed request, 401 for missing or invalid credentials, 403 for a permission refusal, 404 for an absent resource, and 405 for a method the resource does not allow. A 401 must include a challenge in the WWW-Authenticate header naming the scheme, and a 405 must include an Allow header listing the methods that are permitted. The distinction between 401 and 403 is authentication against authorisation: 401 says the server does not know who the client is, 403 says it does know and still refuses.

Inside the five hundreds, 500 is an unhandled failure in the application, 502 means a gateway received an invalid response from an upstream server, 503 means the service is temporarily unable to handle the request and may include Retry-After, and 504 means a gateway timed out waiting for an upstream response. The difference between 502 and 504 is diagnostic: 502 says the upstream answered badly or not at all, 504 says it did not answer in time.

### 2.6 Message body delimitation

A receiver must know where the body ends, and HTTP offers three mechanisms, applied in a fixed order of precedence.

If a Transfer-Encoding header is present and its final coding is chunked, the body is chunked. The body is a sequence of chunks: a line giving the chunk length in hexadecimal, then that many octets, then a carriage return and line feed. A chunk of length zero ends the body, and an optional trailer section may follow.

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked

f
<!DOCTYPE html>
26
<html><head><title>Shop</title></head>
23
<body><h1>Items</h1></body></html>
0

```

Each size line is hexadecimal; `f` is fifteen octets and `26` is thirty-eight. Chunked encoding lets a server begin sending before the total length is known, which is essential for pages generated as they are produced.

If Transfer-Encoding is absent and Content-Length is present, the body is exactly that many octets. If both are present the message is ambiguous, and a server must reject it rather than guess; treating Content-Length as authoritative while an intermediary treats Transfer-Encoding as authoritative is the mechanism behind request smuggling attacks. If neither is present, the body length is determined by the connection closing, which prevents the connection being reused.

Status codes 204 and 304, and any response to a `HEAD` request, never carry a body regardless of what the headers say.

### 2.7 Methods, safety, and idempotence

The definitions below are the ones an examiner expects, stated in the language of the specification.

`GET` transfers a current representation of the target resource. It is safe and idempotent, and it is cacheable by default.

`HEAD` is identical to `GET` except that the server must not send a body. It is safe and idempotent, and its response headers should be the same as those a `GET` would produce, which is what makes it useful for checking existence, size, and freshness.

`POST` asks the target resource to process the enclosed representation according to its own semantics. It is neither safe nor idempotent, and it is cacheable only when the response explicitly says so with freshness information.

`PUT` requests that the state of the target resource be replaced by the enclosed representation. It is idempotent but not safe. Sending the same representation twice leaves the resource in the same state as sending it once, which is why retrying a `PUT` after a network failure is permitted.

`DELETE` requests removal of the target resource. It is idempotent but not safe. A second `DELETE` may return 404 or 204, but the state of the server is the same either way, which is what idempotence requires.

`OPTIONS` requests information about the communication options available for the target. It is safe and idempotent, and its response typically includes an Allow header listing supported methods.

`TRACE` requests a loop-back of the request message so the client can see what intermediaries did to it. It is safe and idempotent, and it is normally disabled because reflecting headers can expose credentials and internal addresses.

| Method | Safe | Idempotent | Typical success code | Changes state |
|---|---|---|---|---|
| GET | Yes | Yes | 200 | No |
| HEAD | Yes | Yes | 200 | No |
| POST | No | No | 201 or 200 | Yes |
| PUT | No | Yes | 200 or 204 | Yes |
| DELETE | No | Yes | 204 or 200 | Yes |
| OPTIONS | Yes | Yes | 200 or 204 | No |
| TRACE | Yes | Yes | 200 | No |

Idempotence is a promise about the effect on the server, not about the response. The second `DELETE` may return a different code from the first; what must not differ is the resulting state. This is precisely why a client or an intermediary may retry an idempotent request automatically but must not retry a `POST` without an explicit agreement, such as an idempotency key.

### 2.8 The header fields that carry the design

Headers are the mechanism by which a uniform interface stays usable. Seven are examined closely, and each answers a specific question.

`Host` answers "which site do you want". It is mandatory in HTTP/1.1 and is the basis of virtual hosting.

`User-Agent` answers "what is asking". It identifies the client software and version. It is used for compatibility decisions and analytics, and it is trivially forgeable, so it must never be used for security decisions.

`Accept` answers "what media types can you handle". It is a comma-separated list, optionally weighted with q-values from zero to one, so a client can express preference order. `Accept-Encoding` performs the same function for compression algorithms and `Accept-Language` for natural languages.

`Content-Type` answers "what is in the body". Its value is a media type and optional parameters, for example `text/html; charset=UTF-8` or `application/json`. A server that receives a body without knowing its type cannot parse it reliably, which is why a request that posts JSON must state the type and a server may answer 415 Unsupported Media Type if it does not accept it.

`Authorization` answers "who is this and what may they do". Its value is a scheme name followed by credentials formatted for that scheme. In the Basic scheme the credentials are a user name and password joined by a colon and encoded in Base64, which is encoding, not encryption, and is therefore only safe inside TLS. In the Bearer scheme the credentials are a token issued earlier.

`Cache-Control` answers "who may store this reply, and for how long". Directives include `no-store`, which forbids storage; `no-cache`, which permits storage but requires validation before reuse; `max-age` in seconds, which sets freshness; `private`, which restricts storage to the single user's browser; `public`, which permits shared caches; and `must-revalidate`, which forbids serving stale content.

`Set-Cookie` answers "here is state to remember". It is the only header that creates client-side state, and its attributes are examined separately below. The matching request header is `Cookie`, which carries the stored pairs back.

Other headers recur in diagnosis: `Location` gives the target of a redirect or the address of a newly created resource; `ETag` gives a version tag for validation; `Last-Modified` gives a timestamp for the same purpose; `If-None-Match` and `If-Modified-Since` carry the client's cached version for comparison; `Vary` tells caches which request headers affected the response; `Connection` controls persistence; and `Strict-Transport-Security` instructs a browser to use HTTPS for that host for a stated period.

### 2.9 Statelessness in operation

Statelessness is a property of the protocol, not of the application. The server may hold any amount of data about a user; what it may not do is rely on the transport connection to tell it which user is calling. Every request must identify the user explicitly, through a cookie, a token, or a credential.

This design produces three practical consequences. Requests become independently routable, so any of a hundred servers can answer any request as long as they share the session store. Recovery becomes simple, because a crashed server loses nothing that the protocol required it to remember. Requests become self-contained and therefore cacheable and replayable, which is what enables proxies and content delivery networks.

The cost is that every request carries the identity overhead, and that the session store becomes a central dependency with its own scaling and consistency problems. It is also the reason a logout is not automatic: the server must invalidate the session identifier, because the client will keep presenting it until it expires.

### 2.10 Cookie mechanics and attributes

A cookie is a name, a value, and a set of attributes that govern where and how it is returned. The server sets it with one header per cookie.

```http
Set-Cookie: session_id=8f21c9d4e77a; Domain=shop.example.com; Path=/; Expires=Fri, 07 Nov 2026 10:15:22 GMT; Secure; HttpOnly; SameSite=Lax
```

`Domain` sets the scope of the host names to which the cookie applies. When it is omitted the cookie is host-only and returns only to the exact host that set it, which is the safest default. When it is present the cookie also returns to subdomains of the stated domain. A server may not set a domain unrelated to the host that set it, and browsers refuse such a cookie, which is what prevents one site from writing cookies for another.

`Path` sets the scope of request paths. A cookie with `Path=/catalog` is returned for `/catalog` and `/catalog/items` but not for `/orders`. A narrower path reduces exposure, though it is a scoping mechanism, not a security boundary.

`Expires` sets an absolute expiry date and `Max-Age` sets a lifetime in seconds. When both appear, `Max-Age` takes precedence. A cookie without either is a session cookie that the browser discards when it closes the session, which modern browsers treat as when the last window closes rather than when the tab closes.

`Secure` restricts the cookie to encrypted connections. Without it, the cookie can be sent over plain HTTP once, and an attacker on the network can read it and take over the session.

`HttpOnly` makes the cookie invisible to scripts running in the page. It does not stop an attacker from making requests that carry the cookie, but it does stop the cookie value being read out and exfiltrated, which converts many cross-site scripting bugs from session theft into less severe problems.

`SameSite` controls whether the cookie accompanies requests initiated by another site. `Strict` withholds it entirely on cross-site navigation, which is the most protective but makes an inbound link appear logged out. `Lax` sends it on top-level navigations using a safe method such as a link click, but not on cross-site form posts or embedded requests, which blocks the classic cross-site request forgery pattern while keeping links working. `None` sends it everywhere and must be combined with `Secure`. When the attribute is absent, modern browsers apply `Lax` behaviour by default, but relying on that default is unwise because older clients do not.

### 2.11 Connection persistence

HTTP/1.0 closed the connection after each response unless the client asked for `Connection: keep-alive`. HTTP/1.1 inverted the default: connections persist unless a participant sends `Connection: close`. Persistence saves the three-way handshake and the slow-start ramp of the congestion window for every subsequent request, which on a high-latency link is the dominant cost of a page with many small resources.

Persistence brings its own problems. Sequential requests on one connection suffer head-of-line blocking: a slow response delays everything behind it. Servers must also impose idle timeouts, because a client that holds a connection open consumes a slot. HTTP/2 addressed head-of-line blocking at the application layer by multiplexing independent streams over one connection and compressing headers, at the cost of a new form of blocking at the transport layer when a TCP segment is lost. HTTP/3 moves to a transport built on datagrams so that loss on one stream does not stall the others.

### 2.12 TLS: record layer and handshake

TLS has two layers. The record layer fragments application data into records, protects each with an authenticated cipher, and carries handshake messages in the same framing. The handshake layer negotiates parameters and establishes keys.

A TLS 1.2 full handshake proceeds as follows.

1. The client sends a ClientHello containing the highest version it supports, a 32-byte random value, a session identifier, a list of cipher suites, and extensions including the server name indication, the groups it supports for key agreement, and the signature algorithms it accepts.
2. The server replies with a ServerHello containing the chosen version, its own random value, and the selected cipher suite, followed by its certificate chain.
3. In an ephemeral Diffie-Hellman suite the server sends a ServerKeyExchange containing its public key share and a signature over the handshake transcript made with the private key matching its certificate.
4. The server sends ServerHelloDone.
5. The client sends its own key share in ClientKeyExchange. Both sides can now compute the same shared secret without either transmitting it.
6. The client sends ChangeCipherSpec and then a Finished message, which is a keyed hash over the transcript, proving that it derived the same keys.
7. The server sends ChangeCipherSpec and its Finished message, proving the same in the other direction.
8. Both sides switch to the negotiated authenticated cipher for application data, with separate keys for each direction.

A TLS 1.3 handshake is shorter because the key share travels in the first flight.

1. The client sends a ClientHello with supported versions, a key share for a guessed group, cipher suites restricted to authenticated encryption, and a signature algorithm list.
2. The server replies with a ServerHello containing its key share, so both sides can derive the handshake secret after one round trip. If the client's guessed group is unacceptable, the server sends a HelloRetryRequest and the exchange costs an extra round trip.
3. Everything after the ServerHello is encrypted: EncryptedExtensions, the Certificate message, a CertificateVerify message containing a signature over the transcript, and the server's Finished.
4. The client validates the certificate and the signature, then sends its Finished.
5. Application data flows, protected by keys derived from the handshake secret, with the client able to send early data in a resumed session.

TLS 1.3 removed static RSA key exchange, which means every connection provides forward secrecy: an attacker who later obtains the server's private key cannot decrypt previously recorded traffic, because the session keys came from ephemeral values that no longer exist.

### 2.13 Certificates and the validation chain

A certificate is a signed data structure. In the widely used X.509 form it contains a subject name, an issuer name, a validity period, the subject's public key, a serial number, extensions, and a signature made by the issuer over all of the above.

The issuer is a certificate authority. Authorities are arranged in a hierarchy: a root authority signs intermediate authorities, and an intermediate signs the certificate presented by the server, which is the leaf. A client trusts a small set of roots installed with the operating system or browser, and it trusts everything reachable from them by a valid chain.

Validation is a sequence of checks, and a client performs all of them.

1. Build a chain from the leaf through any intermediates to a trusted root.
2. Verify each signature in the chain using the public key of the certificate above it.
3. Check that every certificate's validity period contains the current time.
4. Check the extensions that constrain use: a certificate marked as a certificate authority may sign others, and a leaf must be marked for server authentication.
5. Match the requested host name against the subject alternative names in the leaf. The older common name field is no longer accepted for this purpose.
6. Check revocation, either by consulting a revocation list or by an online status query, or accept the certificate if the client policy does not require it.
7. Confirm that the root is one the client already trusts.

Only when every step succeeds does the client proceed. The padlock therefore states a chain of inference: the private key matching this public key signed this handshake, the authority named in the certificate vouched for that key belonging to this name, and the client trusts that authority.

### 2.14 Why two kinds of encryption

Public key cryptography solves key distribution: the server publishes a key that anyone may use, and only the holder of the matching private key can undo what was done with it. It does not solve bulk encryption, for three reasons.

The first is cost. A modular exponentiation with a 2048-bit key takes on the order of a millisecond and processes no payload at all, while a modern symmetric cipher with hardware acceleration processes gigabytes per second. Per byte of protected data, the asymmetric operation is thousands of times more expensive.

The second is capacity. Asymmetric encryption can only encrypt a short block, on the order of a few hundred bytes for a 2048-bit key, so it cannot carry a page, an image, or a video.

The third is integrity. Asymmetric encryption on its own provides no authentication of a long stream, whereas authenticated symmetric ciphers such as AES-GCM and ChaCha20-Poly1305 provide confidentiality and integrity together with a per-record nonce.

The practical arrangement is therefore a hybrid: the asymmetric exchange authenticates the server and establishes a shared secret, and symmetric keys derived from that secret protect the bulk data. One expensive operation, then cheap ones for everything else.

## 3. Methods and Operations

### 3.1 Composing a valid request

1. Choose the method from the semantics of the operation, not from convenience.
2. Write the request target in origin form unless a proxy requires absolute form.
3. State the version.
4. Include Host exactly once, with the port only when it is not the default for the scheme.
5. Add the representation metadata if a body is present: Content-Type, and either Content-Length or chunked transfer coding.
6. Add negotiation headers that describe what the client can accept.
7. Add conditional headers if a cached copy is held.
8. Add credentials only when the resource requires them, and only over TLS.
9. Terminate the header section with an empty line, then send the body.

### 3.2 Content negotiation

Negotiation lets one address serve several representations. The client states preferences in Accept, Accept-Encoding, and Accept-Language; the server selects one and reports which request headers influenced the choice in Vary.

The Vary header is not optional bookkeeping. If a response differs by encoding and the cache is not told, it may serve a compressed body to a client that cannot decompress it. If it differs by language and Vary omits the language header, a cache may serve French to an English reader.

When no acceptable representation exists, the correct answer is 406 Not Acceptable rather than a silent substitution, because a silent substitution looks to the client like success.

### 3.3 Conditional requests and cache validation

Validation converts a full transfer into a cheap comparison. The server supplies a validator, usually an ETag, and the client returns it in If-None-Match on the next attempt.

```http
GET /catalog/items HTTP/1.1
Host: shop.example.com
If-None-Match: "7d3f9a1c-4800"
```

```http
HTTP/1.1 304 Not Modified
Date: Fri, 07 Nov 2026 09:20:41 GMT
ETag: "7d3f9a1c-4800"
Cache-Control: public, max-age=300
```

The 304 has no body, so the saving is the whole payload. The same pattern with Last-Modified and If-Modified-Since uses a timestamp rather than a tag; the tag is preferred because a timestamp has one-second resolution and cannot express a change that restores an older version.

Conditional headers also prevent lost updates. A `PUT` with If-Match carrying the tag the client last saw fails with 412 Precondition Failed if someone else has changed the resource in the meantime, which is optimistic concurrency control built into the protocol.

### 3.4 Selecting methods for a data model

1. Reading one item maps to `GET` on its address.
2. Reading a collection with filters maps to `GET` with query parameters.
3. Creating an item whose address the server assigns maps to `POST` on the collection, answering 201 with Location.
4. Creating or replacing an item at a client-chosen address maps to `PUT`, which is idempotent and therefore safe to retry.
5. Partially updating an item has no dedicated method; `PATCH` is the usual choice and is neither safe nor necessarily idempotent, while `PUT` with a complete representation remains the safest option where the full state is known.
6. Deleting maps to `DELETE`, answering 204 on success and 404 when the resource is already gone if the client needs to know.
7. Discovering capabilities maps to `OPTIONS`, whose Allow header should list the methods the resource supports.

Where a `POST` must be retried safely, the usual industrial answer is an idempotency key: the client generates a unique value, sends it in a header, and the server stores the first result against that key so a repeat returns the same result instead of creating a second record. The protocol does not provide this; it is an application convention layered on a non-idempotent method.

### 3.5 Designing the status code a client sees

1. Return 200 when a read succeeds and a body is present.
2. Return 201 with Location when a resource is created.
3. Return 204 when an action succeeds and there is nothing to return.
4. Return 304 when a conditional read finds the client's copy current.
5. Return 301 or 308 when a resource has moved permanently, choosing 308 when the method must be preserved.
6. Return 302 or 307 when the move is temporary, choosing 307 for the same reason.
7. Return 303 after a form submission that should be followed by a `GET`.
8. Return 400 for a malformed or invalid request, 401 with a challenge for missing credentials, 403 for a refusal, 404 for absence, 405 with Allow for a wrong method, 409 for a state conflict, 415 for an unsupported media type, and 429 with Retry-After for rate limiting.
9. Return 500 only for genuine application faults, 502 and 504 for upstream faults at a gateway, and 503 with Retry-After when the service is temporarily unavailable.

### 3.6 Establishing and inspecting TLS

1. Resolve the host name and connect to port 443.
2. Send the ClientHello with the server name indication set to the host being requested, which is essential on a server hosting many sites.
3. Receive the server's flight: parameters, certificate chain, and proof of key possession.
4. Build and validate the chain against the local trust store, checking names, dates, and constraints.
5. Derive the shared secret from the ephemeral key exchange and verify the Finished messages.
6. Confirm the negotiated protocol with the application protocol negotiation extension, which is how a browser and server agree on HTTP/2 rather than HTTP/1.1.
7. Exchange application data under the negotiated authenticated cipher.

### 3.7 Establishing and scoping a session

1. Authenticate the client over TLS with a credential in the request body.
2. Generate a session identifier with a cryptographically secure random source, long enough that guessing is infeasible.
3. Store the server-side state keyed by that identifier, with an expiry.
4. Send the identifier in a Set-Cookie header with Secure, HttpOnly, SameSite set appropriately, a narrow Path, and a bounded lifetime.
5. On later requests, read the Cookie header, look up the session, and reject the request with 401 if the session is absent or expired.
6. On logout, delete the server-side state and expire the cookie by setting Max-Age to zero.

### 3.8 Diagnosing with command-line clients

A verbose request shows the request line, the response status, the headers in both directions, and the TLS summary. That single view answers most questions: which method was sent, which address was used, whether the connection was reused, which cipher was negotiated, and which status came back. When a body is involved, printing the response headers alongside the body separates a payload problem from a protocol problem.

## 4. Worked Implementation from the Notes

### 4.1 Task: conduct a raw HTTP conversation by hand

### 4.2 Implementation: write the request octets directly to a socket

Step 1. Open a plain connection to the server on port 80.

```bash
telnet shop.example.com 80
```

Step 2. Type the request exactly, ending the header section with an empty line.

```http
GET /catalog/items?category=books HTTP/1.1
Host: shop.example.com
Connection: close
```

Step 3. Observe the reply.

```http
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:15:22 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 18432
Connection: close
```

Step 4. Explain what this proves. The request line named the method, the origin-form target, and the version. The Host header told the server which site was wanted. The response echoed a status line and headers, and because Connection was close, the server ended the stream after the body, which is how the body length was delimited in the absence of ambiguity. Writing the message by hand removes every abstraction: there is no accept header, no caching, and no automatic redirect handling.

Step 5. Repeat with a missing Host header. The server answers `400 Bad Request`, which demonstrates that Host is mandatory in HTTP/1.1 and not an optional convenience.

### 4.3 Task: observe chunked transfer coding

### 4.4 Implementation: a response whose length is unknown in advance

Step 1. Request a page that is generated as it is produced.

```bash
curl -i --http1.1 https://shop.example.com/catalog/stream
```

Step 2. Read the framing.

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked

f
<!DOCTYPE html>
26
<html><head><title>Shop</title></head>
23
<body><h1>Items</h1></body></html>
0

```

Step 3. Decode the sizes. The first size line reads `f`, which is fifteen octets, matching the fifteen characters of the doctype declaration. The second reads `26`, which is thirty-eight octets. The third reads `23`, which is thirty-five octets. The final zero-length chunk marks the end of the message, and the empty line after it is the empty trailer section.

Step 4. State the advantage. The server could begin transmitting the head of the page before the database query that fills the body had finished. With Content-Length it would have to buffer the whole page first.

### 4.5 Task: turn a full transfer into a validation

### 4.6 Implementation: ETag round trip

Step 1. Fetch the resource and record its validator.

```bash
curl -s -D headers1.txt -o page1.html https://shop.example.com/catalog/items
grep -i etag headers1.txt
```

Step 2. The output is a tag such as `ETag: "7d3f9a1c-4800"`. The quoted string is opaque; a client must not parse it.

Step 3. Send it back on the next request.

```bash
curl -s -D headers2.txt -o page2.html \
  -H 'If-None-Match: "7d3f9a1c-4800"' \
  https://shop.example.com/catalog/items
head -n 1 headers2.txt
```

Step 4. The first line reads `HTTP/1.1 304 Not Modified`, and `page2.html` is empty. The client keeps its cached copy. This is the mechanism that makes a return visit cheap: the server compared two short strings instead of sending eighteen kilobytes.

Step 5. Change the resource, then repeat. The tag changes, the server answers 200 with a body, and the cache is replaced. A tag that never changes would be a defect, because clients would serve stale content for ever.

### 4.7 Task: read a TLS 1.3 handshake

### 4.8 Implementation: verbose client output

Step 1. Request the page with transport detail.

```bash
curl -v -o /dev/null https://shop.example.com/catalog/items
```

Step 2. Read the connection section.

```text
* Connected to shop.example.com (203.0.113.10) port 443
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN: server accepted h2
```

Step 3. Map the lines to the handshake sequence. The client hello carries the key share. The server hello completes the key agreement in one round trip. The encrypted extensions carry the application protocol choice. The certificate message carries the chain. The certificate verify message proves possession of the private key by signing the transcript. The finished messages prove that both sides derived identical keys. The cipher line names an authenticated symmetric cipher, and the application protocol line shows the connection will carry HTTP/2.

Step 4. Note what is absent compared with TLS 1.2: there is no ServerKeyExchange, no ClientKeyExchange, and no ChangeCipherSpec in the modern sense, because the key share travelled in the hello messages.

### 4.9 Task: verify the certificate chain

### 4.10 Implementation: read the chain and check it

Step 1. Print the chain the server presents.

```bash
openssl s_client -connect shop.example.com:443 -servername shop.example.com </dev/null 2>/dev/null | head -n 12
```

Step 2. Read representative output.

```text
CONNECTED(00000003)
depth=2 C = US, O = Example Trust Services, CN = Example Trust Root CA
verify return:1
depth=1 C = US, O = Example Trust Services, CN = Example Trust RSA CA 2024
verify return:1
depth=0 CN = shop.example.com
verify return:1
---
Certificate chain
 0 s:CN = shop.example.com
   i:C = US, O = Example Trust Services, CN = Example Trust RSA CA 2024
 1 s:C = US, O = Example Trust Services, CN = Example Trust RSA CA 2024
   i:C = US, O = Example Trust Services, CN = Example Trust Root CA
```

Step 3. Interpret the depths. Depth zero is the leaf, issued for the site. Depth one is the intermediate that signed the leaf. Depth two is the root, which the client already trusts, so the chain terminates. Each `verify return:1` line means that step of the chain check succeeded.

Step 4. Inspect the leaf's names and dates.

```bash
openssl s_client -connect shop.example.com:443 -servername shop.example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

Step 5. A representative result shows `subject=CN = shop.example.com`, an issuer matching the intermediate, a validity window of roughly one year, and a subject alternative name extension listing both the bare host and the `www` form. A browser requesting either name succeeds; a request for a name absent from that list would fail even if the certificate were otherwise valid, which is precisely the check that defeats impersonation.

Step 6. Demonstrate the failure mode by connecting with a mismatched server name and observe the verification error. The handshake may complete cryptographically, but the client refuses to trust it, which shows that encryption without name validation is worthless.

### 4.11 Task: set a scoped and hardened cookie

### 4.12 Implementation: choose every attribute deliberately

Step 1. Set the cookie from the login response.

```http
HTTP/1.1 200 OK
Set-Cookie: session_id=8f21c9d4e77a; Domain=shop.example.com; Path=/; Max-Age=3600; Secure; HttpOnly; SameSite=Lax
Content-Type: application/json
Content-Length: 29

{"status": "signed in"}
```

Step 2. Justify each attribute. Secure keeps the value off plain connections. HttpOnly keeps it away from scripts. SameSite=Lax keeps it off cross-site form posts. Path narrows the scope. Max-Age bounds the exposure to one hour. Domain allows the value to be shared with the checkout subdomain, which is a deliberate trade of exposure for convenience and would be omitted if the subdomain did not need it.

Step 3. Observe the return path: the next request to the same host carries `Cookie: session_id=8f21c9d4e77a`, with no attributes, because only the pair is returned.

Step 4. Observe the scope boundary. A request to `https://other.example.net/` carries nothing, because the domain does not match. A request to `https://shop.example.com/orders` carries the cookie. A request to `https://shop.example.com.evil.example/` carries nothing, because the domain must match as a suffix on a label boundary and the attacker's host only resembles the name.

Step 5. Expire it deliberately on logout by returning the same name with an empty value and Max-Age zero, then delete the server-side record so the identifier cannot be replayed even if a copy was stolen.

### 4.13 Task: prove connection reuse

### 4.14 Implementation: two requests, one connection

Step 1. Request two resources on the same host in one invocation.

```bash
curl -v -o /dev/null https://shop.example.com/a -o /dev/null https://shop.example.com/b
```

Step 2. In the verbose output the second request is preceded by a line stating that the existing connection is being reused, and no second TLS handshake appears.

Step 3. Explain the saving. The second request avoided the name lookup, the transport handshake, and the key agreement. On a link with a hundred milliseconds of round-trip delay that is several hundred milliseconds saved for a single small resource, and the saving repeats for every resource on the page.

Step 4. Force the opposite behaviour with `Connection: close` in the request and observe a fresh handshake for the second request. This demonstrates that persistence is a negotiated property rather than a fixed one.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Tests of understanding

- Write a request and a response from memory with correct line terminators, and explain the significance of the empty line.
- Explain why Content-Length and Transfer-Encoding together constitute a security problem rather than a redundancy.
- Justify the classification of all seven methods on the two axes of safety and idempotence, and give a case where retrying a `POST` would create a duplicate order.
- Explain the difference between 301, 302, 303, 307, and 308 in terms of permanence and method preservation.
- Explain why a 304 response has no body and why that is a success.
- Trace a TLS 1.3 handshake from ClientHello to Finished, naming what each flight proves.
- Describe certificate validation as an ordered list and say what fails at each step.
- Explain why the bulk of the traffic uses symmetric encryption, using cost, capacity, and integrity as the three arguments.
- State the effect of Secure, HttpOnly, SameSite, Domain, Path, and Expires on a cookie, and give the attack each mitigates.
- Explain how persistence reduces latency and what problem it introduces.

### 5.2 Interpreting traces correctly

A status line is the first thing to read and the last thing to trust on its own. A 200 with an empty body is a successful request that returned nothing useful, which is often a defect in the application rather than in the protocol. A 200 with a page that says "not found" is an application that chose the wrong code, and clients will treat it as success. A 302 that points to the same address is a redirect loop, and a browser will stop after a small number of hops.

A missing header is as informative as a wrong one. A response without Cache-Control may be cached heuristically by an intermediary, which is how private data ends up in a shared cache. A response without Vary on a negotiated resource may be served in the wrong format to the wrong client. A request without Content-Type on a body may be rejected as unsupported or, worse, parsed by guessing.

### 5.3 Symptom to cause

| Symptom | Likely cause | Check |
|---|---|---|
| 400 on a request that looks correct | Missing or duplicated Host, malformed target | Print the raw request line and headers |
| 401 despite correct password | Credential not sent, or challenge scheme mismatch | Inspect Authorization and WWW-Authenticate |
| 403 with valid credentials | Authorisation rule refuses the action | Compare role or scope with the rule |
| 405 on a valid address | Wrong method for the resource | Read the Allow header |
| 301 chain that never ends | Canonical host rule conflicting with proxy | Follow each hop and compare hosts |
| 304 with old content | Validator not changed when content changed | Compare ETag with the stored version |
| 502 but the backend works | Gateway cannot parse the upstream response | Check upstream framing and timeouts |
| 503 at peak hours | Connection or worker pool exhausted | Check keep-alive timeouts and limits |
| Cookie missing on later request | Domain, Path, SameSite, or Secure mismatch | Inspect the stored cookie and the request scheme |
| Handshake failure with a valid certificate | Name mismatch, expired chain, or incomplete chain | Print the chain and the negotiated server name |

### 5.4 Common errors in rigorous answers

- **Describing HTTP as connection-oriented.** The protocol is stateless and, in HTTP/1.1, uses a persistent connection; the connection is not what makes the protocol stateful, and state is reconstructed per request.
- **Saying idempotent means "no side effects".** That is safety. Idempotence means repeated application produces the same state.
- **Treating 401 and 403 as one code.** They differ in whether identity is established, and the required response headers differ too.
- **Forgetting that a 405 must carry Allow and a 401 must carry a challenge.** The code without its mandatory header is an incomplete answer.
- **Claiming HTTPS encrypts the URL path from the server.** HTTPS protects the message from observers on the path. The server of course sees the request; the host name may also be visible to an observer through the server name indication unless encrypted client hello is in use.
- **Describing the certificate as "the encryption key".** The certificate binds a name to a public key and is signed by an authority. The session keys are derived from an ephemeral exchange and are not in the certificate.
- **Saying that TLS uses asymmetric encryption for the whole session.** It uses asymmetric cryptography to authenticate the server and to agree a shared secret, then symmetric encryption for everything else.
- **Assuming a cookie is secure because the site uses HTTPS.** The Secure attribute governs the cookie; a session identifier also needs HttpOnly and an appropriate SameSite value, and it must be unguessable.
- **Assuming keep-alive is unlimited.** Idle timeouts, maximum requests per connection, and proxy behaviour all close connections, and a client must be prepared to reconnect at any time.
- **Ignoring message framing.** A response without Content-Length, Transfer-Encoding, or a closing connection is ambiguous, and ambiguity at a boundary is a security defect, not a style issue.

### 5.5 Trade-offs to state in a conclusion

Every mechanism here buys something and costs something, and a conclusion that says so is stronger than a list. Statelessness buys scale and costs a session store. Persistence buys latency and costs connection slots and head-of-line blocking. Caching buys bandwidth and costs freshness, which is why validation exists. Chunked encoding buys streaming and costs framing complexity. Asymmetric cryptography buys key distribution and costs compute, which is why it is confined to the handshake. Cookies buy continuity and cost privacy, which is why their scope attributes matter. Naming names these trade-offs, rather than describing the protocol as a set of features, is what separates a strong answer from a summary.
