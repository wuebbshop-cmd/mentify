## 1. Concept and Use Case

### 1.1 The application layer as a set of agreements

Everything below the application layer moves bytes reliably or unreliably between two addresses. Nothing below it knows what the bytes mean. The meaning is supplied entirely by agreement between two programs, and that agreement is the application-layer protocol. A mail server and a mail client can be written by different organisations in different decades and still interoperate because both implement the same document, down to the wording of the commands and the numbering of the replies.

This topic covers the first generation of those agreements: file transfer, remote terminal access, mail transmission and retrieval, news distribution, and menu-driven information retrieval. They share a design idiom that is worth naming before any of them is examined individually, because the idiom explains most of the examination questions.

The idiom has four parts. Sessions are **textual**, so that a human can drive them by hand and a fault can be diagnosed by reading. Commands are **short imperative verbs** in upper case with space-separated arguments. Replies are **short lines beginning with a status token**, either a three-digit number in FTP or a keyword in the mail protocols. State is **held by the server across a sequence of commands**, which is why command order matters and why a command issued in the wrong state is rejected with a specific reply rather than ignored.

### 1.2 Why the client-server split is structural, not incidental

In every service here, the server process is long-lived, bound to a well-known port, and ignorant of which client will arrive. The client process is short-lived, chooses the server, and holds the session state that the server does not need to keep between sessions. This split exists because the two sides have different availability requirements.

A mail server must be reachable at all times, because a sender in another time zone cannot wait for the recipient to switch a laptop on. A mail client is available only when its user is. If the two roles were merged, either the recipient would have to remain online permanently, or messages would have to be held somewhere in the middle with no defined owner. The store-and-forward architecture exists precisely to decouple the two availabilities, and the split between transmission and retrieval protocols follows from it.

The same reasoning applies to file transfer and news. Files must be served from a machine that is up, so FTP puts the files on a server and the client pulls them. News articles must be propagated to every server that carries the group, so UseNet is a mesh of servers that push to one another, with readers attaching at the edge.

### 1.3 The foundational services and the problems they solved

**Electronic mail** solved asynchronous written communication between people who were not simultaneously present, on machines that were not simultaneously powered. It required, and produced, the concepts of the mailbox, the relay, and the return address.

**Telnet** solved remote operation of a machine without travelling to it. It required a standardised virtual terminal, because the terminals attached to the remote machine were diverse and the protocol had to hide that diversity.

**File Transfer Protocol** solved the movement of whole files between incompatible systems. It required a way to negotiate representation, which is why FTP has an explicit transfer type, an explicit file structure, and an explicit transmission mode rather than simply sending bytes.

**UseNet** solved group discussion at a scale no single machine could host, by copying articles between servers. It required a naming scheme for groups, an article identity that survives copying, and a loop-prevention mechanism.

**Gopher** solved navigable information retrieval before hypertext was widely implemented, by presenting a hierarchy of menus that any client could render.

**The World Wide Web** solved the cross-reference problem that Gopher's menus could not, by allowing a document to link directly to any other document.

### 1.4 The four architectural motifs examined in this topic

Almost every comparison question can be answered from one of four motifs. Learn them as motifs and the individual protocols stop being lists of facts.

**Out-of-band control.** FTP separates the channel that carries instructions from the channel that carries content, so that instructions remain responsive while a large transfer is in progress and so that either can be configured independently. The cost is that firewalls must understand two connections, which is the origin of the active-passive problem.

**Push versus pull.** SMTP pushes: the sender's server initiates delivery to the recipient's server. POP3 and IMAP pull: the recipient's client initiates collection. HTTP pulls for the same reason a mail client pulls, while UseNet both pushes between servers and pulls at the reader. A protocol designed for one direction is a poor fit for the other, which is why mail needs two protocol families where the web needs one.

**Store-and-forward.** A message is accepted, stored durably, and forwarded later. Acceptance is an acknowledgement of responsibility, not proof of delivery. This is why an SMTP success reply means "queued" and why a bounce can arrive minutes or days after the original send.

**Stateful sessions.** The server tracks where the session is in a defined state machine. In POP3 a retrieval command is invalid before authentication. In IMAP a fetch is invalid before a mailbox is selected. In FTP a retrieval is invalid before a transfer type and a data connection are arranged. Commands that violate the state machine are answered with a specific refusal, and knowing which refusal identifies the state error quickly.

### 1.5 Use cases that still exercise these protocols

An administrator uses SFTP to move a configuration archive to a server that is reachable only through SSH. Underneath, it is the same file-movement problem FTP was designed for, solved with a different transport.

A monitoring system connects to port 25 of each mail exchanger and reads the banner, because a banner that does not begin with 220 is a reliable early warning that mail delivery is failing.

A user with a laptop, a phone and a webmail tab reads one mailbox. Only a synchronising protocol can keep three views consistent, which is why IMAP survives while POP3 is now mostly a niche protocol for single-device collection and for archival scripts.

A security analyst reads a mail header to find which server accepted a message, in what order, and whether the envelope sender matches the header sender. The `Received` lines are the audit trail left by store-and-forward.

### 1.6 Scope and standard references

The normative documents are short and worth consulting once. FTP is Request for Comments 959, with later extensions for security and for IPv6. Telnet is Request for Comments 854 with a long series of option documents. SMTP is Request for Comments 5321, with the message format in 5322 and extensions for authentication and encryption in separate documents. POP3 is Request for Comments 1939. IMAP version 4 revision 1 is Request for Comments 3501. NNTP is Request for Comments 3977, superseding 977. Gopher is Request for Comments 1436.

## 2. Data, Syntax, and Core Concepts

### 2.1 Ports and the demultiplexing key

A TCP connection is identified by four values: the source address, the source port, the destination address and the destination port. That four-tuple is the key by which the receiving host decides which process should receive a segment. A server that listens on a port is not identified by the port alone but by the pair of address and port; a host with two addresses can run two servers that use the same port number on different addresses.

Ports from 0 to 1023 are the system range and are assigned by the Internet Assigned Numbers Authority for well-known services. Ports from 1024 to 49151 are the user range and are registered for particular applications. Ports from 49152 to 65535 are dynamic or ephemeral, and are used as the client's source port and as the server's chosen port in passive FTP. That last fact is the mechanical reason passive FTP can collide with a firewall's idea of what a client should be doing.

| Service | Transport | Default port | Secure variant | Secure port |
|---|---|---|---|---|
| FTP control | TCP | 21 | FTPS explicit | 21 with TLS negotiated in band |
| FTP data | TCP | 20 in active mode | FTPS implicit | 990 |
| SSH and SFTP | TCP | 22 | not applicable | not applicable |
| Telnet | TCP | 23 | Telnet over TLS | 992 |
| SMTP relay | TCP | 25 | SMTP over TLS | 465 |
| SMTP submission | TCP | 587 | same port with STARTTLS | 587 |
| DNS | UDP and TCP | 53 | DNS over TLS | 853 |
| HTTP | TCP | 80 | HTTPS | 443 |
| POP3 | TCP | 110 | POP3S | 995 |
| NNTP | TCP | 119 | NNTPS | 563 |
| IMAP | TCP | 143 | IMAPS | 993 |
| Gopher | TCP | 70 | Gopher over TLS | 70 |

Two of these entries need justification rather than memorisation. Port 587 exists because port 25 traditionally accepts mail from any sender, including forged senders, and therefore cannot be trusted to carry a user's authenticated submission. Port 587 requires authentication before it will accept a message, which makes it the correct port for a mail client. Port 465 was once used for a proprietary encrypted scheme, was deprecated, and was later reinstated as the standard for implicit TLS submission, so a modern client may legitimately use either 465 with encryption from the first byte or 587 with encryption negotiated after the greeting.

