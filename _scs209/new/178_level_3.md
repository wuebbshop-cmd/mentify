## 1. Concept and Use Case

### 1.1 What the examiner is actually testing

This topic looks like a vocabulary list to a student who has memorised element names, and looks like a set of habits to a student who has built pages. Examiners reward the second reading. Almost no question in this topic asks you to recite a tag; almost every question asks you to state what a piece of markup means, or to predict what a browser will produce from it.

Four skills are being tested, and the mark schemes follow them closely.

The first is **definitional precision**. You must be able to say what HTML is, in a sentence that distinguishes it from a programming language, and to say what a tag, an element and an attribute are without confusing the three. These definitions appear at the start of long questions and carry the first marks.

The second is **structural reasoning**. You must be able to read a fragment of markup and say what tree it produces, and to write a fragment that produces a required tree. Most of the lost marks in this topic come from nesting errors, not from missing facts.

The third is **operational knowledge**. You must be able to say what happens when a page is loaded: which element becomes the tab caption, which declaration selects the rendering mode, which attribute is read by a screen reader, and how a relative address is resolved.

The fourth is **judgement about consequences**. Questions increasingly ask why a practice matters, and the answer is always a consequence: a missing declaration produces a compatibility mode, a missing description excludes a reader, a relative address ties a document to its location.

### 1.2 The definition that earns the first marks

A full-mark definition has three parts, and examiners give roughly one mark for each.

**HTML is the standard markup language for creating documents on the World Wide Web.** The words "standard" and "markup" both do work: standard means published and interoperable, and markup means the notation annotates content instead of computing with it.

**It describes the structure of a document using elements denoted by tags**, so that a heading is identified as a heading and a list as a list, independently of how either is presented.

**Browsers parse the markup into a tree and render that tree**, which is why the structure, rather than the visual arrangement, is what other technologies read.

A one-line version that scores in a short-answer slot is: HTML is the standard markup language used to describe the structure and content of documents on the World Wide Web, by enclosing content in elements denoted by tags; it is not a programming language, and it does not describe presentation.

Three additions commonly earn a further mark when the question invites them. HTML descends from the Standard Generalized Markup Language, abbreviated SGML, and was originally defined as an application of it. Modern HTML5 is specified independently and does not require an SGML parser. And HTML describes the document, while Cascading Style Sheets, abbreviated CSS, describe its presentation.

### 1.3 Why this topic recurs in every paper

HTML appears at the base of every later topic in web development, so examiners use it as a reliable discriminator. Anybody can produce a page that displays; far fewer candidates can say why a page displays the way it does.

The topic also supports questions at every cognitive level your syllabus is likely to use. Recall questions ask for the six heading levels. Comprehension questions ask what a fragment link does. Application questions give a file layout and ask where a relative address resolves. Analysis questions give broken markup and ask what tree results. Evaluation questions ask whether a practice is appropriate in a stated context, which is where alternative text and heading ranks are examined.

The consequence for revision is that breadth of recall is not enough. You need to be able to move in both directions: from markup to tree, and from a required tree to markup.

### 1.4 The question shapes you will meet

| Question shape | Typical wording | Usual marks | What earns them |
| --- | --- | --- | --- |
| Define | Define HTML and state two features of a markup language | 3 to 4 | The three-part definition, then two features |
| Describe the skeleton | Describe the structure of a valid HTML document | 6 to 8 | One mark per element, in order, with its purpose |
| Explain a distinction | Distinguish a tag from an element and from an attribute | 4 to 5 | Three definitions plus one example of each |
| Apply syntax | Write markup that produces a stated structure | 5 to 8 | Correct nesting, quoted values, void elements closed |
| Trace resolution | Given a base address, state where each link points | 4 to 6 | One mark per resolved address, with the rule |
| Justify accessibility | Explain why the alt attribute is required | 4 to 5 | The consequence for a reader, plus the decorative case |
| Compare | Compare absolute and relative addressing | 5 to 6 | A paired difference and a stated trade-off |
| Diagnose | A page displays incorrectly; identify the cause | 4 to 6 | A named cause and a stated correction |

Two habits convert these shapes into marks. Answer in the order the question lists, since mark schemes are usually written in that order and a marker scanning for a point will not search your whole answer. And always add the consequence to the definition, because "it is required" earns less than "it is required because a reader who cannot see the image must still receive its information".

### 1.5 Terminology that must be used exactly

Examiners award marks for the named term, so an answer that describes the right idea with the wrong word often scores nothing.

