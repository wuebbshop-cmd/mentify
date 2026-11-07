## 1. Concept and Use Case

### 1.1 Imagine a library where the books point at each other

Imagine a very large public library with a rule that makes it special: you are never allowed to walk into the stacks yourself. Instead you sit at a reading desk, write a request slip for one item, and hand it to the person at the counter. That person walks away, finds the shelf that holds the item, and brings back exactly what you asked for. If the item is not on their shelves, they either tell you it does not exist or fetch it from a partner library and hand it to you as if it had been there all along.

Now add three refinements. First, every item has a call number that is unique in the whole building, so there is never any doubt about which book you meant. Second, some books are printed in advance and stored on the shelf, while others are compiled fresh at the counter each time somebody asks, so a weather almanac is always up to date and no two readers necessarily receive the same pages. Third, and most importantly, the margins of every book are full of notes that say "for this idea, see also the book on page 412 of shelf Q". A reader can therefore abandon the order the author intended and follow their own curiosity from shelf to shelf, arriving at a topic through whichever route interests them.

That library is a service built out of three parts: a person who asks, a desk that answers, and a shared convention about how requests are written and how answers are returned. Once those three parts exist, it stops mattering where the shelves are or who owns the building. A reader in one town can use the catalogue of a library in another town through the same desk, the same slip, and the same margin notes.

### 1.2 What the analogy keeps and what it leaves out

The library story captures the shape of the World Wide Web almost completely. The reading desk is the **client**, the counter staff with access to the shelves are the **server**, the request slip is a **web address**, the margin note is a **hyperlink**, and the rule that every request is written the same way and every answer comes back in the same wrappers is the **protocol**. The library catalogue that turns a title into a shelf location plays the part of the **Domain Name System**.

Two things the analogy hides are worth naming now, because both matter later. The first is speed: a real library trip takes minutes, whereas a web request from a laptop to a server on the same continent usually completes in tens of milliseconds, so people click without thinking about cost. The second is scale: the library has one counter, while a popular website is answered simultaneously by many machines, some of them holding copies of the same static pages, so the reader never notices that they were served from a different building.

### 1.3 A working definition of the World Wide Web

The World Wide Web is a collection of documents and other resources that are identified by addresses, linked to one another, and delivered over the Internet using a shared request-and-response protocol. Three properties are doing the work in that sentence, and each can be tested separately.

The first property is **addressing**. Every resource has a uniform locator, so a page, an image, a video clip, a style sheet and a downloadable file can all be named in the same way. The second property is **linking**. Documents carry references to other documents, and the reader can follow those references without knowing the address in advance. The third property is **transport over the Internet**, which means the Web does not build its own cables or its own routing; it borrows the global network and sends messages across it.

A stricter, engineering definition is that the World Wide Web is the set of all resources and users that communicate using the Hypertext Transfer Protocol. A broader definition, offered by the World Wide Web Consortium, the standards body that grew out of the project, describes the Web as the universe of network-accessible information and an embodiment of human knowledge. Both definitions are correct at different levels of abstraction, and an examination answer that gives only one of them is incomplete but not wrong.

It is important to keep the Web separate from the Internet. The Internet is the transport system: cables, routers, addresses and the Internet Protocol. The Web is one service that runs on top of it. Electronic mail, file transfer, remote login and name resolution all work over the Internet without involving the Web at all, and they existed before the Web did. The relationship is best stated as: the Web is a service delivered over the Internet, not a second name for it.

### 1.4 The client and the server

A **client** is the program that asks for something. In ordinary use the client is a **web browser**, such as Chrome, Firefox, Safari, Edge or Opera, running on a personal computer, a phone or a tablet. A **server** is the program, and usually the dedicated machine, that waits for requests and answers them. The server holds the files or the logic needed to build an answer, and it stays reachable so that clients can find it at any hour.

The arrangement is called the **client-server model**. Its key features are easy to list. The client always starts the conversation; the server never telephones a browser out of the blue. The server is passive until a request arrives, and one server answers many clients, often thousands at once. The exchange is normally **stateless**, meaning the server does not automatically remember the previous request, so each request has to carry enough information on its own. The server identifies what is being asked for by the path in the address, and it identifies which service is wanted by the **port number** attached to the address.