### 2.2 FTP architecture and the two channels

FTP, defined in Request for Comments 959, is built from four cooperating components. On the client side there is a **user interface** that accepts typed commands, a **client protocol interpreter** that understands FTP's grammar, and a **client data transfer process** that moves content. On the server side there is a **server protocol interpreter** and a **server data transfer process**, usually one of each per connected user.

The control connection is opened by the client to the server's port 21 and remains open for the whole session. It carries commands and replies in a simple textual grammar. The data connection is opened when content must move, and closed when the transfer ends. This is the definition of out-of-band control: the control information never shares a channel with the data it describes.

A consequence that is often missed in examination answers is that the control connection can survive a failed data connection. If the data connection cannot be opened, the server answers with 425 on the control connection and the session continues, so the client may retry with a different address or mode. This is a deliberate robustness property, and it is why an FTP client can report a transfer error without losing the login.

The protocol interpreter maintains a small amount of state per session: the login status, the current directory, the transfer type, the file structure, the transmission mode, and the address and port that the next data connection should use. Every command is interpreted against that state, which is why the order of commands matters.

### 2.3 FTP commands, replies, and the reply classes

A command is a three- or four-letter verb, in upper case by convention, followed by a space and an argument where the command takes one, terminated by the two-character end-of-line sequence. The commands fall into functional groups.

| Group | Commands | Purpose |
|---|---|---|
| Access control | USER, PASS, ACCT, REIN, QUIT | Establish and end the session |
| Transfer parameters | TYPE, STRU, MODE | Choose representation, file structure, transmission mode |
| Data connection | PORT, PASV, EPRT, EPSV | Say where or how the data connection is made |
| File transfer | RETR, STOR, STOU, APPE, REST, ABOR | Move or interrupt content |
| Directory navigation | CWD, CDUP, PWD, LIST, NLST | Move around and list |
| File system change | DELE, RNFR, RNTO, MKD, RMD | Delete, rename, create and remove directories |
| Information | SYST, STAT, HELP, NOOP, FEAT | Query the server, keep the session alive |

Replies are a three-digit code followed by a space and explanatory text. A hyphen instead of a space after the code means that the reply continues on following lines until a line that begins with the same code and a space. That convention allows a greeting or a help text to span many lines without ambiguity.

The first digit gives the class, and the second digit refines the meaning within the class. The second digit of one means a reply about the connection, two means a reply about the control channel, three means a reply about authentication or accounting, five means a reply about the file system. This is why 230 is "logged in" while 530 is "not logged in", and why 150 and 226 both concern the data connection.

| Code | Meaning | Consequence for the client |
|---|---|---|
| 220 | Service ready for new user | The session may proceed |
| 221 | Service closing control connection | The server is ending the session |
| 227 | Entering passive mode | Read the address and port from the reply text |
| 230 | User logged in | Authentication is complete |
| 331 | User name accepted, password needed | Send PASS next |
| 332 | Account needed for login | Send ACCT next |
| 150 | File status okay, about to open data connection | The transfer is starting |
| 226 | Closing data connection, transfer complete | The transfer finished correctly |
| 425 | Cannot open data connection | The data connection failed; the control connection is intact |
| 426 | Connection closed, transfer aborted | The data connection broke mid-transfer |
| 450 | File unavailable, but the condition is temporary | Retry later |
| 452 | Insufficient storage space | The target volume is full |
| 500 | Syntax error, command unrecognised | The verb is wrong |
| 501 | Syntax error in parameters | The verb is right, the argument is wrong |
| 503 | Bad sequence of commands | The state machine rejected the order |
| 530 | Not logged in | Authenticate before retrying |
| 550 | File unavailable, for example not found or no permission | Retrying will not help |

### 2.4 Active and passive data connections

The direction of the data connection is the single most examined fact in FTP, and the mechanism is simple once the arithmetic is understood.

In **active mode**, the client opens a listening socket on its own address at an ephemeral port, then sends the address and port to the server with the PORT command. The argument is six decimal numbers separated by commas: four for the address and two for the port, the port being the first number multiplied by 256 plus the second. The server then opens the data connection from its own port 20 to the address and port the client named. The client's operating system accepts that connection and the transfer proceeds.

```plaintext
PORT 192,168,1,24,196,52
200 PORT command successful.
```

The port in that command is 196 times 256 plus 52, which is 50228, so the server connects from source port 20 to destination 192.168.1.24 port 50228. Two properties follow. First, the server initiates a connection toward the client, which any stateful firewall in between will classify as an unsolicited inbound connection and block. Second, the client must be able to accept a connection at an address it has advertised, which fails outright if the client is behind network address translation, because the advertised address is private and unroutable.

In **passive mode**, the client sends PASV and the server opens a listening socket, then reports it with a 227 reply whose text contains the same six-number encoding.

```plaintext
PASV
227 Entering Passive Mode (203,0,113,9,195,84).
```

The port here is 195 times 256 plus 84, which is 50004, so the client connects to 203.0.113.9 port 50004. Both connections now run from client to server, which is what a stateful firewall expects, and which is why passive mode works from behind a home router without any configuration on the client side. The new cost is on the server side: the firewall in front of the server must allow inbound connections to the range of ports the server uses for passive data, and that range has to be configured because it is otherwise arbitrary.

For IPv6, the same two commands exist in extended form. EPRT carries a protocol family and a full address rather than four comma-separated octets, and EPSV carries only a port, with the address implied by the control connection. The reply to EPSV is 229 with the port between vertical bars.

```plaintext
EPSV
229 Entering Extended Passive Mode (|||50005|)
```

The negotiation of representation is the other parameter that matters practically. TYPE A selects ASCII transfer, in which line endings are converted to the network convention on transmission and to the local convention on receipt. TYPE I selects image, meaning raw binary with no conversion. TYPE E selects EBCDIC for the rare host that needs it, and TYPE L 8 selects local byte size eight. STRU F selects a file with no internal structure, STRU R a record structure, and STRU P a page structure. MODE S selects stream, MODE B block, and MODE C compressed. In practice every modern implementation uses TYPE I or TYPE A with STRU F and MODE S, and the other values exist because the protocol was designed to interoperate with systems that were not byte-oriented.

Restart and abort deserve a mention because they show the value of a persistent control channel. REST n sets a marker so that the next retrieval or store begins at offset n, which allows a partial transfer to be resumed. ABOR asks the server to stop the current transfer; the server abandons the data connection and answers 426 followed by 226. Neither would be possible if commands shared the data channel.

### 2.5 Telnet: the network virtual terminal

Telnet, defined in Request for Comments 854, gives a user an interactive terminal session on a remote host. Its central abstraction is the **Network Virtual Terminal**, a notional terminal that both ends agree to emulate. The client converts the local keyboard's behaviour into the virtual terminal's conventions, and the server converts the virtual terminal's conventions into whatever the remote operating system expects.

The virtual terminal defines a set of control functions rather than characters: an interrupt, an abort, an are-you-there, an erase-character, an erase-line, a break, and a data mark that resynchronises after a break. Because those signals must be distinguishable from ordinary data, the protocol reserves one byte, the **Interpret As Command** byte with the decimal value 255, and any literal 255 in the data stream is doubled.

Option negotiation runs in band and is symmetric: either side may propose enabling an option, and either side may refuse. Four commands carry the negotiation: WILL, meaning the sender intends to enable an option; DO, meaning the sender asks the other side to enable it; WONT, meaning a refusal; and DONT, meaning a demand that the other side stop. An option is only in force when both directions have agreed, which prevents a client from assuming a capability the server has not confirmed.