A **tag** is the lexical unit in angle brackets. An **element** is the start tag, content and end tag together. An **attribute** is a name and value inside a start tag, and its value is an **attribute value**.

A **void element** is an element with no content and no end tag. A **self-closing** element is the name used for the Extensible HyperText Markup Language, abbreviated XHTML, form in which a trailing solidus closes the tag.

A **root element** is the single topmost element. A **parent**, **child** and **sibling** describe tree relationships. A **content model** is the specification of what an element may contain.

An **absolute** address names a scheme and a host. A **relative** address is resolved against the base address of the document. A **root-relative** address begins with a slash and is resolved against the host root. A **fragment** begins with a hash mark and identifies a location inside a document.

**Metadata** is information about the document rather than content of it. **Alternative text** is the text replacement for an image. **Quirks mode** is the compatibility rendering mode selected by a missing or obsolete declaration.

## 2. Data, Syntax, and Core Concepts

### 2.1 Tag syntax: the facts with their mark values

An element consists of a start tag, content and an end tag. One mark is usually available for each of the three parts being identified correctly.

The start tag contains the tag name and every attribute. The end tag contains a solidus and the tag name, and it may not contain attributes; a candidate who writes an end tag carrying an attribute has demonstrated a misunderstanding worth more than a mark.

An attribute has a name, an equals sign and a value in quotation marks. Attribute names must be unique within an element, since a duplicate is discarded. Boolean attributes take no value.

Names are written in lowercase in conforming documents even though HTML compares them case-insensitively. Attribute values are quoted, and they are case-sensitive in ordinary cases such as an address.

Five syntax rules are examined repeatedly:

1. Elements must be properly nested, so the inner element closes before the outer one.
2. Every non-void element needs both tags, even when the browser could infer the end tag.
3. Void elements have no end tag at all.
4. Attribute values are enclosed in matching quotation marks.
5. The three syntactic characters are written with character references: an ampersand, a less-than sign and a quotation mark.

A common four-mark question asks for the difference between a tag, an element and an attribute. The full-mark answer defines all three and gives one example where all three occur in a single line.

```html
<a href="guide.html" title="The guide">Read the guide</a>
```

That line is one anchor element, consisting of a start tag carrying two attributes, the content text, and an end tag.

### 2.2 The skeleton: the highest-yield sequence in the topic

The document skeleton is the single most examined item in this topic, because it can be asked at any mark value from four to ten and because the order is fixed.

| Order | Item | Purpose | Mark |
| --- | --- | --- | --- |
| 1 | Document type declaration | Selects standards mode; states that the document is HTML5 | One |
| 2 | Root element with a language attribute | Encloses the whole document; states its language | One |
| 3 | Head element | Holds metadata, not rendered content | One |
| 4 | Title element | Names the document in the tab, bookmarks and results | One |
| 5 | Meta elements | Declare encoding, viewport and description | One to two |
| 6 | Link element | Attaches an external style sheet | One |
| 7 | Body element | Holds everything the reader sees | One |

Two supporting facts earn marks on their own. There is exactly one root element, exactly one head and exactly one body in a conforming document. And the declaration is not a tag: it is a declaration, it begins with an exclamation mark, and it has no closing counterpart.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Notes on Keeping a Cat</title>
  </head>
  <body>
    <h1>Notes on Keeping a Cat</h1>
    <p>One household, one cat, and a number of surprised mice.</p>
  </body>
