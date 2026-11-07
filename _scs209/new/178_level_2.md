## 1. Concept and Use Case

### 1.1 The problem a markup language solves

A web browser and a web server are separate programs, usually on separate machines, often written by different organisations, and frequently several versions apart. The server must transmit a document to the browser in a form the browser can interpret without knowing anything about how the document was produced. That requirement rules out sending the authoring application's internal format, because the browser would have to implement every authoring tool that has ever existed. It also rules out sending only the visible characters, because a stream of characters carries no information about which part is a heading, which part is a list, and which part is a quotation.

The solution is a shared, public, declarative notation in which the author states the structure of the document and nothing else. HyperText Markup Language, abbreviated HTML, is that notation. It is transmitted as the body of a Hypertext Transfer Protocol response, where Hypertext Transfer Protocol is abbreviated HTTP, and it is parsed by the browser into an internal tree that every subsequent technology in the browser reads.

Three properties of the design deserve to be stated explicitly, because each one explains a rule that appears later in this note.

The first is that HTML is **declarative**. The author declares what a piece of content is; the browser decides how to present it. There is no instruction anywhere in HTML that says "draw this at forty pixels", and the sizing that does occur, such as the width attribute of an image, is a hint about the resource rather than a drawing command.

The second is that HTML is **tolerant**. A conforming parser is required to accept malformed input and to produce a tree anyway, using a repair algorithm that is specified in complete detail so that every browser repairs the same input in the same way. This is why a page written carelessly still displays, and it is also why careless markup is dangerous: the repair is well defined but it is not the structure the author had in mind.

The third is that HTML is **semantic rather than visual**. Every element name answers the question "what is this?", not "how should this look?". A heading element is a heading because it ranks in the document outline, not because it is large. Appearance is the responsibility of Cascading Style Sheets, abbreviated CSS, which select elements by the names and attributes that HTML provides.

### 1.2 A precise definition

HTML is the standard markup language for creating documents on the World Wide Web, abbreviated WWW. It consists of a fixed vocabulary of element names and a fixed syntax for writing them, and it describes the structure of a document: its headings, paragraphs, lists, links, images and metadata.

Four parts of that definition carry weight in an examination answer.

**Standard** means that the vocabulary and the syntax are published by a standards body rather than invented by a vendor. The consequence is interoperability: a document written once is rendered by every conforming browser.

**Markup language** means that the notation annotates content rather than computing with it. There is no assignment, no branching and no iteration. A markup language describes a document; a programming language manipulates values.

**Structure** is the operative word. HTML does not describe the visual arrangement of a page. A document that renders as three columns on a desktop and one column on a phone has exactly the same HTML; only the style sheet differs.

**Document** is the fourth word, and it is the one most often skipped. The unit that HTML describes is a document, which may be rendered on a screen, printed, spoken aloud, or indexed by a machine. The visual page is one rendering of the document, not the document itself.

### 1.3 Where the syntax came from

The syntax of HTML descends from the Standard Generalized Markup Language, abbreviated SGML, which is published as ISO 8879. SGML is not a language but a system for defining document types: it supplies a notation for declaring which elements exist, which may contain which, and which attributes each may carry. An HTML document was originally defined as an application of SGML, that is, as a document type declared in SGML and parsed by an SGML parser.

That ancestry explains several features that would otherwise look arbitrary. Angle brackets around names, attributes written inside the opening tag, and the convention of paired start and end tags are all SGML conventions. So is the idea of a document type declaration at the top of the file, which originally named the declaration that governed the document.

Modern HTML is no longer defined as an SGML application. HTML5 is specified by the Web Hypertext Application Technology Working Group, abbreviated WHATWG, as a living standard with its own complete parsing algorithm, and it does not require an SGML parser. The syntax survives the change of definition, which is why the older description remains useful for understanding why the notation looks as it does.

A related historical branch is Extensible HyperText Markup Language, abbreviated XHTML, which reformulated HTML as an application of Extensible Markup Language, abbreviated XML. XHTML required every element to be closed, every attribute value to be quoted, all names to be lowercase, and every void element to carry a trailing solidus. Those stricter habits are still good practice, and they explain why older tutorials show image and line-break tags with a slash before the closing bracket. In HTML5 that slash is permitted on void elements but has no effect.

### 1.4 Document, page, site and application

Four words are used loosely in conversation and precisely in specification, and the distinctions prevent a great deal of muddled thinking.

A **document** is a single HTML file, together with the resources it references. A **page** is a document as presented to a reader at one moment, which is why the same document can look different in two browsers, or on two screen sizes. A **site** is a collection of documents that share an origin, meaning the same scheme, host and port, and usually share navigation and styling. A **web application** is a site whose documents are generated or modified by scripts in response to input, so that a single document may present many different states.

This topic is about the document. Everything else is built on it.

### 1.5 Who consumes the structure

The reason the structure must be right, rather than merely plausible, is that several independent consumers read it, and each reads a different aspect.

The **rendering engine** parses the markup into a tree, applies the default style sheet of the browser, applies the author's style sheets, computes a layout, and paints the result. It needs the tree because CSS selectors and layout both operate on tree relationships.

The **accessibility layer** exposes the same tree in a simplified form, called the accessibility tree, to screen readers and other assistive technology. It reports roles such as heading level two, list with five items, link, and image with a given description. A page whose visual appearance is convincing but whose tree is meaningless is a page that cannot be operated without sight.

The **search index** extracts the outline, the title, the description and the link graph. It uses heading rank to judge importance and anchor text to judge what the destination is about.

The **reader** navigating by keyboard, by heading, or by link list is consuming structure directly rather than visually.

Each consumer is a reason for a specific rule in this note: the tree for nesting and content models, the accessibility tree for headings and alternative text, the index for titles and descriptions, and the keyboard reader for link text.

### 1.6 Scope of this topic

This note covers the syntax of tags and attributes, the skeleton of a document, the metadata that configures a document, the structural text elements, the void elements, the anchor element and address resolution, the image element and its accessibility requirements, and the two list types. It does not cover tables, forms, embedded frames, scripting, or style sheets, except where a rule of this topic depends on them.

## 2. Data, Syntax, and Core Concepts

### 2.1 The exact anatomy of a tag

