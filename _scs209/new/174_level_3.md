## 1. Concept and Use Case

### 1.1 What this topic is examined for

Questions on Internet services and application-layer protocols are almost never about history. They test four abilities, and every past-style question maps onto one of them.

The first is **recall of a numbered fact**: a default port, a protocol's standard number, a command name, a reply code's meaning. These marks are cheap and are lost through carelessness rather than ignorance.

The second is **description of an architecture**: how many connections a protocol uses, which side opens each, which component holds which state, and where a message is stored at each stage. These answers are marked by counting named components and stated relationships.

The third is **comparison**: POP3 against IMAP, active against passive mode, Telnet against SSH. These are marked by counting distinct, correct points of difference, so a candidate who writes one long paragraph usually scores less than one who writes six labelled points.

The fourth is **applied reasoning**: given a symptom, name the cause; given a requirement, choose the protocol and justify it. These marks are awarded for the link between the fact and the scenario.

### 1.2 The scope, reduced to one page

Seven services are examinable. **File Transfer Protocol** moves files, uses two TCP connections, and runs on port 21 for control and port 20 for data in active mode. **Telnet** provides a remote terminal on port 23 and is unencrypted. **Electronic mail** is an architecture of user agents, submission agents, transfer agents, delivery agents and message stores. **SMTP** transmits mail on port 25 and accepts authenticated submission on port 587. **POP3** collects mail on port 110 and **IMAP** synchronises mail on port 143. **UseNet** distributes news articles between servers by NNTP on port 119. **Gopher** serves menus and documents on port 70.

The secure variants complete the picture and are worth one mark each in a security question: FTPS and SFTP for FTP, SSH for Telnet, POP3S on 995 and IMAPS on 993 for retrieval, and submission with TLS on 465 or 587 for sending.

### 1.3 Where the marks actually sit

An analysis of how these questions are marked shows a consistent pattern. Roughly forty per cent of marks are for naming the correct protocol or port. Roughly thirty per cent are for the sequence of steps in a session or a delivery. Roughly twenty per cent are for a stated reason or consequence. The remaining ten per cent are for correct use of terminology, which is to say for not writing "the FTP server sends the file down the same pipe".

That distribution tells you how to budget an answer. Naming comes first because it is fastest. Sequences come second because they are mechanical once memorised. Reasons come third, and they are what separate a pass from a distinction.

### 1.4 The four motifs that generate reasons

Almost every "explain why" or "give one reason" mark can be earned from one of four motifs, so learning them is more efficient than memorising explanations protocol by protocol.

**Out-of-band control.** FTP uses a separate control connection so that commands such as abort remain usable while a large transfer saturates the data connection, and so that the two channels can have different settings.

**Push versus pull.** SMTP pushes from sender to recipient; POP3 and IMAP pull from server to client. A push protocol cannot serve a device that is switched off, and a pull protocol cannot deliver to a server that does not know the message exists.

**Store-and-forward.** Mail is accepted, stored and forwarded later, which decouples the availability of sender and recipient and makes acceptance different from delivery.

**Stateful sessions.** Each protocol defines states and only accepts commands valid in the current state, which is why a correct answer describes order rather than listing commands.

### 1.5 Scenarios that the questions are built from

An examiner rarely asks for a protocol in the abstract. The question is dressed as a situation, and the situation contains the constraint that selects the answer.

A student must upload a 200 MB project to a department server from home, behind a router that performs address translation. The constraint is the router, so the answer must be passive mode, and the reason is that active mode requires the server to open a connection back to a private address.

An administrator must manage a switch in a remote building across an untrusted network. The constraint is the untrusted path, so the answer is SSH and the reason is encryption plus server authentication; Telnet sends the password in clear text.

A lecturer wants the same mailbox on a laptop, a phone and a webmail page, with read state preserved. The constraint is multiple devices, so the answer is IMAP and the reason is that folders and flags live on the server.

A department wants a local archive of course announcements that readers can browse by subject. The constraint is group discussion with local retention, which points at a newsgroup, not at mail.

An old documentation server presents numbered menus with no hyperlinks. The description identifies Gopher, and the reason is that a Gopher menu is self-describing while a document in that system cannot link to another document.

## 2. Data, Syntax, and Core Concepts

### 2.1 High-yield facts and the marks they carry

The following facts are the ones that appear most often, with the mark value a typical question attaches to each. Learn them as a set; each is worth one or two marks on its own, and the set is worth most of a short-answer paper.

| Fact | Typical marks |
|---|---|
| FTP uses two TCP connections, control on 21 and data on 20 in active mode | 2 |
| The client opens the control connection; the server opens the data connection in active mode | 2 |
| In passive mode the client opens both connections; the server announces the port with 227 | 2 |
| FTP reply codes are three digits, and the first digit gives the class | 1 |
| 150 means the data connection is opening; 226 means the transfer completed | 2 |
| 530 means not logged in; 550 means the file is unavailable | 2 |
| Telnet runs on port 23 and provides remote terminal emulation through a network virtual terminal | 2 |
| Telnet is unencrypted, so credentials and session data are readable on the path | 2 |
| SSH on port 22 is the secure replacement for Telnet | 1 |
| The mail architecture has a user agent, a transfer agent and a message store | 3 |
| SMTP pushes mail on port 25 between servers | 1 |
| SMTP commands in order are EHLO, MAIL FROM, RCPT TO, DATA, QUIT | 3 |
| A single full stop on a line ends the message content | 1 |
| POP3 runs on port 110 and downloads then deletes by default | 2 |
| IMAP runs on port 143 and keeps the mailbox on the server | 2 |
| UseNet uses NNTP on port 119 and distributes articles between servers | 2 |
| Gopher uses port 70 and returns menus whose lines carry an item type | 2 |
| FTP and Telnet are insecure because they have no encryption; SFTP, FTPS and SSH replace them | 3 |