</html>
```

Three marks are frequently lost here. Candidates write the declaration after the root element, which is an error of order. Candidates place content in the head, which is an error of purpose. Candidates give the document two bodies, or no head, which is an error of count.

### 2.3 Metadata: four configurations, four purposes

Each configuration answers a distinct question, and a mark scheme usually allocates one mark per configuration plus one per purpose.

| Configuration | Markup | Question it answers |
| --- | --- | --- |
| Encoding | `meta` element with the charset attribute set to utf-8 | How do these bytes map onto characters? |
| Viewport | `meta` element with name viewport and content width=device-width, initial-scale=1 | How wide is the layout on this device? |
| Description | `meta` element with name description and the summary in content | What should be quoted beneath the title in results? |
| Style sheet | `link` element with rel stylesheet and an href | Which file supplies presentation? |

Two facts carry extra marks. The encoding declaration must appear within the first 1024 bytes of the file, because the parser may begin interpreting text before it reaches the declaration. And the description is never displayed on the page; a candidate who writes that it appears on the page has confused metadata with content.

A trap worth pre-empting: the keyword metadata element is not part of the modern requirement and is ignored by major search engines. If a question asks for three metadata configurations, the description, the encoding and the viewport are the safe answers.

### 2.4 Headings and paragraphs

Six heading levels exist. The first is the most important, and each following level is subordinate. A page has one first-level heading, and levels are not skipped.

The mark-earning statements are these. Headings form an outline, not a set of font sizes. A heading must be chosen by rank, and its size should be adjusted with a style sheet. Consecutive headings must not skip a level, because the accessibility layer reports the outline and a gap is reported as a fault. And heading elements are block-level, so each occupies its own line.

A paragraph is a block-level element whose content model admits phrasing content only, which is the reason a block element cannot legally be nested inside it. Paragraphs are separated by vertical margins supplied by the default style sheet, not by line breaks in the source, and all runs of whitespace in the source collapse to a single space.

One high-value point: a parser closes an open paragraph when a block-level element begins. So the markup that appears to put a box inside a paragraph produces a paragraph, then the box, then a new paragraph. Candidates who can state that repair rule are answering at analysis level.

### 2.5 Void elements

A void element has no content and therefore no end tag. The standard lists them: `area`, `base`, `br`, `col`, `hr`, `img`, `input`, `link`, `meta`, `track` and `wbr`. For an examination answer, naming the four that occur in this topic is normally sufficient: `br`, `hr`, `img` and `meta`.

The two structural ones are the ones most often examined.

The line-break element inserts a break in the flow of text without starting a new paragraph. It is correct inside an address, a poem or a couplet of quoted code, and incorrect as a spacing device between paragraphs.

The thematic break element marks a change of subject. The default style sheet draws it as a horizontal rule, but its meaning is a shift in topic, not decoration.

The decisive statement for marks is this. HTML5 treats both as void elements, so they carry no closing tag and must not be given one; the XHTML form with a trailing solidus before the closing bracket is tolerated by the parser but is unnecessary in HTML5.

Two marks are commonly available for the reason rather than the rule. An element that has no content cannot have a closing tag, because a closing tag delimits content; a line break or a thematic break inserts something into the flow rather than enclosing anything.

### 2.6 Links, addresses and resolution

The anchor element creates a hyperlink, wraps the clickable content, and carries the destination in the `href` attribute.

An absolute address names the scheme and the host and therefore works from any document. A relative address omits both and is resolved against the base address of the document that contains it. A root-relative address begins with a single slash and is resolved against the host root. A network-path reference begins with two slashes and inherits the scheme while replacing the host.

Resolution is the highest-yield calculation in this topic, and it is not arithmetic. Take a document at `https://www.example.com/docs/guide/page.html`, so that the base directory is `https://www.example.com/docs/guide/`. Then:

| Reference | Resolved | Principle |
| --- | --- | --- |
| `photo.jpg` | `https://www.example.com/docs/guide/photo.jpg` | Replace the final path segment |
| `../photo.jpg` | `https://www.example.com/docs/photo.jpg` | Remove one segment per double dot |
| `/photo.jpg` | `https://www.example.com/photo.jpg` | Restart at the host root |
| `//cdn.example.net/photo.jpg` | `https://cdn.example.net/photo.jpg` | Inherit the scheme, replace the host |
| `#section` | `https://www.example.com/docs/guide/page.html#section` | Keep the path, replace the fragment |
| `?page=2` | `https://www.example.com/docs/guide/page.html?page=2` | Keep the path, replace the query |

Three supporting facts are worth a mark each. The fragment is never sent to the server; the browser strips it before the request and applies it after the response. The fragment must match the identifier of an element in the target document, so the target needs an `id`. And the link text is both the clickable area and the name announced by assistive technology, which is why a page full of links named "click here" fails an accessibility check.

### 2.7 Images and alternative text

The image element is void and requires the `src` attribute and the `alt` attribute in conforming markup.

The `src` attribute gives the address and obeys the same resolution rules as a link. The `width` and `height` attributes give the intrinsic size in CSS pixels as plain numbers, and their function is to let the browser reserve space and derive the aspect ratio, so that the page does not shift while images load.

The `alt` attribute is the examination favourite, and the full-mark explanation has three parts: what it is, who reads it, and what happens without it. It is a text replacement for the image. It is read by screen readers and displayed when the image cannot load. Without it, a reader who cannot see the image receives either nothing or the file name, and the information the image carried is lost.

The empty value is the part weaker answers omit. When an image is decorative, the correct value is an empty pair of quotation marks, which tells assistive technology to skip the image. Omitting the attribute is not the same as leaving it empty: the first is an error, and the second is a deliberate statement that the image has no informational content.