This division of labour is not an accident of history; it is what makes the Web cheap to operate and easy to extend. Because the client is responsible for presentation and the server is responsible for content, a new browser can be released without changing any server, and a server can be upgraded without changing any browser. Both sides only need to agree on the messages that pass between them.

### 1.5 How the architecture evolved

The first version of the Web was deliberately minimal. A client asked for a file by name, and a server returned that file as **Hypertext Markup Language**, which is a text format that can carry links. Nothing else was possible: there was no way to send data from the browser to the server, no way to say what kind of data the browser preferred, and no way to describe images inside the page. This early arrangement is usually called the basic web model, and it is still the mental picture that most people have of the Web.

The second version added the missing pieces. The browser could now **post** data back to the server, so a form could be submitted and a search phrase could be sent. The body of a message could hold any format, from plain text to binary data, and the request could declare which formats the browser was able to accept. This is the interactive web model, and it turned the Web from a publishing system into an application platform.

Everything since has been an extension of that second model rather than a replacement of it. Servers gained the ability to run programs that generate a page on demand, which is how a bank statement or a shopping basket can be different for every visitor. Browsers gained the ability to run programs themselves, which is how a page can respond to a click without asking the server again. The protocol gained encryption, which is how a padlock appears next to an address, and it gained more efficient ways of carrying many requests over one connection. Through all of these changes the underlying shape has remained the same: a client asks, a server answers, and both sides follow an agreed format.

### 1.6 Where this shows up in practice

Every time a page loads, the whole architecture is exercised. Typing an address into the bar triggers a name lookup, then a connection, then a request, then a response, then the assembly of a page out of a dozen separate files. Clicking a link repeats the request half of that sequence. Submitting a form adds the posting direction. Signing in adds state, which has to be carried in a small piece of data because the protocol itself does not remember anything.

The practical use cases that follow from the architecture are the ones that matter in practice: publishing information so that it can be read anywhere, building interactive services such as banking and shopping, distributing media, and integrating systems so that one program can call another over the same protocol. Understanding the parts and their responsibilities is what allows a person to diagnose a slow page, a broken form, or a site that works in one browser and not another.

## 2. Data, Syntax, and Core Concepts

### 2.1 Three ingredients: an address, a protocol, and a markup language

The Web is built from three ingredients that fit together so neatly that they are often mistaken for one thing. The **address** says what you want. The **protocol** says how to ask for it and how the answer will be packaged. The **markup language** says how the answer is written so that a browser can present it.

The address family is called **Uniform Resource Identifiers**, usually shortened to URIs. A URI is any string that names a resource unambiguously. The most familiar kind is the **Uniform Resource Locator**, or URL, which names a resource by saying where to find it. A URL for a page might read `https://coffee.example/beans.html`. Reading it from left to right: `https` is the scheme, which names the protocol; `coffee.example` is the host, which names the machine; `/beans.html` is the path, which names the file on that machine.

The protocol is the **Hypertext Transfer Protocol**, or HTTP. It defines a small vocabulary of request methods, a set of headers that describe the message, a status code that summarises the outcome, and rules about how the body is delimited. It is a text-based protocol, which is why a request can be read by a human without special tools.

The markup language is **Hypertext Markup Language**, or HTML. It is a way of writing a document as a tree of elements, some of which are links. A browser reads the markup and turns it into the structures it needs in order to draw the page. The other presentation language, **Cascading Style Sheets**, or CSS, describes appearance, and **JavaScript** describes behaviour. Together these three languages are what a browser actually consumes.

### 2.2 Reading a web address properly

A full URL has more parts than most people realise, and knowing them prevents a great deal of confusion.

The **scheme** comes first, followed by a colon and two slashes. It tells the client which protocol to speak. `http` means plain Hypertext Transfer Protocol on port 80 by default; `https` means the secure form, Hypertext Transfer Protocol Secure, which is HTTP protected by **Transport Layer Security**, or TLS, on port 443 by default. Other schemes appear in links as well: `mailto` opens a mail program, `ftp` uses the File Transfer Protocol, and `file` refers to a local file that never travels over the network.

The **host** comes next. It is a name such as `coffee.example`, and it must be translated into an **Internet Protocol** address, or IP address, before a connection can be made. That translation is the job of the **Domain Name System**, or DNS, which is a global directory service. Numbers may be used in place of a name, but names are preferred because they can be moved to a different machine without changing the published address.

