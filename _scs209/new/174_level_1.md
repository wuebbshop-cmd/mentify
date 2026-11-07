## 1. Concept and Use Case

### 1.1 A very large building with numbered doors

Imagine a single large building on a busy street. The building has one postal address, but inside there are hundreds of rooms, and every room has a number painted on the door. A courier carrying a parcel does not need a map of the whole building: the street address gets the parcel to the right building, and the room number gets it to the right person. Most rooms are ordinary offices, but a few are special. One is a mailroom where letters are sorted and forwarded. One is a records office where documents are handed across a counter in either direction. One is a control booth from which an operator can work equipment in a distant part of the building. One is a public noticeboard where announcements are pinned up for anyone who walks past.

That picture is the whole idea behind this topic. The street address is the address a computer holds on the network, called an Internet Protocol address, usually shortened to **IP address**. The painted room numbers are **port numbers**. The rooms are **services**. The people who work inside the rooms are **server programs**, and the person who walks in with a request is a **client program**. A visitor needs to know only two things to get served: the address of the building and the number of the door.

Two visitors can arrive at the same building at the same moment without interfering with each other, because one goes to the mailroom and the other goes to the records office. In the same way, one computer can be a mail server, a file server and a web server at the same time, because each service answers on its own port number. Nothing about the network has to change when a new room is opened. Somebody simply starts a new program that listens on a new number, and word gets around that the service exists.

### 1.2 What an Internet service actually is

An Internet service is a program running on a remote computer that waits for requests, follows a published set of rules for answering them, and does something useful on the requester's behalf. The published rules are called a **protocol**. A protocol is not a suggestion; it is a contract, written down in a document so that two programs written by different people in different countries can work together without ever having met.

Those documents are called **Requests for Comments**, abbreviated **RFC**. The name is a historical accident: the first ones were circulated informally in 1969 and nobody expected them to become standards. Today an RFC number is the definitive citation for a protocol's behaviour, and the numbers matter. The File Transfer Protocol is RFC 959, the Simple Mail Transfer Protocol is RFC 5321, and the Post Office Protocol version 3 is RFC 1939.

Port numbers are managed by the **Internet Assigned Numbers Authority**, abbreviated **IANA**. IANA keeps a register that says which numbers are reserved for which service, so that a mail server written by one company and a mail client written by another will look for each other in the same place.

### 1.3 The services that came first

Long before anybody spoke of a web page, the Internet already carried several distinct services. The five that are usually listed as foundational are the following.

**Electronic mail**, usually written as **email**, is a way to send a written message to one or more people who are not present, and to have that message wait for them until they are ready. It was the first application that ordinary people found a reason to use, and surveys from the early commercial Internet placed it far ahead of everything else in popularity, with roughly eighty-five per cent of connected users sending and receiving mail.

**Telnet** is a protocol for logging in to a remote computer and using it as though the keyboard and screen in front of you were attached directly to it. The name comes from "teletype network", after the teletype terminals it was designed to serve. It is a remote terminal service, so it is useful for running programs on a machine that is somewhere else, and it was the standard way to administer servers and network equipment for two decades.

**File Transfer Protocol**, abbreviated **FTP**, moves whole files between computers. It was designed for the era of large documents and program archives, when the interesting thing was not reading a document in place but obtaining a complete copy of it. FTP handles text and binary files, whole directories of files, and it can run for hours without losing its place.

**UseNet news**, sometimes written **Usenet**, is a distributed noticeboard. Articles are posted into named groups, the groups are copied from one server to another around the world, and readers use a special program to read and reply. The name comes from "user network". It is a discussion system rather than a publishing system, and it is older than the web by more than a decade.

**The World Wide Web**, abbreviated **WWW**, is a hypertext service: documents that contain links to other documents, so that a reader can move from one to another by following a link instead of by typing an address.

Three further services are worth naming because they appear in the same discussions. The **Domain Name System**, abbreviated **DNS**, turns a memorable name such as a university's hostname into the numeric address that the network actually uses, and it does so on port 53. **Gopher** is a menu-driven information service that presents a hierarchy of choices rather than a page of links, and it was a serious rival to the web in the early 1990s. And **Internet Relay Chat**, abbreviated **IRC**, carried live text conversation between groups of people.

### 1.4 Why a modern student still studies these services

It is tempting to treat this material as history, because a browser now hides most of it. There are four reasons not to.

The first is that the mechanisms are still in daily use, only wrapped in something friendlier. Every time a phone checks for new mail it runs the **Internet Message Access Protocol**, abbreviated **IMAP**, or the older Post Office Protocol. Every time a message is sent it is handed to a mail server that speaks the Simple Mail Transfer Protocol. Every time an administrator changes a setting on a switch they use a secure descendant of Telnet.

The second is diagnostic. Because these protocols are simple text conversations, they can be driven by hand. Typing a mail server's commands one line at a time is the fastest way to discover whether the server is reachable, whether it accepts your credentials, and what it says when it refuses. A graphical mail program hides that conversation, and hiding it hides the fault.