A tag is a lexical unit: a tag name enclosed in angle brackets. A tag is either a start tag or an end tag. The start tag is an opening angle bracket, the tag name, zero or more attributes each preceded by whitespace, optional whitespace, and a closing angle bracket. The end tag is an opening angle bracket, a solidus, the tag name, optional whitespace, and a closing angle bracket. An end tag may not carry attributes.

An element consists of a start tag, its content, and an end tag. The element's name is the tag name. Some elements have no content and no end tag; those are treated in Section 2.10.

Take one line and label every part of it:

```html
<a href="guide.html" title="Open the guide">Read the guide</a>
```

| Part | Text in the example | Rule that applies |
| --- | --- | --- |
| Start tag | the opening bracket through the closing bracket | Contains the name and every attribute |
| Tag name | the letter a | Lowercase by convention, case-insensitive in HTML |
| Attribute name | href | Followed by an equals sign and a value |
| Attribute value | guide.html | Delimited by matching quotation marks |
| Second attribute | title, with its value | Attributes are separated by whitespace |
| Content | Read the guide | The text between the tags |
| End tag | the slash, the name, the bracket | Carries no attributes |

Whitespace rules are worth stating because they surprise beginners. Whitespace between attributes is required, since without it the names run together. Whitespace before the closing bracket is allowed. Newlines inside a tag are allowed and are treated as ordinary whitespace, which is why long tags are often wrapped across several lines. Whitespace between the start tag and its content is part of the content.

### 2.2 Serialization rules that must be obeyed

The syntax of HTML is defined by a set of rules, and a document that breaks them is not conforming even if browsers display it. The rules that matter for this topic are the following.

**Names are written in lowercase.** HTML treats tag and attribute names case-insensitively, so the browser accepts capitals. The standard nonetheless requires lowercase in conforming documents, and downstream tools, style sheets and scripts match on the name as written, which makes consistent case a practical requirement rather than a matter of taste.

**Attribute values are quoted.** The standard permits unquoted values when the value contains no space, no quotation mark, no backtick, no equals sign, and no angle bracket. That exception should not be used, because a single space silently ends the value and the remainder becomes a stray attribute.

**Attributes may not repeat.** If the same attribute name appears twice on one element, the second occurrence is discarded and the document is flagged as an error. This rule matters most with `class`, which is often duplicated by accident when markup is edited by hand.

**Attribute order carries no meaning.** Writing `src` before `alt` or after it produces identical behaviour. Consistency of order is a readability convention only.

**Certain attributes are boolean.** A boolean attribute's presence means true and its absence means false, and it takes no value at all. Writing `disabled="disabled"` is tolerated, and writing `disabled="false"` is a mistake, because the attribute is present and therefore true.

**Character references replace the three syntactic characters.** An ampersand introduces a reference; a less-than sign begins a tag; a quotation mark delimits an attribute value. Where these must appear as literal text, the references `&amp;`, `&lt;` and `&quot;` are used. The greater-than sign does not strictly need escaping but should be escaped for symmetry.

**Entities are resolved during parsing, exactly once.** Writing `&amp;lt;` produces the text `&lt;`, not a less-than sign, because the first ampersand is consumed in the single pass.

**Comments are delimited** by an opening sequence of an angle bracket, an exclamation mark and two hyphens, and the matching closing sequence of two hyphens and a closing angle bracket. A comment may not contain the string of two hyphens in the middle, and comments are visible to anyone who views the source.

### 2.3 Nesting, content models and the tree

Nesting is the whole of structure. Every element except the root has exactly one parent, and its children are the elements it directly contains. The specification defines, for each element, a **content model**: which elements may be its children, in what order, and whether text is allowed directly inside it.

Some content models are strict. A list may contain only list items. A table row may contain only cell elements. A list item must be a child of a list. Other content models are permissive: the body element accepts essentially any flow content, which means any block-level element or inline content.

The practical consequence of a content model is that a violation is not merely untidy; it changes the tree. Consider an attempt to put a paragraph directly inside a list: the list opens, one list item contains the word Food, and then a paragraph is written before the list is closed. The paragraph is not a permitted child of a list. The parser's repair is to close the list before the paragraph, so the resulting tree contains a list with one item followed by a paragraph that is a sibling of the list, not a child of it. The page looks approximately as the author intended, which is exactly why the error survives unnoticed, while a screen reader announces a list of one item followed by unrelated prose.

The same mechanism explains a well-known behaviour of paragraph elements. A paragraph has no permitted block-level children, so when a block-level element such as a heading or a list begins while a paragraph is still open, the parser closes the paragraph first. An author who opens a paragraph, writes a sentence, opens a block container inside it, and then writes another sentence before closing the paragraph does not get one paragraph containing a box. The paragraph is closed at the point the box opens, the box follows, and the trailing sentence becomes a second paragraph. The repair is correct per the specification and surprising per the author's expectation.

Nothing in the standard requires an author to rely on these repairs. Start and end tags for the root, the head and the body are formally optional and are inferred by the parser, and the end tags of list items and paragraphs may be omitted in specific circumstances, but writing every tag explicitly removes an entire class of reasoning from the page and makes the structure readable by a person.

### 2.4 The document tree

Parsing produces a **tree**, and the tree is the structure that every consumer uses. The root of the tree is a document node that is not itself an element. Its single element child is the root element, and the root element has two element children, the head and the body.

```text
Document
  html
    head
      meta (charset)
      title
        text: Lucky the Cat
      meta (viewport)
      link (stylesheet)
    body
      h1
        text: Lucky the Cat
      p
        text: She sleeps on the warmest chair.
```

Every element in the tree contains nodes, and the nodes are of a small number of kinds: element nodes, text nodes, comment nodes, and attribute nodes attached to their element. The indentation in the listing represents depth, and depth is what the terms describe.

The vocabulary of the tree is used constantly in web development and appears directly in examination questions. The **root** is the topmost element. A **parent** is the element that directly contains another. A **child** is an element directly contained. **Siblings** share a parent. **Ancestors** are the parents, the parents' parents, and so on. **Descendants** are children, their children, and so on. A **leaf** is a node with no children, which in practice is a text node or a void element.

Two consequences follow immediately from the tree shape.

First, a fragment identifier can only reach an element, because identifiers live on elements, and a text node cannot carry one.

Second, a style rule written against a descendant selector depends on ancestry rather than on document order. Two elements that appear adjacent in the source may sit at completely different depths, and the tree is what the style engine sees.