### 2.2 The port numbers, with the trap in each

Ports are the easiest marks in the topic and the easiest to lose. The full set follows, with the mistake that candidates actually make beside each.

| Service | Port | The trap |
|---|---|---|
| FTP control | 21 | Candidates write 20 because they remember that FTP has a data port |
| FTP data, active mode | 20 | Writing 21 here, which reverses the pair |
| SSH | 22 | Confusing 22 with 23, or with SFTP, which also uses 22 |
| Telnet | 23 | Writing 22 because SSH is "the same service" |
| SMTP | 25 | Writing 587 for server-to-server relay |
| SMTP submission | 587 | Writing 25 for authenticated client submission |
| DNS | 53 | Writing 80 or 43 |
| HTTP | 80 | Writing 8080, which is a common alternate but not the default |
| POP3 | 110 | Writing 143 |
| NNTP | 119 | Writing 25 or 110 |
| IMAP | 143 | Writing 110 |
| HTTPS | 443 | Writing 8443 |
| SMTPS | 465 | Writing 25 with "encryption" and leaving it there |
| IMAPS | 993 | Writing 143 and calling it secure |
| POP3S | 995 | Writing 110 and calling it secure |

Two rules remove most of the confusion. The two FTP numbers are adjacent and the control port is the higher one, which is counter-intuitive until you remember that the control connection is the one that stays open and was chosen first. And every secure mail port is the plaintext port plus a distinctive offset that must be learned as a pair: 110 becomes 995, 143 becomes 993. Writing "port 143 with TLS" for IMAPS is a mark lost, because 143 with negotiated TLS is a different service from 993 with TLS from the first byte.

### 2.3 FTP facts worth memorising

The FTP architecture has four named components and an examination answer should name all four. On the client there is a user interface, a **protocol interpreter** and a **data transfer process**. On the server there is a protocol interpreter and a data transfer process, one of each per session.

| Component | Function |
|---|---|
| Client user interface | Accepts typed commands or drives the protocol from a program |
| Client protocol interpreter | Interprets commands, manages session state, sends the data connection request |
| Client data transfer process | Reads and writes the file on the data connection |
| Server protocol interpreter | Authenticates the user, validates commands, reports status |
| Server data transfer process | Reads and writes the file on the data connection |

The commands that appear in questions, grouped by purpose, are these.

| Purpose | Commands | Note for answers |
|---|---|---|
| Authenticate | USER, PASS, ACCT | 331 follows USER, 230 follows PASS |
| Set representation | TYPE A, TYPE I | ASCII for text, image for binary |
| Choose data connection | PORT, PASV, EPRT, EPSV | PORT is active, PASV is passive |
| Move files | RETR, STOR, APPE, REST, ABOR | RETR is download, STOR is upload |
| Navigate | CWD, CDUP, PWD, LIST, NLST | LIST opens a data connection |
| Change the file system | DELE, RNFR, RNTO, MKD, RMD | RNFR followed by RNTO to rename |
| End | QUIT | Answered with 221 |

The reply codes that earn marks, with the reason they are quoted, are these.

| Code | Meaning | Why it is quoted in an answer |
|---|---|---|
| 220 | Service ready | Proves the control connection opened |
| 331 | Password required | Proves the user name was accepted |
| 230 | Logged in | Proves authentication succeeded |
| 227 | Entering passive mode | Proves the server nominated the data port |
| 150 | About to open the data connection | Proves the data channel is being established |
| 226 | Transfer complete | Proves the data channel closed cleanly |
| 425 | Cannot open the data connection | Proves the data channel failed while control survived |
| 530 | Not logged in | Proves a state error |
| 550 | File unavailable | Proves a permanent file-system refusal |

### 2.4 Telnet facts worth memorising

Telnet is defined in Request for Comments 854 and runs on port 23. Its central abstraction is the **network virtual terminal**, a notional terminal whose conventions both ends convert to, so that a client and a server built for different real terminals can interoperate. Control functions such as interrupt, abort and break are distinguished from data by the **interpret as command** byte, decimal 255, and a literal 255 in the data is doubled.

Options are negotiated in both directions with WILL, DO, WONT and DONT, so nothing is enabled until both sides agree. Terminal type and window size are exchanged as subnegotiations. The client may operate in character-at-a-time mode, in which each keystroke is sent immediately, or in line mode, in which a line is edited locally and sent on Enter.

| Point | Marks |
|---|---|
| Port 23, TCP | 1 |
| Remote terminal emulation of a network virtual terminal | 1 |
| Option negotiation with WILL, DO, WONT, DONT | 1 |
| No encryption and no server authentication, so the password is readable on the wire | 1 |
| Replacement is SSH on port 22, with SFTP for file transfer over the same channel | 1 |