An optional **port** may follow the host after a colon, as in `coffee.example:8080`. Ports allow one machine to run several services at once, each listening on a different number. Well-known ports are fixed by convention: 80 for HTTP, 443 for HTTPS, 25 for mail transfer, 53 for name service, 22 for secure remote login, 21 for file transfer.

The **path** identifies the resource inside the site, and an optional **query string** after a question mark carries data, as in `/search?q=beans`. A **fragment** after a hash mark, as in `/beans.html#single-origin`, names a place inside the document. The fragment never reaches the server; the browser uses it to scroll to the right spot after the page has arrived.

### 2.3 Hypertext, hypermedia and non-linear navigation

**Hypertext** is text that contains references to other text, where the reference can be followed immediately. The idea is older than the Web: it was proposed in the 1940s as a way of organising knowledge by association rather than by shelf order, and it was named in the 1960s. **Hypermedia** is the same idea extended to media other than text, so a page may link to an image, a sound recording or a video.

The consequence for the reader is **non-linear navigation**. A printed book imposes one order: page one, then page two. A hypertext document imposes no order at all beyond the ones its author suggests with links. A reader can begin at a definition, jump to an example, follow a citation to a related topic, and return by pressing the back button. Learning is driven by association and curiosity rather than by sequence, which is the property that makes browsing feel natural and also the property that makes it easy to lose track of where you are.

Links come in a few recognisable forms. An **internal link** points to another page on the same site; an **external link** points to a different site. A **relative link** such as `beans.html` is interpreted against the address of the current page, so the whole site can be moved to a different host without rewriting every link. An **absolute link** carries the full address and therefore keeps working regardless of where the page itself lives. A **fragment link** points to a named place inside a document. A **mail link** starts an email to an address rather than fetching a page.

Non-linear structure has costs as well as benefits. Because there is no single path through the material, a reader may become disoriented, a problem often described as being lost in hyperspace. Because any page can be reached from anywhere, authors must repeat context or risk being misread. And because links can rot, a page that was correct when written may point at nothing a year later. Good sites therefore use consistent navigation, breadcrumb trails and descriptive link text, all of which are attempts to restore a sense of place inside a deliberately placeless medium.

### 2.4 The basic web model

The simplest description of the Web has five parts. The **client** is the user's window onto the network. The **address** identifies the resource. The **server** holds or can obtain the resource. The **protocol** carries the request and the response. The **markup** describes what comes back.

In this model information flows in one direction. The client asks, and the server answers with a document. The server cannot ask the client for anything. There is no way to submit a form, and there is no way to express a preference for one data format over another. The connection is stateless, so the server treats every request as if it had never seen this client before.

This model corresponds to the first published versions of HTTP and HTML, and it is worth understanding even though it is obsolete as a description of real sites, because every later development is an addition to it rather than a departure from it. When you load a page today, the first exchange is still exactly this: one request for one document, followed by one response containing markup.

### 2.5 The interactive web model

The interactive model makes three additions. First, the client can send data as well as request it, so a form submission, a comment, a file upload or a search phrase can travel from browser to server. Second, the body of a message can be any format, so a response may be an image, a document, a data record or a stream rather than only markup. Third, the client can state what it is able to accept, so the server can choose an appropriate representation.

The result is a general resource exchange system rather than a document delivery system. The protocol no longer cares what the payload means; it only carries it. That is why the same mechanism serves a web page, a photograph, a calendar feed and a software download. It is also why the protocol can wrap messages from older services, which is how a proxy server can relay several different protocols through one HTTP conversation.

The interactive model also introduces the possibility of a server acting as a client. If one server needs a resource held by another, it can issue a request of its own and pass the answer back to the original client. This chain of intermediaries is what allows caching layers, load balancers and content delivery networks to exist without the browser knowing anything about them.

### 2.6 What a browser is made of

A browser looks like a single program but is really several cooperating parts. Naming them separately makes it possible to explain why two browsers can display the same page differently.

The **user interface** is everything you can click or type into except the page itself: the address bar, the back and forward buttons, the tabs, the bookmark menu, the download list and the settings screens. Its job is to translate human intentions into commands for the rest of the program.

