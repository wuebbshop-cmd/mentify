## 1. Concept and Use Case

### 1.1 Imagine opening a shop in a large market hall

Imagine you have decided to open a small shop. Before a single customer can walk in, four separate things have to be arranged, and each one is handled by a different person. First, you need a name that people can find and remember, and that name has to be listed in the market's official directory so that anyone asking for it is sent to the right stall. Second, you need a stall: either a corner of a shared counter where you keep your goods in one drawer, or a lockable booth of your own, or a whole unit, or a building you own standing inside somebody else's market. Third, you need the stall to be safe, with a lock on the door, a way of proving who is allowed behind the counter, and a shutter that comes down at night. Fourth, you need copies of your account books kept somewhere else, because a flood, a fire, or a careless hand with a cup of coffee can destroy the only copy in a moment.

A website is exactly that shop, and the four arrangements are exactly the same four. The directory is the naming system of the Internet. The stall is the hosting account. The lock and the shutter are the security controls. The copies of the account books are the backups. Almost everything in this topic is one of those four arrangements, or the set of decisions that connects them.

The value of the comparison is that it separates things beginners tend to blur together. If your shop's name is listed in the directory but the stall is empty, customers arrive at nothing. If the stall is full of goods but the directory still lists your old address, nobody arrives at all. If both are perfect but the account books exist only in one drawer, a single bad afternoon can end the business. Keeping the four arrangements distinct is the first step towards being able to fix a problem, because the first question in any outage is which of the four has broken.

### 1.2 What actually happens when somebody visits

The journey from a typed name to a visible page has more steps than most people expect, and knowing them makes the rest of the topic much easier to follow.

A visitor types a name into a browser. The browser cannot use a name to send data across the network; it needs a numeric address, rather like a postal service needing a house number rather than the words "the blue house on the corner". A lookup service called the Domain Name System, shortened to DNS, performs that translation. DNS is a worldwide directory, split into many pieces, and each piece is kept by a different organisation. The last part of a name, such as `com` or `org`, is called a top-level domain, or TLD. One organisation, called a registry, keeps the official list for each top-level domain.

Once the address is known, the browser opens a connection to the machine at that address. The machine is a computer in a data centre somewhere, and the arrangement that gives you space on it is called web hosting. Before any page content is exchanged, the two ends usually perform a short encrypted introduction so that nobody sitting on the network in between can read or alter what is said. That introduction is provided by a protocol whose older name, Secure Sockets Layer or SSL, is still used in ordinary speech, and whose modern name is Transport Layer Security, or TLS. When a site uses it, the address in the browser begins with `https` instead of `http`, and a small padlock appears.

The request then reaches a program on the server, which may look something of it up in a database, and the answer travels back. Every one of those stages can fail on its own: the name may not resolve, the address may not answer, the encrypted introduction may fail because a certificate has expired, the program may crash, or the database may be unavailable.

### 1.3 The four decisions you are really making

Behind the sales pages and the plan names, a site owner makes four decisions, and each has a price and a consequence.

**The naming decision.** You choose a name and an ending, you rent it for a period, and you decide which company will hold it on your behalf. You do not buy a name outright; you rent the right to use it, and if the rent is not paid it eventually returns to the pool and somebody else may take it.

**The hosting decision.** You choose how much of a machine is exclusively yours. At one extreme you share a machine with hundreds of other sites; at the other you own the hardware and rent only the space, power, and network connection in somebody else's building.

**The security decision.** You decide how much of the machine is exposed to the public Internet, who may administer it, how they prove who they are, and what happens to information that should never be visible.

**The recovery decision.** You decide how much data you are willing to lose, how quickly you need the site back, and where the copies live. This is the decision most often postponed, and the only one that cannot be made after the loss.

Each decision constrains the others. A shop that takes card payments needs stronger security and a more capable hosting plan than a three-page brochure. A site whose data changes every minute needs a different backup rhythm from one that changes twice a year. A business that cannot tolerate an hour offline needs a different recovery arrangement from one that can tolerate a day.

### 1.4 Why backups are not an optional extra

Four things happen to real websites with depressing regularity, and none of them is exotic.

The first is hardware failure. A disk inside a server stops spinning, and everything on it becomes unreadable. Providers replace disks, but replacement is not recovery: the disk that failed held your files, and a new empty disk holds nothing.

The second is human error. A file is deleted, a folder is overwritten, a command is run in the wrong directory, or an update is applied that changes data in a way nobody intended. The person responsible is usually competent and tired, which is precisely why the mistake is common.