### 2.5 The mail architecture, as an examinable list

Five roles, each with a one-line definition, is the answer shape that scores full marks.

| Role | Definition | Protocol or port |
|---|---|---|
| Mail user agent | The program the person uses to compose and read mail | Submits with SMTP on 587, retrieves with POP3 on 110 or IMAP on 143 |
| Mail submission agent | Accepts authenticated mail from a user agent | SMTP on 587 |
| Message transfer agent | Moves messages between domains and queues what it cannot deliver | SMTP on 25 |
| Mail delivery agent | Writes the message into the recipient's store, applying filters | Local, no network port |
| Message store | The durable container holding delivered mail, organised into mailboxes | Read by POP3 or IMAP |

Two further distinctions earn marks in longer answers. The **envelope** is the pair of addresses in MAIL FROM and RCPT TO and is what servers route on; the **header** is the visible From, To, Cc and Subject and is what the reader sees. And message **format** is separate from message **transfer**: the format defines headers and body under Request for Comments 5322, and MIME adds Content-Type and Content-Transfer-Encoding so that attachments and character sets survive a seven-bit transport.

### 2.6 The SMTP dialogue as a fixed sequence

This sequence is worth writing out until it is automatic, because it answers describe, explain and trace questions simultaneously.

| Step | Client sends | Server replies | Meaning |
|---|---|---|---|
| 1 | connection opened | 220 | Service ready |
| 2 | EHLO client domain | 250, then the extension list | Session opened, extensions available |
| 3 | MAIL FROM with the envelope sender | 250 | Envelope sender accepted |
| 4 | RCPT TO for each recipient | 250 or 550 per recipient | Per-recipient acceptance or refusal |
| 5 | DATA | 354 | Permission to send content |
| 6 | headers, blank line, body, full stop line | 250 with a queue identifier | Content accepted and queued |
| 7 | QUIT | 221 | Session closed |

The details that earn the second mark in a part question are these. A reply beginning with 4 is transient and the sender must retry later; a reply beginning with 5 is permanent and the sender must bounce the message to the envelope sender. A body line that begins with a full stop is sent with an extra full stop and the receiver removes one, which is dot-stuffing. Each transfer agent prepends a Received header, so the delivered copy carries the whole path in reverse order.

### 2.7 POP3 and IMAP facts, reduced to answers

POP3 has three states and the name of each is worth a mark. In the **authorization** state the client supplies credentials. In the **transaction** state it lists and retrieves messages and marks them for deletion. In the **update** state, entered only when the client sends QUIT, the marks are committed. Replies are a status word rather than a number: plus, OK for success and a minus sign with ERR for failure.

| POP3 command | Effect |
|---|---|
| USER and PASS | Authenticate |
| STAT | Report the count and total size |
| LIST | Report the size of each message |
| RETR | Retrieve one whole message |
| TOP | Retrieve headers and a stated number of body lines |
| DELE | Mark for deletion |
| RSET | Remove all deletion marks |
| UIDL | Report a persistent identifier for each message |
| QUIT | Commit deletions and close |

IMAP has four states: not authenticated, authenticated, selected, and logout. Every client command carries a tag; replies are tagged with that tag, or untagged with an asterisk. The commands that a question is likely to want named are LOGIN, SELECT, FETCH, STORE, EXPUNGE and LOGOUT.

| IMAP command | Effect |
|---|---|
| LOGIN | Authenticate |
| SELECT | Open a mailbox read-write and report its status |
| EXAMINE | Open a mailbox read-only |
| FETCH | Retrieve flags, headers or body parts |
| STORE | Change flags, including the deleted flag |
| EXPUNGE | Permanently remove messages marked deleted |
| APPEND | Add a message to a mailbox |
| LOGOUT | End the session |

The two commands that implement deletion must not be merged in an answer. STORE sets the deleted flag; EXPUNGE removes flagged messages. This separation is what allows an undo, and it is a favourite one-mark distinction.

### 2.8 POP3 against IMAP, as a scored comparison

| Dimension | POP3 | IMAP |
|---|---|---|
| Default port | 110, with 995 for TLS from the first byte | 143, with 993 for TLS from the first byte |
| Model | Download and delete | Remote mailbox that is synchronised |
| Where mail is stored | On the collecting device | On the server |
| Folders | Local to the client | Server-side |
| Read and answered flags | Local, so devices disagree | Server-side, so devices agree |
| Multiple devices | Inconsistent | Consistent |
| Partial retrieval | Headers plus a few lines with TOP | Any header field or body part with FETCH |
| Server storage | Small after collection | Whole mailbox |
| Offline use | Natural, since mail is local | Needs a local cache |
| Session states | Authorization, transaction, update | Not authenticated, authenticated, selected, logout |

A comparison question normally carries eight to ten marks and awards about one mark per row that is stated correctly and in the candidate's own words. Six rows, each a sentence, is a safe full-mark answer; one paragraph of prose is not.

### 2.9 UseNet and Gopher facts