### 2.5 The DOM is not the source file

The **Document Object Model**, abbreviated DOM, is the programming interface through which scripts read and modify the parsed tree. It is a data structure produced by parsing, not a copy of the file. Three differences between the file and the DOM are worth knowing.

The DOM contains only what the parser produced. If the source omitted a closing tag and the parser supplied one, the DOM contains the supplied element and no record that the tag was absent. If the source contained an unclosed paragraph, the DOM shows a paragraph that was closed at a point the author never wrote.

The DOM normalises attribute values and resolves character references. An attribute written with a reference such as `&amp;` appears in the DOM as a literal ampersand.

The DOM is mutable in a way the file is not. A script may add, remove or reorder nodes, and the rendered page follows the DOM. The file on the server is unchanged. This is why "view source" and the element inspector can disagree: the first shows the bytes received, and the second shows the current tree.

For this topic the distinction has one practical use. Reading the inspector is the fastest way to discover what structure you actually produced, as opposed to what you intended to produce. Section 4 demonstrates it.

### 2.6 The document type declaration and rendering modes

The first line of a conforming document is the document type declaration:

```html
<!DOCTYPE html>
```

Its effect is to select the **standards mode** of the rendering engine. Browsers support at least three modes. Standards mode follows the specifications. Quirks mode reproduces the inconsistent behaviour of browsers from before the specifications were widely followed, including a different box-sizing model in some cases and different handling of table cell heights. Limited-quirks mode is an intermediate compatibility mode.

The mode is chosen by matching the declaration against a table in the specification. A document with no declaration at all is rendered in quirks mode. A document with an obsolete declaration that points at a transitional document type definition may be rendered in limited-quirks mode. Only the short declaration above selects full standards mode in every browser.

Because the difference is invisible in the source, a missing declaration produces symptoms that look like style-sheet bugs: a container is a few pixels wider than its stated width, or an image gains an unexpected gap beneath it. The correct diagnostic order for such a symptom is to check the first line before editing any rule.

### 2.7 The skeleton, element by element

The root element is written with its start and end tags, opening with `<html lang="en">` and ending with the matching closing tag after every other element has closed, and it carries the `lang` attribute.
The `lang` attribute takes a language tag such as `en`, `en-GB` or `sw`. It allows the rendering engine to choose hyphenation and fonts, and it lets a screen reader choose the correct pronunciation dictionary. The content model of the root is exactly one head followed by exactly one body.

The **head** element contains metadata. Its permitted children include the title, meta, link, style, script and base elements. It contains no content that is rendered in the page area.

The **title** element contains text only, and exactly one is required. Its text is used as the window or tab caption, as the default name of a bookmark, as the heading of a search result, and as the name a screen reader announces when the page loads or when the reader switches between tabs. A document with no title is a validation error, and a document whose title is the same on every page is an accessibility failure that is easy to avoid.

The **body** element contains the rendered content. Exactly one body is permitted. It accepts flow content, meaning block-level elements, and it may also contain inline content and bare text.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lucky the Cat</title>
  </head>
  <body>
    <h1>Lucky the Cat</h1>
    <p>She sleeps on the warmest chair in the house.</p>
  </body>