The third is deliberate destruction. Somebody gains access to the site and deletes or encrypts what they find, sometimes demanding payment to release it. Modern attacks of this kind deliberately look for connected backup systems and destroy those as well, which is why a copy that cannot be reached from the server matters.

The fourth is the loss of the provider. A hosting company closes without notice, a data centre burns, a flood fills the basement where the servers stood, or a business dispute leaves the account frozen and inaccessible. In each case the data still exists somewhere, but not anywhere you can reach.

In all four cases the difference between an inconvenience and the end of the business is a copy kept somewhere else, made recently, and known to work because somebody has restored it once.

### 1.5 The words you will meet, spelled out

Technical writing is full of abbreviations, so here they are in one place.

**DNS** is the Domain Name System, the worldwide directory that turns names into numeric addresses. **TLD** is a top-level domain, the final part of a name, such as `com`, `org`, `net`, or a country code such as `uk`. **IP** stands for Internet Protocol, and an IP address is the numeric address of a machine on the network; version four addresses look like `203.0.113.10`, and version six addresses are longer and written with colons.

**VPS** is a virtual private server: a slice of a physical machine, created by software called a hypervisor, which behaves like a separate computer with its own operating system. **RAM** is random access memory, the fast working memory a program uses while it runs; a machine with too little of it slows down badly under load.

**SSL** is Secure Sockets Layer and **TLS** is Transport Layer Security; they are the same family of protocols, and the second is the modern name for the successor of the first. **SNI** is Server Name Indication, a part of the encrypted introduction in which the browser states which name it is asking for. **HTTP** is HyperText Transfer Protocol, the language a browser and a server use to exchange pages; **HTTPS** is the same language carried inside an encrypted connection.

**FTP** is File Transfer Protocol, an older method of copying files to a server, now largely replaced by secure variants and by deployment from a code repository. **SSH** is Secure Shell, the encrypted way of logging in to administer a server. **WAF** is a web application firewall, a filter that inspects the requests themselves rather than only the addresses they come from.

**PCI DSS** is the Payment Card Industry Data Security Standard, the rule set that applies to any business handling card details. **RPO** is the recovery point objective, the greatest amount of data loss you are prepared to accept, measured in time. **RTO** is the recovery time objective, the greatest time you are prepared to be offline.

## 2. Data, Syntax, and Core Concepts

### 2.1 Names, labels, and addresses

A domain name is read from the most specific part on the left to the most general on the right. In `shop.example.com`, the computer is called `shop`, the organisation's zone is `example`, and the ending is `com`. Each part between the dots is a label, and a label may be up to sixty-three characters long, using letters, digits, and hyphens, though a hyphen may not sit at either end.

A name identifies a zone, which is an area of the directory that one organisation is responsible for. Within that zone you may create as many subdomains as you like, at no extra cost and without asking anybody. `shop.example.com`, `help.example.com`, and `blog.example.com` are three names inside the same zone, and each can point to a different machine or to a different part of the same machine. This is why a business needs only one registered name to run several services.

The address that a name points to is quite separate from the name. Two names may point to the same address, one name may point to several addresses for reliability, and the address may change while the name stays the same. That separation is the reason a site can move to a new provider without changing its name at all.

### 2.2 Who is who in the directory

Four roles appear in the registration system, and mixing them up causes a great deal of confusion when something goes wrong.

| Role | Plain description | What it decides |
|---|---|---|
| Registry | The organisation that keeps the official list for one ending | The official record of which servers are responsible for a name |
| Registrar | The company you pay, accredited to update that official list | Your rental record, the renewal date, the settings for your servers |
| Registrant | You, the person or business renting the name | Which registrar you use, and what the name points to |
| DNS provider | The service that holds your zone's actual records | The address of the website, the mail servers, and other records |

The key point is that the registry knows only one thing about your name: which servers are responsible for answering questions about it. It does not know your website's address, and it does not know where your mail goes. Those details live at the DNS provider, in the zone. When you change hosting, you usually change one or two records at the DNS provider, and the registry is not involved at all.

If you change to a different DNS provider, then the registry must be told, because the identity of the responsible servers is stored in the official list. That change is made through your registrar. It is a small change with a long shadow, because the old information is cached around the world for a period, and during that period different visitors may reach different servers.

### 2.3 Renting a stall: the hosting models

Hosting plans differ in one fundamental way: how much of the machine belongs to you alone.

**Shared hosting** puts many websites on one machine, each in its own folder with its own login. It is the cheapest option and the easiest to start with, because the provider manages the operating system, the web server, and the database service. The weakness is that the neighbours share everything: a busy neighbour slows your pages, a bug in a shared component can affect every site, and you cannot install software of your own.