Good description practice earns a further mark: describe the information rather than the picture, do not begin with "image of", and do not repeat the caption verbatim.

### 2.8 Lists

An unordered list is declared with `ul` and represents a set whose order does not matter. An ordered list is declared with `ol` and represents a sequence whose order matters. Both contain list items declared with `li`, and a list may contain nothing but list items as direct children.

A list item may contain flow content, which is how nesting is achieved: the inner list goes inside the list item to which it belongs.

```html
<ul>
  <li>Food
    <ul>
      <li>Wet food</li>
      <li>Dry food</li>
    </ul>
  </li>
  <li>Toys</li>
</ul>
```

The attributes worth naming are the `start` attribute, the `reversed` attribute and the `type` attribute on an ordered list. The mark-earning point about nesting is a structural one: the inner list must be a child of a list item, because a list may contain only list items, and placing the inner list between two items makes it a sibling of the outer list with the same list type.

### 2.9 Block-level and inline

A block-level element occupies its own line and fills the available width; headings, paragraphs, lists, list items and thematic breaks are block-level. An inline element sits within a line and takes the width of its content; anchors, images, strong text and emphasis are inline.

Three statements earn marks. A block element may contain inline elements and other block elements where the content model permits; an inline element may not contain a block element. The image is an inline replaced element, so it affects the height of its line and leaves a small baseline gap beneath it. The `display` property can change the rendering without changing the meaning, which is why styling never substitutes for correct element choice.

### 2.10 Numbers and counts worth carrying into the exam

Small factual quantities are asked directly and are cheap marks.

| Quantity | Value | Context |
| --- | --- | --- |
| Heading levels | Six, from first to sixth | Outline depth |
| Elements in the skeleton | Three, namely root, head and body | Exactly one of each |
| Bodies per document | One | A second is non-conforming |
| Title elements per document | One | Names the document |
| Bytes before the encoding declaration | 1024 | Parser must meet it early |
| Void elements in the standard | Eleven | No end tag is permitted |
| Attribute quoting | Mandatory in conforming markup | Values in matching quotes |
| Default port for HTTP | 80 | Used when no port is written |
| Default port for HTTPS | 443 | Used when no port is written |
| Components of a URL | Scheme, host, port, path, query, fragment | Fragment is never sent |

## 3. Methods and Operations

### 3.1 The answer skeleton for a document-structure question

A six- to eight-mark question of the form "describe the structure of a valid HTML document" is answered by walking the skeleton in order and giving each element's purpose. Use this sequence without deviation.

1. State the document type declaration, that it comes first, and that its purpose is to select standards mode.
2. State the root element, that it encloses the whole document, and that it carries the language attribute.
3. State the head element and that it holds metadata rather than rendered content.
4. State the title element and its three uses: tab caption, bookmark name and search-result heading.
5. State the meta elements, naming encoding, viewport and description, with one purpose each.
6. State the link element and that it attaches a style sheet.
7. State the body element and that it holds all rendered content.
8. Close by stating that the document is a tree with one root, one head and one body, and that correct nesting is what makes the tree valid.

Eight sentences, eight marks, no padding. Add a short code sample only if the question invites one, and keep it minimal and valid.

### 3.2 The answer skeleton for a comparison question

Comparisons are marked in pairs, so each paragraph must contain both sides rather than describing one side and then the other.

1. Define both terms with the property that separates them.
2. State the difference in behaviour, in one sentence each.
3. Give a concrete example of each, with the actual text that would appear.
4. State the consequence or the trade-off.
5. Conclude with a judgement only if the question asks for one.

Applied to absolute and relative addressing, the five paragraphs are: an absolute address names the scheme and host while a relative address omits both; an absolute address resolves identically wherever it appears while a relative address depends on the location of the containing document; the examples are a full address and a bare file name; the trade-off is portability against fragility under relocation; and the judgement is that relative addressing suits internal links because it survives a change of host, and absolute addressing suits external links because it cannot be made stale by relocation.

### 3.3 The answer skeleton for a resolution question

1. Write the base address in full.
2. Strip the final segment to obtain the base directory, and write it down.
3. Handle the reference by its first characters: one slash means host root, two slashes mean a new host with the inherited scheme, otherwise apply double dots and append.
4. Write the resolved address in full, including the scheme.
5. Add one clause naming the rule applied, because the clause is often a separate mark.
6. If several references are given, keep the same order as the question, so the marker can find each answer immediately.

### 3.4 The answer skeleton for an accessibility or justification question