The third is security. The older protocols in this topic send everything, including passwords, as readable text. Understanding exactly what an eavesdropper sees is what makes the case for encryption concrete rather than an instruction to be memorised.

The fourth is examination value. Questions on this topic ask for the difference between two protocols, the purpose of a numbered channel, or the sequence of commands in a session. Those questions are answered by knowing the design, not by knowing a menu.

### 1.5 Use cases you will recognise

A student finishes an assignment and uploads it to a department server. The server is not a web server; it accepts files on port 21 and stores them in the student's home directory. The tool on the laptop is an FTP client, or its encrypted successor.

A network administrator is told that a switch in another building has stopped responding. The administrator connects to it over the network, gets a command prompt, and inspects its configuration. Two decades ago that connection was made with Telnet; today it is made with the **Secure Shell**, abbreviated **SSH**, which does the same job over an encrypted channel on port 22.

A lecturer sends a circular to a class. Her mail program hands the message to her department's outgoing mail server, which finds the recipient's mail server by looking up a DNS record and passes the message across. The recipient may be asleep. The message waits in a mailbox until the recipient's phone collects it.

A student reads the same mailbox on a laptop and a phone. If the mailbox uses IMAP, both devices see the same folders and the same read and unread marks. If it used the older Post Office Protocol, the first device to collect the mail would normally remove it, and the second device would never see it.

A researcher in 1992 wants a document from a university on another continent. She opens a Gopher client, sees a menu of institutions, chooses one, sees a menu of departments, chooses one, and finally chooses a document. Every step is a numbered menu, and no address has to be typed.

### 1.6 The single sentence that holds the topic together

Everything in this topic is one idea seen seven times: a client program and a server program agree on a small vocabulary of text commands, exchange them over a numbered connection, and use that conversation to move a file, open a terminal, deliver a message, or fetch a document.

## 2. Data, Syntax, and Core Concepts

### 2.1 Client and server: who starts the conversation

A **server** is a program that opens a port and waits. It does not know in advance who will contact it, and it may serve thousands of clients in a day. A **client** is a program that decides to make contact, knows the address and port of the server, and starts the conversation.

The distinction is about who initiates, not about which machine is more powerful. A phone collecting mail is a client, and a large server farm is the server, but the same laptop can be a server for a file-sharing program while it is a client of a mail server. The words describe roles in one conversation, not permanent properties of a device.

Three consequences follow from this arrangement, and they explain most of the behaviour you will observe.

The server must be reachable, which means its address must be known and its port must not be blocked. If a firewall refuses connections to port 21, no amount of correct client configuration will make file transfer work.

The server must be able to serve several clients at once, so it either starts a new process or thread per connection or handles them in a loop. This is why an overloaded server can accept a connection and then answer slowly.

The client holds the state of the session: which directory it is in, which file it is transferring, how much of it has arrived. If the client crashes halfway through a transfer, the server notices only that the connection closed.

### 2.2 Port numbers: the painted doors

A computer's IP address identifies the machine; a port number identifies the service on that machine. A port is a sixteen-bit number, so it ranges from 0 to 65535. The range below 1024 is reserved for well-known services and normally requires administrator rights to use, which is a safety measure: a program run by an ordinary user cannot impersonate a mail server.

The ports that belong to this topic, and to its immediate neighbours, are worth learning as a set. Two transport protocols are named in it and must not be confused. The **Transmission Control Protocol**, abbreviated **TCP**, first sets up a connection and then guarantees that the data arrives, and arrives in order. The **User Datagram Protocol**, abbreviated **UDP**, sends one self-contained message with no guarantee at all. The service names in the table are also worth meeting once together: SMTP is the Simple Mail Transfer Protocol, POP3 is the Post Office Protocol version 3, IMAP is the Internet Message Access Protocol, NNTP is the Network News Transfer Protocol, HTTP is the Hypertext Transfer Protocol, HTTPS is the same protocol carried over an encrypted connection, DNS is the Domain Name System, and FTP is the File Transfer Protocol.

| Service | Protocol | Port | What travels on it |
|---|---|---|---|
| FTP data | TCP | 20 | The actual file contents, in active mode |
| FTP control | TCP | 21 | Commands and replies |
| SSH | TCP | 22 | Encrypted remote login and secure file transfer |
| Telnet | TCP | 23 | Plain remote login |
| SMTP | TCP | 25 | Mail between servers |
| DNS | UDP and TCP | 53 | Name-to-address lookups |
| HTTP | TCP | 80 | Web pages |
| POP3 | TCP | 110 | Mail collection, older style |
| NNTP | TCP | 119 | UseNet news articles |
| IMAP | TCP | 143 | Mail access, modern style |
| HTTPS | TCP | 443 | Encrypted web pages |
| SMTP submission | TCP | 587 | Mail from a client to its own server |
| IMAPS | TCP | 993 | Encrypted IMAP |
| POP3S | TCP | 995 | Encrypted POP3 |

Two entries deserve a comment because they are the ones students misremember. FTP uses two ports, not one, and the data port is 20 while the control port is 21. And mail uses different ports depending on direction: port 25 carries mail between servers, while port 587 carries mail from a person's mail program to their own provider, because that path requires authentication and port 25 traditionally does not.

