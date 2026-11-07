## 1. Concept and Use Case

### 1.1 How this topic is examined

This topic is examined as a **process-plus-judgement** subject rather than as a vocabulary test. Questions ask you to trace a procedure, to compare two arrangements, to justify a recommendation, or to repair a plan that contains a deliberate fault. Marks are awarded for the correct sequence of steps, for the precise term, and for the consequence of each step. A list of terms with no sequence earns little; a sequence with the wrong term earns less than it looks, because the marker is checking whether you know which layer you are talking about.

Four question shapes recur.

The **trace** question asks for the path of a request or the sequence of a registration, and awards one mark per correctly ordered stage. The **compare** question asks for differences between hosting models or between backup types, and awards marks for discriminators rather than descriptions: not "shared hosting is cheap" but "the isolation boundary is a user account inside one kernel, so a neighbour can read files through a shared component". The **design** question supplies a business requirement, usually a recovery point, a recovery time, a traffic estimate, and a compliance constraint, and asks you to select and justify. The **diagnose** question supplies a symptom and asks for the layer and the next check.

The mark tariff is usually proportional to the number of defensible points, roughly one mark per distinct correct statement, with a cap on repetition. That has a practical consequence: an answer with eight distinct correct points scores eight, while four points restated in different words scores four. Breadth beats elegant prose.

### 1.2 The four-layer skeleton

Every long answer in this topic can be organised around four layers, and using the skeleton prevents the commonest structural failure, which is answering about the wrong layer.

**Layer one, naming.** The domain name, the registry, the registrar, the delegation, the authoritative zone, the record, the time to live. Failures here produce a name that does not resolve, a name that resolves to the wrong place, or a name that resolves differently for different visitors.

**Layer two, transport and identity.** The address, the listening socket, the packet filter, the certificate, the handshake, the server name indication. Failures here produce a connection that is refused, a connection that is intercepted with a warning, or a certificate that is valid for a different name.

**Layer three, execution.** The server model, the processor and memory allocation, the runtime, the application, the worker limit. Failures here produce a site that is slow, a site that returns an error page, or a site that works until traffic rises.

**Layer four, persistence.** The database, the transaction, the backup set, the retention policy, the restore procedure. Failures here produce lost data, and the loss is permanent when a copy does not exist or cannot be restored.

A strong answer names the layer before it names the remedy. "The name resolves and the port answers, so the fault is at the certificate layer; the subject name in the certificate does not match the requested name" is a sentence that earns several marks because it demonstrates both the diagnosis and the mechanism.

### 1.3 Command words and what each one requires

**State** or **give** requires a fact with no explanation, typically one mark. **Define** requires a precise boundary: what is included and what is excluded. **Describe** requires the mechanism in order, with the actors named. **Explain** requires a cause-and-effect chain, so the word "because" or its equivalent must appear. **Compare** requires at least two explicit dimensions and a statement of which is better for a stated purpose. **Justify** requires a reason tied to the requirement in the question. **Evaluate** requires both sides and a conclusion with a criterion.

The distinction is worth marks because examiners write the tariff around it. A question worth six marks that begins "Explain why a differential backup grows" expects a reference point, a growth mechanism, a comparison with the incremental case, and a consequence for restore time. Six separate facts about backups generally will not fit the question.

### 1.4 Where the marks actually sit

Marks cluster in four places, and revision should be weighted accordingly.

The **delegation chain** is the most reliably examined mechanism because it has an exact order and several named parts. Expect a question worth four to six marks that requires the root, the top-level domain, the authoritative server, and the distinction between the parent-side delegation and the child-side zone.

**Hosting model discrimination** is examined as a scenario. The question supplies a business and asks for a recommendation with justification. The marks are for the isolation boundary, the administrative responsibility, the cost consequence, and the suitability for the stated traffic.

**Backup arithmetic** is examined as a calculation plus a procedure. The calculation is the conversion of a stated recovery point into a schedule; the procedure is the ordered list of sets required for a restore. This is where the differential and incremental distinction is tested, and it is the single most common place to lose marks through vagueness.

**Security control mapping** is examined as a table or a short essay. The marks are for naming the control and the specific failure it prevents. "A firewall" alone earns little; "a default-deny inbound packet filter prevents the database port from being reachable from the Internet" earns the mark because the failure is named.

### 1.5 The scope in one sentence each

Domain registration: a name is rented through a registrar, written into a registry, and delegated to authoritative servers that hold the actual records. Hosting: four models differ in where the isolation boundary sits, and the price rises as the boundary moves outward. Resources: disk, monthly transfer, processing, and uptime are the four numbers, and uptime converts into downtime that can be memorised. Commerce: encryption, an address policy that understands server name indication, a payment integration model that determines compliance scope, and a transactional database. Security: least privilege, strong authentication, source code protection, and a default-deny filter. Backup: three strategies defined by their reference point, and a policy defined by recovery point, recovery time, retention, location, and testing.

## 2. Data, Syntax, and Core Concepts

### 2.1 High-yield facts and their typical mark values

The following facts recur across papers. The mark column is the typical value of the fact stated correctly and in context, not the value of the whole question.