| Code | Name | Meaning |
|---|---|---|
| 255 | IAC | The next byte is a command, not data |
| 251 | WILL | I will enable this option |
| 252 | WONT | I will not enable this option |
| 253 | DO | Please enable this option |
| 254 | DONT | Please do not enable this option |
| 250 | SB | Begin subnegotiation, ended by 240 SE |
| 1 | ECHO | Who echoes the typed characters |
| 3 | SGA | Suppress go-ahead, used in full-duplex operation |
| 24 | TTYPE | Terminal type, sent as a subnegotiation |
| 31 | NAWS | Negotiate about window size |
| 34 | LINEMODE | Line-at-a-time rather than character-at-a-time editing |

The practical significance of all this is that a Telnet session is not a raw byte pipe. It is a session in which echo, editing, flow control and terminal size are negotiated. That is why a Telnet client can be used to drive an interactive program sensibly on a machine whose terminal conventions differ from the local ones.

Telnet's deficiency is equally structural. Neither the negotiation nor the session data is encrypted or integrity-protected, and the server is not authenticated by any cryptographic means. A password typed at a Telnet prompt crosses every intervening link in readable bytes. Anyone able to capture traffic on the path, including anyone on the same wireless network, obtains the credential and can replay it. Telnet is therefore insecure by modern standards and must not be used over an untrusted network. The replacement is the Secure Shell on port 22, which provides an encrypted channel, server host-key authentication, and integrity checking, and which carries both terminal sessions and file transfer. For the diagnostic purpose of testing whether a TCP port accepts connections and reading its banner, a Telnet client remains useful and safe, because no credential is involved.

### 2.6 The electronic mail architecture

Mail is the most layered of the services in this topic, and the layering is the point. Five roles are distinguished, and an examination answer that conflates them loses marks.

The **mail user agent** is the program the person uses. It composes messages, renders them, and manages a local view of folders. Examples include a desktop client and a phone application. It never delivers anything itself.

The **mail submission agent** is the server-side function that accepts a message from an authenticated user agent. In modern deployments this is a separate service listening on port 587, distinct from the relay service on port 25, because submission requires authentication and relay does not.

The **message transfer agent** moves messages between domains. It resolves the recipient's domain to a mail exchanger using a DNS query of type MX, connects to that host, and speaks SMTP. It queues what it cannot deliver and retries later, and it generates a non-delivery report when retries are exhausted.

The **mail delivery agent** takes a message from the transfer agent and writes it into the message store, applying filters, quota checks and folder rules on the way.

The **message store** is the durable container for delivered mail. It may be a set of files in a directory, one file per message, or a database. The store is what retrieval protocols read, and its layout determines which retrieval protocol is feasible: a store that keeps one file per message with an index supports IMAP's random access well, while a simple spool of files supports POP3 adequately and IMAP poorly.

| Role | Acts on behalf of | Protocol it speaks | Typical port |
|---|---|---|---|
| Mail user agent | The person | SMTP for submission, POP3 or IMAP for retrieval | 587, 110, 143 |
| Mail submission agent | The sending domain | SMTP with authentication | 587 |
| Message transfer agent | The domain | SMTP | 25 |
| Mail delivery agent | The recipient | Local delivery only | not a network port |
| Message store | The recipient | Read by POP3 or IMAP | 110, 143 |

Two addressing layers run through all of this and must be kept apart. The **envelope** consists of the sender and recipient addresses given in the protocol dialogue, with MAIL FROM and RCPT TO. It is what servers use for routing, for loops, and for bounces. The **header** consists of the lines the reader sees, with From, To, Cc, Subject, Date and Message-ID. The two can disagree, legitimately or maliciously; a mailing list rewrites the envelope sender so that bounces come back to the list, while a forged message can claim any header sender at all.

The message format itself is defined separately from the transfer protocol. Header fields are a name, a colon, and a value, folded onto continuation lines when long. A blank line separates headers from body. The body in the original standard was seven-bit US-ASCII text with lines no longer than 998 characters; the **Multipurpose Internet Mail Extensions**, abbreviated MIME, added the Content-Type, Content-Transfer-Encoding and Content-Disposition fields that allow arbitrary content, character sets and attachments, encoded as text so that the transfer protocol need not change.

### 2.7 SMTP: the transmission protocol

SMTP is a push protocol with a strictly linear dialogue. The client speaks, the server answers, and either side may end the session. The commands are four-letter words with arguments, and the replies are three-digit codes with optional enhanced status codes and human-readable text.

The session has four phases. In the **greeting** phase the server sends 220 and the client identifies itself with HELO or EHLO. HELO is the original command and gives only the client's domain. EHLO is the extended command and causes the server to list the extensions it supports, one per line, which is how a client discovers that it may authenticate, start encryption, pipeline commands, or use an eight-bit body.

In the **envelope** phase the client gives MAIL FROM with the sender's address and optional parameters such as SIZE, then RCPT TO for each recipient. Each recipient is accepted or refused separately, so a message to three people can be delivered to two and bounced for one. If a recipient is refused, the client may either continue with the others or abandon the transaction with RSET.

In the **data** phase the client sends DATA, receives 354, and then sends the entire message as headers, a blank line, and a body. The end of the content is a line containing only a full stop. Because a body line could legitimately begin with a full stop, the sending side prefixes an extra full stop to any such line, and the receiving side removes one leading full stop from any line that begins with two. This is dot-stuffing, and a message that arrives with stray leading dots is the signature of an implementation that got it wrong.

In the **termination** phase the client sends QUIT and receives 221, or the server ends the session with 421 when it is shutting down or overloaded. A 421 can arrive at any point and means the session is over; the message may or may not have been accepted.

| Command | Argument | Purpose |
|---|---|---|
| EHLO | client domain | Open an extended session and list server extensions |
| HELO | client domain | Open a basic session |
| MAIL FROM | reverse path, optional SIZE | Begin a transaction and name the envelope sender |
| RCPT TO | forward path | Name one recipient |
| DATA | none | Begin content transfer, answered with 354 |
| RSET | none | Abandon the transaction but keep the session |
| NOOP | none | Test that the session is alive |
| VRFY | address | Ask whether an address exists; usually disabled |
| AUTH | mechanism and response | Authenticate, after STARTTLS on port 587 |
| STARTTLS | none | Upgrade the session to TLS in place |
| QUIT | none | End the session |

The replies that matter in practice, and the ones an answer should be able to name, are these.

| Reply | Meaning |
|---|---|
| 220 | Service ready |
| 221 | Closing transmission channel |
| 250 | Requested action completed |
| 251 | User not local, will forward |
| 252 | Cannot verify the user, but will accept and attempt delivery |
| 354 | Start mail input, end with a full stop on a line alone |
| 421 | Service not available, closing the channel |
| 450 | Mailbox unavailable, try again later |
| 451 | Local error in processing, try again later |
| 452 | Insufficient system storage |
| 500 | Syntax error, command unrecognised |
| 501 | Syntax error in parameters |
| 503 | Bad sequence of commands |
| 550 | Mailbox unavailable, for example unknown recipient or policy refusal |
| 552 | Exceeded storage allocation |
| 553 | Mailbox name not allowed |
| 554 | Transaction failed, often a policy or content rejection |

The first digit of the reply tells the client what to do next. Two means proceed to the next phase. Three means send more input, which only 354 does in practice. Four means a transient failure, so the client must queue the message and retry. Five means a permanent failure, so the client must bounce the message to the envelope sender rather than retrying. Treating a five as a four produces a queue that grows forever; treating a four as a five produces bounces for momentary overloads.

Delivery between domains is directed by DNS. The sending transfer agent looks up the MX records for the recipient's domain, sorts them by preference, and tries them in order. A domain with no MX record but with an address record may still receive mail through that address as a fallback, which is a historical convention rather than a requirement. Because the lookup names a host and not a person, all recipients at one domain normally arrive at the same server.