1. State the mechanism: which attribute or element supplies the information.
2. State who consumes it: which reader or tool, named.
3. State the consequence of its absence, described from the reader's point of view.
4. State the exception, which is always the decorative case for images and the single-page case for headings.
5. State one authoring rule that improves quality, such as describing the information rather than the picture.

Four or five sentences, each carrying one marking point, is the whole answer. Anything longer risks repeating a point already made.

### 3.5 Phrasing that earns marks and phrasing that loses them

Marks are awarded for named mechanisms and for stated consequences, not for enthusiasm.

Phrasing that earns marks names the element, the attribute and the effect: "the encoding is declared with a meta element whose charset attribute is utf-8, and it must appear within the first 1024 bytes so the parser meets it before interpreting text".

Phrasing that loses marks substitutes a vague verb for the mechanism: "the meta tag tells the browser the language", which names the wrong element, the wrong attribute and the wrong purpose in one sentence.

Three specific habits are worth adopting. Always write the element name as a name rather than pointing at it. Always give the consequence after the rule. Never describe appearance when the question asked for structure, because markers treat a description of colour as evidence that the candidate has confused markup with style.

### 3.6 Allocating effort to marks

Marks in this topic are distributed roughly as follows, and effort should follow the distribution.

Definitions and terminology take about a fifth of the available marks and require only accurate sentences, so they should never be lost.

The skeleton and its metadata take about a third, and they are entirely recall, so they should be reproduced perfectly.

Address resolution takes about a sixth, and it is a procedure that can be practised until it is mechanical.

Accessibility and structural nesting take the remainder, and they reward the habit of explaining consequences rather than restating rules.

The pattern is that almost nothing in this topic requires insight under time pressure. It requires accurate recall and disciplined structure, which is why this topic is one of the most reliable sources of marks in the paper.

## 4. Worked Implementation from the Notes

### 4.1 Task: model answer for a question on document structure

### 4.2 Implementation: an eight-mark description with one point per sentence

**Question.** Describe the structure of a valid HTML document and state the purpose of each part. (8 marks)

**Step 1. State the declaration.** The document begins with the document type declaration, written as an exclamation mark, the word DOCTYPE and the word html, whose purpose is to select the standards rendering mode rather than a compatibility mode. [1 mark]

**Step 2. State the root.** The root element encloses the entire document and carries a language attribute that identifies the language of the content for pronunciation and hyphenation. [1 mark]

**Step 3. State the head.** The head element contains metadata about the document rather than content for the reader, and there is exactly one in a valid document. [1 mark]

**Step 4. State the title.** The title element contains text only and names the document, and that name is used as the tab caption, the default bookmark name and the heading of a search result; a document without a title is invalid. [1 mark]

**Step 5. State the metadata.** The head holds meta elements that declare the character encoding, which must appear within the first 1024 bytes, the viewport configuration that makes a mobile browser use the device width, and the page description that search engines may quote. [2 marks]

**Step 6. State the style sheet link.** A link element with a rel value of stylesheet and an href attaches an external style sheet, which is how presentation is separated from structure. [1 mark]

**Step 7. State the body.** The body contains all rendered content, including headings, paragraphs, lists, links and images, and there is exactly one body in a valid document. [1 mark]

**Total: 8 marks.**

The markup that the answer describes, in compressed form, is this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Notes on Keeping a Cat</title>
  </head>
  <body>
    <h1>Notes on Keeping a Cat</h1>
  </body>
</html>
```

**Why this answer scores full marks.** Every sentence names an element and a purpose, the order matches the order in which a parser meets the elements, and the two facts that examiners look for specifically, namely the standards mode and the one-thousand-and-twenty-four-byte rule, are both present without being emphasised with extra words.

### 4.3 Task: model answer for a resolution question

### 4.4 Implementation: a six-mark trace with a rule beside each address

**Question.** A page is served from `https://www.example.com/docs/guide/page.html`. State the address to which each of the following references resolves, and name the rule that applies: `photo.jpg`, `../photo.jpg`, `/photo.jpg`, `#section`. (6 marks)

**Step 1. Establish the base directory.** The base address is the address of the containing document, so the base directory is `https://www.example.com/docs/guide/`, and the host root is `https://www.example.com/`. [1 mark]

**Step 2. Resolve the bare file name.** The reference `photo.jpg` resolves to `https://www.example.com/docs/guide/photo.jpg`, because a reference with no leading slash replaces the final path segment of the base directory. [1 mark]