</html>
```

### 2.8 Metadata configuration

Metadata is declared with elements in the head. Each of the four configurations below is examined separately because each answers a different question.

**Character encoding.** The declaration is written as a meta element with the `charset` attribute:

```html
<meta charset="utf-8">
```

The encoding decides how the bytes of the file map onto characters. A document saved as UTF-8 and declared as anything else will display incorrect characters wherever a byte sequence is ambiguous, which is most visible with quotation marks, apostrophes, accented letters and non-Latin scripts. The declaration must appear within the first 1024 bytes of the file, because the parser may begin interpreting text before it reaches the declaration; that is why it belongs immediately after the opening head tag. Where the transport layer also declares a character set in the HTTP response header, the transport declaration takes precedence, and a mismatch between the two is a common cause of corrupted text on a server that was configured for an older encoding.

UTF-8, formally Unicode Transformation Format, 8-bit, encodes every character in the Unicode repertoire and is backward compatible with plain English text. It is the correct default.

**Viewport.** The declaration is:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without it a mobile browser lays the page out on a virtual screen roughly a thousand pixels wide and then scales the result down to the physical display, so that a desktop layout fits but text becomes unreadably small. The `width=device-width` directive makes the layout viewport equal the device width in CSS pixels, and `initial-scale=1` sets the initial zoom to one hundred per cent. Both are needed for a page whose style sheet contains responsive rules to behave as designed.

**Description.** The declaration is a meta element with a `name` of `description` and the summary in the `content` attribute:

```html
<meta name="description" content="A short record of one cat, her habits, and the animals she brings home.">
```

Search engines frequently use this text beneath the page title in results. It has no effect on rendering, and it should read as a sentence rather than as a keyword list.

**Linked style sheet.** The declaration is a link element:

```html
<link rel="stylesheet" href="css/style.css">
```

The `rel` attribute states the relationship, which is that the target is a style sheet for this document. The `href` attribute gives the address, resolved by exactly the rules in Section 2.11. A style sheet link in the head is render-blocking: the browser will not paint the page until the sheet has been fetched, which prevents a flash of unstyled content at the cost of a small delay.

Other metadata is worth recognising even though it is not required here. The `keywords` meta element is ignored by major search engines. The `robots` meta element advises crawlers. The `http-equiv` form of meta was used historically to declare the content type and to request a redirect, and the modern equivalents are the charset attribute and a server-side redirect respectively.

### 2.9 Headings, paragraphs and the outline

Six heading elements exist, numbered one to six. They rank in a hierarchy: the first is the most important and the sixth the least. The heading elements accept phrasing content, meaning text and inline elements, and they are block-level.

Correct practice is to treat the headings as the outline of the document. One first-level heading names the page. Second-level headings divide it into sections. Third-level headings divide those sections. No level is skipped, because a skipped level leaves a gap that the accessibility layer reports.

Paragraphs are the unit of prose. The paragraph element is block-level and accepts phrasing content only, which is the reason a block element cannot legally appear inside it. Browsers apply a vertical margin above and below by default, which produces the familiar separation between paragraphs.

The distinction between a heading and styled text is not cosmetic. A heading contributes a node with the role of heading and a level, which is what enables navigation by heading; a large bold paragraph contributes nothing. The same argument applies to a list, which reports its length and its type, and to a link, which reports its destination.

Browsers also add a small default margin to headings, which is the reason two consecutive headings appear with a gap. That margin is part of the default style sheet and may be overridden; the level, however, is part of the markup and cannot be faked.

### 2.10 Void elements

A void element is an element with no content and therefore no end tag. The standard lists them explicitly: `area`, `base`, `br`, `col`, `hr`, `img`, `input`, `link`, `meta`, `track` and `wbr`. Each either inserts an object into the flow or marks a boundary.

The two structural void elements are the line break and the thematic break.

The line-break element inserts a break in the flow of text without beginning a new paragraph. It accepts no content and has no attributes other than global ones. It is correct inside an address, a poem, or a line of code quotation, and it is incorrect as a device for spacing blocks of prose.

The thematic break element marks a shift in topic. It is rendered by the default style sheet as a horizontal rule, but its meaning is the change of subject. The `hr` element is not a decoration, and a page that uses it as a divider between layout regions is using it outside its purpose.

```html
<p>Lucky<br>4 Mouse Lane<br>Nairobi</p>
<hr>
<p>Six months later, the frog returned.</p>
```

The rule about closing tags is absolute in HTML5. A void element must not be given an end tag, and a document that contains one is not conforming; the parser treats the stray end tag as an error and ignores it. The XHTML-style trailing solidus, as in a line break written with a slash before the closing bracket, is permitted, because the standard's syntax rules allow a solidus on void elements, but it has no effect on the parse and is described as unnecessary. Both forms below are accepted; only the second is conventional in HTML5.

```html
<p>First line<br />
Second line</p>
```

```html
<p>First line<br>
Second line</p>
```

The distinction matters when converting between serialisations. In XHTML the solidus is mandatory, because XML has no concept of a void element and every tag must be closed. In HTML it is optional. A file that mixes conventions is not automatically wrong, but it signals an author who has not decided which standard applies.

### 2.11 The anchor element, addresses and resolution

The anchor element creates a hyperlink. It accepts phrasing content, and in HTML5 its content model is transparent, meaning it may also wrap block content when its parent allows block content. It carries the destination in the `href` attribute, which stands for hypertext reference.

An address used in `href` is a Uniform Resource Locator, abbreviated URL, which is a specialised Uniform Resource Identifier. The general shape is scheme, then a colon, then an authority, then a path, then an optional query, then an optional fragment.

```text
https://www.example.com:8443/docs/guide/page.html?section=intro#top
```

| Component | Value in the example | Meaning |
| --- | --- | --- |
| Scheme | https | The protocol used to retrieve the resource |
| Host | www.example.com | The server named in the address |
| Port | 8443 | The service on that server; omitted when it is the default |
| Path | /docs/guide/page.html | The location of the resource on the server |
| Query | section=intro | Parameters passed to the server |
| Fragment | top | A location inside the retrieved document |

Two facts about the fragment are frequently examined. The fragment is never sent to the server: the browser strips it before making the request and uses it after the response arrives. And the fragment is matched against the identifier of an element in the retrieved document, which is why the target element must carry an `id` attribute whose value equals the fragment text.

An **absolute** URL contains a scheme and a host, and therefore identifies a resource independently of where the reference appears:

```html
<a href="https://www.example.com/docs/guide/page.html">Guide</a>
```

A **relative** URL omits the scheme and the host, and is resolved against the address of the document that contains it, which is called the base URL. Resolution proceeds by a defined algorithm rather than by intuition, and the algorithm behaves differently depending on whether the relative reference begins with a slash.

Suppose every link below appears in a document whose own address is `https://www.example.com/docs/guide/page.html`. The base directory is therefore `https://www.example.com/docs/guide/`.

| Reference written in the page | Resolved address | Rule applied |
| --- | --- | --- |
| `photo.jpg` | `https://www.example.com/docs/guide/photo.jpg` | Replace the last path segment with the reference |
| `./photo.jpg` | `https://www.example.com/docs/guide/photo.jpg` | A single dot means the current directory |
| `../photo.jpg` | `https://www.example.com/docs/photo.jpg` | A double dot removes one path segment |
| `../../photo.jpg` | `https://www.example.com/photo.jpg` | Each double dot removes one further segment |
| `/photo.jpg` | `https://www.example.com/photo.jpg` | A leading slash restarts at the host root |
| `//cdn.example.net/photo.jpg` | `https://cdn.example.net/photo.jpg` | A network-path reference inherits the scheme |
| `?page=2` | `https://www.example.com/docs/guide/page.html?page=2` | Replace the query, keep the path |
| `#section` | `https://www.example.com/docs/guide/page.html#section` | Replace the fragment, keep everything else |
| `sub/page.html` | `https://www.example.com/docs/guide/sub/page.html` | Descend into a subdirectory |

Three consequences follow from the table, and each is a common source of broken links.

The first is that a relative reference is resolved against the page, not against the site. Two pages in different folders may contain the identical attribute value and resolve it to different addresses. A link that works on one page may therefore fail on another, which is why testing must be done from the page that contains the link.

The second is that a leading slash does not mean "the current folder"; it means "the root of the host". Root-relative references are stable across pages at different depths, and they break when the site is served from a subdirectory rather than from the host root, unless the application rewrites them or a base element is present.

The third is that the base URL may be changed by a `base` element in the head, which supplies its own `href`. When present, it becomes the base for every relative reference in the document. That is powerful and easy to misuse, since a single wrong base breaks every link at once.

Two further forms are worth naming. A `mailto:` reference opens the reader's mail program with a new message addressed to the given address, and a `tel:` reference begins a call on a device that can place calls. Both are ordinary anchors with an unusual scheme.

The `target` attribute controls where the destination opens. The value `_blank` opens a new browsing context, and modern browsers implicitly apply `rel="noopener"` to such links so that the new page cannot manipulate the opener. The `rel` attribute states the relationship, and values such as `nofollow` and `noopener` are recognised.

Link text deserves its own rule. The content between the anchor tags becomes both the clickable area and the name announced by assistive technology, and it is also the text a search engine associates with the destination. A page whose links are all named "click here" produces a list of identical names that conveys nothing when read out of context.