UseNet is a distributed discussion system in which servers exchange articles in named groups. The protocol is the **network news transfer protocol** on port 119. An article carries a Message-ID that is unique across the whole system, a Path header listing the servers it has crossed, and a References header naming the article it answers. Group names are hierarchical with the general category first, and the principal hierarchies are computing, science, recreation, social issues, debate, news about the network itself, miscellaneous and humanities. A group is moderated or unmoderated, and articles travel between servers by being offered and accepted rather than by being broadcast to clients.

Gopher is a menu-based retrieval protocol on port 70, defined in Request for Comments 1436. A client sends a selector and receives either a menu or a document, with no session state kept between requests. A menu line carries five tab-separated fields: an item type character, a display string, a selector, a host and a port. The item type is what makes the protocol self-describing: type 0 is a text file, type 1 is a menu, type 7 is a search server and type 9 is a binary file. Search indexes over Gopher menus were called Veronica and Jughead.

| Question cue | Answer |
|---|---|
| "Menu-driven information service" | Gopher, port 70, item type characters |
| "Distributed bulletin board of discussion groups" | UseNet, NNTP, port 119 |
| "Why did hypertext beat menus" | A menu can point outward, but a document cannot link to another document |
| "How are loops prevented in news propagation" | The Message-ID plus a history file on each server, and the Path header |

### 2.10 Definitions that earn a mark each

A **protocol** is an agreed set of rules for the format and order of messages exchanged between two programs. A **port number** identifies a service on a host, so that one address can carry many services. **Out-of-band control** means that control information travels on a channel separate from the data it controls. **Store-and-forward** means that a node accepts a message, stores it durably and forwards it later, so acceptance is not delivery. **Dot-stuffing** is the doubling of a leading full stop on a content line so that it cannot be mistaken for the end of the message. A **spool** is a holding area for messages awaiting delivery or collection. An **open relay** is a mail server that forwards mail for domains it does not own without requiring authentication. A **network virtual terminal** is the notional terminal whose conventions both ends of a Telnet session convert to and from.

### 2.11 Request for Comments numbers worth one mark

The numbers are occasionally asked directly. FTP is 959. Telnet is 854. SMTP is 5321, with the message format in 5322. POP3 is 1939. IMAP version 4 revision 1 is 3501. NNTP is 3977, superseding 977. Gopher is 1436. If a question asks only for the protocol's standard, the name of the document is enough; the number is a bonus.

## 3. Methods and Operations

### 3.1 The six question shapes you will meet

Almost every question on this topic is one of six shapes. Recognising the shape in the first ten seconds determines the structure of the answer, and structure is what a marker rewards when the mark scheme is a list.

**Shape one: name the protocol.** "Which protocol would you use to move a 500 MB file to a server, and on which port does it listen?" The answer names the protocol, gives the port, and adds one clause of justification. Two marks, thirty seconds.

**Shape two: describe an architecture.** "Describe the components of an electronic mail system." The answer is a list of named components, each with one sentence of function, and then one sentence on how they connect. Marks are counted per component.

**Shape three: describe a sequence.** "Describe what happens when a client retrieves mail with POP3." The answer is numbered steps in order, using the real command names. Order matters and is separately marked.

**Shape four: compare.** "Compare POP3 and IMAP." The answer is a table or a set of labelled points, each point stating both sides. Marks are counted per distinct dimension.

**Shape five: explain a consequence.** "Explain why active mode FTP fails when the client is behind a router." The answer states the mechanism, then the consequence, then the remedy. Three sentences, three marks.

**Shape six: diagnose.** "A user can log in to the FTP server but cannot list the directory. Give two possible causes." The answer gives causes that are consistent with the symptom, which in this case means causes that affect the data connection rather than the control connection.

### 3.2 Recipe cards: sequences to reproduce exactly

Four sequences answer most of the descriptive questions. Reproduce them with the real verbs, in order, and say what each reply means.

**FTP retrieval in passive mode.** Connect to port 21, read 220. USER, read 331. PASS, read 230. TYPE I, read 200. PASV, read 227 and decode the port. Connect to that port. RETR, read 150. Receive bytes. Read 226. QUIT, read 221.

**FTP retrieval in active mode.** Connect to port 21, read 220. USER and PASS as above. TYPE I. Open a local listening socket, then PORT with the address and port encoded as six numbers, read 200. RETR, read 150. Accept the incoming connection from the server's port 20. Receive bytes, read 226, QUIT.

**SMTP delivery.** Connect to port 25, read 220. EHLO, read 250 and the extension list. MAIL FROM, read 250. RCPT TO for each recipient, read 250 or 550 per recipient. DATA, read 354. Send headers, blank line, body, then a line with a single full stop. Read 250 and the queue identifier. QUIT, read 221.

**POP3 collection.** Connect to port 110, read the plus and OK greeting. USER, read plus OK. PASS, read plus OK. STAT, read the count and size. LIST, read the sizes. RETR for each message, reading until a line with a single full stop. DELE for each unwanted message. QUIT, which commits the deletions.

**IMAP retrieval.** Connect to port 143, read the untagged OK with capabilities. LOGIN with a tag, read the tagged OK. SELECT the inbox, read the untagged EXISTS, RECENT and the tagged OK. FETCH with flags and header fields, read the untagged FETCH and the tagged OK. STORE to change flags, read the tagged OK. LOGOUT, read the untagged BYE and the tagged OK.