| Fact | Typical marks | What the marker looks for |
|---|---|---|
| The registry holds only the delegation; the zone holds the records | 2 | The word delegation, and the contrast with the child zone |
| The registrar acts on the registry through a provisioning protocol | 1 | A named protocol or the phrase provisioning interface |
| A name must be delegated before it resolves | 2 | Order: create, then delegation, then zone contents |
| Shared hosting isolates by account, not by kernel | 2 | The words account and kernel in contrast |
| A virtual private server isolates through a hypervisor | 2 | Hypervisor, and reserved processor and memory |
| Colocation rents the facility while the customer owns the hardware | 2 | Ownership of hardware, responsibility for faults |
| Uptime percentages convert to annual downtime | 1 | A correct figure, not a description |
| 99.9 per cent is about eight hours forty-six minutes a year | 2 | The figure and the unit |
| Server name indication removes the need for one address per certificate | 3 | The extension named, the mechanism, the modern conclusion |
| A dedicated address is still requested for legacy clients and some gateways | 2 | Both reasons, stated as practical rather than technical necessity |
| A hosted payment page keeps card data outside the merchant's scope | 2 | The compliance consequence, not just the redirect |
| A payment notification must be verified before the order is marked paid | 3 | Signature over the raw body, and amount comparison |
| Least privilege limits the damage after a compromise | 2 | The phrase after a compromise |
| A salted slow hash is required for stored passwords | 2 | Salt and slowness, not just hashing |
| A default-deny inbound policy is the correct firewall posture | 2 | Default deny, with explicit permits |
| A differential backup is measured against the last full | 3 | The reference point and the growth consequence |
| An incremental backup is measured against the last backup of any kind | 3 | The reference point and the chain consequence |
| A restore needs two sets under differential and the full chain under incremental | 3 | The ordered list |
| A recovery point objective is a data-loss tolerance | 2 | Time, and loss rather than downtime |
| A recovery time objective is a downtime tolerance | 2 | Time, and service rather than data |
| Three copies on two media with one off-site is the minimum rule | 2 | All three numbers |
| A replica is not a backup because it copies deletion | 2 | The mechanism of the failure |

### 2.2 Registration, delegation, and the exact order

The order is the answer, so it should be memorised as a sequence rather than as a set of facts.

First, the registrant chooses a name that is available and a registrar that is accredited. Second, the registrar submits a create command to the registry over a provisioning protocol, usually the Extensible Provisioning Protocol, abbreviated EPP, carried over an encrypted session. Third, the registry writes the name into the top-level zone with the nameserver record set supplied, which is the delegation. Fourth, the authoritative servers named in that delegation serve the zone, which holds the address records, the mail exchanger, and the policy records. Fifth, resolvers cache each answer for its time to live, which is why changes are not instantaneous.

The delegation is a pair of records at the parent, and the zone is a set of records at the child. A question that asks why a correctly delegated name still fails almost always expects this answer: the delegation points at servers that do not hold the zone, or hold an empty one, which yields a negative answer or a server failure rather than a referral.

The status values that appear in registration records are worth one mark each in a short-answer question.

| Status | Who sets it | What it means for the visitor |
|---|---|---|
| `ok` | Registry | The name behaves normally |
| `inactive` | Registry | The name exists but has no delegation, so nothing resolves |
| `clientTransferProhibited` | Registrar | The site works, but the name cannot be moved to another registrar |
| `clientHold` | Registrar | The name is removed from the zone, so the site disappears |
| `serverHold` | Registry | The same removal, imposed at the registry |
| `redemptionPeriod` | Registry | The name is deleted but recoverable for a fee |
| `pendingDelete` | Registry | The name is about to return to general availability |

The distinction that earns marks is between a status that affects the **registration** and a status that affects **resolution**. Transfer prohibition does not disturb visitors; a hold does.

### 2.3 Hosting models compared on examinable dimensions

The dimensions that earn marks are isolation, administrative responsibility, cost, performance predictability, and suitability. Descriptions of features earn less than statements about boundaries.

| Dimension | Shared | Virtual private server | Dedicated | Colocated |
|---|---|---|---|---|
| Isolation boundary | User account in one operating system | Hypervisor between guests | Physical machine | Physical machine, plus the building |
| Kernel control | None; the provider's kernel | Full, inside the guest | Full, including firmware | Full, including hardware choice |
| Patching responsibility | Provider | Customer or managed service | Customer | Customer |
| Cost band | Lowest | Moderate | High | High, plus hardware |
| Neighbour effect | Processor, memory, and disk all contested | Disk and network only | None | None, but facility shared |
| Suitability | Brochure site, low traffic | Growing application, staging | High traffic, regulated data | Large estate, special hardware |

A recommendation answer needs three moves: state the requirement from the scenario, match it to a boundary, and state the cost consequence. "The shop takes card payments and has bursty traffic, so the isolation of a virtual private server is the minimum, because a shared account is a permission boundary rather than a kernel boundary; the cost is that patching and certificate renewal become the shop's responsibility, which can be met by a managed service at additional cost" is a complete answer.

### 2.4 Resource metrics and the conversions worth memorising