### 2.12 The image element and accessibility

The image element places a replaced element into the flow. It is void, it accepts no content, and it requires at least the `src` and `alt` attributes in conforming markup.

```html
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
```

The `src` attribute gives the address and obeys the same resolution rules as `href`. The `width` and `height` attributes give the intrinsic dimensions in CSS pixels, written without a unit; a value of `480` means four hundred and eighty pixels. Their practical function is now better than it once was. Because the browser knows both dimensions before the file arrives, it can reserve the correct space and, from the two numbers, derive the aspect ratio, so that the paragraph below does not move when the image loads. Removing them reintroduces the movement, which is measurably worse on a slow connection.

The `alt` attribute is the accessibility requirement, and the reasoning behind it is worth stating precisely, because the attribute is often treated as a formality.

An image carries information in a visual channel that a screen reader cannot use. The accessibility layer therefore exposes each image as an object with a role of image and a name taken from the alternative text. A sighted reader sees the picture. A reader who cannot see it receives whatever the attribute contains, in the position the picture occupies. If the attribute is absent, the screen reader may announce the file name, or may announce nothing at all, depending on the browser and the reader; both outcomes leave the listener without the information that the author intended to convey. If the attribute is present but empty, the accessibility layer is told explicitly that the image is decorative, and the image is skipped, which is the correct outcome for a spacer, a background flourish, or a picture whose content is already given in the adjacent text.

The decision procedure has three branches, and every image falls into one of them.

**Informative images** convey something not stated in the text. The alternative text describes the information, not the picture: "Lucky asleep across a wooden desk chair" rather than "a photograph". The words "image of" and "picture of" add nothing, because the role already announces that it is an image.

**Decorative images** convey nothing beyond appearance. The correct value is an empty string, written as a pair of quotation marks with nothing between them. Writing a file name or a generic word here is worse than writing nothing, because it makes the reader listen to noise.

**Functional images** act as controls or links, such as a button drawn as a picture. The alternative text names the action, in the same way that link text names the destination.

A fourth case, the image that is a complex chart or table rendered as a picture, requires a longer description placed in the surrounding text, with the attribute naming the short version. That case lies outside this topic but follows from the same reasoning.

Two further attributes are worth knowing. The `loading` attribute with the value `lazy` defers the fetch of an image until it approaches the visible area, which saves bandwidth on long pages. The `decoding` attribute offers a hint about whether decoding may be done asynchronously. Neither affects correctness, and neither is required.

### 2.13 Lists

Two list types are used in ordinary documents, and both share the same item element.

An **unordered list** is declared with the `ul` element and represents a set whose order carries no meaning. Its permitted children are list items and script-supporting elements only.

An **ordered list** is declared with the `ol` element and represents a sequence whose order carries meaning. Its permitted children are the same. The `start` attribute sets the first number, the `reversed` attribute counts downwards, and the `type` attribute selects a numbering style such as decimal or lower-case letters.

A **list item** is declared with the `li` element, and it is valid only as a child of a list. Its content model is flow content, which means an item may contain paragraphs, headings, images, links, and other lists.

```html
<ol start="3" type="a">
  <li>Third step, lettered c.</li>
  <li>Fourth step, lettered d.</li>
</ol>
```

Nesting is achieved by placing the inner list inside the list item to which it belongs:

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

The tree produced by that markup is a list with two items, the first of which has a nested list with two items of its own. The accessibility layer reports the depth, so a listener is told that they are inside a sub-list rather than being read a flat sequence. Placing the inner list between two items instead produces a repair in which the inner list becomes a sibling of the outer list, and the indentation that the author saw is lost.

A third list type, the description list, uses `dl`, `dt` and `dd` for pairs of term and definition. It is not required here, but it is the correct structure for a glossary and is frequently confused with an unordered list.

### 2.14 Block-level and inline rendering

The distinction between block-level and inline is a statement about how a box participates in layout, and it is the part of this topic most often learned by observation rather than by rule.

A **block-level** box participates in a block formatting context. It is placed on its own line, its width by default fills the available space of its containing block, and the next sibling begins below it. Vertical margins between adjacent block boxes may collapse, which is why the gap between two paragraphs can be smaller than the sum of their margins. Headings, paragraphs, lists, list items and thematic breaks are block-level.

An **inline** box participates in an inline formatting context. It is placed within a line, its width is determined by its content, and it breaks across lines when the line is full. Horizontal margins and padding apply, vertical margins do not affect line height. Anchors, images, strong text and emphasis are inline.

The image element is a special case that repays attention: it is inline by default but it is a **replaced** element, meaning its content comes from an external resource and its intrinsic dimensions come from that resource. That is why an inline image can set the height of the line it sits in, and why an image placed between two paragraphs appears to sit on a baseline with a small gap beneath it. The gap is not a margin; it is the space reserved for the descender of the line box.

Three practical rules follow.

First, a block-level element may contain inline elements, and it may contain other block-level elements where its content model permits. An inline element may not contain a block-level element, because the block would need its own line while the inline box is trying to remain inside a line. The transparent content model of the anchor is the notable modern exception: an anchor may wrap block content when its parent permits blocks.

Second, the initial value of the `display` property is determined by the element's role in the default style sheet, not by the element's name. A style sheet may set a paragraph to `display: inline` or an anchor to `display: block`, and the rendering changes while the accessibility role does not. This is why changing appearance with CSS never changes meaning.

Third, text that appears directly inside a block container alongside block children is wrapped by the browser in an anonymous block box, so that the inline content has somewhere to sit. That anonymous box is invisible in the source but visible in the layout, and it explains why a stray run of text between two paragraphs receives the vertical spacing of a paragraph.

### 2.15 The default style sheet

Browsers ship a default style sheet, sometimes called the user-agent style sheet, which gives every element its initial appearance. Its rules are what make an unlabelled page look like a document rather than like a wall of text.

| Element | Effect of the default style sheet |
| --- | --- |
| Heading, first level | Block display, bold weight, large font, vertical margins |
| Heading, sixth level | Block display, bold weight, small font, vertical margins |
| Paragraph | Block display, vertical margins of about one line |
| Unordered list | Block display, left padding, disc markers |
| Ordered list | Block display, left padding, decimal markers |
| List item | List-item display, marker generated outside the box |
| Anchor | Inline display, underlined, coloured, cursor changes on hover |
| Strong | Inline display, bold weight |
| Emphasis | Inline display, italic style |
| Image | Inline replaced element, intrinsic size from the file |
| Line break | Forces a line break in the inline formatting context |
| Thematic break | Block display, inset border producing a horizontal line |

