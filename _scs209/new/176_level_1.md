## 1. Concept and Use Case

### 1.1 An everyday picture of the web

Imagine a city where every building has a mail slot, and every piece of information in the city lives in a labelled drawer inside one of those buildings. To obtain a document you post a card through a slot. On the card you write the building's name, the floor, the cabinet, and the exact sheet you want, and you add a very short instruction such as "send me a copy", "replace this sheet with the one I am enclosing", or "just tell me whether this sheet still exists". A clerk inside the building reads the card, does what the card asks, and posts back a reply card. The first line of the reply card is a three-digit code: two hundred means "done, here is your copy", four hundred and four means "there is no such sheet", five hundred means "our filing room has broken, please come back later". The clerk keeps no memory of you. Every card must carry every instruction needed, because the clerk treats each card as if it arrived from a stranger. That is exactly how a busy office works when thousands of visitors post cards every second and nobody has time to remember faces.

That picture is the whole subject of this note with the everyday words replaced by technical ones. The buildings are computers called servers. The cards are messages. The instruction words are called request methods. The three-digit codes are called status codes. The set of rules governing how a card must be laid out, what each instruction means, and what a reply card must contain is called a protocol, and the protocol used by the web is the Hypertext Transfer Protocol, shortened to HTTP. The address written on the card is a Uniform Resource Locator, shortened to URL. The general idea that any resource on the web can be named by such an address is a Uniform Resource Identifier, shortened to URI. When the mail slot is protected by a guard who checks identity badges and seals every card in a tamper-evident envelope, the protocol is called HTTP Secure, written HTTPS.

### 1.2 Why the picture matters more than the definitions

Most students can recite that HTTP stands for Hypertext Transfer Protocol. Far fewer can explain what that name commits the protocol to. The word "hypertext" refers to text that contains links to other text, which is what a web page is: a document where certain words point at other documents. The word "transfer" refers to the job of moving a copy of that document from the machine that holds it to the machine that asked for it. The word "protocol" refers to an agreed set of rules that both sides follow so that a message written by one side can be understood by the other. Put together, the name says: this is the agreed way to move linked documents from a holder to a requester.

The picture also explains why the web scales. Because the clerk remembers nothing, any clerk can serve any card. A large site can put a thousand identical clerks behind a single address and send each incoming card to whichever clerk is free. If the protocol required the clerk to remember the previous conversation, that flexibility would disappear.

The picture explains the two roles. The program that sends the card is the client, usually a web browser. The program that receives the card and produces the reply is the server. A single exchange consists of one request and one response. Everything else in this topic is detail about those two messages: how the address in the request is built, which instruction word is used, which code comes back, what extra labels travel with the message, and how the reply is protected in transit.

### 1.3 The address is the interesting part

A postal address is hierarchical for a reason. "Flat 4, Rose Court, Ngong Road, Nairobi" narrows from the smallest unit to the largest, so a postal worker can route the letter one step at a time without knowing the whole city. A web address works the same way in reverse: it narrows from the largest unit to the smallest. The scheme says which protocol to speak. The host says which machine to speak to. The optional port says which service on that machine. The path says which resource on that service. An optional query adds parameters, and an optional fragment points at a place inside the resource.

That hierarchy is why one server can hold millions of pages and still answer correctly. The server reads the path, looks up the resource it names, and returns it. Two pages on the same site differ only in their paths, so the same machine and the same protocol serve both.

The hierarchy is also why a web address is more than a machine name. The machine name alone identifies a computer; the full address identifies a document on that computer. This distinction is the reason a URI is described as a naming scheme for resources, not merely a way of finding computers.

### 1.4 What the reply code buys you

A three-digit code is a compact contract. The first digit places the reply in a family, and the family tells the client what kind of action is appropriate. A code beginning with two means the request succeeded. A code beginning with three means the resource has moved and the client should look elsewhere. A code beginning with four means the client did something wrong: a bad address, missing credentials, or an instruction the resource does not allow. A code beginning with five means the server failed even though the request was reasonable.