### 2.3 Every conversation has a grammar

All the protocols in this topic are text conversations, and all of them follow the same broad shape. The server speaks first with a greeting. The client identifies itself. The client authenticates. The client issues commands one at a time. The server answers each command, and the answer says whether the command succeeded. Eventually the client says goodbye and the connection closes.

What differs is the vocabulary. FTP uses words such as USER, PASS, RETR for retrieve and STOR for store, and answers with three-digit codes. The mail protocols use a smaller vocabulary and answer with a code followed by a short explanation. Telnet has almost no vocabulary of its own, because after the connection is open it simply carries whatever the remote computer's operating system expects.

The three-digit reply code in FTP is a small design masterpiece and worth understanding early, because it makes error messages readable at a glance. The first digit says what class of answer it is.

| First digit | Meaning | Example |
|---|---|---|
| 1 | The command was accepted and something is still in progress | 150 about to open a data connection |
| 2 | The command completed successfully | 220 service ready, 230 logged in |
| 3 | The command was accepted but more information is needed | 331 password required |
| 4 | The command failed for now, but retrying may work | 421 service not available |
| 5 | The command failed and will keep failing | 530 not logged in, 550 no such file |

The difference between a four and a five is the difference between "try again shortly" and "do not bother". A client that treats a permanent failure as temporary will loop forever.

### 2.4 FTP: two doors used at once

FTP is the service that surprises beginners, because it uses two separate connections for one job. One connection carries instructions, and the other carries the file. This is called an **out-of-band** design, because the control information travels outside the channel that carries the data.

The control connection is opened by the client to the server's port 21, and it stays open for the whole session, even for hours. On it travel the login name, the password, the commands, and the replies. The data connection is opened only when a file or a directory listing has to move, and it is closed when that transfer finishes.

Why bother? Because the control connection must stay responsive while a huge file is in flight. If commands and file data shared one channel, a client could not tell the server to abort a transfer, and a server could not report progress. Splitting them also lets the two travel with different settings: the control channel is always text, while the data channel can be switched between text mode for readable text files and binary mode for images and programs.

Two modes decide who opens the data connection, and this is the second thing that surprises beginners.

In **active mode**, the client tells the server where to connect, and the server makes the connection back to the client. The server connects from its own port 20 to the port the client nominated. This works perfectly between two machines on the same network, and fails badly when the client is behind a home router, because the router did not expect an incoming connection and refuses it.

In **passive mode**, the client asks the server to open a port and wait, the server replies with the port number it has opened, and the client makes the second connection itself. Because both connections now travel in the same direction, from client to server, the home router is satisfied and the transfer works.

The practical rule is that passive mode is the default for good reason, and the reason is not that it is faster. It is that it survives the whole world being behind a router.

### 2.5 Telnet: a keyboard extension cable

Telnet gives you the remote computer's command line as though your keyboard were plugged into it. What arrives at your screen is whatever the remote machine would have printed on its own console, and what you type is delivered as though it had been typed there.

The protocol has to solve one problem that seems trivial and is not: the two machines may disagree about how characters are represented. One may send a line when the user presses Enter, another may send each keystroke as it is pressed. One may use a particular character as a signal to interrupt, another may use a different one. Telnet solves this with a notional terminal called the **Network Virtual Terminal**, abbreviated **NVT**, which defines a common baseline that both sides convert to and from. Both sides then negotiate which extras they support, such as the type of terminal, the size of the window, and whether either side wants to echo characters.

That negotiation is the part of Telnet that is actually complex, and it is invisible to the user. What the user sees is a login prompt.

Telnet's weakness is simple and brutal: nothing is encrypted. The login name and the password cross the network as readable text, as does everything typed afterwards. Anyone who can watch the traffic, on a shared wireless network or on any router along the path, can read the session and replay the password. For that reason Telnet is now regarded as insecure by modern standards and must not be used across an untrusted network. The replacement is SSH on port 22, which provides an encrypted channel and also verifies the identity of the server. For the narrow purpose of testing whether a port accepts connections, a Telnet client is still a convenient tool, and that use is harmless because nothing secret is typed.

### 2.6 Email: three workers and a pigeonhole

An email system is easier to understand if you separate the jobs that are often bundled together in one program.

The **mail user agent**, abbreviated **MUA**, is the program a person actually uses: it composes, displays, and files messages. A phone mail app and a desktop mail program are user agents. A user agent does not deliver anything; it hands the message to the next worker.

The **message transfer agent**, abbreviated **MTA**, moves messages between computers. It takes a message from a user agent or from another transfer agent, discovers which computer should receive it, and passes it on. Transfer agents are the postal service of email: they know routes, they retry when a destination is unavailable, and they report failure back to the sender. The protocol they speak to each other is the Simple Mail Transfer Protocol.

The **message store** is where delivered mail waits. It is usually a directory of files or a small database on the recipient's mail server, organised into a mailbox for the inbox and folders for anything the user has filed. The word **mailbox** is used for the container that holds one user's messages.