Understanding that these appearances come from a style sheet rather than from the markup resolves a confusion that catches many students. A heading is not large because it is a heading; it is large because the default style sheet says so. The heading element supplies the meaning, and the size is one possible presentation of that meaning. A reader who increases the base font size sees everything scale, which is the behaviour a document should have and which a page built from faked headings does not have.

## 3. Methods and Operations

### 3.1 Constructing a conforming document

1. Create the file with the extension `.html` and save it as UTF-8.
2. Write the document type declaration on the first line.
3. Write the root element with a `lang` attribute.
4. Open the head and declare the encoding first, so the parser meets it within the first kilobyte.
5. Add exactly one title that names this document specifically.
6. Add the viewport declaration, the description, and any style sheet link.
7. Close the head, and open the body.
8. Add one first-level heading.
9. Add the sections, each beginning with a heading one level below its container.
10. Add paragraphs, lists, links and images where the content requires them, checking each element against its content model as it is written.
11. Close the body, then the root.
12. Validate, then read the page.

### 3.2 Resolving a relative reference by hand

1. Write down the absolute address of the document that contains the reference. This is the base.
2. Remove everything after the last slash of the base path. What remains is the base directory.
3. Look at the first character of the reference. If it is a slash, discard the base directory and start from the host.
4. If the reference begins with two slashes, keep the scheme of the base and replace everything from the host onwards.
5. Otherwise, apply each leading double dot by removing one segment from the base directory, and then append the remaining reference.
6. If the reference contains no path at all, keep the base path and replace only the query or the fragment.
7. Compare the result with the address you expect. A mismatch is either a wrong reference or a wrong assumption about where the document lives.

### 3.3 Deciding what an image's alternative text should say

1. Ask whether the image conveys information that is absent from the surrounding text.
2. If it does not, write an empty value and stop.
3. If it does and it is a control, name the action.
4. If it does and it is content, write one short sentence stating what a sighted reader learns from it.
5. Remove any phrase such as "image of", and remove any repetition of the caption.
6. Load the page with the image blocked and read the result. If the sentence is comprehensible in place, the description is adequate.

### 3.4 Building and checking a heading outline

1. Write the single sentence that names the document and mark it with the first heading level.
2. Write one heading at the next level for each major section, in reading order.
3. Write one heading at the level below that for each subsection.
4. Extract the headings alone, without the prose, and read them as a list.
5. If a heading at a deeper level appears before its parent level, raise it until the sequence is continuous.
6. If two headings at the same level overlap in meaning, demote one of them.
7. If a heading was written for its size rather than its rank, change the level and adjust the style sheet instead.

### 3.5 Inspecting what was actually produced

1. Open the page in a browser.
2. View the source to see the bytes that were received; this shows what the server sent, including any server-side rewriting.
3. Open the element inspector to see the parsed tree; this shows the structure the browser is using, including every repair it performed.
4. Expand the root element and compare the children with what was written. An element in an unexpected position is a content-model violation.
5. Open the accessibility panel of the inspector, which lists the roles and names as assistive technology sees them, and confirm that each heading reports the intended level, each list reports its length, and each image reports its description.
6. Run the file through the validator published by the World Wide Web Consortium, abbreviated W3C, and fix reported errors from the first line downwards, since one unclosed element produces a cascade of later complaints.

### 3.6 Recognising and replacing obsolete markup

Older documents contain elements that are no longer conforming and that this topic should displace.

| Obsolete practice | Why it fails | Correct replacement |
| --- | --- | --- |
| A font element to set type | Mixes appearance into structure | A style rule selecting the element |
| A centre element to align text | Appearance with no meaning | A style rule for text alignment |
| A background colour attribute on the body | Presentation in markup | A style rule on the body |
| Repeated line breaks for spacing | Meaningless structure | Paragraphs, and margins from a style sheet |
| An image with no alternative text | Inaccessible | A description, or an empty value if decorative |
| A heading chosen for its size | Breaks the outline | The correct rank, styled to the desired size |
| A table used to lay out a page | Destroys the meaning of cells | Block containers and a style sheet |
| A link with no href, used as a button | Not keyboard operable | A button element |

## 4. Worked Implementation from the Notes

### 4.1 Task: build a complete document with configured metadata and a semantic body

### 4.2 Implementation: write the skeleton, then add each layer in order

Step 1. Declare the document type and open the root with its language. The declaration selects standards mode, so every subsequent measurement follows the specification.

```html
<!DOCTYPE html>
<html lang="en">
</html>
```

Step 2. Add the head with the encoding declaration first. The encoding must be met early, before the parser interprets any text that depends on it.

```html
<head>
  <meta charset="utf-8">
</head>
```

Step 3. Add the title, the viewport declaration, the description and the style sheet link. Each answers a different question: the title names the document, the viewport governs layout width on a mobile device, the description is quoted by search engines, and the link attaches appearance.

```html
<head>
  <meta charset="utf-8">
  <title>Lucky the Cat: Habits and Hazards</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A short record of one cat, her habits, and the animals she brings home.">
  <link rel="stylesheet" href="css/style.css">
</head>
```

Step 4. Open the body and add the single first-level heading, then two second-level sections. At this point the outline already describes the document, before any prose exists.

```html
<body>
  <h1>Lucky the Cat</h1>
  <h2>Who she is</h2>
  <h2>What she does</h2>
</body>
```

Step 5. Add prose as paragraphs, one idea in each, with no line breaks used for spacing. The vertical gaps between them come from the default style sheet, not from the source layout.

```html
<h2>Who she is</h2>
<p>Lucky is a small grey cat with one white paw.</p>
<p>She has lived in this house for six years and has never used the bed that was bought for her.</p>
```

Step 6. Add an ordered list for a sequence and an unordered list for a set, and confirm the content model: each list contains list items and nothing else.

```html
<h2>What she does</h2>
<p>Her morning follows a fixed order.</p>
<ol>
  <li>Wake the household at five.</li>
  <li>Demand food, then refuse it.</li>
  <li>Patrol the hedge.</li>
</ol>
```