### 3.3 The trap table

This is the table to read twice. Each row is a statement that sounds right, is written by many candidates, and loses marks.

| Trap | Why it is wrong | Write this instead |
|---|---|---|
| "FTP uses port 21." | It uses 21 for control and 20 for data in active mode | "FTP uses TCP 21 for control and TCP 20 for data in active mode" |
| "The server always opens the data connection." | Only in active mode | "In active mode the server connects from port 20; in passive mode the client connects to the port announced in the 227 reply" |
| "Passive mode is faster." | It is not about speed | "Passive mode works through network address translation because the client initiates both connections" |
| "SMTP sends and receives mail." | SMTP only pushes | "SMTP transmits; POP3 or IMAP retrieves" |
| "Port 25 is used to send mail from a mail client." | Submission uses 587 with authentication | "Port 25 is relay between servers; port 587 is authenticated submission" |
| "A 250 reply means the mail was delivered." | It means accepted and queued | "250 means the server has taken responsibility; delivery is confirmed only by the absence of a bounce" |
| "354 means the message was accepted." | 354 is permission to send | "354 means begin the content and end with a full stop line" |
| "The To header is the address used for routing." | Routing uses the envelope | "MAIL FROM and RCPT TO form the envelope; To is a header field the reader sees" |
| "POP3 deletes the message when DELE is sent." | It marks; deletion is committed in the update state | "DELE marks; the update state on QUIT commits" |
| "IMAP downloads the whole mailbox." | It fetches structures and parts | "IMAP fetches flags and headers first, then body parts on demand" |
| "IMAP's message numbers are permanent." | Sequence numbers change after expunge | "UIDs are permanent; sequence numbers are relative to the selected mailbox" |
| "STORE deletes a message." | STORE sets a flag | "STORE sets the deleted flag; EXPUNGE removes flagged messages" |
| "Telnet is insecure because it is old." | Age is not the reason | "Telnet has no encryption and no server authentication, so credentials and session data are readable and the server can be impersonated" |
| "FTPS and SFTP are the same." | Different protocols | "FTPS is FTP wrapped in TLS; SFTP is a file transfer subsystem carried inside SSH on port 22" |
| "UseNet is part of the web." | Separate network and protocol | "UseNet is a store-and-forward news system using NNTP on port 119" |
| "Gopher is a search engine." | It is a menu protocol | "Gopher serves menus and documents on port 70; search was one item type" |
| "Secure mail uses the same port with encryption switched on." | Secure variants have their own ports | "POP3S is 995 and IMAPS is 993; STARTTLS on 110 or 143 is a different arrangement" |
| "A DNS MX record names the mailbox." | It names a mail exchanger | "An MX record names a host that accepts mail for the domain, with a preference value" |

### 3.4 How to lay out a comparison answer

A comparison question is marked against a list of dimensions, so present the answer as a list of dimensions. The order that covers the most mark schemes is: purpose, port, model of storage, what happens to the message, multi-device behaviour, state kept by the server, and security.

Write each point as a matched pair, so that the marker can see both sides in one line. "POP3 downloads each message to the device and by default deletes it from the server, whereas IMAP leaves the message on the server and keeps a synchronised view on each device." That sentence alone usually carries two marks, because it states the storage model and the consequence.

Do not waste time on a hand-drawn table if ruled lines are not provided. A bulleted list of matched pairs scores identically, and it is safer under time pressure.

### 3.5 Describing an architecture in prose, without a figure

Some questions say "with the aid of a diagram", and some do not allow one. When a diagram is not available, describe the architecture as a chain of custody, which the marker can follow.

Start with the sender's user agent and what it produces. Then say which server receives it and on which port, and what that server adds. Then say how the recipient domain is found and which protocol carries the message onward. Then say who writes the message into the store and in what form. Then say which protocol the recipient's client uses to read it, and what state that protocol keeps. Every stage has an owner, an input, an output and a port, and stating all four for each stage is the prose equivalent of a diagram.

### 3.6 Budgeting words per mark

A one-mark fact needs one clause. A two-mark fact needs a clause and a reason. A four-mark description needs four named items. A six-mark explanation needs three mechanisms and three consequences. As a rough calibration, one mark is worth about twenty-five words of correct content, so a ten-mark answer is roughly two hundred and fifty words of substance, not six hundred words of introduction. Candidates lose more marks to padding that crowds out later questions than to brevity.

## 4. Worked Implementation from the Notes

### 4.1 Task: a ten-mark question on FTP modes

Question: "Describe the File Transfer Protocol, explaining the difference between active and passive mode. Illustrate your answer with the commands exchanged. (10 marks)"

### 4.2 Implementation: model answer built step by step with marking points

Step 1. Define the protocol and its transport. FTP is an application-layer protocol for transferring files between a client and a server over TCP, defined in Request for Comments 959. **1 mark** for the purpose and **1 mark** for TCP.

Step 2. State the two-channel architecture. FTP uses two connections: a control connection to server port 21 that carries commands and replies and stays open for the whole session, and a data connection that carries file content or directory listings and is opened and closed per transfer. This is out-of-band control. **2 marks**, one for each connection being named with its port and role.