Relaying is the act of accepting a message for a domain that is not the server's own and forwarding it onward. An **open relay** accepts such messages from anyone, and is a serious fault, because it allows spammers to launder traffic through an innocent third party's reputation and bandwidth. Modern servers refuse to relay unless the client has authenticated or is inside a trusted network. This is the operational reason submission moved to port 587: authentication is expected there, and therefore relaying to arbitrary destinations is safe to permit.

Because SMTP itself has no notion of sender authenticity, three supplementary mechanisms are used in practice. SPF publishes, in DNS, which hosts may send mail for a domain. DKIM attaches a cryptographic signature covering selected headers and the body. DMARC tells a receiver what to do when either check fails. None of them is part of SMTP, and all of them act on the same weakness: the envelope sender is trivially forgeable.

### 2.8 POP3: collection from a spool

POP3, defined in Request for Comments 1939, is a small protocol with a three-state machine. In the **authorization** state the client supplies credentials. In the **transaction** state the client lists, retrieves, and marks messages. In the **update** state, entered only on a clean QUIT, the server performs the deletions it was asked for.

The state machine is the whole design. A RETR before authentication is answered with a failure; a QUIT from the transaction state moves the session to update and closes it; a session that ends any other way, including a dropped connection, never enters the update state, so no deletion is committed.

Replies begin with the three characters plus, O and K for success, or a minus sign followed by the letters ERR for failure, followed by explanatory text. Message numbering is per session and starts at one, which means a message number is not a stable identifier across sessions; the UIDL command exists to provide one.

| Command | Argument | Meaning |
|---|---|---|
| USER | mailbox name | Identify the mailbox |
| PASS | string | Supply the password |
| APOP | name and digest | Authenticate without sending the password in the clear |
| STAT | none | Report the message count and total size |
| LIST | optional message number | Report sizes |
| RETR | message number | Retrieve a whole message |
| TOP | message number and line count | Retrieve headers and the first lines of the body |
| DELE | message number | Mark for deletion |
| RSET | none | Remove all deletion marks |
| NOOP | none | Do nothing, keep the session alive |
| UIDL | optional message number | Report a persistent unique identifier |
| QUIT | none | Enter the update state and close |

Two commands reveal the protocol's assumptions. TOP exists so that a client can show a preview without downloading an entire message, which matters on a slow link. UIDL exists so that a client which is configured to leave mail on the server can avoid downloading the same message twice, which matters because message numbers are recycled. Both are optional extensions to the base protocol, so a client must be prepared for their absence.

### 2.9 IMAP: a remote mailbox rather than a download

IMAP version 4 revision 1, defined in Request for Comments 3501, treats the mailbox as a remote data structure to be queried rather than a spool to be drained. The session has four states: not authenticated, authenticated, selected, and logout. Commands are only valid in the appropriate state, and the server enforces this explicitly.

The syntax differs from POP3 in three important ways. Every client command carries a **tag**, an alphanumeric label chosen by the client, and each reply carries either that tag or an asterisk for an untagged reply. Tags allow a client to pipeline commands and match responses even when the server interleaves untagged notifications. Replies end with OK, NO or BAD, and a continuation request begins with a plus sign and asks the client to send more data, which is how literals and authentication exchanges are carried.

The second difference is that responses are **structured**. A FETCH reply is a parenthesised list of attribute and value pairs, with literal lengths so that arbitrary binary content can be embedded without ambiguity.

The third difference is that messages carry **flags** stored on the server: seen, answered, flagged, deleted, draft, and recent. The backslash prefix marks system flags as opposed to keywords defined by the user. Flags are what make a shared mailbox consistent across devices.

| Command | Purpose |
|---|---|
| CAPABILITY | List what the server supports |
| LOGIN | Authenticate with a name and password |
| AUTHENTICATE | Authenticate with a challenge-response mechanism |
| SELECT | Open a mailbox for read-write access and report its status |
| EXAMINE | Open a mailbox read-only |
| LIST | List mailboxes matching a pattern |
| STATUS | Report counts for a mailbox without selecting it |
| FETCH | Retrieve flags, headers, body parts, or sizes |
| STORE | Change flags |
| SEARCH | Find messages matching criteria |
| COPY | Copy messages to another mailbox |
| EXPUNGE | Permanently remove messages marked deleted |
| APPEND | Add a message to a mailbox, used for saving sent mail |
| CLOSE | Return to the authenticated state, expunging if permitted |
| LOGOUT | End the session |

The two commands that together implement deletion are worth separating in an answer. STORE with the deleted flag marks messages; EXPUNGE removes them. Between the two, a client can present an undo. A CLOSE performs an implicit expunge in the selected mailbox, which is why a careful client uses it deliberately rather than as a shortcut.

### 2.10 POP3 and IMAP compared

| Dimension | POP3 | IMAP |
|---|---|---|
| Standard | Request for Comments 1939 | Request for Comments 3501 |
| Default port | 110, or 995 with TLS from the first byte | 143, or 993 with TLS from the first byte |
| Model | Download and typically delete | Remote mailbox, synchronised |
| Session states | Authorization, transaction, update | Not authenticated, authenticated, selected, logout |
| Command tagging | None; one command at a time | Every command tagged; pipelining possible |
| Message identity | Session-relative number, plus optional UIDL | Persistent unique identifier, plus sequence number |
| Folders | Local to the client | Stored on the server |
| Flags and read state | Local to the device | Stored on the server |
| Partial retrieval | TOP for headers and a few lines | FETCH of arbitrary body parts and header fields |
| Server storage | Minimal after collection | The whole mailbox |
| Offline use | Natural, because the mail is local | Requires a local cache |
| Multiple devices | Inconsistent unless mail is left on the server | Consistent by design |
| Best suited to | Single device, metered links, archival scripts | Multiple devices, large mailboxes, shared folders |

The examinable summary is that POP3 optimises for a device and IMAP optimises for a mailbox. Every other difference follows from that choice.

### 2.11 UseNet and the news transfer protocol

UseNet is a distributed discussion system built from servers that exchange articles. An article is a message with a defined set of headers. The Newsgroups header lists the groups it belongs to, the Message-ID header gives it a globally unique identity that survives copying, the Path header records the servers it has traversed, the References header links it to what it answers, and the Subject header carries the thread title, conventionally prefixed with the word "Re" on replies.

Group names are hierarchical, with components separated by full stops and the most general component first. The principal hierarchies are computing, science, recreation, social issues, debate, news about the network itself, miscellaneous, and humanities, collectively known as the big eight, together with the unmoderated alternative hierarchy and a set of regional hierarchies. A group is either moderated, in which case articles are mailed to a moderator who reposts accepted ones, or unmoderated, in which case any server will accept a posting.

Articles travel by the **Network News Transfer Protocol**, defined in Request for Comments 3977. A server offers new articles to its peers with IHAVE, and a peer that wants them requests the body. A client reads with GROUP to select a group, then OVER or XOVER for a summary of each article, then ARTICLE by number or message identifier. Each server decides which groups to carry and how long to keep articles, so propagation is not instantaneous and retention differs from site to site.

| Command | Meaning |
|---|---|
| CAPABILITIES | List what the server supports |
| MODE READER | Announce that this connection is a reader rather than a peer |
| GROUP | Select a group and report its article range |
| OVER | Return summary lines for a range of articles |
| ARTICLE | Return the headers and body of one article |
| HEAD | Return only the headers |
| BODY | Return only the body |
| STAT | Report whether an article exists |
| POST | Submit a new article |
| IHAVE | Offer an article to a peer |
| QUIT | End the session |

The mechanism that keeps propagation sane is the Path header and the history file. A server records the message identifiers it has seen, refuses to accept an article whose identifier is already known, and appends its own name to the path. Without those two devices, a mesh of servers exchanging articles would circulate the same article forever.