Because the code is short and its meaning is fixed by the protocol, software can act on it without understanding the body of the reply. A browser follows a three-hundred-and-one code automatically. A caching proxy stores a two-hundred reply but not a five-hundred one. A monitoring system raises an alarm on a five-hundred series code without reading a single word of the page. This is the practical value of a standardised code: automation becomes possible.

### 1.5 What the lock in the address bar actually means

When a web address begins with https instead of http, the client and the server first perform a separate negotiation that establishes a protected channel, and only then exchange the ordinary HTTP messages through it. The protection is provided by a family of protocols whose older member is the Secure Sockets Layer, shortened to SSL, and whose current member is Transport Layer Security, shortened to TLS. In everyday speech people still say "SSL certificate" even when the connection uses TLS; the correct term for the modern protocol is TLS.

The padlock in a browser means three things at once, and it is worth separating them. First, the traffic is encrypted, so somebody watching the network cannot read the page or the password. Second, the traffic is integrity-protected, so somebody cannot alter a bank balance in transit without the change being detected. Third, the server proved that it holds a certificate issued for that exact name, so the client is talking to the machine that the domain owner authorised. The padlock does not mean the site is honest, well run, or free of malware. It means the connection is private and the name is vouched for.

### 1.6 Where these ideas appear in practice

Every one of these ideas is used by anybody who builds or operates a website. A developer who adds a search box is choosing a query parameter. A developer who submits a form is choosing between a request that can be repeated safely and one that changes data. A developer who returns a page after a successful creation should return a created code with the new address in a header. An operator who moves a site to a new domain must return a permanent redirect so that search engines update their index. An operator who serves images to a slow connection tunes caching headers. A security engineer who hardens a login flow sets cookie flags that stop scripts from reading the session value.

The topic also underpins the rest of this course. Everything delivered over the web, whether a page written in the Hypertext Markup Language (HTML), an image, a script, or a data file in JavaScript Object Notation (JSON), travels inside these messages. Understanding the envelope is what makes the contents intelligible.

## 2. Data, Syntax, and Core Concepts

### 2.1 A web address, part by part

Take one complete address and examine it slowly:

```text
https://shop.example.com:8443/catalog/items?category=books&page=2#reviews
```

Reading from left to right, the pieces are as follows.

The scheme is `https`. It tells the client which protocol to use and therefore which default port to assume. A scheme is followed by a colon and, for web schemes, two forward slashes.

The authority is `shop.example.com:8443`. It names the machine and, optionally, the service on it. The authority begins after the two slashes and ends at the next slash, question mark, or hash.

The host is `shop.example.com`. This is the name that the Domain Name System, shortened to DNS, converts into an Internet Protocol address, which is the numeric address a computer actually uses. A host may also be written as a numeric address directly.

The port is `8443`. A port is a numbered doorway on a machine, and different services listen at different doorways. If the port is omitted, the client assumes the default for the scheme: 80 for http and 443 for https. Port 8443 is a common choice for an alternative secure service.

The path is `/catalog/items`. It identifies the resource inside that service, in the same way a file path identifies a file inside a directory tree. The path is case sensitive in general.

The query is `category=books&page=2`. It begins at the first question mark and carries data to the server that helps the server decide what to return. It is a sequence of name and value pairs separated by ampersands.

The fragment is `reviews`. It begins at the hash mark and points to a position inside the resource. Browsers use it to scroll to a named element. The fragment is never sent to the server; it is handled entirely by the client.

| Component | Example | Purpose | Sent to server |
|---|---|---|---|
| Scheme | `https` | Chooses the protocol and default port | Yes |
| Authority | `shop.example.com:8443` | Names the machine and service | Yes, as the Host header |
| Host | `shop.example.com` | Domain name resolved by DNS | Yes |
| Port | `8443` | Selects the service on the machine | Yes |
| Path | `/catalog/items` | Names the resource | Yes |
| Query | `category=books&page=2` | Passes parameters to the server | Yes |
| Fragment | `reviews` | Points inside the returned document | No |