**Virtual private server** hosting, abbreviated VPS, gives you a slice of a machine that behaves like a computer of its own, with its own operating system and a reserved amount of memory and processing. You can install what you like and restart it when you like. The catch is that you, or somebody you pay, must look after it: updates, security settings, and monitoring become your responsibility.

**Dedicated hosting** gives you an entire physical machine. Nobody else's website runs on it, so nothing a neighbour does can affect you. It costs considerably more and is normally chosen when traffic is high or when rules about data handling require the whole machine to be controlled.

**Colocated hosting** means you own the machine and rent space for it in somebody else's data centre, with their power, cooling, physical security, and network. It gives the greatest control and the greatest responsibility, because a failed disk is yours to notice and replace.

| Model | Who shares the machine | Who manages the software | Usual choice for |
|---|---|---|---|
| Shared | Hundreds of sites on one operating system | The provider | Small brochure sites, first projects |
| Virtual private server | A few slices of one physical machine | You, or a managed service | Growing businesses, web applications |
| Dedicated | Nobody | You | High traffic, strict requirements |
| Colocated | Nobody, and you own the hardware | You, including the hardware | Large estates, special equipment |

A helpful way to remember the difference is to think about what a neighbour's mistake can reach. On shared hosting it can reach your files. On a virtual private server it can reach the shared disk and network, but not your files. On a dedicated machine there is no neighbour at all. On colocation the neighbour is irrelevant, but the building is shared.

### 2.4 The four numbers on a hosting plan

Plans are sold on four numbers, and each needs a plain explanation.

**Disk space** is how much room your files have. It must hold the website itself, the pictures and videos, the database, the log files, and enough spare room to make a copy during an upgrade. A small site with text and photographs fits in a gigabyte or two; a site offering video needs far more.

**Monthly traffic**, also called bandwidth, is how much data leaves the server in a month. It is not the same as disk space: a small site with a popular video can fill a large allowance while using almost no disk. Some plans stop the site when the allowance is used, some charge for the excess, and some slow the connection instead. It is worth knowing which, because a site that vanishes at the end of a busy month is a business problem.

**Processing speed** is the vaguest of the four. On a shared plan you are buying a share of something that is not stated, and the only honest guide is how quickly other sites on the same provider respond. On a virtual private server or a dedicated machine the plan states the number of processors and the amount of memory, and the memory usually matters more, because it decides whether the database can keep its working data in fast storage or must keep fetching it from disk.

**Uptime** is the percentage of time the service is promised to be available. The percentage sounds similar across plans but the differences are large once converted into time.

| Promised uptime | Roughly how much downtime a year |
|---|---|
| 99 per cent | Three and a half days |
| 99.5 per cent | Nearly two days |
| 99.9 per cent | About nine hours |
| 99.99 per cent | Under an hour |

Two cautions belong with the numbers. First, the promise usually excludes planned maintenance and events the provider does not control, so the achieved figure can be worse than the promised one. Second, compensation is normally a credit on a future bill rather than payment for lost trade, so the promise softens the loss rather than removing it.

### 2.5 What an online shop needs on top

A shop adds requirements that a brochure site does not have.

**A padlock, properly configured.** Every page that shows a form, and every page at all once a visitor has signed in, must travel over the encrypted version of the protocol. The certificate behind the padlock must match the name visitors use and must be renewed before it expires. A certificate that expired last night produces a full-page warning in most browsers, and many visitors will leave rather than click past it.

**An address of its own, sometimes.** Older explanations say that encryption requires a dedicated address for every site. That was true when the server had to choose a certificate before learning which name the visitor wanted. The extension called Server Name Indication, or SNI, now lets the browser state the name first, so one address can serve many certificates. A dedicated address is therefore not strictly required for modern browsers. It is still requested for two practical reasons: very old devices may not send the name and would receive the wrong certificate, and some payment providers ask for a fixed address as part of setting up an account. Both halves of that answer are worth remembering, because the outdated half is still repeated in many textbooks.

**A payment gateway.** A payment gateway is the service that talks to the banks, checks whether a card can be charged, and reports the result. There are three common ways to connect one. In the first, the visitor is sent to the gateway's own page to enter card details, so the card details never touch your server. In the second, the gateway supplies the input boxes, which are displayed inside your page but still send the details directly to the gateway. In the third, your server receives the card details and passes them on. The first is the easiest to secure and the least demanding in terms of the card industry's rules; the third gives the most control and places the heaviest obligations on you.