### 2.12 Gopher: menus and selectors

Gopher, defined in Request for Comments 1436, is a request-response protocol on port 70 with no session state at all. The client sends a selector string terminated by a carriage return and line feed, and the server sends a response and closes the connection. A selector is a path within the server's namespace, and the empty selector means the root.

A menu response is a sequence of lines. Each line has five tab-separated fields: an item type character, a display string, a selector, a host name, and a port number. The response ends with a line containing a single full stop. A text document response is simply the bytes of the document.

| Type | Meaning |
|---|---|
| 0 | Text file |
| 1 | Directory or menu |
| 2 | CSO name server |
| 3 | Error |
| 5 | DOS binary archive |
| 6 | UUencoded file |
| 7 | Index search server |
| 8 | Telnet session |
| 9 | Binary file |
| g | GIF image |
| I | Image of another kind |
| h | HTML document |

The type character is what makes a menu self-describing: a client knows before requesting anything whether a choice opens another menu, downloads a document, or starts a search. Type 7 choices are search services, and a client that selects one must send the query after the selector. Because a menu line carries the host and port of the item it describes, a single menu can point at resources on other servers, which is how the Gopher universe was stitched together without a central index. The best-known independent indexes were Veronica, which indexed menu titles across servers, and Jughead, which indexed a single server's menus.

The design limitation is that documents cannot link to one another. A menu can point outward, but a document cannot contain a reference that a reader can follow, and that absence is exactly what hypertext supplied.

## 3. Methods and Operations

### 3.1 The common opening sequence

Every service in this topic is reached through the same four preparatory steps, and separating them makes fault-finding systematic rather than speculative.

Step 1. Resolve the name. A query to the domain name system on port 53 returns either an address or a negative answer. A negative answer stops everything downstream, and the diagnostic is a name resolution failure rather than a connection failure.

Step 2. Establish a TCP connection to the service port. The three-way handshake either completes, is refused, or times out. A refusal means an address was reached and a reset came back, so the host is up and nothing is listening. A timeout means no answer at all, which points to a firewall dropping packets, a wrong address, or a routing failure.

Step 3. Read the server banner. FTP sends 220, SMTP sends 220, POP3 sends a plus sign, OK and text, IMAP sends an untagged OK with a capability list, NNTP sends 200 or 201, Telnet sends nothing at all because the remote login program speaks next. A banner is the cheapest evidence that the correct service, rather than some other program, is listening on that port.

Step 4. Authenticate, if the service requires it, and note the exact reply. A 331 in FTP means the user name was accepted and a password is expected; a 530 means the login was rejected; a 535 in SMTP means the credentials were refused. The distinction between "wrong password" and "authentication not offered" is visible only in the code.

### 3.2 Operating an FTP session

The order of commands is not arbitrary, and the reasons are worth stating because each corresponds to a piece of session state.

The client authenticates with USER and PASS, or with ACCT if the server demands an accounting string. It then sets the transfer type, because the default type of ASCII will corrupt a binary file. It sets the directory with CWD, or verifies it with PWD. It establishes the data connection policy, by sending PORT for active mode or PASV for passive mode. Then, and only then, it issues RETR or STOR, or one of the listing commands.

The listing commands are transfers in their own right. LIST returns a directory listing in a format resembling the output of a long directory command, and NLST returns bare names. Both open a data connection, both are affected by the transfer type, and both can fail with 425 or 426 exactly as a file transfer can. A client that reports "cannot list directory" is reporting a data connection problem, not a permission problem, unless the reply is 550.

Retrieval with REST allows resumption. The client sends REST with a byte offset, receives 350, and then issues RETR; the server starts sending from that offset. On the receiving side the client must append rather than overwrite, so the safe procedure is to verify the local partial file's length before resuming. This is the mechanism that later protocols replaced with explicit range requests.

Interruption is handled with ABOR. Because the control connection is independent, the client can send ABOR while the data connection is saturated. The server stops sending, closes the data connection, and replies 426 followed by 226, which tells the client that the transfer was aborted but the session is still usable.

### 3.3 Deciding and forcing the data connection mode

The decision procedure has three questions, answered in order.

Is the client behind network address translation or a stateful firewall? If yes, active mode cannot work, because the address the client advertises is private and the inbound connection the server attempts will be discarded. Use passive mode.

If the client is not translated but the server is behind a firewall that permits outbound connections from port 20 and no others, active mode is required. This configuration is now rare but still appears on hardened file servers.

If neither constraint applies, use passive mode anyway, because it is the default behaviour of modern clients and the mode least likely to be interfered with by an intermediate device that inspects connection direction.

On the server side the corresponding configuration is to restrict the passive port range to a small block and open that block in the firewall. A server configured with an unrestricted passive range opens ephemeral ports that the firewall blocks, and the symptom is a session that logs in, lists nothing, and hangs after a successful 227 reply. That particular symptom, a good login followed by a stalled transfer, is almost diagnostic of a passive port range that the firewall does not permit.

### 3.4 Operating a Telnet session and migrating away from it

The session itself is short: connect to port 23, read the login prompt, authenticate, work, log out, close. The operational discipline is what matters.

Before connecting, establish whether the path is trusted. On a laboratory segment with no other hosts, Telnet to a legacy device may be an accepted, if temporary, risk. On any network where another party could capture traffic, it is not acceptable, and the correct action is to enable SSH on the device if the firmware supports it.

If the device supports only Telnet, the compensating controls are to confine management to a dedicated management network, to restrict the source addresses that may reach port 23, and to log every session. Those controls reduce exposure; they do not make the protocol confidential.

The diagnostic use of a Telnet client is different and remains sound. Connecting to a service port and reading its banner sends no secret, so the absence of encryption causes no harm. This is the standard way to check that a mail server, a web server or an FTP server is answering on the port it should.

The migration path is SSH on port 22, with SFTP for file transfer over the same channel, and FTPS where an FTP workflow must be retained but must be encrypted. Both replace a plaintext protocol with one that negotiates keys, encrypts the session, and verifies the server's identity.

### 3.5 Tracing a message through SMTP

A delivery can be traced as a sequence of decisions, each of which leaves evidence.

Step 1. The user agent submits the message to its provider's submission service on port 587, authenticating first and upgrading to encryption with STARTTLS. The submission service adds a Received header recording the client, the time, and the encryption state.

Step 2. The submission service determines the recipient domain and queries DNS for its MX records. The record set is sorted by preference, and the lowest preference value is tried first.

Step 3. The transfer agent connects to the chosen exchanger on port 25, reads the banner, and issues EHLO. It negotiates the extensions it needs: SIZE to declare the message size before sending, 8BITMIME if the body is not seven-bit, and STARTTLS if policy requires encryption in transit.

Step 4. It issues MAIL FROM with the envelope sender, RCPT TO for each recipient, and DATA. The receiving server applies policy at each of those three points, which is why a rejection can arrive before any content has been sent.

Step 5. The receiving server accepts the content, adds its own Received header at the top, and answers 250 with a queue identifier.

Step 6. The receiving server's delivery agent writes the message into the recipient's store, or forwards it if the recipient has moved.

Step 7. The recipient's client retrieves or synchronises the message. Every Received header added along the way is visible in the delivered copy, newest first, so the path can be reconstructed from the bottom upward.

### 3.6 Operating POP3 and IMAP correctly

For POP3 the safe sequence is USER, PASS, STAT, LIST, then RETR for each wanted message, then either DELE and QUIT, or QUIT alone to leave everything in place. Two disciplines prevent data loss. Never send DELE until the retrieved copy has been written successfully to stable storage. And never rely on message numbers across sessions; use UIDL when the server offers it, because a client that leaves mail on the server and tracks messages by number will eventually download the wrong message.