The **mail delivery agent**, abbreviated **MDA**, is the worker that takes a message from the transfer agent and puts it into the message store, applying any filtering rules on the way. Many systems fold this into the transfer agent, and many exam answers simply say that delivery writes the message into the mailbox.

The **mail retrieval protocol** carries messages from the message store to the user agent. It is not the same protocol as transmission, and this separation is deliberate. Transmission pushes mail toward a server that is always on. Retrieval pulls mail toward a device that may be switched off for days. Trying to use one protocol for both jobs would force the always-on server to behave like a client.

### 2.7 SMTP: five sentences and a full stop

The Simple Mail Transfer Protocol is small enough to learn by heart. The whole of a delivery is five statements.

The client says **HELO** with its own name, or **EHLO** if it wants the extended form that offers encryption and authentication. The server answers with its name and, for EHLO, a list of what it can do.

The client says **MAIL FROM** with the sender's address. This is the return address used for error reports, and it is not necessarily the address shown in the message header.

The client says **RCPT TO** once for each recipient. The server may accept or refuse each one individually, which is why a message to three people can arrive for two of them.

The client says **DATA**, and the server replies that it is ready. The client then sends the headers and the body, and ends with a line containing a single full stop.

Finally the client says **QUIT**, and the server closes the connection.

Two details catch students out. First, a line in the message that itself begins with a full stop would look like the end of the message, so the client doubles it; the receiving side removes the extra stop. Second, the message as transmitted carries two kinds of addressing: the envelope, which is what MAIL FROM and RCPT TO say and what the servers use for routing, and the header, which is what the reader sees.

### 2.8 POP3 and IMAP: two ways to read a mailbox

Both protocols let a mail program read a mailbox on a server. They differ in what they assume about how many devices a person uses, and in how much of the mailbox has to move.

**Post Office Protocol version 3**, abbreviated **POP3**, treats the mailbox like a pigeonhole at a post office. You arrive, you collect everything, and the pigeonhole is emptied. The default behaviour is to download each message to the local device and then delete it from the server when the session is closed properly. It is simple, it works over a poor connection, and it uses almost no server storage. Its weakness is that the mailbox lives on one device: collect mail on a phone and the laptop sees nothing, and read a message in two places and the read marks disagree.

**Internet Message Access Protocol**, abbreviated **IMAP**, treats the mailbox like a filing cabinet that stays in the office. The messages remain on the server, and the mail program fetches summaries, headers, or individual parts of messages on demand. Folders exist on the server, so every device sees the same folders. Flags such as read, answered, and flagged are stored on the server, so a message read on a phone shows as read on a laptop. The cost is that the server stores everything and the client depends on a live connection for anything it has not cached.

The comparison, in words a beginner can use:

| Question | POP3 | IMAP |
|---|---|---|
| Where does the mail live? | On the device that collected it | On the server |
| What happens after collection? | Deleted from the server by default | Left in place |
| Several devices? | Awkward, and usually inconsistent | Natural, all see the same mailbox |
| Folders? | Only on the local device | Created and stored on the server |
| Read and unread marks? | Local to each device | Shared through the server |
| Works on a slow link? | Yes, after the download finishes | Yes, because only parts are fetched |
| Server storage needed? | Very little | As much as the mailbox holds |

### 2.9 UseNet and Gopher: two older ways of finding things

**UseNet** is a network of servers that exchange articles in named groups. A group has a hierarchical name whose parts are separated by full stops, so a group about network protocols might be named with the words computer, protocols and tcp-ip in that order, separated by full stops. The first part of the name places the group in a broad category: computing, science, recreation, social issues, debate, news about the network itself, or the unmoderated alternative hierarchy.

Articles are copied from server to server by the **Network News Transfer Protocol**, abbreviated **NNTP**, on port 119. Propagation is a flood: each server passes new articles to its neighbours, and each article carries a path header recording the servers it has crossed so that it is not sent back where it came from. A newsgroup is a discussion, not a publication: replies are simply further articles.

**Gopher** presents information as menus. A menu is a list of numbered choices, and each choice is either another menu, a text document, a search service, or a binary file. Selecting a choice sends a short request to the server on port 70, and the server replies with the document or with the next menu. The design is deliberately minimal: no images inside documents, no scripting, no styling. Its advantage over the early web was consistency, and its disadvantage was that a menu cannot express a cross-reference from one document to another.

### 2.10 The vocabulary in one place

| Term | Plain meaning |
|---|---|
| Client | The program that starts the conversation |
| Server | The program that waits on a port and answers |
| Port | The number that identifies which service is wanted |
| Protocol | The agreed vocabulary and order of a conversation |
| Session | One complete conversation, from greeting to goodbye |
| Authentication | Proving who you are, usually with a name and password |
| Anonymous access | A service that accepts a conventional guest name instead of a personal one |
| Plaintext | Data sent in a form anyone watching can read |
| Ciphertext | Data that has been encrypted |
| Relay | A server that forwards a message on someone else's behalf |
| Mailbox | The container holding one user's stored messages |
| Header | The addressing and labelling lines above the body of a message |
| Envelope | The addresses the servers use for routing, which the reader does not see |
| Flag | A mark such as read or answered, stored with a message |