The **browser engine** is the coordinator. It receives a command such as "go to this address", arranges for the network layer to fetch the document, keeps the history and the session, decides when to load a page from cache, and hands the resulting content to the rendering component. It is the part that knows about navigation and about the browser as an application.

The **rendering engine** is the part that turns markup and style into pixels. It parses the HTML into a tree of elements, parses the CSS into a description of appearance, combines the two, computes the position and size of every box, and paints the result. Different browsers use different rendering engines, and small differences in interpretation are the usual cause of a layout that works in one browser and not another.

The **networking component** speaks HTTP and HTTPS, performs the name lookup, opens the connection and handles encryption. The **JavaScript engine** executes scripts. The **user interface backend** draws the standard widgets such as drop-down lists and dialog boxes. The **storage layer** keeps data on disk: the cache of downloaded files, cookies, saved passwords, browsing history, and the storage areas that scripts are allowed to use.

That last part deserves emphasis because beginners often assume a browser forgets everything when closed. It does not. A browser keeps a **cache** so that returning to a page does not require downloading everything again, **cookies** so that a site can recognise a returning visitor, **local storage** for larger pieces of data that should survive a restart, and **session storage** for data that should disappear when the tab closes. All of it is governed by rules that stop one site reading another site's data.

### 2.7 The browsers you will meet

Five browsers account for almost all ordinary use, and each is built on one of three rendering engines. Getting the pairings right matters, because examination questions ask for them and because a developer needs to know which engine a bug report refers to.

**Google Chrome** uses the Blink rendering engine and the V8 JavaScript engine. Blink began as a fork of Apple's WebKit and has been independent since 2013. Chrome runs on Windows, macOS, Linux and Android.

**Microsoft Edge** was originally built on an engine called EdgeHTML, but since 2020 it has been built on Chromium, which means Blink and V8. It runs on Windows, macOS, Linux and Android, and on Apple's mobile systems it must use the platform's own engine.

**Mozilla Firefox** uses Gecko and SpiderMonkey. It is developed by the Mozilla Foundation and runs on all the major desktop and mobile systems.

**Apple Safari** uses WebKit and JavaScriptCore. It is the default browser on macOS and the only browser engine permitted on iOS and iPadOS, which means that every browser on an iPhone renders pages with WebKit underneath.

**Opera** used its own engine called Presto until 2013 and has used Blink since then. Its miniature variant, Opera Mini, is unusual because it asks a server to fetch and compress pages before sending them to the phone.

The pairings are worth committing to memory: Chrome and Edge use Blink, Firefox uses Gecko, Safari uses WebKit, and Opera uses Blink.

### 2.8 What a web server is

A web server is a program that listens for requests on a port and answers them. The word refers both to the software and, loosely, to the machine that runs it. The software's responsibilities are consistent across products even though the details differ.

It must **listen**. That means holding a socket open on a port such as 80 or 443 and accepting incoming connections. It must **parse** the request: read the request line to learn the method and the path, read the headers to learn the host and the client's preferences, and read the body if one was sent. It must **decide**: map the path onto something that can be answered, check whether the client is allowed to have it, and choose between sending a stored file and running a program. It must **respond**: build a status line, add headers that describe the body, and send the body. And it must **record**: write a line to an access log so that traffic can be analysed and faults diagnosed.

Beyond that core, a modern server also performs **virtual hosting**, which is serving several different sites from one machine by looking at the host name in the request. It performs **compression**, so that text is sent smaller than it is stored. It performs **caching instructions**, telling browsers and intermediate caches how long a file may be reused. It may perform **encryption**, terminating a secure connection before passing the request inward. And it may act as a **reverse proxy**, forwarding requests to other programs and returning their answers.

### 2.9 Static and dynamic resources

A **static** resource is a file that is stored exactly as it will be sent. An HTML page, a photograph, a style sheet, a PDF document and a video clip are all normally static. The server opens the file, reads it, sends it, and the bytes leaving the machine are identical to the bytes on disk. Because the file does not change between requests, the server can tell the browser when it was last modified and let the browser reuse its copy.

A **dynamic** resource is produced at the moment of the request. Nothing on disk contains the finished page. Instead a program runs, consults a database or a clock or a user's profile, builds the answer and sends it. A bank statement, a shopping basket, a search results page and a live scoreboard are all dynamic. The same address may produce a different answer for every visitor, and two consecutive requests may produce different answers for the same visitor.