### 2.2 URI, URL and URN: three words that are not synonyms

A Uniform Resource Identifier is the general term for any string that identifies a resource. It is the family name. Inside the family there are two practical kinds.

A Uniform Resource Locator identifies a resource by saying where and how to get it. Almost every address typed into a browser is a locator, because it names a scheme, a host, and a path.

A Uniform Resource Name identifies a resource by a persistent name that does not depend on where the resource currently sits. The classic example is a book identifier such as `urn:isbn:9780132350884`, which names a specific book without saying which server holds a copy.

The relationship is therefore one of containment: every locator is an identifier, but not every identifier is a locator. Saying "URL" when the correct word is "URI" is a small error that examiners notice, because a question about the general scheme of naming is not answered by naming only the addressing kind.

There is a second layer of terminology that matters in practice: an absolute reference contains a scheme and is complete, while a relative reference is resolved against a base address. A link written as `/help/faq` inside a page fetched from `https://shop.example.com/catalog/items` resolves to `https://shop.example.com/help/faq`. A link written as `images/shoe.png` resolves relative to the directory of the current document. Relative references keep pages portable, because a site can be moved to a new host name without rewriting every link.

### 2.3 Characters that are not allowed, and what replaces them

Addresses may only contain a restricted set of characters. Letters, digits, the hyphen, the full stop, the underscore, and the tilde are unreserved and may appear as they are. Characters with structural meaning, such as the slash, question mark, hash, and ampersand, may appear only where the syntax expects them. Everything else must be percent-encoded: the character is converted to its byte value in hexadecimal and written after a percent sign.

A space becomes `%20`. A question mark used as data inside a query becomes `%3F`. A non-Latin character is first encoded as bytes in a Unicode transformation format and then each byte is percent-encoded, so a page name in Japanese becomes a long sequence of percent-triplets. This is why the same page can appear in a browser as readable text and in a log file as an unreadable string: the log records the wire form, and the browser displays the decoded form.

Form submission introduces one exception that surprises beginners. In the query string of a form submission encoded as `application/x-www-form-urlencoded`, a space is written as a plus sign rather than `%20`. Both forms are accepted by most servers, but the plus sign is the canonical form for that particular encoding.

### 2.4 The request message, in plain words

A request is a short block of text with a strict shape. The first line names the method, the target, and the protocol version. Then come header fields, one per line, each a name, a colon, and a value. A blank line ends the headers. If the request carries data, as a form submission does, that data follows the blank line.

```http
GET /catalog/items?category=books&page=2 HTTP/1.1
Host: shop.example.com:8443
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-GB,en
Connection: keep-alive
```

The word `GET` is the instruction. It means "send me a copy of the resource identified by the target and change nothing". The target is the path plus the query, without the scheme or host, because the host is supplied separately in the Host header. The version says which revision of HTTP the client speaks.

The response has the same shape with a different first line. It names the version, then the status code, then a short human-readable phrase.

```http
HTTP/1.1 200 OK
Date: Fri, 07 Nov 2026 09:15:22 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 18432
Cache-Control: max-age=300
ETag: "7d3f9a1c"
```

The status line says the request succeeded. The headers describe the body that follows: its media type, its length in bytes, how long it may be cached, and a version tag that lets the client ask later whether anything has changed.

### 2.5 The verbs of the web

The methods are the instruction words. Seven are examined in this course, and each has a precise meaning.

`GET` asks for a copy of a resource. It must not change anything on the server. It is the method used when you type an address or click an ordinary link.

`HEAD` asks for the same response as `GET` but without the body. It is used to check whether a resource exists, how large it is, and when it last changed, without downloading it.

`POST` sends data to the server for processing. It is used for submitting a form, creating a record, or posting a comment. Repeating the same `POST` can create a second record, so it is not a method you can safely repeat.

`PUT` sends a complete replacement for a resource at a known address. Sending the same replacement twice leaves the same result, so repeating it is harmless even though it does change data.