| Availability | Annual downtime | Monthly downtime |
|---|---|---|
| 99 per cent | About 3 days 15 hours | About 7 hours 18 minutes |
| 99.5 per cent | About 1 day 20 hours | About 3 hours 39 minutes |
| 99.9 per cent | About 8 hours 46 minutes | About 43 minutes 50 seconds |
| 99.95 per cent | About 4 hours 23 minutes | About 21 minutes 55 seconds |
| 99.99 per cent | About 52 minutes 36 seconds | About 4 minutes 23 seconds |

Three qualifications earn a mark each when the question is evaluative. Scheduled maintenance is normally excluded from the promise. Compensation is normally a credit against future charges rather than a payment for lost trade. Server availability is not site availability, because an expired certificate, a failed deployment, or a saturated database takes the site down while the machine reports itself healthy.

For the other three resources, the examinable point is the metering method rather than the number. Disk space is a capacity that must cover files, database, logs, and temporary working room during upgrades. Monthly transfer is either capped or billed on a percentile of sampled rates, and the two are not comparable. Processing speed on a shared plan is unstated, so the only evidence is the measured response of other sites on the same provider, while on a virtual or dedicated plan the meaningful figures are virtual processors, memory, and input and output operations per second, with memory usually deciding the database's behaviour.

### 2.5 E-commerce prerequisites, stated with the correct nuance

**Encryption.** A valid certificate matching the requested name, a complete chain including intermediates, a redirect from the plain scheme, and a strict transport header once the site is ready for it. The header is difficult to withdraw and should be introduced with a short lifetime first.

**The address question.** The historically correct statement was that each encrypted site needed its own address, because the server chose the certificate before knowing the requested name. Server name indication, sent by the client at the start of the handshake, carries the requested name in the clear and allows one address to serve many certificates. The modern statement is therefore that a dedicated address is **not strictly required** for current clients, but is **still requested** because some legacy clients do not send the name and would receive the default certificate, producing a mismatch, and because some payment providers require a fixed address during onboarding. An answer that states only the old absolute loses the nuance marks; an answer that denies any remaining reason also loses them.

**Payment integration.** Three shapes with different compliance consequences. A hosted payment page keeps card data entirely off the merchant's server and corresponds to the lightest self-assessment. Hosted fields, rendered by the gateway inside the merchant's page, also keep card data away from the merchant's code. A server-to-server interface passes card data through the merchant's server and carries the heaviest obligations, including network segmentation. In every shape, the notification that reports an outcome must be verified by computing a signature over the raw request body with a shared secret and comparing it in constant time, and the amount and currency must be compared with the stored order before the order is marked paid.

**Database requirements.** Transactions with atomicity, consistency, isolation, and durability; an isolation level chosen against the concurrency anomalies the business can tolerate; least-privilege accounts, so the account serving pages cannot alter the schema; and parameterised statements so that visitor input cannot become statement text.

### 2.6 Security controls and the failure each prevents

| Control | Precisely what it prevents |
|---|---|
| Least-privilege accounts | An intruder who steals the web account rewriting every file on the host |
| Multi-factor authentication | A password stolen elsewhere being replayed against the administrative panel |
| Key-only shell access | Automated password guessing against the server |
| Salted slow password hashing | Reversal of a stolen user table in hours on commodity hardware |
| Disabled error display in production | Disclosure of file paths, queries, and framework versions through error pages |
| No repository or backup inside the document root | Download of source history or a database dump by a scanner |
| Default-deny stateful packet filter | Unrequested inbound connections to database and cache ports |
| Web application firewall | Known injection and scanning patterns reaching the application |
| File integrity monitoring | A backdoor surviving unnoticed in an unvisited file |
| Content security policy | Script from an untrusted origin executing in a visitor's session |
| Network segmentation | Lateral movement from a compromised front end to the database |
| Encrypted, immutable off-site backups | Destruction of recovery copies by ransomware |

The distinction between authentication and authorisation is worth two marks whenever it appears: authentication establishes who is present, authorisation decides what that identity may do. A 403 response means the identity is known and refused; a 401 response means no acceptable identity was presented.

### 2.7 Backup definitions, restore dependency, and the arithmetic

| Property | Full | Differential | Incremental |
|---|---|---|---|
| Reference point | None | Last full | Last backup of any kind |
| Content | All selected data | All change since that full | All change since that backup |
| Set size over time | Constant and largest | Growing | Constant and smallest |
| Restore sets | One | Two | Full plus every incremental |
| Restore order | Not applicable | Full, then latest differential | Full, then incrementals oldest to newest |
| Failure mode | Cost and duration | Growing backup window | A missing or corrupt set breaks the chain |

Two consequences are worth memorising as sentences. Under a differential schedule, the newest differential already contains every change since the full, so intermediate differentials are not needed. Under an incremental schedule, each set contains only the delta from its immediate predecessor, so every set is needed and the order is mandatory.

### 2.8 Recovery objectives, retention, and location

The recovery point objective is the maximum tolerable data loss, expressed in time. It is met by the backup frequency plus the transaction log interval. The recovery time objective is the maximum tolerable outage, expressed in time. It is met by the restore method: restoring from object storage, restoring onto a warm standby, or failing over to a hot site.