**A database.** A shop records customers, products, orders, and payments, and those records are related to one another. A database is the program that stores them and keeps the relationships correct. It must be able to group several changes into one unit that either fully succeeds or fully fails, because an order that is marked paid without a payment record is worse than an order that failed.

### 2.6 Keeping the site safe: four ideas

Security can look like an enormous list of products. In practice four ideas cover most of it.

**Who may enter.** Every account should have only the permissions it needs. The account that serves pages should not be able to change the structure of the database, and nobody should log in as the all-powerful administrator for routine work. This is called least privilege, and its value appears after a mistake: if an account with small rights is stolen, the damage is small.

**Proving who you are.** A password alone is a weak proof, because people reuse passwords and because lists of stolen passwords circulate. Adding a second, different kind of proof, such as a code from a small application on a phone, makes a stolen password much less useful. Two passwords are not two factors; the factors must be different in kind.

**Protecting the blueprint.** Much of an attack begins with reading things that were never meant to be public: an error message that reveals file paths, a folder listing, a copy of the database left in a download folder, or the hidden folder where the code's history is stored. Turning off detailed error messages, removing stray copies, and refusing to list folders removes the easiest routes in.

**A gate with a list.** A firewall is a filter that decides which network conversations are allowed. The sensible arrangement is to refuse everything by default and then permit only what must be public: the web ports and the administrative port, ideally restricted to known addresses. A web application firewall goes further and inspects the requests themselves, which is how it catches an attack that arrives on a perfectly legal port.

### 2.7 Three ways to make copies

Backups differ in one thing: what they compare against.

A **full backup** copies everything, every time. It stands alone, so restoring is simple, but it takes the longest and uses the most space.

A **differential backup** copies everything that has changed since the last full backup. Because the comparison point stays fixed, each day's set is a little larger than the day before, and the set contains all the changes since Sunday rather than only the changes since yesterday. To restore, you need the full backup and the most recent differential.

An **incremental backup** copies everything that has changed since the last backup of any kind. Each set is small and quick, because it covers only one day. To restore, you need the full backup and then every incremental set in the order they were made, because each one contains only the changes since the one before.

| Property | Full | Differential | Incremental |
|---|---|---|---|
| What it copies | Everything | Changes since the last full | Changes since the last backup of any kind |
| Size each time | Largest | Grows each day | Smallest |
| Time to make | Longest | Moderate | Shortest |
| What a restore needs | The set alone | The full and the latest differential | The full and every incremental, in order |
| Main risk | Slow and expensive to make | Grows until the next full | One missing set breaks the chain |

A useful way to picture the difference is a notebook. A full backup photocopies the whole notebook. A differential photocopies every page written since the last full photocopy, so the pile grows all week. An incremental photocopies only the pages written since the last photocopy of any kind, so each day's pile is thin, but rebuilding the notebook means putting all the thin piles in order.

### 2.8 A backup policy in plain words

A policy answers five questions, and a plan that answers only the first is not a policy.

**How often?** Often enough that the data you would lose is data you can afford to lose. A shop that takes orders all day cannot copy its database once a week.

**What is copied?** The files, the database, and the configuration. A backup of the files alone restores a website with no content, and a backup of the database alone restores content with no website.

**Where does it go?** Somewhere the original failure cannot reach. A second folder on the same disk is not a copy; a second machine in the same room is better; a storage service in another region is better still.

**How long is it kept?** Long enough to cover the mistakes that are noticed late. A fault introduced three weeks ago needs a copy from before it was introduced.

**Has it been tested?** A copy that has never been restored is a hope. The test is to restore into a spare place and check that the site opens and the numbers match.

## 3. Methods and Operations

### 3.1 Buying a name, step by step

Step 1. Choose the name and the ending. Keep it short, easy to say aloud, and easy to spell after hearing it once. Choose the ending for the audience: a country code places the business in a country, a generic ending suits an international audience, and some endings have eligibility rules that must be met.

Step 2. Check whether it is free. A registrar's search is convenient, but the authoritative answer comes from the official list at the moment of purchase, because a name can be taken between the search and the payment.

Step 3. Choose a registrar and read the renewal price. The first year is often discounted; the renewal is the price you will pay for as long as you keep the name. Also check the transfer rules and whether privacy protection for the published record is included.

Step 4. Supply accurate details. The official record needs the name of the holder, a postal address, and a working mailbox that somebody actually reads. An unreachable record is how names are lost at renewal, because the reminder never arrives.

Step 5. Pay and complete any checks. Some endings require proof of eligibility, and the name may sit in a pending state until that proof is accepted.