`DELETE` asks the server to remove a resource. Removing something twice produces the same end state, so it is also safe to repeat, although it does change data.

`OPTIONS` asks which methods and capabilities the server supports for a resource. It changes nothing.

`TRACE` asks the server to echo the request back. It is a diagnostic tool that is usually disabled in production because echoing headers can reveal information to an attacker.

Two properties summarise these methods. A method is safe when it does not change server state; safe methods are `GET`, `HEAD`, `OPTIONS`, and `TRACE`. A method is idempotent when repeating it produces the same effect as making it once; all the methods above except `POST` are idempotent. `POST` is neither safe nor idempotent.

### 2.6 The five families of status code

The first digit of a status code names its family. Knowing the family tells you where to look for the fault.

A code in the one hundreds means the server has received part of the request and is inviting the client to continue. The common case is a client that is about to send a large body and has asked permission first.

A code in the two hundreds means success. The request was understood, accepted, and acted on.

A code in the three hundreds means the client must take further action to reach the resource. Usually the resource now lives at another address, and the response carries that address. A permanent move is reported as 301, a temporary one as 302, and the code 304 carries no address at all: it says that the copy the client already holds is still current, so nothing needs to be transferred.

A code in the four hundreds means the request itself is faulty: a malformed address, missing credentials, a resource that does not exist, or a method the resource does not permit. The fault is on the client side.

A code in the five hundreds means the server failed while handling an otherwise valid request. The fault is on the server side, and retrying later may succeed.

| Family | Meaning | Whose fault | Typical examples |
|---|---|---|---|
| 1xx | Informational, continue | Neither | 100 Continue, 101 Switching Protocols |
| 2xx | Success | Neither | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection, further action needed | Neither | 301 Moved Permanently, 302 Found, 304 Not Modified |
| 4xx | Client error | Client | 400, 401, 403, 404, 405 |
| 5xx | Server error | Server | 500, 502, 503 |

### 2.7 Headers are labels around the message

Headers are the labels that travel with the message. They divide into three groups by purpose.

Request headers describe the client and what it wants. The Host header names the site being requested, which is essential because one server may host many sites. The User-Agent header names the browser and operating system. The Accept header lists the media types the client can handle. The Authorization header carries credentials when a resource is protected.

Response headers describe the reply. Content-Type gives the media type of the body, for example `text/html; charset=UTF-8`, so the client knows whether to render a page, display an image, or parse data. The charset parameter inside that value names the character encoding, and UTF-8, which stands for Unicode Transformation Format with eight-bit units, is the usual choice because it can represent almost every writing system. Content-Length gives the body size in bytes. Set-Cookie asks the client to store a small piece of state. Location is used with redirections to give the new address.

General headers apply to both directions. Cache-Control governs caching. Connection controls whether the underlying connection stays open for further requests.

Representation headers describe the body itself: its type, its length, its encoding, and a version tag. The header that carries the version tag is ETag, which stands for entity tag, and it is what lets a client ask later whether anything has changed. This group matters for caching and for content negotiation, in which the client and server agree on a format.

### 2.8 HTTPS, from the outside

HTTPS is not a separate protocol in the sense that FTP is separate from HTTP. It is ordinary HTTP carried inside a protected tunnel. The tunnel is created by TLS, formerly SSL, and it provides three properties: confidentiality, so an observer cannot read the messages; integrity, so an observer cannot modify them undetected; and authentication of the server, so the client knows which machine it reached.

The protection is negotiated in two stages. First the two sides agree on algorithms and exchange enough information to derive a shared secret, using public key techniques so that the secret is never sent in the clear. Then they switch to a fast symmetric cipher, where both sides use the same key, for the bulk of the traffic. The reason for the two stages is speed: public key operations are computationally expensive, while symmetric ciphers handle large volumes cheaply.

The server's identity is carried in a certificate, which is a signed statement binding a domain name to a public key. The signature comes from a certificate authority, an organisation that the client's operating system already trusts. The client checks the signature chain, the validity dates, and the name, and only then accepts the connection.