Step 7. Add the nested list inside the item it belongs to. The inner list closes before the outer item closes, so the tree keeps the sub-list as a child of its parent item.

```html
<ul>
  <li>Sleeping places
    <ul>
      <li>The warmest chair</li>
      <li>The one a person has just left</li>
    </ul>
  </li>
  <li>Toys</li>
</ul>
```

Step 8. Add the links: one relative, one root-relative, one absolute, and one fragment. The fragment requires an identifier on its target, so the second heading carries one.

```html
<p>See the <a href="feeding.html">feeding routine</a>, the <a href="/contact.html">contact page</a>, or the <a href="https://www.example.com/cats/">general guide</a>.</p>
<p><a href="#habits">Jump to habits</a></p>
<h2 id="habits">Habits</h2>
```

Step 9. Add the image with a description and dimensions. The description states what a sighted reader learns; the dimensions let the browser reserve space and derive the aspect ratio.

```html
<p>She is usually in the chair by this point in the day.</p>
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
```

Step 10. Assemble, then read the result. The tab shows the title, the outline runs first level then second level with no gap, the ordered list is numbered by the browser, the nested list is announced as a sub-list, the fragment scrolls to the habits heading, and the image reserves its space before the file arrives.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lucky the Cat: Habits and Hazards</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="A short record of one cat, her habits, and the animals she brings home.">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <h1>Lucky the Cat</h1>
    <h2>Who she is</h2>
    <p>Lucky is a small grey cat with one white paw.</p>
    <p><a href="#habits">Jump to habits</a></p>
    <h2 id="habits">Habits</h2>
    <ol>
      <li>Wake the household at five.</li>
      <li>Demand food, then refuse it.</li>
      <li>Patrol the hedge.</li>
    </ol>
    <ul>
      <li>Sleeping places
        <ul>
          <li>The warmest chair</li>
          <li>The one a person has just left</li>
        </ul>
      </li>
      <li>Toys</li>
    </ul>
    <img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
    <hr>
    <p>More at the <a href="https://www.example.com/cats/">general guide</a>.</p>
  </body>
</html>
```

### 4.3 Task: resolve a set of relative references against a known base

### 4.4 Implementation: apply the resolution rules and compare the results

Step 1. Establish the base. The document is served at `https://www.example.com/docs/guide/page.html`, so the base directory is `https://www.example.com/docs/guide/` and the host root is `https://www.example.com/`.

Step 2. Write the candidate references into the document exactly as they will appear, so that the browser performs the resolution rather than the author guessing.

```html
<nav>
  <a href="photo.jpg">Sibling file</a>
  <a href="../photo.jpg">Parent directory</a>
  <a href="/photo.jpg">Host root</a>
  <a href="//cdn.example.net/photo.jpg">Other host</a>
  <a href="#section">Fragment on this page</a>
</nav>
```

Step 3. Read the resolved address of each link from the browser. Hovering over a link shows the resolved target in the status area, and the inspector shows the property that holds the resolved absolute address.

```text
photo.jpg                    -> https://www.example.com/docs/guide/photo.jpg
../photo.jpg                 -> https://www.example.com/docs/photo.jpg
/photo.jpg                   -> https://www.example.com/photo.jpg
//cdn.example.net/photo.jpg  -> https://cdn.example.net/photo.jpg
#section                     -> https://www.example.com/docs/guide/page.html#section
```

Step 4. State why each result follows. The first keeps the base directory and replaces the final segment. The second removes one segment. The third discards the path entirely. The fourth keeps the scheme and replaces the authority, which is why it is called a network-path reference. The fifth keeps the path and replaces only the fragment.

Step 5. Move the same document one directory deeper, to `https://www.example.com/docs/guide/v2/page.html`, and re-read the results. The fragment, the root-relative and the network-path references resolve exactly as before, while the first two now resolve to different addresses. This is the proof that a relative reference is resolved against the page rather than the site, and it is why a link must be tested from the page that contains it.

### 4.5 Task: make three images accessible and observe the difference

### 4.6 Implementation: one informative image, one decorative image, one functional image

Step 1. Write the informative image with a description of the information.

```html
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
```

Step 2. Write the decorative image with an empty value, so that assistive technology skips it rather than announcing noise.

```html
<img src="images/divider.png" alt="" width="600" height="8">
```

Step 3. Write the functional image, which acts as a control, with a description of the action rather than of the picture.

```html
<a href="/home"><img src="images/home.png" alt="Return to the home page" width="32" height="32"></a>
```

Step 4. Open the accessibility panel of the inspector and read the reported names. The first image reports the sentence as its name. The second reports no name and is not exposed as an image at all. The third exposes a link whose name comes from the text of the picture, so the destination is announced correctly.

Step 5. Remove the attribute from the first image and reload. The reported name falls back to the file name or disappears, and the listener is left without the information that the picture carried. This is the concrete demonstration that the attribute is a content requirement and not a formality.

### 4.7 Task: show how the tree records a content-model violation

### 4.8 Implementation: build a valid list, then read what the parser does with a misplaced paragraph

Step 1. Write a list that obeys the content model, so that every direct child of the list is a list item.

```html
<ul>
  <li>Food</li>
  <li>Water is separate.</li>
  <li>Toys</li>
</ul>
```

Step 2. Inspect the parsed tree and confirm that it matches the source one level at a time. Each item is a child of the list, and each item owns its own text.

```text
ul
  li
    text: Food
  li
    text: Water is separate.
  li
    text: Toys
```

Step 3. Now move the middle sentence out of its list item so that it sits directly inside the list, before the third item. The content model forbids that placement, because a list may contain only list items.

Step 4. Inspect the tree again rather than the source. The parser closes the list before the paragraph, so the paragraph becomes a sibling of the list and the third item begins a second list.

```text
ul
  li
    text: Food
p
  text: Water is separate.
ul
  li
    text: Toys
```

Step 5. Interpret the repair. The rendered result looks approximately correct, which is why the error passes unnoticed, but the structure now reports two lists of one item each with a paragraph between them. A listener hears "list of one item, water is separate, list of one item".

Step 6. State the general principle: when a repair surprises you, the cause is always an element placed where its content model does not allow it, and the remedy is to move the element or to wrap it in a permitted container.