Step 6. The registrar updates the official list. This is the moment the name becomes real: the registry records which servers are responsible for it.

Step 7. Configure those servers. The responsible servers must hold your zone with the address of your website and the records for your mail. The two steps happen in two different places, and forgetting the second produces the classic result: the name exists, the servers are named, and every visitor sees an error.

Step 8. Wait, then check from outside. Ask the responsible server directly, and then ask an ordinary resolver. The first answer proves your zone is correct; the second proves the world can see it.

Step 9. Lock the name and set it to renew automatically. The lock stops anybody who obtains your login from moving the name elsewhere. Automatic renewal prevents the commonest cause of losing a name, which is a payment card that expired quietly.

### 3.2 Pointing the name at the server

If your DNS provider is the registrar, you edit records in a control panel and the change takes effect within the record's time to live. If you use a separate DNS provider, you first tell the registrar which servers are responsible, and then edit the records at that provider.

The safe order is: create the zone at the new provider with every record copied; test the new servers directly by asking them; lower the time to live on the old records a day in advance; make the change; wait for the old time to live to pass; and only then switch the old service off. Doing it in the other order creates a window in which visitors are sent to servers that no longer know the answers.

### 3.3 Putting the files on the server

There are three common ways to get the site onto the machine.

The first is to copy files directly with a secure file transfer tool. It is simple and fine for a small site, but it is easy to copy a half-finished change and there is no record of what was deployed.

The second is to upload an archive and unpack it on the server. This is faster for many small files and gives a clean, repeatable step, provided the archive is built from a known version.

The third, and the best for anything that will be maintained, is to keep the code in a version control system and have the server fetch a specific version. The record of what is running is then exact, and going back to the previous version is a single step rather than a hunt for the file that changed.

Whichever method is used, three rules apply. Never deploy into the folder that holds uploads, because a mistake there destroys customer content. Keep credentials outside the code, in the server's environment rather than in a file that might be served to a visitor. And never leave a copy of the database, an archive, or a backup inside the folder that the web server publishes.

### 3.4 Turning on the padlock

Step 1. Make sure the name already points at the server, because the certificate authority will check that you control the name by asking the server a question.

Step 2. Request a certificate for the exact name visitors use, and for the other form of the name if both are used. A certificate for `www.example.com` does not cover `example.com`.

Step 3. Prove control. The commonest method is to place a small file at a known path and let the authority fetch it over the ordinary web port. A second method places a special value in a DNS record, which also allows a single certificate to cover every subdomain.

Step 4. Install the certificate together with the intermediate certificates supplied by the authority. A missing intermediate is the reason a site can look correct in one browser and produce a warning in another.

Step 5. Redirect ordinary requests to the encrypted version, and add the header that tells browsers to use the encrypted version in future.

Step 6. Automate renewal and test it. A certificate is not a one-off purchase; it is a subscription that must renew itself, and the failure mode is a site that works perfectly until a date nobody wrote down.

### 3.5 Setting the gate rules

Step 1. Decide which ports must be public. For an ordinary site that is the web port and the encrypted web port. The administrative port should be reachable only from known addresses where possible.

Step 2. Refuse everything else by default, in both directions where the provider allows it. Refusing outbound traffic as well makes it much harder for an intruder to send stolen data away or to fetch further tools.

Step 3. Turn off password logins for administration and use a key instead. A key is a very long random value that cannot be guessed, and it removes the entire category of password guessing.

Step 4. Create a separate account for administration, and do not use the all-powerful account for ordinary work.

Step 5. Check what is actually listening. A firewall rule cannot help if a database is listening on the public interface, so the database should be configured to accept connections only from the machine itself.

Step 6. Write the rules down and keep them in the repository with the code. Rules that exist only in somebody's memory are lost with that person.

### 3.6 Making and testing the first backup

Step 1. Write down what must be copied: the site files, the database, and the configuration. Add the list of installed software versions, which saves hours during a rebuild.

Step 2. Copy the files into an archive with a date in the name, so that sets can be told apart without opening them.

Step 3. Copy the database using the database's own export tool rather than by copying its files while it runs, because a running database's files are not consistent with one another.

Step 4. Record a checksum for each file. A checksum is a short fingerprint of the contents; if the copy is truncated or altered, the fingerprint no longer matches.

Step 5. Send the set somewhere else, in a way that does not delete older sets by accident.

Step 6. Restore it into a spare place and check that the site opens and the record counts match. This is the step everybody skips and the only one that turns a copy into a backup.

### 3.7 The weekly routine