Step 3. Give the reason for the split. Keeping instructions off the data channel means a command such as ABOR remains usable while a large transfer saturates the data connection, and the two channels can use different representations, such as ASCII on the control channel and binary on the data channel. **1 mark**.

Step 4. Show the login and preparation sequence with real verbs and codes.

```text
220 (vsFTPd 3.0.5)
USER student
331 Please specify the password.
PASS training-password-01
230 Login successful.
TYPE I
200 Switching to Binary mode.
```

**1 mark** for the correct verbs and codes in the correct order.

Step 5. Describe active mode concretely. The client opens a listening socket and sends its address and port with the PORT command, encoded as six decimal numbers. The server opens the data connection from its own port 20 to that address and port.

```text
PORT 192,168,1,24,196,52
200 PORT command successful.
150 Here comes the directory listing.
226 Directory send OK.
```

The encoded port is 196 times 256 plus 52, which is 50228. **2 marks**, one for the client advertising its port and one for the server connecting from port 20.

Step 6. Describe passive mode concretely and contrast the direction. The client sends PASV, the server opens a listening port and announces it in a 227 reply, and the client opens the data connection to that port.

```text
PASV
227 Entering Passive Mode (203,0,113,9,195,84).
150 Opening BINARY mode data connection for toolkit.zip (7340032 bytes).
226 Transfer complete.
```

The announced port is 195 times 256 plus 84, which is 50004. **2 marks**, one for the server nominating the port and one for the client initiating the connection.

Step 7. State the operational consequence, which is the part that distinguishes a full-mark answer. Active mode fails when the client is behind network address translation or a stateful firewall, because the address the client advertises is private and the inbound connection the server attempts is discarded. Passive mode works in that situation because both connections are outbound from the client, at the cost of requiring the server's firewall to permit its passive port range. **1 mark** for the consequence, giving ten in total.

### 4.3 Task: a twelve-mark question on the mail architecture

Question: "Describe the architecture of an electronic mail system and trace the delivery of a message from sender to recipient, naming the protocols and ports used at each stage. (12 marks)"

### 4.4 Implementation: model answer as a chain of custody

Step 1. Name the five components and their functions. A user agent is the program the person uses to compose and read. A submission agent accepts authenticated mail from the user agent. A message transfer agent moves mail between domains and queues undeliverable mail. A delivery agent writes mail into the store. The message store holds delivered mail in mailboxes. **3 marks**, one per component correctly defined, up to three.

Step 2. State the separation of transmission from retrieval and why it exists. Transmission pushes toward a server that is always available; retrieval pulls toward a device that may be switched off. Merging them would force the always-on server to act as a client. **1 mark**.

Step 3. Begin the trace with submission. The user agent hands the message to the provider's submission agent on TCP port 587, authenticating first and upgrading to encryption with STARTTLS. **1 mark** for port 587 and authentication.

Step 4. Continue with domain resolution. The submission agent, or the transfer agent acting for it, queries DNS on port 53 for the MX records of the recipient's domain and sorts them by preference. **1 mark** for MX resolution.

Step 5. Show the SMTP dialogue to the recipient's exchanger on port 25.

```text
220 smtp.example.net ESMTP Postfix
EHLO mx.example.ac.ke
250-smtp.example.net
250-SIZE 10240000
250-STARTTLS
250 8BITMIME
MAIL FROM:<amina@example.ac.ke>
250 2.1.0 Ok
RCPT TO:<brian@example.net>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Subject: Lab group meeting moved to Thursday
Date: Fri, 07 Nov 2025 09:20:15 +0300
Message-ID: <20251107092015.4821@example.ac.ke>

The group meeting has moved to Thursday 14:00.
.
250 2.0.0 Ok: queued as 4Bv2k19XhQz3n
QUIT
221 2.0.0 Bye
```

**3 marks**, one for the correct command order, one for the meaning of 354 and the terminating full stop, and one for the meaning of the final 250.

Step 6. Distinguish the envelope from the header. MAIL FROM and RCPT TO form the envelope used for routing and bounces; the From and To lines are header fields the reader sees, and they may legitimately differ, for example after list rewriting. **2 marks**.

Step 7. Complete the trace with delivery and retrieval. The delivery agent writes the message into the recipient's store, each server having prepended a Received header. The recipient's client then retrieves with POP3 on port 110, which downloads and by default deletes, or with IMAP on port 143, which leaves the message on the server and synchronises flags and folders. **1 mark** for delivery into the store, giving twelve in total; the retrieval point is often carried as a bonus mark when the question asks for the reader's side.

### 4.5 Task: an eight-mark comparison of retrieval protocols

Question: "Compare the Post Office Protocol version 3 with the Internet Message Access Protocol, indicating the situation in which each is appropriate. (8 marks)"

### 4.6 Implementation: model answer as matched pairs

Step 1. State the purpose of both. Both allow a mail client to read a mailbox held on a server; they differ in where the mailbox is considered to live. **1 mark**.

Step 2. Give the ports. POP3 uses TCP 110, or 995 with TLS from the first byte; IMAP uses TCP 143, or 993 with TLS from the first byte. **1 mark**.