For IMAP the safe sequence is LOGIN, SELECT, FETCH of flags and headers, FETCH of a body part, STORE of flags, then either EXPUNGE followed by LOGOUT, or LOGOUT alone. Two disciplines matter here as well. Use BODY.PEEK when reading content that should not be marked as seen, because a plain BODY fetch sets the seen flag as a side effect. And remember that EXPUNGE removes every message with the deleted flag in the selected mailbox, not just the ones the client has been looking at, so a client sharing a mailbox must re-read flags before expunging.

### 3.7 Reading news and retrieving Gopher documents

News reading is a session with three phases. The client connects, optionally announces itself as a reader with MODE READER, and selects a group with GROUP, which returns the count, the lowest article number and the highest. It then requests summaries for a range, which is cheap, and fetches only the articles the reader opens. Posting is a separate transaction that begins with POST and ends with a line containing a single full stop, exactly as in SMTP, because the article format and the content-termination convention were borrowed from mail.

Gopher retrieval is stateless and therefore trivially scriptable. Send the selector and a line ending, read until the connection closes, and interpret the first character of each line as an item type. A client that wants to follow a menu parses the five fields of the chosen line and connects to the host and port named there, which may be a different server entirely. Caching is safe because there is no session state to invalidate, and that made Gopher easy to mirror.

### 3.8 Verifying with local tools

Three local checks answer most questions about a running service. A listing of listening sockets shows which addresses and ports a host has bound, which confirms that a service is running and whether it is bound to all interfaces or only to the loopback address. A connection listing shows established sessions with their four-tuples, which is how the direction of an FTP data connection is proved. A capture of the traffic shows the actual dialogue, which is how the absence of encryption is proved rather than asserted.

| Symptom | Likely layer | Check |
|---|---|---|
| Name does not resolve | Naming | Query the name server directly |
| Connection refused immediately | Transport or service | List listening sockets |
| Connection hangs then times out | Filtering | Compare with a port known to be open |
| Banner arrives, login refused | Authentication | Read the exact reply code |
| Login succeeds, listing stalls | FTP data connection | Compare active and passive mode |
| Mail accepted with 250 but never arrives | Delivery | Read the Received headers and the queue |

## 4. Worked Implementation from the Notes

### 4.1 Task: demonstrate active mode and prove the direction of the data connection

### 4.2 Implementation: force PORT and observe the four-tuple

Step 1. Open the control session and authenticate.

```text
Connected to ftp.example.ac.ke.
220 (vsFTPd 3.0.5)
Name (ftp.example.ac.ke:student): student
331 Please specify the password.
Password:
230 Login successful.
```

Step 2. Set the transfer type to binary, because the demonstration moves an archive.

```text
ftp> binary
200 Switching to Binary mode.
```

Step 3. Send an explicit PORT command naming the client's own address and a chosen port. The last two numbers encode the port.

```text
ftp> literal PORT 192,168,1,24,196,52
200 PORT command successful. Consider using PASV.
```

Step 4. Start a transfer of a directory listing, which is small enough to complete instantly, and note the two replies: 150 announces the data connection, 226 closes it.

```text
ftp> ls
150 Here comes the directory listing.
drwxr-xr-x    2 1002     1002         4096 Nov 07 09:00 submissions
-rw-r--r--    1 1002     1002      7340032 Nov 07 09:02 toolkit.zip
226 Directory send OK.
```

Step 5. Prove the direction from the client's own socket table while the session is idle but the control connection is still open. The foreign port is 20, which only ever appears as the source port of a server-initiated data connection.

```powershell
Get-NetTCPConnection -RemotePort 20 | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

```text
LocalAddress  LocalPort RemoteAddress  RemotePort State
------------  --------- -------------  ---------- -----
192.168.1.24     50228 203.0.113.9            20 TimeWait
```

Step 6. Explain. The local port 50228 is exactly the value encoded by the two numbers 196 and 52. The remote port 20 is the server's data port and the local port is the client's chosen port, so the connection was opened from server to client. That is the definition of active mode, and it is also the reason the mode fails whenever a firewall on the client's side refuses inbound connections from port 20.

### 4.3 Task: perform the same transfer in passive mode from behind a router

### 4.4 Implementation: let the server nominate the port and the client connect

Step 1. Use a client that reports its own commands, and ask for the archive with passive mode selected. The client requests an extended passive port first.

```bash
curl --verbose --ftp-pasv --user student:training-password-01 \
  ftp://ftp.example.ac.ke/toolkit.zip --output toolkit.zip
```

Step 2. Read the negotiation in the verbose output.

```text
> EPSV
< 229 Entering Extended Passive Mode (|||50005|)
> TYPE I
< 200 Switching to Binary mode.
> RETR toolkit.zip
< 150 Opening BINARY mode data connection for toolkit.zip (7340032 bytes).
< 226 Transfer complete.
```

Step 3. Confirm, while the transfer is still running, that the data connection was opened by the client.

```powershell
Get-NetTCPConnection -RemotePort 50005 | Select-Object LocalPort, RemoteAddress, RemotePort, State
```

```text
LocalPort RemoteAddress  RemotePort State
--------- -------------  ---------- -----
    50230 203.0.113.9         50005 Established
```

Step 4. Explain. Both connections now run from the client outward, to port 21 for control and port 50005 for data, so a router that permits outbound connections needs no special rule. The protocol still has two channels and the control channel is still out of band; only the direction of the second channel has changed. The remaining server-side obligation is that the firewall in front of the server must permit inbound connections to the passive range, which is why a server administrator restricts that range to a known block.

Step 5. State the failure signature. If the session logs in, receives a valid 229 or 227, and then stalls before any bytes arrive, the passive port is blocked. If the session logs in and the transfer fails immediately with 425, the server could not open the data connection at all, which usually means the passive address it advertised is wrong for the network it sits behind.

### 4.5 Task: deliver a message to two recipients, one of which does not exist

### 4.6 Implementation: drive the envelope one recipient at a time

Step 1. Connect and open an extended session.

```text
220 smtp.example.ac.ke ESMTP Postfix
EHLO workstation.example.ac.ke
250-smtp.example.ac.ke
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250 SMIME
```

Step 2. Declare the sender and the message size, which lets the server refuse an oversized message before any content is transferred.

```text
MAIL FROM:<amina@example.ac.ke> SIZE=742
250 2.1.0 Ok
```

Step 3. Offer the first recipient and read the acceptance.

```text
RCPT TO:<brian@example.net>
250 2.1.5 Ok
```

Step 4. Offer the second recipient, who does not exist at that domain, and read the refusal.

```text
RCPT TO:<grace@example.net>
550 5.1.1 <grace@example.net>: Recipient address rejected: User unknown in local recipient table
```

Step 5. Continue with the recipient that was accepted, since a refusal applies only to the address it was given for.

```text
DATA
354 End data with <CR><LF>.<CR><LF>
From: Amina Wanjiku <amina@example.ac.ke>
To: Brian Otieno <brian@example.net>
Cc: Grace Muthoni <grace@example.net>
Subject: Lab group meeting moved to Thursday
Date: Fri, 07 Nov 2025 09:20:15 +0300
Message-ID: <20251107092015.4821@example.ac.ke>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

The group meeting has moved from Wednesday to Thursday 14:00.
Room remains LT-3.