A small site can be kept healthy with a short routine. Check that the site loads and that the padlock is valid. Check that last night's backup exists and that its fingerprint matches. Check the free disk space, because a full disk stops a database in a way that looks like a crash. Check the list of failed logins, because a long list is the signature of automated guessing. Read the error log for anything repeated. And once a quarter, restore something on purpose.
## 4. Worked Implementation from the Notes

### 4.1 Task: find out where a name actually points

### 4.2 Implementation: ask the directory, then ask the machine

Step 1. Ask the local resolver for the address behind a name.

```bash
nslookup shop.example.com
```

Observed output:

```text
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
Name:   shop.example.com
Address: 203.0.113.10
```

Step 2. Read the words carefully. "Non-authoritative" means the answer came from a cache rather than from the server that is responsible for the zone. It is a perfectly good answer for ordinary use, but it cannot tell you whether the zone itself is correct, because it may be a copy of an answer that was correct an hour ago.

Step 3. Ask the responsible server directly, naming it explicitly. The tool `dig` is available on most systems and gives more detail than `nslookup`.

```bash
dig @ns1.example-dns.net shop.example.com A +short
```

Observed output:

```text
203.0.113.10
```

Step 4. Ask the same server for the full answer and look at the flags.

```bash
dig @ns1.example-dns.net shop.example.com A
```

Observed output:

```text
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 30214
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; ANSWER SECTION:
shop.example.com.       300     IN      A       203.0.113.10
```

Step 5. Explain what the answer proves. The `aa` flag stands for authoritative answer, so this server holds the zone and this is the real address. The number 300 is the time to live in seconds, so the answer may be cached for five minutes. If this query had returned `SERVFAIL`, meaning the server could not complete the lookup, the problem would be the delegation rather than the zone; if it had returned `NXDOMAIN`, meaning the name does not exist, the name would genuinely be missing.

### 4.3 Task: confirm what certificate a site presents

### 4.4 Implementation: ask for the certificate by name

Step 1. Request the certificate for a specific name and print its subject and dates.

```bash
echo | openssl s_client -connect shop.example.com:443 -servername shop.example.com 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

Observed output:

```text
subject=CN = shop.example.com
issuer=C = US, O = Let's Encrypt, CN = R11
notBefore=Nov  1 09:12:00 2026 GMT
notAfter=Jan 30 09:11:59 2027 GMT
```

Step 2. Explain each line. The subject names the site the certificate was issued for, shown as `CN` for common name, and it must match the name the visitor typed. The issuer names the authority that signed it, and that authority must be one the browser trusts. The dates bound the period of validity, and the second date is the one that produces the warning page when it passes.

Step 3. Check the response headers, including the redirect from the unencrypted port.

```bash
curl -I http://shop.example.com/
```

Observed output:

```text
HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Sat, 07 Nov 2026 09:14:02 GMT
Location: https://shop.example.com/
```

Step 4. Check the encrypted version and look for the security header that tells browsers to stay encrypted.

```bash
curl -I https://shop.example.com/
```

Observed output:

```text
HTTP/1.1 200 OK
Server: nginx
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
```

Step 5. Explain the result. The 301 is a permanent redirect, which is correct because the encrypted address is the real one. The strict transport header tells the browser to refuse the unencrypted version for the next year, which closes the brief window in which a visitor could be redirected by somebody on the network.

### 4.5 Task: make a small, complete backup

### 4.6 Implementation: files, database, fingerprint, copy elsewhere

Step 1. Write a short script that performs the whole job and stops at the first error.

```bash
#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M)"
DEST="/srv/backup/daily/$STAMP"
mkdir -p "$DEST"