### 2.9 Cookies, the claim ticket

Because HTTP is stateless, a server that must recognise a returning client hands out a claim ticket. The ticket is a cookie: a small name and value pair that the server sends in a Set-Cookie header and the client stores. On every later request to the same site, the client sends the cookie back in a Cookie header. The server reads the value, looks it up in its own store, and thereby learns who the client is.

A cookie is not a program and cannot read files. It is a string. Its power comes entirely from the server trusting the value, which is why a cookie that holds a session identifier must be protected: it should be sent only over HTTPS, should be hidden from page scripts, and should not be sent along with requests from other sites.

### 2.10 Keeping the connection open

Opening a connection costs time. A connection over the Transmission Control Protocol, which is the reliable transport protocol beneath HTTP, requires a three-step handshake before any data moves. If every request needed a fresh connection, a page with thirty images would pay that cost thirty-one times.

HTTP therefore allows connection persistence. In HTTP/1.1 a connection stays open by default and can carry many requests one after another. When the client is finished, or the server decides the connection has been idle too long, the connection closes. The modern versions of the protocol go further: HTTP/2 carries many requests at once over one connection, and HTTP/3 replaces the underlying transport with a protocol built on datagrams.

## 3. Methods and Operations

### 3.1 Following one request from typing to painting

The sequence below is the ordinary life of a page load. Each step names the component responsible and the evidence it produces.

1. You type an address or click a link. The browser parses the address into scheme, host, port, path, query, and fragment.
2. The browser asks DNS for the numeric address of the host, unless it already holds a cached answer.
3. The browser opens a connection to that address at the port. For HTTPS it then performs the TLS negotiation.
4. The browser writes the request line, the headers, and any body, and sends them.
5. The server reads the request, decides what to do, and writes a status line, headers, and usually a body.
6. The browser interprets the status code. A success code means it renders or stores the body. A redirect code means it repeats the request at the new address. An error code means it shows an error page or retries.
7. The browser requests the sub-resources named in the page, reusing the open connection where possible.
8. When the page is complete, the browser may keep the connection idle for a while before closing it.

### 3.2 Reading a response without downloading it

A single request can answer most questions about a resource if it is a `HEAD` request. The client asks only for the headers, so it learns the status, the media type, the size, the last modification date, and the cache instructions without transferring the body. This is how a link checker verifies thousands of addresses cheaply, and how a download manager discovers the size of a file before starting.

The equivalent at the command line is a request that prints only the response headers. It is the fastest way to see what a server actually says, because it shows the codes and labels with no page content in the way.

### 3.3 Choosing between GET and POST

The choice follows from the meaning, not from convenience.

Use `GET` when the request only reads. Its parameters belong in the query string, which makes the request bookmarkable, shareable, and cacheable. Because a `GET` may be repeated by a proxy or a browser without warning, it must not have side effects.

Use `POST` when the request changes something or when the data is too large or too sensitive for a query string. A password in a query string is written into server logs, browser history, and the referrer field of later requests, which is a serious leak. A body is not recorded in those places.

A useful rule of thumb for revision: if refreshing the page twice should not create two orders, the request must not be a `POST` without protection, and if the request must never be repeated automatically, it must not be a `GET` that changes data.

### 3.4 Choosing the right success code

Returning the correct code is part of designing an interface that other software can use.

A plain read that succeeds returns 200. A creation that succeeds returns 201 and includes a Location header naming the new resource. A deletion or an update that succeeds with nothing to say returns 204 and no body. A partial download returns 206 and states the byte range it covers.

The distinction between 201 and 200 matters because a client that creates a record needs the address of the new record. If the server returns 200 alone, the client must guess the address or make a second request.

### 3.5 Choosing the right error code

The error codes carry information that changes behaviour.