Step 3. Contrast the storage model. POP3 downloads each message to the device and by default deletes it from the server when the session closes normally; IMAP leaves messages on the server and fetches only what is needed. **1 mark**.

Step 4. Contrast the treatment of state. POP3 keeps no folders or flags on the server, so read and answered marks are local to each device; IMAP stores folders and flags on the server, so every device sees the same view. **1 mark**.

Step 5. Contrast partial retrieval. POP3 can fetch headers and a few body lines with TOP; IMAP can fetch any header field or body part with FETCH, which makes it usable on large messages over slow links. **1 mark**.

Step 6. Contrast the session machinery. POP3 has three states, authorization, transaction and update, and one command at a time; IMAP has four states and tagged commands, so a client can pipeline and can receive unsolicited updates. **1 mark**.

Step 7. Show the behavioural difference concretely with two short sessions.

```text
+OK Dovecot ready.
USER brian
+OK
PASS training-password-01
+OK Logged in.
STAT
+OK 2 3204
DELE 1
+OK Marked to be deleted.
QUIT
+OK Logging out, messages deleted.
```

After that session a second client sees an empty mailbox. The IMAP equivalent leaves the message in place and only changes a flag.

```text
a1 LOGIN brian training-password-01
a1 OK Logged in
a2 SELECT INBOX
* 2 EXISTS
a2 OK [READ-WRITE] Select completed.
a3 STORE 1 +FLAGS (\Seen)
* 1 FETCH (FLAGS (\Seen))
a3 OK Store completed.
a4 LOGOUT
a4 OK Logout completed.
```

**1 mark** for demonstrating the difference in behaviour rather than only asserting it.

Step 8. State the appropriate situations. POP3 suits a single device on a metered or intermittent link, and archival scripts that collect and clear a mailbox. IMAP suits a user with several devices, a large mailbox, server-side folders, and shared or web access. **1 mark**, giving eight in total.

### 4.7 Task: a six-mark question on Telnet and its risks

Question: "Describe the Telnet protocol and explain two security weaknesses. Name a replacement and state one advantage it provides. (6 marks)"

### 4.8 Implementation: model answer with evidence

Step 1. Define the service. Telnet provides remote terminal emulation: it lets a user log in to a remote computer and use its command line as though the keyboard and screen were attached locally. **1 mark**.

Step 2. Give the port and the key abstraction. It uses TCP port 23 and is built around a network virtual terminal, a notional terminal whose conventions both ends convert to, so that differing real terminals can interoperate. Options such as echo, terminal type and window size are negotiated with WILL, DO, WONT and DONT, and the interpret-as-command byte, decimal 255, separates control from data. **1 mark**.

Step 3. Show a session, which makes the first weakness visible.

```text
Trying 198.51.100.7...
Connected to lab-switch-01.
login: admin
Password:
lab-switch-01>
```

**1 mark** for a correct session shape.

Step 4. State the first weakness with its evidence. There is no encryption, so the user name and password cross the network as readable text. A capture of the same session shows the credential in the payload.

```text
10:14:02.118 IP 198.51.100.22.49152 > 198.51.100.7.23: Flags [P.], length 6
..... admin
10:14:05.402 IP 198.51.100.22.49152 > 198.51.100.7.23: Flags [P.], length 24
.....Summer2025!
```

**1 mark**.

Step 5. State the second weakness. There is no cryptographic authentication of the server and no integrity protection, so an attacker on the path can impersonate the device, and can alter commands in transit without detection. **1 mark**.

Step 6. Name the replacement and its advantage. SSH on TCP port 22 encrypts the whole session, authenticates the server with a host key, and protects integrity; SFTP carries file transfer over the same channel, and FTPS provides encryption for FTP workflows that must be retained. **1 mark**, giving six in total.

### 4.9 Task: a five-mark question on news and Gopher

Question: "Describe two information retrieval systems that predate the World Wide Web, stating the protocol and port used by each. (5 marks)"

### 4.10 Implementation: model answer with a real exchange

Step 1. Describe UseNet. UseNet is a distributed discussion system: articles are posted into named hierarchical groups and copied between servers, and readers attach at the edge with a newsreader. **1 mark**.

Step 2. Give its protocol and port. Articles move by the network news transfer protocol on TCP port 119, with a secure variant on 563. **1 mark**.

Step 3. Demonstrate a news exchange.

```text
200 news.example.ac.ke InterNetNews NNTP server ready
MODE READER
200 Reader mode, posting permitted
GROUP comp.protocols.tcp-ip
211 1523 4021 5543 comp.protocols.tcp-ip
OVER 5541-5541
224 Overview information follows
5541	Re: Port 21 versus port 20	Brian Otieno <brian@example.net>	412	18
.
QUIT
205 closing connection
```

**1 mark** for a correct command and reply pair.

Step 4. Describe Gopher. Gopher presents information as menus; each choice opens another menu, a document, a search service or a binary file, and each menu line is self-describing with an item type character. **1 mark**.

Step 5. Give its protocol and port, and the reason for its decline. It uses TCP port 70, defined in Request for Comments 1436. Its menu lines carry five tab-separated fields, type, display string, selector, host and port, which allows a menu to point at another server, but a document within Gopher cannot link to another document, and that is the limitation hypertext removed. **1 mark**, giving five in total.