tar --create --gzip --file "$DEST/site.tar.gz" -C /var/www shop
mysqldump --single-transaction shop > "$DEST/shop.sql"
cp /etc/nginx/sites-available/shop.conf "$DEST/nginx-shop.conf"
sha256sum "$DEST"/* > "$DEST/SHA256SUMS"

rsync -a "$DEST" backup@offsite.example.net:/srv/shop-backup/daily/
echo "backup complete: $DEST"
```

Step 2. Explain the three important choices. The first line makes the script stop if any command fails, so a failed database export cannot be followed by a cheerful "complete" message. The option passed to the database export takes a consistent copy while the site keeps serving. The last copy command sends the set to a different machine, which is what makes it a backup rather than a second copy of the same risk.

Step 3. Run it and read the output.

```bash
chmod +x /usr/local/bin/site-backup
/usr/local/bin/site-backup
```

Observed output:

```text
backup complete: /srv/backup/daily/20261107-0200
```

Step 4. Prove the copy is intact by checking the fingerprints.

```bash
cd /srv/backup/daily/20261107-0200
sha256sum -c SHA256SUMS
```

Observed output:

```text
nginx-shop.conf: OK
shop.sql: OK
site.tar.gz: OK
```

Step 5. Explain why this step matters. A backup script that reports success has told you only that its commands ran. The fingerprint check tells you that the bytes stored are the bytes written. Neither tells you that the set can be restored, which is why the next task exists.

### 4.7 Task: restore one file and one table

### 4.8 Implementation: put the copy back and compare

Step 1. Delete something small on purpose in a test environment, so that the restore is exercised before it is needed.

```bash
rm /var/www/shop/logo.png
```

Step 2. Extract just that one file from the archive.

```bash
tar --extract --gzip --file /srv/backup/daily/20261107-0200/site.tar.gz \
    -C /var/www shop/logo.png
```

Step 3. Restore the database into a scratch database rather than over the live one, so that the test cannot make things worse.

```bash
mysql -e "CREATE DATABASE shop_restore;"
mysql shop_restore < /srv/backup/daily/20261107-0200/shop.sql
```

Step 4. Compare the important numbers between the copy and the live database.

```sql
SELECT COUNT(*) AS products FROM shop_restore.products;
SELECT COUNT(*) AS orders FROM shop_restore.orders;
```

Observed output:

```text
products
--------
148

orders
------
9021
```

Step 5. Explain the result. The counts match what the live database reported before the test, so the restore produced a usable copy. If the counts had been zero, the archive would have contained an empty dump, which is the classic failure of a backup that copied the database files while the service was running.

### 4.9 Task: close the doors that do not need to be open

### 4.10 Implementation: default refuse, explicit permits, then look

Step 1. Permit the key-based login and refuse passwords.

```ini
# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers deploy
```

Step 2. Reload the service and confirm the setting that is actually in force.

```bash
sudo systemctl reload ssh
sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication'
```

Observed output:

```text
permitrootlogin no
passwordauthentication no
```

Step 3. Set the network filter to refuse by default and permit only the public services.

```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

Step 4. Look at what is listening, because a filter is no help against a service that is reachable some other way.

```bash
sudo ss -tulpn
```

Observed output:

```text
Netid State  Local Address:Port   Process
tcp   LISTEN 0.0.0.0:22           sshd
tcp   LISTEN 0.0.0.0:80           nginx
tcp   LISTEN 0.0.0.0:443          nginx
tcp   LISTEN 127.0.0.1:3306       mysqld
```

Step 5. Explain the last line. The database is listening only on the loopback address, which means it accepts connections from the machine itself and from nowhere else. Even if a firewall rule were changed by mistake tomorrow, the database would still be unreachable from outside. Two independent protections of that kind are worth more than ten rules that all depend on one setting.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Beginner misconceptions, and what is actually true

**"Buying a domain means owning it forever."** A name is rented for a period, usually one year at a time. If it is not renewed, it passes through a grace period, then a redemption period during which it can be recovered for a fee, and then back to general availability, where anybody may take it within minutes of its release.

**"The registrar hosts my website."** The registrar maintains the registration and the identity of the responsible servers. The website itself lives on a hosting service, which may be a completely different company. Many registrars sell hosting as well, which is why the two are confused, but they are separate services with separate failures.

**"Changing the nameservers moves my website."** It changes which servers answer questions about the name. The actual files stay wherever they were. Moving the site and moving the name are two operations that must be planned together, and doing one without the other produces an outage.

**"DNS changes travel around the world in a few minutes."** Cached answers survive until their time to live expires, which may be minutes or may be two days for the delegation itself. The delay is bounded by a number that can be read in advance and lowered deliberately.

**"Shared hosting is fine for a shop because each site has its own password."** A password protects a folder inside one operating system. It does not separate one customer's files from another's at the level the operating system works at, and it does not stop a neighbour from consuming the shared processor.

**"A padlock means the site is safe."** The padlock means the connection is encrypted and the certificate matches the name. It says nothing about whether the site has been updated, whether its database is backed up, or whether the business behind it is honest.

**"Every site needs its own IP address for encryption."** Modern browsers state the name they want at the start of the connection, so many certificates can share one address. A dedicated address is still useful for very old devices and is still requested by some payment providers.

**"A backup is a copy in another folder."** A copy on the same disk disappears with the disk. A copy in the same building disappears with the building. A backup is a copy that a single failure cannot reach.

**"The backup job said it succeeded, so the backup is good."** The message means the commands finished. Only a fingerprint check and a test restore show that the data can actually be used.

**"A differential backup is the same as an incremental one."** A differential compares against the last full backup, so it grows each day, and a restore needs only the full and the latest differential. An incremental compares against the last backup of any kind, so it stays small, and a restore needs every set in order.

**"The replica is my backup."** A replica copies every change, including a deletion and including the encryption performed by an intruder. It protects against a broken disk, not against a mistake.

**"Uptime of 99.9 per cent means the site is nearly always up."** It means the machine is promised to be available for all but about nine hours a year, excluding planned maintenance. It also says nothing about whether the site itself is working, since an expired certificate or a broken update takes the site down while the machine stays perfectly healthy.

**"Security is a product I can install."** Security is a set of controls: who may enter, how they prove it, what is exposed, and what is copied. Products help with each, but no single product supplies all four.

### 5.2 Reading simple outputs

A name lookup tells you two different things depending on where you ask. Asking your own machine tells you what your machine believes, which may be an old cached answer. Asking the responsible server tells you what is actually published. When the two disagree, the zone is usually right and the cache is stale, and the cure is to wait for the time to live to pass.

A certificate check tells you four things at once: the name it was issued for, the authority that signed it, the first valid day, and the last valid day. Read all four. A certificate that matches the name but expired yesterday produces a warning; a certificate that is valid but issued for a different name also produces a warning, and the two look identical to a visitor.

A backup check should always include the fingerprint. A file that exists and has a plausible size may still be truncated, and a database export that ran while the service was writing may still be unopenable. The fingerprint catches the first; only a restore catches the second.

A firewall check should always include the list of listening services. Rules describe what is meant to be allowed; the listening list describes what could be reached if a rule were wrong. When the two disagree, the listening list is the more honest document.

### 5.3 Symptom to cause

| What you see | Likely cause | What to check first |
|---|---|---|
| The site does not load at all, and no error appears | The name does not resolve, or the delegation is broken | Look up the name and read whether the answer is authoritative |
| A page saying the site cannot be found | The zone is missing at the DNS provider, or the name was never delegated | Ask the responsible server directly for the name |
| The site works for you but not for a colleague | An old cached answer on one machine, or a change still spreading | Compare the two machines' lookups |
| A full-page warning about the connection | The certificate expired, or it was issued for another name | Print the certificate subject and its dates |
| The padlock appears only in some browsers | The intermediate certificate is missing from the installation | Count the certificates in the chain |
| The site is slow in the afternoon | A neighbour on a shared plan, or too few workers for the traffic | Measure response time at different hours |
| The site stops near the end of the month | The monthly traffic allowance was used | Read the provider's usage page and the plan terms |
| A form fails with a long technical message | Detailed errors are switched on in production | Read the error log rather than the page |
| The database will not start | The disk is full, often from logs or old backups | Check free space before anything else |
| Last night's backup is missing | The job failed silently, or the retention rule deleted it | List the destination and read the job log |
| The restored site has no products | The database was copied from its files while running | Compare the record counts in the dump with the live site |
| Visitors are asked for a password by the browser | A protection was left switched on by mistake | Check the directory protection settings |

### 5.4 Small checks you can do yourself

- Explain, without using the word "propagate", why a change to a record may take time to be seen everywhere.
- Name the four roles in the registration system and say which one you pay.
- Say which hosting model you would choose for a three-page site and why, then for a shop with steady traffic and card payments.
- Convert 99.9 per cent uptime into hours per year, then explain why the real figure may be worse.
- State the difference between a differential and an incremental backup in one sentence each.
- Explain why a dedicated address is no longer required for encryption, and give one reason it is still asked for.
- Describe what a checksum proves and what it does not prove.
- Name three things that should never be left inside the folder the web server publishes.
- Explain why the database should listen only on the local address.
- Say what you would check first if a site suddenly stopped resolving without anybody changing anything.

### 5.5 What to remember

The subject reduces to four arrangements and one habit. The arrangements are the name, the machine, the lock, and the copy. The habit is to ask which of the four has failed before changing anything, because most wasted afternoons come from editing the wrong layer: lowering a record's time to live when the certificate has expired, reinstalling the site when the disk is full, or rebuilding the server when the backup was never tested.

The other habit worth keeping is to write things down. A short note recording which company holds the name, when it renews, which servers are responsible for the zone, where the copies live, and when the last restore was tested turns a frightening outage into a checklist. That note is the beginning of a disaster recovery plan, and it costs nothing to write while everything is working.