**Step 3. Apply the double dot.** The reference `../photo.jpg` resolves to `https://www.example.com/docs/photo.jpg`, because each double dot removes one path segment from the base directory before the remainder is appended. [1 mark]

**Step 4. Apply the leading slash.** The reference `/photo.jpg` resolves to `https://www.example.com/photo.jpg`, because a single leading slash restarts resolution at the host root and discards the base path entirely. [1 mark]

**Step 5. Apply the fragment.** The reference `#section` resolves to `https://www.example.com/docs/guide/page.html#section`, because a fragment replaces only the fragment component and leaves the path unchanged, and it is not sent to the server. [1 mark]

**Step 6. State the consequence.** Because the first two results depend on the location of the containing document, relocating that document changes where those links point while the third and fourth continue to resolve as before; this is the practical difference between relative and root-relative addressing. [1 mark]

**Total: 6 marks.**

The four references, written as they would appear in the page, are these:

```html
<nav>
  <a href="photo.jpg">Sibling file</a>
  <a href="../photo.jpg">Parent directory</a>
  <a href="/photo.jpg">Host root</a>
  <a href="#section">Fragment</a>
</nav>
```

**Why this answer scores full marks.** Each resolved address is written in full with its scheme, each is accompanied by the rule rather than only the result, and the closing sentence converts a list of answers into a stated consequence, which is what the final mark rewards.

### 4.5 Task: model answer for an accessibility question

### 4.6 Implementation: a five-mark justification with the exception stated

**Question.** Explain why the alt attribute is required on the image element, and state what value it should take when the image is decorative. (5 marks)

**Step 1. State the mechanism.** The alt attribute supplies a text replacement for the image, and it is a required attribute in conforming markup rather than an optional enhancement. [1 mark]

**Step 2. State the first consumer.** A screen reader reads the value in the position the image occupies, and the accessibility layer exposes it as the name of the image object, so a reader who cannot see the picture still receives its information. [1 mark]

**Step 3. State the second consumer.** A browser that cannot load the image displays the value in its place, which covers a slow connection, a blocked resource and a text-only browser. [1 mark]

**Step 4. State the consequence of absence.** Without the attribute the reader receives either nothing or the file name, so the information the image carried is lost and the page becomes unusable at that point; omitting the attribute is therefore a content failure rather than a cosmetic one. [1 mark]

**Step 5. State the exception.** When the image is purely decorative and the surrounding text already conveys everything, the correct value is an empty pair of quotation marks, which tells assistive technology to skip the image entirely; this is different from omitting the attribute, which is an error. [1 mark]

**Total: 5 marks.**

The three cases the answer distinguishes are written as follows, so that the empty value can be seen rather than merely described:

```html
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
<img src="images/divider.png" alt="" width="600" height="8">
<a href="/home"><img src="images/home.png" alt="Return to the home page" width="32" height="32"></a>
```

**Why this answer scores full marks.** It separates the mechanism from the two distinct consumers, it states the consequence from the reader's point of view rather than merely asserting a rule, and it makes the distinction that most candidates miss, namely that an empty value is a deliberate statement while a missing attribute is a fault.

### 4.7 Task: model answer for a void-element question

### 4.8 Implementation: a four-mark answer that gives the rule and the reason

**Question.** Explain why the br and hr elements have no closing tag, and state how they are written in HTML5. (4 marks)

**Step 1. Define the category.** Both are void elements, which are elements with no content, and a closing tag exists to delimit content, so an element with no content has nothing for a closing tag to delimit. [1 mark]

**Step 2. State what they do instead.** A line break inserts a break into the flow of text and a thematic break marks a change of subject, so each inserts a boundary rather than enclosing a range of content. [1 mark]

**Step 3. State the rule in HTML5.** HTML5 treats both as void, so they are written as a single tag with no closing tag, and giving them one is a conformance error that the parser ignores. [1 mark]

**Step 4. State the XHTML position.** The Extensible HyperText Markup Language required a trailing solidus before the closing bracket because it was an application of Extensible Markup Language, in which every tag must be closed; HTML5 tolerates that form but describes it as unnecessary. [1 mark]

**Total: 4 marks.**

The two elements, written in the form the answer describes, are these:

```html
<p>Lucky<br>4 Mouse Lane<br>Nairobi</p>
<hr>
<p>Six months later, the frog returned.</p>
```

**Why this answer scores full marks.** The reason comes before the rule, which is what the wording of the question asks for, and the answer distinguishes three positions that weaker answers blur into one: no closing tag in HTML, a trailing solidus in XHTML, and a tolerated but pointless solidus in HTML5.