Return 400 when the request cannot be parsed or a parameter is invalid. Return 401 when authentication is required and absent or wrong, and include a challenge header telling the client which scheme to use. Return 403 when the client is authenticated but not permitted. Return 404 when the resource does not exist. Return 405 when the resource exists but does not permit that method, and list the permitted methods in an Allow header. Return 500 when an unexpected failure occurs inside the application. Return 502 when an upstream service returned an invalid answer to a gateway. Return 503 when the service is temporarily unable to handle the request, with a Retry-After header if the delay is known.

The distinction between 401 and 403 is the one most often lost. A 401 says "I do not know who you are"; a 403 says "I know who you are and you may not do this".

### 3.6 Setting a cookie correctly

A cookie is set with a single response header and is sent back automatically on later requests. Setting one properly requires more than a name and a value.

```http
Set-Cookie: session_id=8f21c9d4; Path=/; Max-Age=3600; Secure; HttpOnly; SameSite=Lax
```

The `Secure` attribute restricts the cookie to HTTPS connections. The `HttpOnly` attribute hides it from page scripts. `SameSite=Lax` stops it being sent with most cross-site requests, which blunts cross-site request forgery. `Path=/` makes it apply to the whole site, and `Max-Age=3600` expires it after one hour.

A session cookie that omits `Secure` and `HttpOnly` is a common and serious defect, because a single cross-site scripting flaw then exposes the session to theft.

### 3.7 Deciding what may be cached

Caching is controlled by headers, and the defaults are not always safe. A response that contains a bank balance must not be stored anywhere, so it should carry `Cache-Control: no-store`. A response that may be reused briefly by anyone should carry `public, max-age=60`. A response that is specific to one user should carry `private, max-age=60`, which permits the browser to store it but forbids shared caches from doing so.

A response with a version tag can additionally be validated rather than re-downloaded. The client sends the tag it holds, and the server replies with 304 Not Modified and no body if nothing has changed.

### 3.8 A procedure for debugging any web problem

1. Identify the exact address involved, including the query string, and check it character by character.
2. Determine the status code. The family alone usually locates the fault.
3. If the code is a redirect, follow the chain and look for a loop.
4. If the code is 401 or 403, examine the Authorization header and the credential.
5. If the code is 404 or 405, compare the method and path with what the server expects.
6. If the code is 500, 502, or 503, look at server logs and at upstream health.
7. If the code is 200 but the page is wrong, the fault is in content negotiation, caching, or the body itself, not in the protocol.

## 4. Worked Implementation from the Notes

### 4.1 Task: inspect the headers of a page without downloading it

### 4.2 Implementation: a HEAD request from the command line

Step 1. Ask the server for the response headers only.

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
ETag: "7d3f9a1c"
Vary: Accept-Encoding
```

Step 3. Interpret each line. The status line confirms success. The media type says the body is HTML in the UTF-8 character encoding, which is why the browser renders it rather than downloading it. The length gives the size, which is what a link checker or download manager needs. The cache directive allows any cache to keep the response for five minutes. The version tag will let the client validate the copy later. The Vary header warns caches that the response depends on the encoding the client asked for.

Step 4. Confirm that nothing was downloaded. The command printed only headers, so no page content crossed the network. This is the practical difference between `HEAD` and `GET`, and it is why link checkers use `HEAD`.

### 4.3 Task: observe a permanent redirect

### 4.4 Implementation: follow the chain and read the Location header

Step 1. Request the old address without following redirections.

```bash
curl -i https://shop.example.com/catalogue
```

Step 2. Read representative output.

```http
HTTP/1.1 301 Moved Permanently
Date: Fri, 07 Nov 2026 09:15:24 GMT
Location: https://shop.example.com/catalog
Content-Length: 0
```

Step 3. Explain the effect. The 301 tells every client, cache, and search engine that the resource has moved for good, so a client may update its bookmark and a search engine may transfer ranking to the new address. The Location header carries the new address; without it the client would have nowhere to go.

Step 4. Verify the target.

```bash
curl -o /dev/null -s -w "%{http_code}\n" -L https://shop.example.com/catalogue
```

The output is `200`, which shows that following the redirect chain ends at a working page. The `-L` option makes the client follow redirections; without it the code reported would be 301.

### 4.5 Task: create a record with POST and read the created code

### 4.6 Implementation: send JSON and inspect the result

Step 1. Send the request with the correct media type.

```bash
curl -i -X POST https://shop.example.com/api/items \
  -H "Content-Type: application/json" \
  -d '{"title":"Canvas tote bag","price":1800}'