Regards,
Amina
.
250 2.0.0 Ok: queued as 4Bv2k19XhQz3n
QUIT
221 2.0.0 Bye
```

Step 6. Explain. The 550 carries an enhanced status code whose class is permanent, so the sending server must not retry; it will generate a non-delivery report for that recipient. The first recipient receives the message normally. Because the refused address appears in the Cc header, the delivered copy still names a person who never received it, which is exactly the envelope-versus-header distinction in practice.

### 4.7 Task: show that a POP3 mailbox is not shared between devices

### 4.8 Implementation: collect on one client, then inspect from a second

Step 1. Collect the mailbox on the first client and delete what was collected.

```text
+OK Dovecot ready.
USER brian
+OK
PASS training-password-01
+OK Logged in.
STAT
+OK 2 3204
LIST
+OK 2 messages:
1 1450
2 1754
.
UIDL
+OK
1 0000000001a3f21c
2 0000000001a3f44e
.
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
DELE 2
+OK Marked to be deleted.
QUIT
+OK Logging out, messages deleted.
```

Step 2. Connect a second client, immediately afterwards, and ask for the status.

```text
+OK Dovecot ready.
USER brian
+OK
PASS training-password-01
+OK Logged in.
STAT
+OK 0 0
```

Step 3. Explain. The second client sees an empty mailbox because the deletion marks from the first session were committed when that session entered the update state on QUIT. Had the first client sent only one of the DELE commands, exactly that one message would have gone. Had the first session dropped without QUIT, nothing would have gone and the second client would have seen both messages. The mailbox state is not synchronised; it is transferred and then cleared.

Step 4. Demonstrate the remedy and its limit. Reconnecting the first client with an option to leave mail on the server would preserve the messages for the second client, but the read and deletion states would still be local to each client, so the two views would drift apart. That drift is the reason IMAP exists.

### 4.9 Task: keep two clients consistent with IMAP

### 4.10 Implementation: fetch headers, read one part, change flags, expunge

Step 1. Log in and select the inbox. Untagged replies begin with an asterisk; the tagged reply confirms the command.

```text
* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE] Dovecot ready.
a1 LOGIN brian training-password-01
a1 OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE] Logged in
a2 SELECT INBOX
* 2 EXISTS
* 0 RECENT
* OK [UNSEEN 1] First unseen.
* OK [UIDVALIDITY 1699012345] UIDs valid
* OK [UIDNEXT 118] Predicted next UID
a2 OK [READ-WRITE] Select completed.
```

Step 2. Fetch the flags of both messages, which is the state shared between devices.

```text
a3 FETCH 1:2 (UID FLAGS)
* 1 FETCH (UID 117 FLAGS (\Seen))
* 2 FETCH (UID 118 FLAGS ())
a3 OK Fetch completed.
```

Step 3. Fetch only two header fields of the second message, peeking so that the read flag is not changed.

```text
a4 FETCH 2 BODY.PEEK[HEADER.FIELDS (SUBJECT FROM DATE)]
* 2 FETCH (BODY[HEADER.FIELDS (SUBJECT FROM DATE)] {86}
Subject: Lab group meeting moved to Thursday
From: Amina Wanjiku <amina@example.ac.ke>
Date: Fri, 07 Nov 2025 09:20:15 +0300
)
a4 OK Fetch completed.
```

Step 4. Set the answered flag on that message and confirm it.

```text
a5 STORE 2 +FLAGS (\Answered)
* 2 FETCH (FLAGS (\Answered))
a5 OK Store completed.
```

Step 5. Mark the first message deleted, then remove it permanently.

```text
a6 STORE 1 +FLAGS (\Deleted)
* 1 FETCH (FLAGS (\Seen \Deleted))
a6 OK Store completed.
a7 EXPUNGE
* 1 EXPUNGE
* 1 EXISTS
a7 OK Expunge completed.
```

Step 6. End the session.

```text
a8 LOGOUT
* BYE Logging out
a8 OK Logout completed.
```

Step 7. Explain. A second client that connects now sees one message, with the answered flag already set, and with no unread message. Nothing was downloaded except two header fields and two flag lists. Compare this with the POP3 session, where the second client saw nothing at all. The same underlying mailbox produced completely different outcomes because the retrieval protocol, not the mailbox, decided where the state lives.

### 4.11 Task: prove that Telnet credentials are readable on the wire

### 4.12 Implementation: capture a session and read the password

Step 1. Start a capture on the client, filtered to the Telnet port, with the packet payload shown as text.

```bash
tcpdump -i eth0 -A -s 0 'tcp port 23'
```

Step 2. Log in to a lab device from another terminal. The session looks normal to the user.

```text
Trying 198.51.100.7...
Connected to lab-switch-01.
login: admin
Password:
lab-switch-01>
```

Step 3. Stop the capture and read what it recorded. The payload appears in clear text, character by character, because Telnet sends each keystroke unless line mode was negotiated.

```text
10:14:02.118 IP 198.51.100.22.49152 > 198.51.100.7.23: Flags [P.], seq 1:7, ack 1, length 6
E..4..@.@..............
..... admin
10:14:05.402 IP 198.51.100.22.49152 > 198.51.100.7.23: Flags [P.], seq 7:31, ack 12, length 24
E..4..@.@..............
.....Summer2025!
```

Step 4. Explain. No decryption was performed and no tool beyond a packet capture was used. The password is visible because Telnet defines no confidentiality mechanism at all: the Network Virtual Terminal carries keystrokes as bytes, and the transport carries those bytes unchanged. An attacker on the same wireless network, or anywhere on the path, obtains the same result. This is the concrete sense in which Telnet is insecure by modern standards.

Step 5. State the replacement and the reason. SSH on port 22 negotiates a session key, encrypts the whole channel including authentication, and authenticates the server with a host key, so neither the password nor the commands are visible and a substituted server is detected. Where file transfer is also needed, SFTP runs over the same channel rather than opening a second, plaintext one.

### 4.13 Task: read a newsgroup and a Gopher menu without a dedicated client

### 4.14 Implementation: two stateless or near-stateless text protocols

Step 1. Connect to the news server and announce that this is a reader.

```text
200 news.example.ac.ke InterNetNews NNTP server ready
MODE READER
200 Reader mode, posting permitted
GROUP comp.protocols.tcp-ip
211 1523 4021 5543 comp.protocols.tcp-ip
```

The group reply says that there are 1523 articles, numbered from 4021 to 5543.

Step 2. Ask for summaries of the newest three articles rather than their full text.

```text
OVER 5541-5543
224 Overview information follows
5541	Re: Port 21 versus port 20	Brian Otieno <brian@example.net>	Fri, 07 Nov 2025 08:02:11 +0300	<9f2c1@example.net>	<9f2b0@example.net>	412	18	Xref: news.example.ac.ke comp.protocols.tcp-ip:5541
5542	Active mode behind NAT	Grace Muthoni <grace@example.net>	Fri, 07 Nov 2025 08:41:03 +0300	<1c88a@example.net>		598	24	Xref: news.example.ac.ke comp.protocols.tcp-ip:5542
5543	Re: Active mode behind NAT	Amina Wanjiku <amina@example.ac.ke>	Fri, 07 Nov 2025 09:05:47 +0300	<77be2@example.ac.ke>	<1c88a@example.net>	655	31	Xref: news.example.ac.ke comp.protocols.tcp-ip:5543
.
```

Step 3. Fetch one article by number.

```text
ARTICLE 5542
220 5542 <1c88a@example.net> article follows
Path: news.example.ac.ke!feed.example.org!not-for-mail
From: Grace Muthoni <grace@example.net>
Newsgroups: comp.protocols.tcp-ip
Subject: Active mode behind NAT
Date: Fri, 07 Nov 2025 08:41:03 +0300
Message-ID: <1c88a@example.net>
References: <9f2b0@example.net>

The server cannot connect back to a private address, so PORT fails.
Use PASV and let the client open both connections.