### 4.9 Task: model answer for a nesting and outline question

### 4.10 Implementation: a six-mark answer with markup and the resulting tree

**Question.** Write markup for a list of two categories, the first of which contains two sub-items, and state the structure that results. (6 marks)

**Step 1. Open the outer list.** The outer container is an unordered list element, because the order of the categories carries no meaning. [1 mark]

**Step 2. Write the first item and open the inner list inside it.** The first list item contains its text and then a complete inner unordered list, which is permitted because a list item accepts flow content. [2 marks]

**Step 3. Close the inner list before closing the outer item.** The inner list is complete before the outer list item closes, so the inner list is a child of that item rather than a sibling of the outer list. [1 mark]

**Step 4. Write the second item and close the outer list.** The second item contains only text, and the outer list closes after it. [1 mark]

**Step 5. State the resulting structure.** The tree is a list of two items, the first of which has a nested list of two items, and the accessibility layer therefore reports a sub-list at the point where it occurs. [1 mark]

The markup that earns those marks is:

```html
<ul>
  <li>Food
    <ul>
      <li>Wet food</li>
      <li>Dry food</li>
    </ul>
  </li>
  <li>Toys</li>
</ul>
```

**Total: 6 marks.**

**Why this answer scores full marks.** The markup is correctly nested, which is where most candidates lose two marks at once, and the answer closes by stating the resulting tree rather than only presenting the code, which is what the phrase "state the structure that results" asks for.

## 5. Testing, Interpretation, and Common Errors

### 5.1 The trap table

Every row below is a mistake that examiners report repeatedly, together with the correct statement that replaces it.

| The trap | Why it is wrong | The correct statement |
| --- | --- | --- |
| "HTML is a programming language" | It has no variables, decisions or arithmetic | It is a markup language that describes structure |
| "A tag and an element are the same" | A tag is punctuation; an element is the whole unit | An element is a start tag, its content and an end tag |
| "Every tag needs a closing tag" | Void elements have none, and adding one is an error | Void elements are written as a single tag |
| "The trailing slash is required" | It is an XHTML requirement, tolerated in HTML5 | It is unnecessary in HTML5 |
| "The doctype is a tag with a closing tag" | It is a declaration with no closing counterpart | It is a declaration that selects standards mode |
| "The title element is inside the body" | It is metadata and belongs in the head | It belongs in the head and names the document |
| "Metadata appears on the page" | Metadata is not rendered | It is consumed by the browser, search engines and previews |
| "The encoding declaration can go anywhere" | The parser may interpret text before reaching it | It must appear within the first 1024 bytes |
| "Heading numbers are font sizes" | They are ranks in an outline | Choose by rank, style by rule |
| "Several first-level headings are fine" | A document has one name | One first-level heading per document |
| "Skipping a heading level is harmless" | The outline reports a gap | Levels must be consecutive |
| "Line breaks are the way to space paragraphs" | They create meaningless structure | Use paragraph elements and style rules |
| "A relative address is resolved against the site root" | It is resolved against the containing document | Only a leading slash resolves against the host root |
| "The fragment is sent to the server" | The browser strips it before the request | It is used only after the response arrives |
| "A fragment can target any text" | Fragments match element identifiers | The target element needs an id |
| "Every image needs a description" | Decorative images should be skipped | The attribute is required; the value may be empty |
| "alt can be omitted if the image is decorative" | Omitting it is a conformance error | Write an empty value |
| "width and height are cosmetic" | They reserve space and give the aspect ratio | They prevent layout shift while loading |
| "A list may contain text directly" | Only list items are permitted children | Wrap the text in a list item |
| "An inline element can contain a block element" | The block needs its own line | Block elements contain inline, not the reverse |
| "Click here is good link text" | The text is the link's accessible name | Name the destination |

### 5.2 Ten self-test items with model answers

**One.** State the purpose of the document type declaration. It selects the standards rendering mode; without it a browser applies a compatibility mode that imitates very old behaviour and produces unexplained layout differences.

**Two.** Distinguish a start tag, an end tag and an element. A start tag is a name in angle brackets with optional attributes; an end tag is a solidus and the same name in angle brackets and carries no attributes; an element is the start tag, the content and the end tag together.

**Three.** Name four void elements and say why they are void. `br`, `hr`, `img` and `meta`; each inserts an object or marks a boundary and therefore has no content for a closing tag to delimit.

**Four.** State what must appear within the first 1024 bytes of a document and why. The character encoding declaration, because the parser may begin interpreting text before it reaches the declaration further into the file.