## 5. Testing, Interpretation, and Common Errors

### 5.1 What the marker rewards, stated plainly

Mark schemes for this topic are lists. They reward named protocols, correct ports, ordered command sequences, stated consequences and correct technical vocabulary. They do not reward introduction, background about the history of the Internet, or restatement of the question.

Three practical rules follow. Put the named fact in the first clause of each point, because a marker scanning for keywords finds it there. Never write a point that contains no fact, such as a sentence about how important email has become. And if you run out of knowledge on a sub-part, write the ports and the command names you do know, because they carry marks even without explanation.

### 5.2 Time strategy

In a paper where this topic is one of several, allocate time by marks rather than by difficulty. A workable rule for a three-hour paper is one minute per mark plus ten minutes of reading time, which gives roughly ten minutes for a ten-mark question and twelve for a twelve-mark question.

Spend the first ninety seconds of each answer writing a skeleton: the headings of the points you intend to make. A skeleton converts a vague answer into a counted one, and it prevents the common failure of writing three points well and running out of time for the other five.

If a question offers a choice, choose the one whose command sequence you can reproduce exactly. An answer with a correct dialogue and a thin explanation scores better than a fluent explanation with invented verbs.

Leave two minutes at the end of each answer to check every port number against the trap table in Section 3.3. Port errors are the single largest avoidable loss in this topic.

### 5.3 Revision checklist

Work through the list and tick only what you can produce without notes.

- Recite the port table, including the secure variants, from memory in under two minutes.
- Draw, or describe in words, the FTP two-channel architecture and say which side opens the data connection in each mode.
- Compute a port number from the six-number PORT argument, and from a 227 reply.
- Recite the FTP commands in the order used to log in and retrieve a file, with the reply code after each.
- State three reasons an FTP session can log in but fail to list a directory.
- Recite the SMTP dialogue from greeting to QUIT, with the code after each line.
- Explain dot-stuffing in one sentence and say why it is needed.
- Distinguish envelope from header with an example where they differ.
- Recite the five mail components and the protocol each speaks.
- Recite the three POP3 states and the command that causes each transition.
- Recite the four IMAP states and name the two commands used to delete a message.
- Produce ten matched pairs comparing POP3 and IMAP.
- State the Telnet port, the network virtual terminal, and two security weaknesses with their evidence.
- Name SSH, SFTP and FTPS and say exactly what each replaces.
- Describe UseNet propagation and the mechanism that prevents loops.
- Describe a Gopher menu line field by field and name four item types.
- Give the Request for Comments number for FTP, SMTP, POP3, IMAP, NNTP and Gopher.

### 5.4 The traps to re-read the night before

Read the trap table in Section 3.3 again rather than re-reading the whole note. The facts are usually known; the losses come from reversed port pairs, from treating 250 as delivery, from treating 354 as acceptance, and from describing Telnet's insecurity as a matter of age rather than of absent encryption and absent server authentication.

Two further traps are worth adding to that list because they appear in longer answers. First, a candidate who writes that passive mode is "more secure" has confused a firewall traversal property with a security property; passive mode is no more encrypted than active mode. Second, a candidate who writes that IMAP "stores mail on the client and synchronises" has the direction wrong; the authoritative copy is on the server and the client holds a cache.

### 5.5 Rapid self-test

Answer each in one line. If any answer takes more than five seconds, revise that row of the fact sheet.

1. Which port carries FTP control, and which carries data in active mode? Twenty-one and twenty.
2. Who opens the data connection in passive mode? The client.
3. What does 227 contain? The address and port the server has opened, encoded as six numbers.
4. Which command retrieves a file? RETR.
5. What does 150 mean? The data connection is about to open.
6. Which SMTP command carries the envelope sender? MAIL FROM.
7. What ends the content of a message? A line containing only a full stop.
8. What does a 4xx reply require? A retry later, because the failure is transient.
9. Which protocol retrieves mail and which transmits it? POP3 or IMAP retrieves; SMTP transmits.
10. Which port is authenticated submission? Five hundred and eighty-seven.
11. Which state commits POP3 deletions? The update state, entered on QUIT.
12. Which IMAP command removes messages marked deleted? EXPUNGE.
13. Which port serves IMAP with TLS from the first byte? Nine hundred and ninety-three.
14. Why is Telnet unsafe? Credentials and session data are unencrypted, and the server is not cryptographically authenticated.
15. What replaces Telnet, and on which port? SSH on twenty-two.
16. Which protocol distributes news articles? NNTP on one hundred and nineteen.
17. What does a Gopher item type of 1 mean? A menu or directory.
18. What prevents a news article from circulating forever? Its unique message identifier, checked against each server's history file, together with the path header.
19. Which record type locates a mail server? MX.
20. What is the difference between FTPS and SFTP? FTPS is FTP inside TLS; SFTP is file transfer inside an SSH channel on port 22.

### 5.6 Final note on interpretation

An answer is interpretable when a marker can count its points. Numbered steps, matched pairs and explicit ports make an answer countable. Prose that circles the right idea without naming it is not countable, and in a paper marked against a list, uncountable is unmarked. The habit worth building is to write the name first and the explanation second, in every sentence, for every mark.