These fourteen words are enough to describe every session in the rest of this note.

## 3. Methods and Operations

### 3.1 How a session is opened, in five steps

Every client-server service in this topic is opened the same way, and knowing the shape makes the individual protocols much easier to learn.

Step 1. The client turns the server's name into an address. It asks the Domain Name System for the address belonging to the name, and DNS answers with a numeric address. If the name does not exist, the conversation never starts, and the error message will be about the name rather than about the service.

Step 2. The client opens a connection to the address on the port belonging to the service. If nothing is listening, the connection is refused immediately. If a firewall is silently dropping the packets, the attempt instead hangs until it times out, which is a different symptom and points to a different cause.

Step 3. The server sends a greeting. A greeting that begins with a two in the reply code is a welcome. A greeting that begins with four or five is a refusal, and the text after the code usually says why.

Step 4. The client identifies itself, then authenticates. Some services allow a form of anonymous access, in which the client gives a conventional guest name and, as a courtesy, any address for the record rather than a real credential.

Step 5. The client issues commands and reads replies until it is finished, then closes the session properly. Closing properly matters, because in several protocols the tidy close is the moment at which pending work is committed. In the Post Office Protocol, for example, messages marked for deletion are only actually removed when the client says goodbye in the correct way.

### 3.2 Transferring a file with FTP

The operation has a fixed pattern that is worth memorising as a sequence.

The client connects to port 21 and reads the greeting, which normally begins 220. It sends the user name, receives a 331 asking for the password, sends the password, and receives a 230 confirming that it is logged in. If the password is wrong the reply is 530.

The client sets the transfer type. Text files are sent with the ASCII type, whose name stands for American Standard Code for Information Interchange, so that line endings can be converted between systems; images, archives, and programs are sent with the binary type so that not one byte is altered. Sending a binary file in text mode is the classic way to corrupt a download.

The client chooses a directory with the change-working-directory command, or asks for the current one, and may list the contents. The listing itself travels on a data connection, so even a simple list of names exercises the two-channel design.

The client asks for the file with the retrieve command, or sends one with the store command. The server replies with 150 to say the data connection is about to open, sends the bytes, and then replies 226 to say the transfer finished cleanly.

Finally the client says goodbye and receives 221. If a transfer is interrupted, the file on the receiving side is shorter than expected, and there is no automatic repair: FTP has no checksum of its own, so a truncated download is detected only by the application that later tries to use it.

### 3.3 Choosing between active and passive mode

The decision is made by the network the client sits in, not by preference.

If the client and server are on the same local network and there is no intervening firewall, either mode works. If the client is behind a home router, a mobile network, or a corporate firewall, passive mode is required, because only passive mode has the server waiting for a connection that the client initiates. If the server is behind a firewall that has been configured to allow the server's port 20 outbound but not a wide range of high ports, then active mode may be the only mode that works, which is why old installations sometimes insist on it.

A useful habit is to try passive mode first, because it succeeds in the overwhelming majority of cases, and to treat a failure as a signal to examine the firewall rules rather than to keep retrying.

### 3.4 Logging in remotely with Telnet, and why not to

The operation is short: open a connection to the remote computer on port 23, wait for its login prompt, type the user name and password, and then use the command line exactly as though sitting at the machine. When finished, log out and close the connection.

The step that must not be skipped is the decision about whether the network is trusted. On a laboratory network with no other users, a Telnet session to a device that only supports Telnet may be acceptable for a few minutes of maintenance. On any network where another person could observe the traffic, it is not acceptable, because the password crosses the wire in a form that any packet capture will display in plain characters.

The replacement is SSH on port 22. The operation is identical from the user's point of view: connect, authenticate, use the command line, log out. The difference is that the whole conversation is encrypted and the server proves its identity with a key. For file transfer over the same secure channel there is the SSH File Transfer Protocol, abbreviated **SFTP**, and for FTP with encryption added there is **FTPS**, which wraps the existing protocol in Transport Layer Security, abbreviated **TLS**. Both are secure; neither is the same thing as the other, and neither should be confused with plain FTP.

### 3.5 Sending a message by hand

Sending a message without a mail program is a five-minute exercise that teaches more than an hour of reading. The steps are as follows.

Connect to the outgoing server on port 25, or on port 587 if the server requires authentication. Read the 220 greeting.

Say EHLO with your own computer's name and read the list of extensions the server offers. Then authenticate if required, and start encryption if the server offers it.

Say MAIL FROM with the sender's address between angle brackets. The server answers 250 if it will accept mail from that address.

Say RCPT TO with each recipient. Each recipient is confirmed or refused separately, and a refusal here is a refusal for that one address only.

Say DATA. The server answers 354, which means "go ahead, end with a line containing only a full stop". Send the headers, a blank line, the body, and then a line with a single full stop.

Read the 250 that says the message has been queued, then say QUIT.

The message is now the responsibility of the server. Whether it reaches the recipient depends on the recipient's domain existing, its mail server accepting the message, and its spam filters not objecting. A 250 means "I have taken it", not "it has arrived".