**Five.** A document at `https://example.com/a/b/page.html` contains the reference `../images/logo.png`. Where does it resolve? To `https://example.com/a/images/logo.png`, because one double dot removes the segment `b`.

**Six.** Explain the difference between a root-relative and an ordinary relative reference. A root-relative reference begins with a slash and is resolved against the host root, so it is independent of the depth of the containing document; an ordinary relative reference is resolved against the containing document's directory and therefore changes meaning if that document is moved.

**Seven.** Why does the image element need both width and height? So that the browser can reserve the correct space and derive the aspect ratio before the file arrives, which prevents the content below from moving as images load.

**Eight.** When is an empty alt value correct? When the image is purely decorative and the surrounding text already conveys its information; the empty value tells assistive technology to skip it, which is different from omitting the attribute.

**Nine.** Why must a nested list be placed inside a list item? Because a list may contain only list items as direct children; placed between items, the inner list becomes a sibling of the outer list and the intended depth is lost.

**Ten.** Give two reasons a page full of links named "click here" fails an accessibility check. The link text is the accessible name, so a list of identical names conveys no destinations; and the text is also the term a search engine associates with the destination, so the destination loses relevant description.

### 5.3 Revision checklist

Work through this list and tick only what you can state aloud without notes.

- Define HTML in three parts, and say why it is not a programming language.
- Define tag, element, attribute and attribute value, and label all four in one line of markup.
- State the eight items of the document skeleton in order, with the purpose of each.
- State the standards-mode purpose of the declaration and the symptom of its absence.
- Name the four metadata configurations and the question each answers.
- State the one-thousand-and-twenty-four-byte rule and its reason.
- State the viewport declaration exactly, including both directives.
- State the six heading levels, the one-first-level rule and the no-skipping rule.
- State why a block element cannot be inside a paragraph, and what the parser does about it.
- Name the void elements that occur in this topic and state the closing-tag rule for each.
- State the XHTML position on the trailing solidus and the HTML5 position.
- Resolve six reference forms against a stated base without hesitating.
- State whether the fragment is sent to the server, and what the target needs.
- State the three branches of the alternative-text decision, including the empty value.
- State the function of the width and height attributes.
- Write a correctly nested two-level list from memory.
- State two differences between block-level and inline rendering.

### 5.4 Time strategy in the examination

The topic is examined in short structured questions more often than in essays, so the strategy is about allocation rather than about writing style.

Read the whole question before writing anything, and count the marks against the parts, because a six-mark question with three named parts is three paragraphs of two marks each, not six unconnected facts.

Allow roughly one minute per mark for structured answers in this topic, which leaves a small margin for checking. A definition worth two marks does not deserve four minutes; an eight-mark skeleton description does.

Answer the parts in the order set. Mark schemes are written in that order, and a marker working down a list will credit a point where it is expected and may not search further.

Write one idea per sentence and number the sentences when the question says "state" or "describe", because numbered points are easier to credit and are never penalised when the answer is correct.

If a question provides markup and asks what results, draw the tree in the margin before writing. Two or three lines of indentation will reveal a nesting error that reading the markup five times will not.

If a question asks for markup, write it as a code block with correct indentation, quote every attribute value, and keep void elements closed by their nature rather than by a solidus. Examiners frequently award a presentation mark for markup that is legible and valid.

Leave the last few minutes for the traps in Section 5.1, checking your own answer for the five most expensive errors: a missing declaration, a second-level heading with no first-level parent, a void element given a closing tag, an unquoted attribute value, and a description of appearance where structure was asked for.

### 5.5 The final ten-minute check

Run this list against your script before the paper is collected. Each item is cheap and each has cost marks before.

First, confirm that every question has an answer and that no part has been left blank, since a blank part scores zero even when the rest is perfect.

Second, confirm that every answer that names an element names it precisely, because "the heading tag" in a paper that distinguishes six heading levels is a lost mark.

Third, confirm that each rule you stated is followed by a consequence, since the consequence is usually a separate marking point.

Fourth, confirm that no answer confuses structure with presentation, and delete any sentence about colour, size or font that crept into a structural answer.

Fifth, confirm that any markup you wrote is correctly nested and that no void element carries an end tag, because a single nesting error can cost two marks in a five-mark question.

Sixth, confirm that any addresses you resolved include their scheme in full, because an address without a scheme is not the address the question asked for.

The final point is the one worth remembering above all others. This topic rewards the student who has decided what each element means, because every question is a question about meaning. A student who has memorised shapes without meanings will recognise every element on the paper and still lose half the marks.