Retention is usually a rotation: daily sets for a fortnight, weekly sets for a quarter, monthly sets for a year. Location follows the rule of three copies on two media with one off-site, extended in current practice by one copy offline or immutable and zero errors on verification. Immutability is the answer to ransomware that searches for and destroys reachable copies. Encryption protects copies in transit and at rest, and the key must be held separately, or an attacker who takes both gains everything.
## 3. Methods and Operations

### 3.1 The six-move template for a process question

A process question can be answered in a fixed shape that fits almost any tariff.

Move one, name the starting state and the actor. "The registrant selects an available name at an accredited registrar." The actor matters because markers award a mark for the party that performs each step.

Move two, name the interface between parties. "The registrar submits a create command to the registry over a provisioning protocol." Naming the interface is usually worth a mark on its own.

Move three, describe the state change. "The registry writes a delegation into the top-level zone, consisting of the nameserver record set for the domain." The state change is what distinguishes a description from a list.

Move four, describe the second state change at the other side. "The authoritative servers publish the zone containing the address record, the mail exchanger, and the policy records." Most candidates stop after move three and lose the marks that depend on knowing there are two sides.

Move five, describe the observable effect. "A resolver walking the chain receives a referral from the root, a referral from the top-level domain, and an authoritative answer from the child servers." This is where the answer becomes testable.

Move six, describe the timing or failure condition. "Each answer is cached for its time to live, so a change is visible only after the previous answer expires; if the delegation points at servers without the zone, the result is a server failure rather than a name that does not exist."

Six moves usually cover eight to ten marks. If the tariff is higher, add a seventh move on verification: how an operator confirms that each stage worked.

### 3.2 The four-move template for a comparison question

Move one, state the dimension being compared. "The first dimension is the isolation boundary."

Move two, state each side's value on that dimension in the same sentence structure, so the contrast is visible. "Shared hosting isolates by user account inside a single kernel, whereas a virtual private server isolates by hypervisor between guests."

Move three, state the consequence. "The consequence is that a vulnerable shared component is reachable from every site on the machine, while a hypervisor prevents a neighbour from reading the guest's memory or filesystem."

Move four, tie the dimension to the scenario. "For a shop handling card data, the shared boundary is insufficient, so the minimum acceptable model is a virtual private server."

Repeating those four moves for isolation, administrative responsibility, cost, and performance predictability produces a complete comparison answer. The failure mode to avoid is a paragraph per model, which reads well but does not compare: the marker is looking for paired statements on the same dimension.

### 3.3 The restore calculation template

Backup questions usually combine three tasks: convert an objective into a frequency, list the sets required, and state the order.

For the frequency, divide the objective by the interval the schedule can achieve, and state the result as a bound. "An objective of fifteen minutes cannot be met by a nightly full backup, which leaves up to twenty-four hours of loss; it requires continuous archiving of the transaction log with a replay to the failure point."

For the set list, name the schedule and the recovery time, then derive the sets. "With a full on Sunday and differentials nightly, a recovery at Friday noon needs the Sunday full and Thursday night's differential, because that differential contains every change since Sunday."

For the order, write the sequence as an explicit list rather than as prose. Ordering is where marks are lost silently, because a correct set of names in the wrong order reads as if it were correct.

For the time, add the components rather than quoting the copy duration. "The restore time is the time to detect, to decide, to locate the sets, to copy them, to apply them in order, and to verify the result; the copy alone is the smallest component."

A compact way to present the derivation in an answer is a short block, which is also easier for a marker to follow.

```text
Given:   full Sunday 02:00, differentials Mon-Sat 02:00
Target:  recover state as at Friday 02:00
Sets:    full(2026-11-01 02:00) + differential(2026-11-06 02:00)
Order:   1. restore full  2. apply differential  3. verify invariants
Why:     differential is measured against the full, so it already
         contains Monday through Friday; intermediate sets are redundant
Counter: under an incremental schedule the sets would be
         full + Mon + Tue + Wed + Thu + Fri, applied in that order
```

### 3.4 The security design template

Security questions reward a control-to-failure mapping and punish a product list.

Move one, restate the asset. "The asset is the customer database and the order records it contains."

Move two, name the threat class. "The relevant threats are credential theft against the administrative panel, injection through the search form, and destruction of the backups by ransomware."

Move three, pair each control with the failure it prevents. "Key-only shell access with a named administrative account prevents automated password guessing from succeeding even if a password is reused elsewhere."

Move four, state the residual risk. "These controls do not prevent a determined attacker who obtains a valid session; the residual risk is met by monitoring and by the ability to restore."

Move five, state the cost or inconvenience. "The cost is administrative overhead: key distribution, a second factor for every administrator, and a restore rehearsal each quarter."

The residual-risk move is what separates a strong evaluation from a checklist, because it acknowledges that controls reduce probability rather than eliminate loss.

### 3.5 The diagnosis template

A diagnosis question supplies a symptom and asks for the cause. Four sentences suffice.