### 3.6 Collecting mail with POP3

The pattern is short. Connect to port 110, read the greeting, which begins with the characters plus, O and K rather than a number. Send the user name, send the password, and read the confirmation. Ask for the status, which reports how many messages there are and how many bytes they occupy. Ask for a list, which reports the size of each message. Retrieve the messages one at a time. Mark each one for deletion if it is no longer wanted. Say goodbye, at which point the deletions take effect.

The important operational point is that deletion is deferred. The delete command only marks a message; the mark is acted upon at the tidy close. This design means that a session interrupted by a lost connection leaves the mailbox unchanged, which is much safer than deleting as you go.

### 3.7 Reading mail with IMAP

The pattern is different because nothing is moved by default. Connect to port 143, or to port 993 with encryption, and read the greeting. Log in. Select the mailbox you want, and read the summary the server returns: how many messages exist, how many are recent, and the first message number that has not been read. Then fetch only what you need: the flags, the headers, a single part of a message, or the whole body. To tidy the mailbox, mark messages as deleted and then ask the server to remove the marked ones. Finally log out.

The operational consequence is that a mail program can show a list of two thousand messages after fetching a few kilobytes of headers, and can read one message without downloading the attachments of the rest. That is why IMAP is comfortable on a slow connection even though the mailbox itself is huge.

### 3.8 Reading news and browsing Gopher

Reading a newsgroup begins with the client connecting to a news server on port 119 and being greeted. The client asks to join a group, and the server replies with the number of articles, the first article number and the last. The client then asks for the headers of the newest articles, presents them as a list, and fetches the body of whichever one the reader selects. Replying is just posting another article into the same group, with headers that reference the article being answered so that readers can see the thread.

Browsing Gopher begins with the client connecting to port 70 and requesting an empty selector, which means "show me your top menu". The server sends a series of lines, each describing one menu entry, and ends with a line containing a single full stop. Each entry carries a type character, the text to display, the selector to send if it is chosen, the host it lives on, and the port to contact. A text document is fetched by sending its selector, and the server responds with the document itself rather than a menu.

### 3.9 Comparing what each service moves

| Service | Direction of the main flow | Typical size | Interruption cost |
|---|---|---|---|
| FTP download | Server to client | Megabytes to gigabytes | Partial file must be resent |
| FTP upload | Client to server | Megabytes | Partial file must be resent |
| Telnet | Both, keystroke by keystroke | Tiny | Session is lost, work may be lost |
| SMTP | Client to server, then server to server | Kilobytes | Message retried by the sender's server |
| POP3 | Server to client | Whole mailbox | Session restarts, mailbox intact |
| IMAP | Server to client, in pieces | Headers first | Reconnect and continue |
| NNTP | Server to server, then to client | Kilobytes | Article re-requested |
| Gopher | Server to client | A menu or one document | Request repeated |
| DNS | Either way, one question and one answer | Tens of bytes | Query repeated |

## 4. Worked Implementation from the Notes

### 4.1 Task: list and download a file from a class FTP server

### 4.2 Implementation: a passive-mode session driven by hand

Step 1. Open the control connection to port 21. The greeting is the server announcing that it is ready.

```bash
ftp ftp.example.ac.ke 21
```

Step 2. The client prints the greeting and asks for a name. The three-digit code 220 means the service is ready, and the number after the code is not an error: every reply begins with a code.

```text
Connected to ftp.example.ac.ke.
220-Welcome to the Example Academic FTP service
220 Service ready for new user.
Name (ftp.example.ac.ke:student): student
331 Password required for student
Password:
230 User student logged in. Access restrictions apply.
```

Step 3. Select binary mode, because the file being fetched is an archive rather than readable text, and ask for the current directory to confirm where the server has placed us.

```text
ftp> binary
200 Type set to I.
ftp> pwd
257 "/home/student" is the current directory.
```

Step 4. Ask the server to open a data port, which is passive mode. The reply contains four numbers for the address and two numbers that encode the port.

```text
ftp> passive
Passive mode on.
ftp> debug
Debugging on (debug=1).
ftp> ls
---> PASV
227 Entering Passive Mode (203,0,113,9,195,84).
---> LIST
150 Opening ASCII mode data connection for file list.
-rw-r--r-- 1 student student 18432 Nov 07 09:14 assignment1.txt
-rw-r--r-- 1 student student 7340032 Nov 07 09:02 toolkit.zip
226 Transfer complete.
```

The two numbers 195 and 84 encode the port as 195 times 256 plus 84, which is 50004. The client connects to that port, the listing arrives, and the reply 226 confirms that the data connection closed cleanly after a complete transfer.

Step 5. Fetch the archive.

```text
ftp> get toolkit.zip
---> PASV
227 Entering Passive Mode (203,0,113,9,195,85).
---> RETR toolkit.zip
150 Opening BINARY mode data connection for toolkit.zip (7340032 bytes).
226 Transfer complete.
7340032 bytes received in 4.8 secs (1.5 MB/s)
```