.
```

Step 4. Explain. The overview reply is a tab-separated record per article, so a reader can show a thread list after transferring a few kilobytes instead of the whole group. The Path header records the servers the article crossed, which is how loops are prevented. The References header names the article being answered, which is how threads are reconstructed without any server-side thread index.

Step 5. Now request a Gopher menu by sending the empty selector.

```text
$ printf '\r\n' | nc gopher.example.ac.ke 70
1Example Academic Gopher Server<TAB>/<TAB>gopher.example.ac.ke<TAB>70
0Undergraduate Handbook 2025<TAB>/0/handbook.txt<TAB>gopher.example.ac.ke<TAB>70
1Department of Computing<TAB>/1/computing<TAB>gopher.example.ac.ke<TAB>70
7Search all Gopher servers known here<TAB>/7/search<TAB>gopher.example.ac.ke<TAB>70
.
```

The separator between fields is a single tab character, written here as the label TAB so that the fields remain visible.

Step 6. Follow one menu item by sending its selector.

```text
$ printf '/1/computing\r\n' | nc gopher.example.ac.ke 70
1Staff directory<TAB>/1/computing/staff<TAB>gopher.example.ac.ke<TAB>70
0Module list, semester one<TAB>/0/computing/modules.txt<TAB>gopher.example.ac.ke<TAB>70
.
```

Step 7. Explain. Each line is self-describing: the first character says that these are menus and documents, the second field is what the reader sees, the third is what to send next, and the last two say where to send it. There is no session, no login and no state, so any line can be followed independently and any document can be cached. That is both the strength of Gopher and the reason it could not express a link between two documents.

## 5. Testing, Interpretation, and Common Errors

### 5.1 A verification checklist for this topic

A complete understanding can be tested by producing each of the following without reference material.

Name the default port of each service and the secure variant where one exists. Explain, in terms of the six-number PORT argument, why active FTP fails behind translation, and compute a port number from the two numbers given. State which side opens the data connection in each mode. Give three reasons why an FTP session might log in successfully and then fail to list a directory. Recite the SMTP commands in order and say which reply code belongs to each phase. Distinguish the envelope from the header using a concrete example. Explain why a 550 must not be retried and a 450 must be. Recite the three POP3 states and say which command causes the transition to the third. Recite the four IMAP states and name the command that moves between the last two. Contrast POP3 and IMAP on five dimensions. Describe how a news article is prevented from circulating forever. Explain what an item type character does in a Gopher menu.

### 5.2 Interpreting replies correctly

Three-digit codes are read left to right. The first digit is the class and decides the client's next action. The second digit identifies the subject of the reply: connection, control channel, authentication, or file system. The third digit distinguishes replies within a subject.

The most commonly misread reply in this topic is 354. It is not a success code; it is an instruction to continue, and it says nothing about whether the message will be accepted. A client that treats 354 as final will never send the body.

The second most commonly misread is 250. It means the server has taken responsibility for the message. It does not mean the message was delivered, and the only way to know about delivery is a subsequent report or the absence of one. Reading 250 as proof of delivery is a conceptual error, not a small one.

In POP3 the replies are words rather than numbers, and the pattern is easier. A plus sign means acceptance and a minus sign means refusal. In IMAP the tagged reply carries the outcome and the tag identifies which command it belongs to; an untagged reply is information or an event, not an answer.

### 5.3 Diagnosing the common failures

| Observation | Cause | Action |
|---|---|---|
| 530 on the first command after login | The command requires an authenticated state | Authenticate before issuing it |
| 503 bad sequence | A command arrived in the wrong state | Check the order against the state machine |
| 425 cannot open data connection | The server could not reach the client, or the passive port is closed | Switch mode, or open the port range |
| 426 during a long transfer | The data connection broke | Resume with REST, or repeat the transfer |
| Transfer completes but the file is corrupt | Type was ASCII for binary content | Set TYPE I |
| Login succeeds and listing hangs | Firewall blocking the passive range | Restrict and open the passive range |
| Message accepted but never arrives | Delivery failed after acceptance, or it was filtered | Read Received headers, check the junk folder |
| 550 rejecting an address that exists | Recipient policy, greylisting, or reputation | Read the enhanced status code and the text |
| IMAP login works, fetch returns nothing | No mailbox selected | Issue SELECT first |
| Deleted messages reappear | The session never reached the update state, or no expunge was issued | QUIT cleanly, or issue EXPUNGE |
| News article missing on one server | Propagation delay or retention policy | Compare article numbers and check the peer configuration |
| Gopher menu is empty | The selector was sent without a proper line ending | Send carriage return and line feed |

### 5.4 Common errors in written answers

- **Saying FTP uses one port.** It uses two, and the number of the data port is 20 only in active mode; in passive mode the server chooses a port and announces it.
- **Saying the server always initiates the data connection.** That is true only in active mode, and the distinction is the whole reason the mode exists.
- **Confusing the control connection with the command channel of a single connection.** Out-of-band control means two separate TCP connections with separate lifecycles.
- **Describing SMTP as a retrieval protocol.** SMTP pushes only; it has no command that reads a mailbox.
- **Treating the message header as the envelope.** Routing uses the envelope; the reader sees the header; they can differ.
- **Claiming a 250 proves delivery.** It proves acceptance and queuing.
- **Saying POP3 deletes on the delete command.** It marks, and commits at the update state.
- **Saying IMAP downloads the whole mailbox.** It fetches structures and parts on demand.
- **Confusing IMAP's sequence numbers with its unique identifiers.** Sequence numbers change when messages are expunged; unique identifiers do not.
- **Describing Telnet as insecure without saying why.** The reason is that credentials and session data are unencrypted and the server is unauthenticated; the replacement is SSH.
- **Suggesting that FTPS and SFTP are the same.** FTPS is FTP with TLS; SFTP is a file-transfer subsystem of SSH on port 22.
- **Treating UseNet as a web service.** It is a separate store-and-forward network with its own protocol on port 119.
- **Treating Gopher as a search engine.** It is a menu-based document retrieval protocol; search was one item type among several.

### 5.5 Security analysis, stated once

Every protocol in this topic except the secure variants named beside it was designed for a closed research network in which every participant was trusted. The consequences are systematic rather than accidental.

FTP, Telnet, POP3 on port 110, IMAP on port 143 and SMTP on port 25 all send credentials and content as readable text, so any observer on the path obtains them. FTP additionally sends data on a second connection whose direction depends on the client, which forces firewall rules that are hard to write safely and easy to write too permissively. SMTP accepts any envelope sender, so the sender identity is unverifiable without the supplementary checks for published sending hosts, cryptographic signatures and published policy. POP3 and IMAP with no encryption expose both the password and the entire mailbox during collection.

The replacements are not cosmetic. FTPS wraps FTP in Transport Layer Security. SFTP moves files inside an SSH channel on port 22. SSH replaces Telnet with an encrypted, authenticated channel. POP3S on 995 and IMAPS on 993 encrypt retrieval from the first byte, and STARTTLS on 110, 143 and 587 upgrades a plaintext session in place. Submission on 587 with authentication separates the trusted user path from the untrusted relay path.

The residual lesson is that a secure variant is a different protocol configuration, not a setting that can be assumed. A client that connects to port 21 and never issues AUTH TLS has an unencrypted session even though the server supports encryption, which is why opportunistic encryption alone is a weak control.

### 5.6 Summary of the architecture in one paragraph

A service is a program bound to a port and governed by a published text protocol. FTP splits instructions from content across two connections and lets either side open the second, which is why mode selection is a firewall decision. Telnet carries a negotiated virtual terminal over an unencrypted channel and is superseded by SSH. Mail separates composition, submission, transfer, delivery and storage, uses SMTP to push between servers, and uses POP3 or IMAP to pull toward devices; the first drains a spool and the second synchronises a mailbox. UseNet floods articles between servers under a loop-prevention scheme, and Gopher answers one selector at a time with a self-describing menu or a document.