```

Step 2. Read representative output.

```http
HTTP/1.1 201 Created
Date: Fri, 07 Nov 2026 09:16:02 GMT
Location: https://shop.example.com/api/items/9042
Content-Type: application/json
Content-Length: 62

{"id": 9042, "title": "Canvas tote bag", "price": 1800}
```

Step 3. Explain why 201 is correct rather than 200. A new resource came into existence, so the client needs its address, which the Location header supplies. The body repeats the created record, which saves the client a second request.

Step 4. Repeat the same command. A second record with a new identifier appears, which demonstrates concretely that `POST` is not idempotent: two identical requests produced two different resources.

### 4.7 Task: demonstrate that GET is safe and can be repeated

### 4.8 Implementation: issue the same read twice and compare

Step 1. Read the newly created record twice.

```bash
curl -s https://shop.example.com/api/items/9042
curl -s https://shop.example.com/api/items/9042
```

Step 2. Both calls return the same body. Nothing was created, nothing changed, and the second call had no additional effect. This is what safety means: the request is a read.

Step 3. State the design consequence. Because a `GET` is safe and idempotent, a browser may prefetch a link, a proxy may serve it from cache, and a retry after a dropped connection is harmless.

### 4.9 Task: keep a session across requests with a cookie

### 4.10 Implementation: log in, store the cookie, reuse it

Step 1. Send credentials and store any cookie that comes back.

```bash
curl -i -c cookies.txt -X POST https://shop.example.com/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"amina@example.com","password":"correct-horse-battery"}'
```

Step 2. Read representative output.

```http
HTTP/1.1 200 OK
Set-Cookie: session_id=8f21c9d4e77a; Path=/; Max-Age=3600; Secure; HttpOnly; SameSite=Lax
Content-Type: application/json
Content-Length: 29

{"status": "signed in"}
```

Step 3. Make a request that requires the session, using the stored cookie.

```bash
curl -s -b cookies.txt https://shop.example.com/api/orders
```

Step 4. The orders are returned, which proves the server recognised the client. Then make the same request without the cookie jar.

```bash
curl -i -s https://shop.example.com/api/orders | head -n 1
```

The first line reads `HTTP/1.1 401 Unauthorized`, which proves the endpoint is protected and that the cookie carried the identity. This pair of results is the clearest demonstration that HTTP itself is stateless and that state is reconstructed from a cookie on every request.

### 4.11 Task: examine the certificate protecting a site

### 4.12 Implementation: read the chain and the subject names

Step 1. Connect and print the certificates the server presents.

```bash
openssl s_client -connect shop.example.com:443 -servername shop.example.com -showcerts
```

Step 2. Read the summary lines near the end of the output.

```text
Verify return code: 0 (ok)
```

Step 3. Inspect the leaf certificate's names and dates.

```bash
openssl s_client -connect shop.example.com:443 -servername shop.example.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

Step 4. Read representative output.

```text
subject=CN = shop.example.com
issuer=C = US, O = Example Trust Services, CN = Example Trust RSA CA 2024
notBefore=Mar 18 00:00:00 2026 GMT
notAfter=Mar 18 23:59:59 2027 GMT
X509v3 Subject Alternative Name:
    DNS:shop.example.com, DNS:www.shop.example.com
```

Step 5. Explain what each part proves. The subject and the alternative names show which names the certificate covers, and a browser rejects the connection if the requested name is absent from that list. The issuer shows which authority signed it, and the client must be able to build a chain from that authority to one it already trusts. The dates show the window of validity, and a clock outside that window produces a warning. The verification code of zero means the chain, the dates, and the names all checked out.

## 5. Testing, Interpretation, and Common Errors