Step 6. Explain what has been demonstrated. One connection carried the commands on port 21 and stayed open throughout; a second connection carried the listing and then the file, and was opened and closed twice. The client, not the server, opened both data connections, which is the definition of passive mode. If this had been active mode, the client would have sent its own address and port with the PORT command and the server would have connected back from port 20.

Step 7. Close the session tidily.

```text
ftp> quit
221 Goodbye.
```

### 4.3 Task: prove that a mail server is reachable without a mail program

### 4.4 Implementation: use a Telnet client as a port tester

Step 1. Connect to the mail server on port 25 with the Telnet client. Nothing secret is typed here, so the lack of encryption does no harm.

```bash
telnet smtp.example.ac.ke 25
```

Step 2. Read the greeting. The 220 says the server is willing to talk, and the name in the banner identifies the software, which is useful when reporting a fault.

```text
Trying 203.0.113.25...
Connected to smtp.example.ac.ke.
Escape character is '^]'.
220 smtp.example.ac.ke ESMTP Postfix
```

Step 3. Greet the server with EHLO and read the extension list.

```text
EHLO labpc.example.ac.ke
250-smtp.example.ac.ke
250-PIPELINING
250-SIZE 10240000
250-STARTTLS
250-ENHANCEDSTATUSCODES
250 8BITMIME
```

Step 4. Leave politely without sending anything.

```text
QUIT
221 2.0.0 Bye
Connection closed by foreign host.
```

Step 5. Interpret. A successful greeting proves three things at once: the name resolved, a route exists, and something is listening on port 25. A refusal would have proved that the packet reached a machine that rejected it. A hang would have suggested a firewall dropping packets silently. This is why a Telnet client remains in every administrator's toolkit even though Telnet as a login service is obsolete.

### 4.5 Task: send one message by hand and watch every step

### 4.6 Implementation: a complete SMTP dialogue

Step 1. Connect and greet with EHLO.

```text
220 smtp.example.ac.ke ESMTP Postfix
EHLO workstation.example.ac.ke
250-smtp.example.ac.ke
250-PIPELINING
250-SIZE 10240000
250-STARTTLS
250 8BITMIME
```

Step 2. Give the sender address. This is the envelope sender and it is what a bounce would be returned to.

```text
MAIL FROM:<amina@example.ac.ke>
250 2.1.0 Ok
```

Step 3. Give the recipient address.

```text
RCPT TO:<brian@example.net>
250 2.1.5 Ok
```

Step 4. Ask to send the content, and note that 354 is not a success code: it is permission to continue.

```text
DATA
354 End data with <CR><LF>.<CR><LF>
```

Step 5. Send the headers, a blank line, the body, and the terminating line.

```text
From: Amina Wanjiku <amina@example.ac.ke>
To: Brian Otieno <brian@example.net>
Subject: Lab group meeting moved to Thursday
Date: Fri, 07 Nov 2025 09:20:15 +0300
Message-ID: <20251107092015.4821@example.ac.ke>

The group meeting has moved from Wednesday to Thursday 14:00.
Room remains LT-3.

Regards,
Amina
.
250 2.0.0 Ok: queued as 4Bv2k19XhQz3n
```

Step 6. Read the queue identifier and close.

```text
QUIT
221 2.0.0 Bye
```

Step 7. Explain. The blank line separates headers from body and is mandatory. The single full stop on a line by itself ends the content. The 250 after it means the server has accepted responsibility for the message and has given it an identifier that can be quoted when tracing it. Nothing in this dialogue proves delivery; it proves acceptance.

### 4.7 Task: collect mail with POP3 and see the mailbox change

### 4.8 Implementation: a short POP3 session

Step 1. Connect and authenticate. POP3 replies begin with a status word rather than a number.

```text
+OK Dovecot ready.
USER brian
+OK
PASS training-password-01
+OK Logged in.
```

Step 2. Ask for the mailbox summary and the size of each message.

```text
STAT
+OK 2 3204
LIST
+OK 2 messages:
1 1450
2 1754
.
```

The status line says there are two messages totalling 3204 bytes, and the list confirms that the two sizes add up to that total, which is a useful sanity check that the numbers mean what they appear to mean.

Step 3. Retrieve the first message and mark it for deletion.

```text
RETR 1
+OK 1450 octets
Return-Path: <amina@example.ac.ke>
From: Amina Wanjiku <amina@example.ac.ke>
Subject: Lab group meeting moved to Thursday
Date: Fri, 07 Nov 2025 09:20:15 +0300

The group meeting has moved from Wednesday to Thursday 14:00.
Room remains LT-3.
.
DELE 1
+OK Marked to be deleted.
```

Step 4. Close the session, which is the moment the deletion is committed.

```text
QUIT
+OK Logging out, messages deleted.
```

Step 5. Explain. The delete was a mark, not an erasure; had the connection dropped before the tidy close, the message would still be in the mailbox. This is the behaviour that makes POP3 safe against a flaky link, and it is also the reason a second device will not see the message afterwards.

### 4.9 Task: read the same mailbox with IMAP and see what is preserved

### 4.10 Implementation: an IMAP session with tags