First, state what is proven. "The name resolves to the correct address from an external resolver, so the delegation and the zone are correct."

Second, state what is excluded. "The port answers, so routing and the packet filter are not the fault."

Third, state the remaining layer and the mechanism. "The handshake fails with a name mismatch, so the certificate presented does not cover the requested name, which happens when the default server block is selected because the client sent no server name."

Fourth, state the next check. "Reading the certificate subject with a name-aware client confirms which certificate was selected, and adding a server block for the missing name corrects it."

### 3.6 Phrasing that earns marks and phrasing that loses them

Earning phrases are comparative and mechanical: "measured against the last full", "because the server selects the certificate before the request arrives", "the consequence is that a neighbour can reach the shared component", "the default is deny with explicit permits for the public ports".

Losing phrases are absolute and decorative: "very secure", "fast and reliable", "the best option", "propagates across the Internet", "the backup is taken regularly". Each of these invites the question "compared with what, and by what mechanism", and the answer is where the marks were.

Two specific habits are worth adopting. Use the precise term even when a plain word would do, because the term is what is on the mark scheme: "delegation" rather than "pointing", "reference point" rather than "starting from", "recovery point objective" rather than "how much we can lose". Then attach a consequence to every term, because a term without a consequence earns the definition mark and nothing else.

### 3.7 A bank of question stems

The following stems cover the shapes that appear most often, and each can be answered with one of the templates above.

- Describe the sequence of events by which a newly registered name becomes reachable.
- Explain the roles of the registry, the registrar, and the authoritative nameserver.
- Compare two hosting models for a stated business, and recommend one with justification.
- Explain what is measured by each of the four resource figures on a hosting plan.
- A plan promises 99.9 per cent availability. Calculate the annual downtime and explain why the achieved figure may differ.
- Explain why encryption once required a dedicated address and why it no longer does.
- Describe two payment integration models and state the compliance consequence of each.
- Explain how a payment notification should be validated before an order is fulfilled.
- Identify four security controls and the failure each prevents.
- Explain why a firewall alone does not secure a web application.
- Explain why regular backups are necessary even when the host promises reliable hardware.
- Distinguish full, differential, and incremental backups by their reference points.
- A full backup is taken on Sunday and differentials nightly. List the sets required to recover Friday's state and justify the list.
- Explain how the answer to the previous question changes under an incremental schedule.
- Define recovery point objective and recovery time objective, and state one design change that improves each.
- Describe a backup retention and storage policy that would survive ransomware.

## 4. Worked Implementation from the Notes

### 4.1 Task: a ten-mark trace from typed name to displayed page

### 4.2 Implementation: answer in ordered stages with the actor named at each stage

Step 1. State the client's first action. The browser's stub resolver checks its local cache and, on a miss, sends a query to a recursive resolver. **(1 mark: the query is sent to a recursive resolver, not directly to the root.)**

Step 2. State the first referral. The recursive resolver asks a root server, which returns a referral naming the servers for the top-level domain rather than the answer itself. **(2 marks: referral, and the fact that the root does not answer the question.)**

Step 3. State the second referral. The resolver asks a top-level domain server, which returns a referral naming the authoritative servers recorded in the delegation for the domain. **(2 marks: the delegation is the source of the referral, and the delegation lives at the parent.)**

Step 4. State the authoritative answer. The resolver asks an authoritative server, which returns the address record with the authoritative flag set and a time to live. **(1 mark: the authoritative flag or the equivalent statement.)**

Step 5. State the connection and the handshake. The browser opens a connection to the address on the encrypted port and performs a handshake in which the client sends the requested name and the server returns a certificate for that name. **(2 marks: the port or the protocol, and the certificate selection by name.)**

Step 6. State the request, the application, and the response. The browser sends the request, the server passes it to the application, the application queries the database, and the response returns along the same connection. **(2 marks: the application and the database are both named as stages.)**

A complete answer reads as a sequence with no gaps, and the marker can tick each stage independently. The commonest loss is at step 2, where candidates write that the root server returns the address, which collapses three stages into one and forfeits the referral marks.

### 4.3 Task: a twelve-mark hosting recommendation

### 4.4 Implementation: compare on four dimensions, then decide and cost the decision

Step 1. Restate the requirement from the scenario. A retailer with steady traffic, card payments, a growing product database, and no in-house system administrator. **(1 mark: the constraint that there is no administrator is extracted from the scenario.)**

Step 2. Compare isolation. Shared hosting isolates by account inside one kernel; a virtual private server isolates by hypervisor; a dedicated machine isolates by hardware. **(3 marks: one per boundary, correctly named.)**

Step 3. Compare administrative responsibility. Shared hosting includes operating system, web server, and database maintenance; a virtual private server moves patching, firewall, and certificate renewal to the customer; a dedicated machine adds firmware and hardware monitoring. **(3 marks: one per responsibility set.)**

Step 4. Compare cost and predictability. Shared is cheapest and least predictable because neighbours compete for processor and memory; virtual is moderate with reserved resources but shared disk and network; dedicated is expensive with no neighbour effect. **(3 marks: cost direction and predictability for each model.)**