The distinction matters practically because the two kinds of resource have different costs and different caching rules. Static files are cheap to serve and can be cached aggressively. Dynamic pages cost processing time and usually must not be cached without care, because the answer depends on who is asking.

### 2.10 The server programs in common use

Four server products dominate current deployments, and each has a distinct character.

**Apache HTTP Server** is produced by the Apache Software Foundation, was first released in 1995, and is free and open source. It runs on almost every operating system, is configured through plain text files, allows per-directory overrides in files named `.htaccess`, and carries an enormous library of extension modules. Its traditional strength is flexibility; its traditional weakness is memory use under very high concurrency with older process models.

**Microsoft Internet Information Services**, usually written IIS, is Microsoft's server and is tightly integrated with Windows. It is administered through a graphical console, supports Microsoft's application platforms, and is common wherever an organisation standardises on Windows.

**Nginx** was written to solve the concurrency problem. It uses an event-driven design, so a small number of worker processes can hold a very large number of connections at once. It is excellent at serving static files, terminating encryption and acting as a reverse proxy or load balancer in front of other programs.

**Sun Java System Web Server** descends from the Netscape Enterprise Server line. It is aimed at medium and large sites, runs on several operating systems, and supports the Java platform technologies used for server-side applications. It is free of charge but not open source.

The pattern to notice is that the choice of server is usually driven by the application platform, the operating system and the concurrency requirement rather than by any single headline feature.

### 2.11 Client-side and server-side code

Some code runs in the browser and some runs on the server, and the difference decides what is possible and what is safe.

**Client-side** code is delivered to the browser and executed there. It can react to a click immediately, validate a form before it is sent, animate an element, or fetch additional data in the background. Its great advantage is responsiveness, because no network round trip is needed. Its great limitation is visibility: the user can read it, change it and run it under their own control, so it can never be trusted to enforce a rule.

**Server-side** code runs on the server before the answer is sent. It can read a database, check a password, apply a business rule, write a file and decide what the client is allowed to see. Its advantage is that the logic and the data remain hidden and authoritative. Its limitations are that every interaction costs a round trip and that the server must have capacity for every user.

The two are normally combined. The browser handles immediacy and presentation, the server handles truth and authority. A form is checked in the browser for speed and checked again on the server for safety, because the browser's check can be bypassed by anyone with a developer console.

## 3. Methods and Operations

### 3.1 Following a link, in the order it really happens

The comfortable illusion is that the page appears the instant the address is typed. What actually happens is a short sequence of distinct steps, and knowing them makes every later explanation easier.

1. The browser reads the address and separates it into scheme, host, path and any query or fragment.
2. The browser checks whether it already holds a usable copy of that resource in its own cache. If the copy is still fresh, the rest of this list is skipped.
3. The host name is translated into an IP address by the Domain Name System. The browser first checks its own memory, then the operating system's cache, then asks a resolver, which may in turn ask other name servers.
4. The browser opens a **Transmission Control Protocol** connection to the address and port. TCP, as it is usually called, performs a short three-part handshake so that both sides agree a connection exists.
5. If the scheme is `https`, the browser and the server perform a security handshake, agree on encryption keys, and verify that the server's certificate genuinely belongs to the requested host.
6. The browser sends a request: a line naming the method and the path, a set of headers describing what it wants and what it can accept, a blank line, and a body if the method carries one.
7. The server decides what to return, builds a response with a status code, headers and a body, and sends it back.
8. The browser reads the answer and begins again for every additional file the page needs: style sheets, scripts, images and fonts. Each of those is a separate request, and the page is assembled only when enough of them have arrived.

The eighth step is the one beginners underestimate. A page that seems to be a single object is usually a dozen or more objects, which is why the number of requests matters as much as the size of each one.

### 3.2 Turning a file into a page

When the answer is HTML, the browser does not simply display the text. It parses the markup into a tree that represents the document, with the page as the root, sections and paragraphs as branches, and words and links as leaves. That tree is called the **Document Object Model**, or DOM, and it is what the browser and any scripts work on.

Style sheets are parsed separately into a second structure that describes which rules apply to which elements. The two structures are then combined, and the browser decides which element goes where, how wide each box is, and how tall each line is. Finally it paints the boxes, fills in the text and images, and puts the layers in the right order. When a script changes the document, the browser repeats part of this work: it updates the tree, recomputes the affected boxes and repaints only what changed.