Step 1. Log in. Each command carries a short tag, and the server repeats the tag in its reply so that a client can match answers to questions.

```text
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE] Dovecot ready.
a1 LOGIN brian training-password-01
a1 OK Logged in
```

Step 2. Select the inbox.

```text
a2 SELECT INBOX
* 2 EXISTS
* 0 RECENT
* OK [UNSEEN 1] First unseen.
* OK [UIDVALIDITY 1699012345] UIDs valid
* OK [UIDNEXT 118] Predicted next UID
a2 OK [READ-WRITE] Select completed
```

Step 3. Fetch only the flags, which shows that messages are stored on the server with their state attached.

```text
a3 FETCH 1 (FLAGS)
* 1 FETCH (FLAGS (\Seen))
a3 OK Fetch completed.
```

Step 4. Fetch only selected header fields, and peek so that viewing the headers does not change the read state.

```text
a4 FETCH 1 BODY.PEEK[HEADER.FIELDS (SUBJECT FROM DATE)]
* 1 FETCH (BODY[HEADER.FIELDS (SUBJECT FROM DATE)] {86}
Subject: Lab group meeting moved to Thursday
From: Amina Wanjiku <amina@example.ac.ke>
Date: Fri, 07 Nov 2025 09:20:15 +0300
)
a4 OK Fetch completed.
```

Step 5. Log out.

```text
a5 LOGOUT
* BYE Logging out
a5 OK Logout completed.
```

Step 6. Explain the contrast with POP3. The message was never removed from the server. Only a header fragment crossed the network. The read flag lives on the server, so a phone and a laptop would agree about it. A second device would see exactly the same two messages, whereas after the POP3 session it would have seen one.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to check that you understand the topic

You have understood the material when you can do all of the following without notes.

State what a port number is for, and give the port of each service in this topic. Explain why FTP needs two connections. Explain why passive mode exists, in terms of a home router. Describe what happens in a Telnet session and why it is unsafe on a shared network. Name the three parts of an email system and say which one talks to which. Recite the five statements of a mail delivery. Explain in one sentence why IMAP suits a person with two devices and POP3 does not. Say what a newsgroup is and what Gopher is, and give one thing each does that the other cannot.

### 5.2 Interpreting the messages you will see

A greeting code that begins with two means the service is alive. A code that begins with three means the server is waiting for you to supply something. A code that begins with four means a temporary problem, and the same command may succeed in a minute. A code that begins with five means a permanent refusal, and repeating the command will produce the same refusal.

A connection refused, arriving immediately, means the machine is reachable but nothing is listening on that port. A connection that hangs and then times out usually means a firewall is discarding the packets without answering. These two failures look similar on screen and have completely different causes, which is why the delay before the error is worth noticing.

A file transfer that reports completion but produces a file that will not open is almost always a mode error: a binary file sent in text mode. This is the single most common fault in an FTP exercise, and it produces no error message at all because both sides believed they had succeeded.

### 5.3 Beginner misconceptions

- **"The port number is part of the address."** It identifies a service on the machine, not the machine. The address gets the packet to the computer; the port gets it to the program.
- **"FTP is one connection."** FTP uses two, a control channel and a data channel, which is why firewalls have to be told about it specially.
- **"Active mode is the modern default."** Passive mode is the default in practice, precisely because active mode fails behind the routers everyone uses.
- **"Telnet is just an old version of SSH."** They do the same job, but Telnet has no encryption and no server authentication, so it is a different class of risk rather than an older release.
- **"Email is sent straight to the recipient's computer."** It is passed between servers and stored until collected. The recipient's device need not even be switched on.
- **"SMTP sends and receives mail."** SMTP only pushes mail toward a server. Reading it back needs a retrieval protocol.
- **"POP3 and IMAP are two names for the same thing."** They make opposite assumptions about where the mailbox lives.
- **"IMAP downloads the whole mailbox when you open it."** It fetches summaries and then pieces, which is the point of the protocol.
- **"UseNet is the same as the web."** It is a separate system with its own protocol and its own servers, and it predates the web.
- **"Gopher was a search engine."** It was a menu-based document service; searching was one item type within it, not its purpose.
- **"Deleting a message in POP3 deletes it immediately."** It is marked, and the mark takes effect at the tidy close.
- **"Encryption makes FTP into SFTP."** FTPS is FTP over an encrypted channel; SFTP is a different protocol that runs inside SSH.

### 5.4 Key takeaways

A service is a program waiting on a numbered port. Protocols are published agreements, and their commands are short, human-readable words. FTP separates commands from data, and the direction of the data connection decides whether a firewall will allow it. Telnet is a plaintext remote terminal and SSH is its encrypted replacement. Email separates composition, transfer, storage and retrieval, and each part has its own protocol. SMTP pushes with five statements and a terminating full stop. POP3 collects and clears, IMAP synchronises and preserves. UseNet distributes articles between servers, and Gopher serves menus one request at a time.

All of the older protocols in this topic share one weakness, and it is worth stating plainly: they were designed for a small, trusted research network and they send credentials in readable text. Where a secure successor exists, the successor should be used, and the reason is encryption rather than fashion.