Step 5. Recommend and justify. A managed virtual private server is the minimum that satisfies card-payment isolation while respecting the absence of an administrator, because the hypervisor boundary separates the shop from other customers and the managed service supplies the patching that the shop cannot. **(1 mark: a recommendation tied to both constraints.)**

Step 6. State the residual cost. The monthly cost is higher than shared hosting and includes a management fee; the benefit is a boundary that a shared account cannot provide. **(1 mark: an explicit trade-off statement.)**

### 4.5 Task: a fifteen-mark backup and recovery design

### 4.6 Implementation: derive the schedule from the objectives, then prove the restore order

Step 1. Restate the objectives. A recovery point objective of fifteen minutes and a recovery time objective of two hours for an order database. **(2 marks: both objectives identified as data-loss and downtime tolerances respectively.)**

Step 2. Derive the base schedule. A nightly full backup alone leaves up to twenty-four hours of loss, so it cannot meet the objective; the base is a weekly full plus nightly differentials, with continuous archiving of the transaction log to cover the interval between sets. **(3 marks: the mismatch stated, the weekly full, the log archiving.)**

Step 3. State the policy in a reviewable form, because an answer that states the schedule as prose is harder to mark and easier to get wrong.

```yaml
backup_policy:
  scope:
    files: /var/www/shop
    database: shop
    configuration: /etc/nginx
  schedule:
    full: "Sunday 02:00"
    differential: "Monday-Saturday 02:00"
    transaction_log: continuous
  retention:
    daily: 14
    weekly: 8
    monthly: 12
  objectives:
    rpo_minutes: 15
    rto_minutes: 120
  storage:
    primary: local volume
    offsite: object storage, different region
    immutable_days: 30
  verification:
    checksum: sha256
    restore_test: quarterly
```

**(3 marks: frequency, retention, and off-site immutability each present.)**

Step 4. Derive the recovery point for a stated failure. Data is lost at Friday 17:40, and the last differential completed at Friday 02:00. The recovery point is Friday 02:00 from the set, plus the transaction log replay to 17:39, which satisfies the fifteen-minute objective because at most the last minute is lost. **(3 marks: the set time, the log replay, the objective satisfied.)**

Step 5. List the sets and the order explicitly.

```text
Restore sequence for recovery point 2026-11-06 17:39

1. Stop application writes; put the site into maintenance mode.
2. Restore the Sunday full: files archive, then database dump.
3. Apply the Friday 02:00 differential over the restored full.
4. Replay the archived transaction log from 02:00 to 17:39.
5. Verify: row counts, last order timestamp, checksum of the manifest.
6. Return traffic to the restored instance; reconcile later transactions.
```

**(2 marks: the full before the differential, and the log replay between the differential and verification.)**

Step 6. Show the counter-case that examiners use to test understanding. Under an incremental schedule, the sets would be Sunday's full plus Monday, Tuesday, Wednesday, Thursday, and Friday, applied strictly in that order, and a missing Thursday set would make Friday's set unusable. **(2 marks: the full chain, and the consequence of a missing set.)**

### 4.7 Task: a ten-mark e-commerce prerequisite answer

### 4.8 Implementation: answer each prerequisite with its mechanism and its nuance

Step 1. State the encryption requirement and the configuration that implements it. A certificate matching the requested name, a complete chain, a redirect from the plain scheme, and a strict transport header.

```nginx
server {
    listen 443 ssl;
    server_name shop.example.com;
    ssl_certificate     /etc/letsencrypt/live/shop.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/shop.example.com/privkey.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;
    add_header Strict-Transport-Security "max-age=31536000" always;
}
```

**(2 marks: the certificate matches the name, and the chain is complete.)**

Step 2. Address the address question with both halves. Server name indication carries the requested name in the handshake, so several certificates can share one address and a dedicated address is not strictly required; it is still requested because legacy clients may omit the name and because some payment providers require a fixed address. **(3 marks: the extension named, the modern conclusion, the two practical reasons.)**

Step 3. State the payment integration and its compliance consequence. A hosted payment page keeps card data off the merchant's server and places the merchant in the lightest self-assessment category, while a server-to-server interface passes card data through the merchant's server and requires the heaviest obligations including segmentation. **(2 marks: the model, and the scope consequence.)**

Step 4. State the validation of the notification. The signature is computed over the raw request body with the shared secret, compared in constant time, and the amount and currency are compared with the stored order before the status changes. **(2 marks: signature over raw bytes, and amount comparison.)**

Step 5. State the database requirement. Transactions must be atomic across the order and payment records, the account must be least-privilege, and the update must be guarded by a status predicate so that a duplicate notification cannot pay an order twice. **(1 mark: the transaction boundary or the idempotent update.)**

### 4.9 Task: an eight-mark evaluation of security controls

### 4.10 Implementation: pair each control with a failure, then state the residual risk

Step 1. Name the asset and the threat. The asset is the customer table; the threat is offline reversal of stolen password hashes. Control: a salted, slow hash such as Argon2id, because a fast digest allows billions of guesses per second. **(2 marks: salt, and slow algorithm.)**