This is why the same markup can look different in two browsers. The rules of the languages are standardised, but the engines that implement them are separate programs with separate histories and separate bugs. Modern engines agree far more closely than the engines of twenty years ago, but the possibility of divergence has never disappeared.

### 3.3 How the server decides what to send

A server receives a path, not a wish. Its first job is to convert the path into something it can answer. The usual rule is that the path is appended to a configured directory called the document root, and the resulting file is examined. A request for `/beans.html` on a server whose document root is `/var/www/coffee` therefore means the file `/var/www/coffee/beans.html`.

Before the file is sent, several checks happen. The server confirms that the file exists and that the process is allowed to read it. It derives the type of the content from the file extension, so `.html` becomes a page, `.css` a style sheet and `.jpg` an image. It may compress the content if the client said it could accept compressed data. It adds headers that tell the client how large the body is and when the file last changed. And it writes a log entry recording the client, the request, the status and the size.

If the path does not correspond to a stored file, the server may still have an answer. It may look for a configured default page such as `index.html` when the path names a directory. It may apply a rewrite rule that maps an attractive address onto an internal one. Or it may hand the request to a program that will generate the answer. If none of those apply, it returns a status code saying that the resource was not found.

### 3.4 Deciding where the code should run

The choice between client-side and server-side execution follows from three questions, asked in order.

The first question is whether the work needs data the user must not see. If the answer is yes, the work belongs on the server, because anything sent to a browser is effectively published.

The second question is whether the work needs the authoritative copy of a rule. If a price, a permission or a stock level must be enforced, the check belongs on the server, even if the same check is repeated in the browser for speed.

The third question is whether the response must be immediate. If a keystroke should highlight a spelling error or a button should respond to a hover, the work belongs in the browser, because a round trip to the server would be felt.

Where all three answers are neutral, splitting the work is normal: the browser produces a quick preview and the server produces the final answer. What is never acceptable is relying on the browser for security, because the browser is under the user's control and any rule enforced only there can be removed in seconds.

### 3.5 Checking a site by hand

Two commands and one menu item let you inspect the model directly.

The first is a request for headers only. It shows what the server claims about a resource without downloading the body, and it distinguishes a static file from a generated one quickly, because a stored file usually reports when it was last modified and a generated page usually does not.

The second is a request for the full answer, saved to a file, so that the raw headers and body can be read side by side.

The menu item is the browser's own view of the page source, which shows what the server actually sent rather than what the browser made of it. Comparing the source with the rendered page is the fastest way to understand where client-side code has altered the result.

### 3.6 Reading a server log line

A typical access log entry looks like a compressed sentence: the client address, the date and time, the request line in quotes, the status code, the number of bytes sent and the browser's self-description. Read from left to right it answers four questions. Who asked. What was asked for. Whether it was delivered. How large the answer was.

Two entries next to each other often explain a user complaint. A page returning a status of 404 for a style sheet means the page will render without its styling. A page returning 500 means the server tried to run a program and the program failed. A long run of 304 responses means the browser is using its cache correctly and the server is doing very little work. Learning to read these four fields turns guesswork into diagnosis.

## 4. Worked Implementation from the Notes

### 4.1 Task: publish two pages, serve them, and then add one dynamic page

### 4.2 Implementation: write the files, serve them with a simple server, inspect the responses, then replace one path with a program

Step 1. Write the home page. The markup is deliberately small, but it is complete: it declares the document type, sets the language and character encoding, names a title and provides navigation links.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kofi's Coffee Roasters</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Kofi's Coffee Roasters</h1>
    <p>Fresh beans, roasted every Thursday.</p>
  </header>
  <nav>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="beans.html">Beans</a></li>
    </ul>
  </nav>
  <main>
    <p>We are a small roastery in Nakuru. Our
    <a href="beans.html#single-origin">single-origin lots</a> change every week.</p>
  </main>
</body>
</html>
```

The links demonstrate the two kinds of reference that matter at this stage. `beans.html` is a relative link, so it resolves against the address of the current page and keeps working if the whole site is moved. `beans.html#single-origin` adds a fragment, which the browser resolves inside the target document rather than sending to the server.