### 5.1 A checklist that shows you understand the topic

You have understood this material when you can do each of the following without notes.

- Break any web address into scheme, authority, host, port, path, query, and fragment, and say which parts reach the server.
- Explain the difference between a URI, a URL, and a URN, and give an example of a name that is not a locator.
- Write a request line and a status line from memory, in the correct order and with the correct separators.
- State the meaning of all seven methods and classify each as safe, idempotent, both, or neither.
- Name the five status-code families and give the meaning of each important individual code.
- Explain what each of the headers Host, User-Agent, Accept, Content-Type, Authorization, Cache-Control, and Set-Cookie does.
- Describe why HTTPS uses two kinds of encryption rather than one.
- Explain how a cookie makes a stateless protocol support a login session.
- Explain what connection persistence saves and why it matters for a page with many images.

### 5.2 Beginner misconceptions to unlearn

- **"HTTPS is a different protocol from HTTP."** It is HTTP carried inside a TLS tunnel. The messages are the same; the tunnel is different.
- **"A URL and a URI are the same thing."** A URL is a kind of URI. A URN is another kind. Using the words interchangeably hides the distinction the examiner is testing.
- **"The fragment is sent to the server."** It is not. The browser strips it before sending and uses it locally after the response arrives.
- **"GET is the safe method and POST is the unsafe one."** "Safe" has a technical meaning: it means no change to server state. `POST` is unsafe because it changes state, but `PUT` and `DELETE` are equally unsafe and are nevertheless idempotent, which `POST` is not.
- **"A 404 means the server is down."** A 404 means the server is working and the resource is not there. A server that is down produces no response at all, or a 502 or 503 from a gateway in front of it.
- **"401 and 403 are interchangeable."** A 401 means credentials are missing or wrong. A 403 means the credentials are fine and the action is still forbidden.
- **"A padlock means the site can be trusted."** The padlock means the connection is encrypted and the domain is verified. Phishing sites obtain certificates for their own domains quite legally.
- **"Cookies are programs."** A cookie is a short string. It cannot execute; only the server's interpretation of it has effects.
- **"The default port is 8080."** The defaults are 80 for http and 443 for https. Port 8080 is a common alternative for development, not a default.
- **"A 304 means the page is missing."** A 304 means the cached copy is still valid, so the client should reuse it. It is a success in effect, not an error.
- **"Redirects are always harmless."** A redirect chain that loops produces a failure, and a redirect that silently downgrades https to http destroys the protection the user believes they have.

### 5.3 How to test your own understanding

A short practical exercise tests almost everything at once. Choose any site, open the developer tools, and record one request and its response. Then answer: which method was used and why; which status code came back and what family it belongs to; which headers described the body; whether a cookie was set and with which attributes; whether the connection was reused for the next request; and whether the response could have been cached.

If all seven answers are available from the recording, the protocol is understood at working level.

### 5.4 Interpreting what you see

Two habits prevent most wrong conclusions. The first is to read the status code before reading the body, because a page that looks like a normal site may have arrived with a 404 status and a friendly error page. The second is to distinguish the address in the address bar from the address actually requested, because after a redirect or a form submission they differ, and the difference explains many confusing results.

A third habit is to remember that the browser is an optimising client. It caches, it reuses connections, it prefetches, and it may serve a page from its cache without contacting the server at all. When a change does not appear, the first test is a forced reload, and the second is the cache headers on the response.

### 5.5 The limits worth naming

HTTP carries no guarantee about delivery time. A request may take a second or a minute, and the protocol does not promise a bound; only the transport's behaviour and the server's capacity determine that.

HTTP does not secure anything by itself. Without TLS, every header and every byte of the body crosses the network in the clear, readable by any device on the path.

HTTP does not remember. Every application that needs continuity must build it from cookies, tokens, or server-side sessions, and every such mechanism introduces its own risks.

Finally, HTTP does not describe meaning. A 200 status says the request succeeded, not that the content is correct, current, or honest. Interpretation of the payload is always the application's job.