Step 2. Name the second control and its failure. Key-only shell access with a named administrative account prevents automated guessing from succeeding, and removing password authentication removes the entire class of attack rather than reducing its rate. **(2 marks: key-only, and the class of attack removed.)**

Step 3. Name the third control and its failure. A default-deny inbound filter with permits only for the web ports prevents the database port from being reachable, and binding the database to the loopback address makes the protection independent of the filter. **(2 marks: default deny, and defence in depth.)**

Step 4. State the residual risk. A valid stolen session is unaffected by all three controls, so monitoring of anomalous administrative actions and a tested restore remain necessary. **(1 mark: an explicit residual risk.)**

Step 5. State the cost. Key distribution, a second factor for every administrator, and a quarterly restore rehearsal each consume staff time, which is the trade for the reduction in probability. **(1 mark: a cost stated as a trade.)**
## 5. Testing, Interpretation, and Common Errors

### 5.1 The trap table

Each row is a statement that looks correct in an exam answer and is not. The last column is what the marker does.

| Trap | Why it is wrong | Say this instead | Marks at risk |
|---|---|---|---|
| "The registrar stores the website's address." | The registrar stores the delegation; the address lives in the zone at the DNS provider | "The registrar records the responsible nameservers; the zone holds the address record" | 2 |
| "DNS changes propagate across the Internet." | Records are cached for a time to live; nothing is pushed | "Cached answers expire after their time to live, which can be lowered in advance" | 1 to 2 |
| "The root server returns the site's address." | The root returns a referral to the top-level domain | "The root returns a referral; the authoritative server returns the address" | 2 |
| "A registered name resolves immediately." | Resolution requires delegation and a populated zone | "The name resolves only after the delegation exists and the zone holds the records" | 2 |
| "A locked domain cannot be used by visitors." | Transfer prohibition affects movement, not resolution | "A hold removes the name from the zone; a transfer lock does not affect visitors" | 1 to 2 |
| "Shared hosting is secure because each customer has a login." | A login is a permission boundary inside one kernel | "The isolation boundary is a user account, not a kernel, so a shared component is reachable" | 3 |
| "A virtual private server is a physically separate machine." | It is a guest on a shared physical host | "Isolation is provided by a hypervisor; disk and network are still shared" | 2 |
| "Colocation means renting a dedicated server." | The customer owns the hardware and rents the facility | "The customer supplies the machine; the provider supplies power, cooling, and connectivity" | 2 |
| "99.99 per cent uptime means about nine hours a year." | That is the figure for 99.9 per cent | "99.99 per cent is about fifty-three minutes a year; 99.9 per cent is about eight hours forty-six" | 2 |
| "Uptime guarantees the site is available." | It guarantees the machine, excluding maintenance | "Server availability is not site availability; certificates and deployments can fail independently" | 2 |
| "Every encrypted site needs its own address." | The statement predates server name indication | "A dedicated address is not strictly required for modern clients but is still requested for legacy clients and some gateways" | 3 |
| "A padlock proves the site is trustworthy." | It proves encryption and a matching certificate | "It proves the connection is encrypted and the certificate matches the name, not that the site is secure" | 2 |
| "The gateway's success callback can be trusted as received." | A callback is untrusted input until its signature verifies | "Verify the signature over the raw body and compare the amount with the stored order" | 3 |
| "A firewall secures the application." | It filters addresses and ports, not request content | "It reduces the exposed surface; injection arrives on an allowed port and needs input handling and a web application filter" | 2 |
| "Hashing a password with a fast digest is sufficient." | Fast digests allow billions of guesses per second | "Use a salted, deliberately slow hash such as Argon2id or bcrypt" | 2 |
| "A differential backup contains only yesterday's changes." | It contains everything since the last full | "It is measured against the last full, so it grows until the next full" | 3 |
| "An incremental backup can be restored with the full and the latest set." | Every incremental in the chain is required | "Restore the full, then every incremental in order" | 3 |
| "A full backup is unnecessary if incrementals run hourly." | Incrementals are deltas from a base | "Without a periodic full there is no base, and the chain lengthens until the restore breaches the objective" | 2 |
| "A replica counts as a backup." | It reproduces deletion and encryption | "A replica protects against hardware failure only; a backup must be independent and retained" | 2 |
| "The backup job exited successfully, so the backup is usable." | Exit status proves the commands ran | "Only a checksum check and a test restore prove usability" | 2 |
| "Recovery point and recovery time are the same objective." | One bounds data loss, the other bounds downtime | "RPO bounds lost data in time; RTO bounds outage duration" | 2 |
| "A shorter RTO is achieved by taking more frequent backups." | Frequency improves the recovery point, not the recovery time | "RTO is improved by a faster restore path such as a warm standby" | 2 |
| "Encrypting the backup is enough protection." | The key may be stolen with the backup | "Hold the key separately, and keep one copy immutable or offline" | 2 |

### 5.2 Revision checklist

Work through the list and mark each item only when you can produce the answer aloud without notes.