Step 2. Write the second page, and give the fragment something to point at.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Our beans</title>
</head>
<body>
  <h1>Our beans</h1>
  <section id="single-origin">
    <h2>Single-origin lots</h2>
    <p>This week: Nyeri Karindundu, washed, 1,700 metres.</p>
  </section>
  <p><a href="index.html">Back to the home page</a></p>
</body>
</html>
```

The `id` attribute is what the fragment refers to. Without it the link would still load the page but would not scroll anywhere, which is a common and easily fixed mistake.

Step 3. Serve the folder with a minimal server so that the client-server split becomes concrete.

```bash
cd /srv/coffee
python3 -m http.server 8000
```

The command prints a line saying it is serving on port 8000. The process is now the server: it holds a socket open, waits for connections, and answers each one by reading the matching file from the directory. The browser is the client.

Step 4. Request the page and read only the headers.

```bash
curl -I http://127.0.0.1:8000/beans.html
```

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.11.4
Date: Fri, 07 Nov 2026 09:14:02 GMT
Content-type: text/html
Content-Length: 236
Last-Modified: Fri, 07 Nov 2026 09:02:47 GMT
```

Every line has a meaning. The status line says the request succeeded. The server line identifies the software. The date is when the answer was produced. The content type tells the browser how to interpret the body. The content length says how many bytes are coming. The last-modified line says when the file on disk changed, which is possible only because the answer is a stored file.

Step 5. Ask for something that does not exist, to see how the model reports failure.

```bash
curl -I http://127.0.0.1:8000/tea.html
```

```text
HTTP/1.0 404 Not Found
Server: SimpleHTTP/0.6 Python/3.11.4
Date: Fri, 07 Nov 2026 09:14:20 GMT
Content-Type: text/html;charset=utf-8
Content-Length: 469
```

The status code changes and nothing else in the exchange does. The client asked in the same way, the server answered in the same way, and only the verdict differs. This is the concrete demonstration that the status code, not the presence or absence of a body, carries the outcome.

Step 6. Replace one address with a program, so that a dynamic resource sits beside the static ones. The following program answers every request with the current time, which no file on disk could contain.

```python
from datetime import datetime, timezone
from wsgiref.simple_server import make_server


def app(environ, start_response):
    stamp = datetime.now(timezone.utc).strftime("%H:%M:%S")
    body = (
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<title>Roastery clock</title></head><body>"
        "<h1>Roastery clock</h1><p>The oven clock reads " + stamp + " UTC.</p>"
        "</body></html>"
    )
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [body.encode("utf-8")]


if __name__ == "__main__":
    make_server("127.0.0.1", 8001, app).serve_forever()
```

Run it, then request it twice.

```bash
python3 clock.py
curl -i http://127.0.0.1:8001/clock
```

```text
HTTP/1.0 200 OK
Date: Fri, 07 Nov 2026 09:15:11 GMT
Server: WSGIServer/0.2 CPython/3.11.4
Content-Type: text/html; charset=utf-8
Content-Length: 178
```

Two observations prove the page is dynamic. The response carries no last-modified line, because there is no stored file whose modification time could be reported. And a second request a few seconds later produces a different body while every header stays the same shape, which is impossible for a stored file.

Step 7. Compare the two kinds of resource by their evidence rather than by their description.

| Evidence in the response | What it implies | Reason |
|---|---|---|
| A last-modified date is present | The answer is a stored file | The server can only report a modification time if bytes exist on disk |
| No last-modified date, but a sensible content length | The answer was generated | The body was built in memory and its size computed |
| The same address returns different bodies over time | The answer depends on something outside the file system | A clock, a database or a session is involved |
| A short response time that barely varies | Likely a static file served from memory | The work is a read and a copy, not a computation |

The fourth row is a tendency rather than a law, because a small dynamic page can be as fast as a static one once the program is warm.

Step 8. Read the log that the simple server writes for each transaction.

```text
127.0.0.1 - - [07/Nov/2026 09:14:02] "HEAD /beans.html HTTP/1.1" 200 -
127.0.0.1 - - [07/Nov/2026 09:14:20] "HEAD /tea.html HTTP/1.1" 404 -
```

The two lines are identical in shape and differ only in the path and the status. That is the evidence that the server treats both requests in exactly the same way up to the moment of resolution, and that everything afterwards depends on whether a target exists.