### 4.9 Task: repair a document that a validator rejects

### 4.10 Implementation: read the report, name each rule, then correct the markup in one pass

Step 1. Read the report. A document in which the image element had gained an end tag, the width had been written with a unit, and the width attribute had been typed twice produces three errors.

```text
Error: Stray end tag img.
Error: Bad value 480px for attribute width on element img: Expected a digit but saw px instead.
Error: Duplicate attribute width.
```

Step 2. Name the rule behind each message. The first is the void-element rule: an image has no content, so an end tag for it is always stray. The second is the dimension rule: width and height are plain numbers of CSS pixels, with no unit written. The third is the uniqueness rule: a second occurrence of an attribute name is discarded, so the value the author believed was applied may be the one that was not.

Step 3. Correct the markup in one pass, keeping one of each attribute, quoting every value, and leaving the void element without an end tag.

```html
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
```

Step 4. Re-run the validator. Fix from the top downwards, because an unclosed element near the top of a document produces a cascade of complaints further down, and clearing the first fault removes several later ones.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to test a document

Testing a document is not the same as looking at it. A page can look correct and be structurally wrong, and the reverse is also possible on an unfamiliar browser.

The first test is **validation**, which compares the document against the standard and reports every departure with a line number. It is mechanical, it takes seconds, and it catches content-model violations, unclosed elements, duplicate attributes, missing required attributes and obsolete elements.

The second test is **inspection of the parsed tree**, which reveals what the browser actually built rather than what the author believes was written. Every repair performed by the parser is visible as a difference between the source and the tree.

The third test is **navigation without a mouse**. Tab through the page and confirm that each link receives focus in a sensible order and that the focused element is visible. A page that cannot be operated by keyboard is inaccessible regardless of how it looks.

The fourth test is **reading without the images**. Block the images and read the page again. Every description should slot into the text as a sensible sentence, and every decorative image should leave no trace.

The fifth test is **the rendered outline**. Extract the headings and read them as a list. If they do not describe the document, the structure is wrong even if the appearance is pleasing.

### 5.2 Interpreting what the tools report

A validator error is not an opinion. Each message names a line, a column and a rule, and the rule is published. The common messages and their real meanings are worth knowing, because the wording can mislead.

A message about a "stray end tag" means an end tag appeared for an element that was not open, which is almost always the result of closing something twice or of closing a void element.

A message about "unexpected end of file" means an element was opened and never closed; the parser reached the end of the document while the element was still open, and the whole remainder of the document became its content.

A message about an element "not allowed as a child of" another means a content-model violation, and the practical remedy is to move the element or to wrap it in a permitted container.

A message about a "duplicate attribute" means the same name appears twice; the second value is discarded, so the fault may be invisible on screen.

An accessibility report adds a different layer. A heading that skips a level, a link with no name, an image with no description, and a page with no title are all reported as failures even though the document may be perfectly valid HTML. Validity and accessibility are separate tests, and passing one does not imply the other.

### 5.3 The error catalogue

| Symptom | Cause | Correction |
| --- | --- | --- |
| Layout differs slightly from other pages | No document type declaration, so quirks mode applies | Add the declaration as the first line |
| Text displays as odd symbols | Encoding of the file differs from the declared encoding | Save as UTF-8 and declare UTF-8 |
| Page is tiny on a phone | No viewport declaration | Add the viewport meta element |
| Paragraph and heading spacing collapse | Source line breaks were relied on for spacing | Use elements, and margins from a style sheet |
| A block element sits inside an inline element | Content model violation, silently repaired | Move the block out, or change the container |
| A list contains stray text | Text placed directly inside the list | Wrap the text in a list item |
| A sub-list appears at the wrong level | Inner list placed between items rather than inside one | Move the inner list inside its parent item |
| A fragment link does nothing | No element carries the matching identifier | Add the identifier to the target element |
| Two elements share an identifier | Identifiers must be unique | Rename one, and update any references |
| A relative link works locally but not when published | Resolved against a different base, or the site is served from a subdirectory | Use a root-relative reference, or correct the relative path |
| An image shifts the page as it loads | No width and height attributes | Add both, in pixels |
| A screen reader announces a file name | The alternative text is missing | Add a description, or an empty value if decorative |
| A screen reader reads a paragraph where a list was intended | Content-model violation changed the tree | Correct the nesting |
| The title on every page is the site name | The title was copied between pages | Give each document its own title |
| A link opens a new tab unexpectedly | A target attribute was copied with the markup | Remove it, or state the relationship |

### 5.4 Limits worth stating plainly

HTML does not control appearance. Two documents with identical markup may look entirely different, and that is the design, not a defect. The corollary is that a markup question is never answered by describing colours or fonts.

HTML is not a programming language. A page cannot compute, decide or repeat. Anything of that kind belongs to a script, and a script operates on the tree that HTML produced, which is why correct structure remains the prerequisite.

The parser is forgiving but the standard is not. A document can be rendered perfectly and still be non-conforming, and the difference matters when the page is read by a device the author did not test, or maintained by a person who relies on the structure being real.

Relative addresses are fragile in a specific way. Their correctness depends on the location of the page that contains them, so a reference that is correct in one file is wrong in another, and moving a file silently breaks every relative reference inside it. Absolute and root-relative references trade that fragility for a different one.

Accessibility cannot be added afterwards by a tool. An automated checker can find a missing description, but it cannot write one, and it cannot tell whether the description that exists is useful. The requirement has to be met when the content is authored.

### 5.5 The rules that summarise this topic

Three sentences carry most of the marks in this topic. A document is a tree of elements, each element having exactly one parent and a content model that says what it may contain. A tag is punctuation and an element is structure, so the start tag, the content and the end tag must be treated as one unit. Structure describes meaning and the style sheet describes appearance, so the choice of element is never a choice about how something should look.

Everything else follows. Void elements exist because some content is inserted rather than enclosed, so they have no end tag and the trailing solidus is a legacy convention. Relative addresses exist because a site is a tree of files and a page should not need to know where the site is mounted, so a reference is resolved against the page that contains it. Alternative text exists because an image occupies a position in a document and a reader who cannot see it must be given the same information in words.

A student who can state those three sentences and illustrate each with one piece of correct markup can answer almost any question set on this topic, and can extend the answer with the specific facts that the question rewards.