1. Name the four parties in a registration and state what each controls.
2. State the three links of the delegation chain in order, and what each returns.
3. Explain the difference between the parent-side delegation and the child-side zone.
4. Explain what a glue record is and why it exists.
5. State what the start of authority record contains and why the serial number matters.
6. Explain why a CNAME cannot coexist with other records at the same name.
7. Explain what the authoritative flag in a response proves.
8. Distinguish a name that does not exist from a server failure in terms of the chain.
9. List three registration statuses and the visitor effect of each.
10. State the complete registration workflow in at least eight ordered steps.
11. Explain why a nameserver change takes longer to settle than a record change.
12. Name the four hosting models and the isolation boundary of each.
13. State two advantages and two disadvantages of shared hosting for a shop.
14. Explain why a virtual private server increases administrative responsibility.
15. Convert 99.9 per cent and 99.99 per cent into annual downtime.
16. Explain the difference between a capped transfer allowance and percentile billing.
17. Explain why memory often matters more than processor count for a database workload.
18. State the four prerequisites of a commerce host and the mechanism behind each.
19. Explain server name indication and state both halves of the dedicated address answer.
20. Name three payment integration models and the compliance consequence of each.
21. Describe how a payment notification is validated before an order is fulfilled.
22. State the properties a transactional database must provide.
23. Name four security controls and the specific failure each prevents.
24. Distinguish authentication from authorisation and give the status code for each failure.
25. Explain why a default-deny posture is preferred to a list of blocked ports.
26. Explain why a replica is not a backup.
27. Define full, differential, and incremental by their reference points.
28. State the sets required to restore each type, in order.
29. Given a weekly full and nightly differentials, list the sets for a stated recovery time.
30. Restate the previous answer for an incremental schedule and explain the difference.
31. Define recovery point objective and recovery time objective, and give one mechanism for each.
32. State the rule of three copies on two media with one off-site, and explain immutability.
33. Explain why the backup key must be stored separately from the backup.
34. Describe how a restore is tested and what a checksum does and does not prove.

### 5.3 Time strategy for the examination

The single largest source of lost marks in this topic is not ignorance but allocation: candidates spend too long on the first question, write a beautiful answer to a six-mark question, and then rush a fifteen-mark design question that carries the difference between grades.

A workable plan for a paper with four questions in three hours is as follows. Spend the first five minutes reading every question and writing the mark tariff beside each, because the tariff tells you how many distinct points are expected. Allocate writing time in proportion to marks, at roughly one and a quarter minutes per mark, which gives ninety minutes of writing for a seventy-two-mark paper and leaves room for planning and checking.

For each question, spend about one eighth of its allocated time planning in the margin. The plan should be a list of headings, not sentences: for a process question, the six moves; for a comparison, the dimensions; for a design question, the requirement, the mechanism, the numbers, and the trade-off. A plan of six headings takes ninety seconds and prevents the commonest structural failure, which is answering three points at length and omitting three that were worth a mark each.

Write the answer in short paragraphs, one point per paragraph, with the term first and the consequence second. This shape is easy to mark and easy to extend if time remains. If a question asks for a calculation, show the derivation on one line and the result on the next, because a bare number earns the answer mark and loses the method mark.

Reserve the final ten minutes for checking three things. First, that every part of every question has been answered, since a question with two parts often carries marks for the second part that are lost silently. Second, that no answer uses an absolute where the question wanted a comparison. Third, that every ordered list is actually ordered, because a restore sequence with the right sets in the wrong order reads as a careless answer and often is marked as one.

If time runs short, write the remaining points as a list rather than as prose. A list of four correct control-to-failure pairs earns four marks; an unfinished paragraph earns one.

### 5.4 Interpreting question wording

Three phrasings cause predictable errors.

"With reference to the scenario" means the marks are for applying the concept to the stated business, not for describing the concept. A shared-hosting answer that never mentions the shop's card payments has answered a different question.

"Justify your choice" means the choice must be defended against the alternative. Naming the chosen model earns little; saying why the next cheaper model is insufficient earns the marks.

"Explain the effect on" means a consequence is required. A description of the mechanism alone is a partial answer; the consequence for the visitor, the operator, or the recovery time is the second half.

Two smaller habits help. When a question gives a number, use it: if the scenario says 40,000 visits and 1.5 MB pages, the answer should contain the resulting transfer figure. When a question names a technology, use the name in the answer, because the mark scheme is indexed by term.

### 5.5 Final self-test

Answer these five without notes, in the time shown, and mark them against the trap table.

In eight minutes: describe how a newly registered name becomes reachable, naming every party and every record involved.

In six minutes: a business runs a small brochure site with no card payments and no administrator. Recommend a hosting model and justify the recommendation against the next cheaper option.

In eight minutes: a shop takes a full backup on Sunday and differentials nightly. State the sets and the order required to recover Friday's state, then restate the answer for an incremental schedule.

In six minutes: explain why a dedicated address is not strictly required for encryption, and give two reasons it is still requested.

In seven minutes: name four security controls for a small commerce site and state, for each, the failure it prevents and the cost it imposes.

If any answer drifts into a list of features without a consequence, return to the templates in Section 3 and rewrite it with the term first and the consequence second. That single habit is worth more than any additional fact, because it converts knowledge that the marker cannot see into marks that the marker can award.