The exercise has now established five facts. A client asked in a fixed format, a server answered in a fixed format, the path selected the resource, the status code reported the outcome, and one address was answered by a file while another was answered by a running program. Every later refinement of the Web, from login sessions to single-page applications, is an elaboration of one of those five statements.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to test your understanding

You have understood this topic when you can do the following without notes.

- Explain the difference between the Internet and the World Wide Web, and name two services that use the Internet but not the Web.
- Take an address apart into scheme, host, port, path, query and fragment, and say which parts reach the server.
- Describe a request and a response in the order they happen, including the name lookup and the connection.
- Say what a browser engine does and what a rendering engine does, and name the engine used by Chrome, Firefox, Safari and Edge.
- Explain what a web server does with a path, and how it decides between sending a file and running a program.
- Give two pieces of evidence that distinguish a static resource from a dynamic one.
- Justify putting a particular piece of logic in the browser or on the server.

### 5.2 Beginner misconceptions to unlearn

- **"The Web and the Internet are the same thing."** The Internet carries the Web. Email, name resolution and remote login have never needed the Web.
- **"A web page is one file."** A page is usually many files, each fetched by its own request, which is why the number of requests affects speed.
- **"The browser stores nothing."** It stores a cache, cookies, history and larger script storage areas, all governed by rules about which site may read what.
- **"A browser engine and a rendering engine are the same."** The browser engine coordinates navigation, history and loading; the rendering engine turns markup and style into pixels. Chrome's rendering engine is Blink, while the coordinating layer is a separate part of the program.
- **"All browsers use the same engine."** Chrome and Edge use Blink, Firefox uses Gecko, Safari uses WebKit. This is why a page can differ between them.
- **"A URL is only an address of a page."** A URL can name an image, a video, a data record or a service endpoint.
- **"The fragment is sent to the server."** It is not; the browser handles it locally after the document arrives.
- **"The server remembers me because I am logged in."** The protocol is stateless. Being logged in depends on a cookie or a token that is sent with every request.
- **"Client-side validation keeps the site safe."** Anything in the browser can be altered. Validation in the browser is a convenience; validation on the server is the control.
- **"A 404 means the server is broken."** It means the requested resource was not found. A 500 means the server tried and failed.
- **"Dynamic always means interactive."** A dynamic page is one generated at request time. A page can be generated and still be entirely read-only.
- **"HTTPS encrypts the page contents, so the address is private too."** The host name is visible in the connection setup even when the path and body are protected.

### 5.3 Interpreting the evidence

The temptation when a page misbehaves is to guess. The architecture gives better options, because each part of the exchange leaves evidence.

If the page never loads and the browser reports that the name could not be resolved, the fault is in the name lookup, not in the server. If the name resolves but the connection times out, the path to the server or the listening process is at fault. If a connection is refused immediately, the machine is reachable but nothing is listening on that port. If a padlock warning appears, the certificate does not match the host or is not trusted. If the page loads without styling, the style sheet request failed and the access log will show it. If the page loads but a button does nothing, the script failed or was blocked, and the browser's console will say so.

Each symptom points at one layer, and the layers were designed to be separable exactly so that this reasoning works. A student who can move from symptom to layer is already thinking like an engineer.

### 5.4 Limits worth knowing

The model has real limitations, and stating them shows understanding rather than doubt.

Because the protocol is stateless, every application that needs memory must add it, usually with a cookie or a token, which introduces questions about privacy and expiry. Because the client controls the browser, no rule enforced only there can be trusted. Because a page is assembled from many requests, latency accumulates, which is why reducing the number of requests is a standard optimisation. Because caching is essential to performance, stale content is a permanent hazard, and cache instructions must be set deliberately. And because the Web runs on the open Internet, any service is exposed to anyone who can reach it, so authentication and encryption are not optional extras.

### 5.5 A revision routine that works

Read the five parts of the basic model aloud and say what each part does. Then add the three additions of the interactive model. Then name the parts of a browser and the parts of a server, and for each part say one thing that would break if it were removed. Finish by taking any address you use daily and explaining, in order, what happens between pressing enter and seeing the page.

If any step of that explanation is missing, the gap is the thing to revise. The topic is not a list of terms to memorise; it is one sequence of events with names attached, and the names only become useful once the sequence is clear.
