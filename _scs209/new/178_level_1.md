## 1. Concept and Use Case

### 1.1 A parcel with a label stuck to the top

Imagine a parcel arriving at your door with a handwritten label stuck to the lid. The label says what is inside, who sent it, and where it belongs. The label does not change the contents of the box in any way. Its whole job is to describe the contents so that every person who handles the parcel knows what to do with it: put it in the fridge, stack it on a shelf, hand it to a named person, or leave it in the hall. A courier holding an unlabelled box is holding something real, but nobody can act on it correctly, and several handlers will each guess differently.

That is exactly the role of HyperText Markup Language in a web page. HyperText Markup Language is abbreviated HTML, and it is the labelling system that surrounds the words, pictures and links on a page. The words themselves are the content. The labels around the words say what each piece of content is: this run of text is a heading, this one is a paragraph, this one is a link to another page, this picture is a logo, and these items form a list. A browser that receives plain words with no labels can still show something, but it has to guess where one idea ends and the next begins. A browser that receives labelled words knows exactly what it is looking at, and it can present them properly, read them aloud to a blind user, or hand them to a search engine.

The rest of this note is about those labels: how they are written, which ones every page needs, and how they fit together. Everything is built from a small number of ideas, and none of them requires any mathematics.

### 1.2 Unpacking the four letters

The name itself explains the idea, so it is worth taking the four words apart slowly.

**HyperText** is text that is connected to other text. In an ordinary book a reference to chapter five forces you to turn pages yourself. In hypertext the reference is clickable: you press it and you are taken to the destination. The word "hyper" simply means beyond or above, and it describes the way one document can point at another so that the reader travels between them instead of reading in a straight line. The collection of documents joined this way is what we call the World Wide Web, abbreviated WWW, and it is a service that runs over the Internet rather than being the Internet itself.

**Markup** is the second word. To mark up a document is to add instructions to the text that describe its parts. Editors once wrote markings in the margin of a manuscript to tell the printer "this line is a heading" or "set this in bold". HTML does the same thing with typed instructions rather than pencil marks.

**Language** is the third word. HTML is a language in the sense of a defined set of words and rules for combining them, not in the sense of English or Kiswahili. It has a fixed vocabulary of names and a fixed way of writing them, and a page that follows the rules can be read by any browser on any operating system.

One point deserves emphasis immediately, because it causes confusion for years if it is left unclear. HTML is a markup language, not a programming language. It has no variables, no arithmetic, no decisions and no loops. It cannot calculate anything. It describes what a piece of content is, and the browser decides how to present it. Behaviour and calculation belong to a separate language, JavaScript, which is loaded into the page but is not HTML.

### 1.3 What mark-up actually does

Think of a shopping list written on a scrap of paper. The scrap contains only words: milk, bread, tomatoes. If you hand it to somebody, they can read it, but they have to work out for themselves that these are three separate items rather than one long sentence. Now imagine you draw a bullet in front of each word. Nothing about the words has changed. The content is identical. What changed is that the structure is now explicit: there are three items, and they sit at the same level in one list.

Markup does exactly this, but in a form a machine can read. Instead of a pencil bullet you write a short instruction before and after the content:

```html
<ul>
  <li>milk</li>
  <li>bread</li>
  <li>tomatoes</li>
</ul>
```

That is real, valid HTML. It says: here begins an unordered list, and it contains three list items. A browser receiving it draws bullets and lines the items up. A screen reader receiving it announces "list of three items" before reading them, so a blind listener knows what is coming. A search engine receiving it understands that these three words belong together. The words were always there; the markup gave them shape.

This is the single most useful habit to build early. When you write HTML, you are not decorating text. You are stating what each piece of text is. The decoration, meaning the colour, the font and the spacing, is a separate job done with a separate language called Cascading Style Sheets, abbreviated CSS. Keeping the two jobs apart is what makes a page easy to change later.

### 1.4 The smallest page that is genuinely complete

Every web page, however complicated it looks, has the same outer shape. Here is a complete page, small enough to read in one go:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lucky the Cat</title>
  </head>
  <body>
    <h1>Lucky the Cat</h1>
    <p>Lucky caught a mouse this morning.</p>
  </body>
</html>
```

Six things are happening here, and each one matters.

The first line, the one beginning with an exclamation mark, is a declaration that tells the browser which version of HTML to expect. The second line opens the document itself and states that its language is English. The third line opens a section that holds information about the page rather than content for the reader. Inside that section are two lines that name the character encoding and give the page a title, which is the name shown on the browser tab. The seventh line closes that section and opens the part the reader actually sees. Inside it there is a heading and a paragraph. The last line closes the document.

The point of showing this now is not to memorise it but to see that a page is a container inside a container inside a container. That idea, nesting, is the whole of HTML structure. Section 2 takes each line apart properly.

### 1.5 Why the structure is worth the effort

A beginner often asks why the labels are needed at all, since the same words could be typed into a document and saved with a different file extension. There are four good answers.

The first is **accessibility**. A screen reader is software that speaks a page aloud for someone who cannot see it. It cannot interpret a picture, and it cannot guess that a line of large text is a heading. It relies entirely on the labels. A properly marked-up page lets a blind user jump from heading to heading, hear "list of five items", and hear a spoken description of each image. A page that looks perfect but has no labels is close to unusable for them.

The second is **search**. A search engine reads the same labels to decide what a page is about and which words on it are important. A heading carries more weight than ordinary body text, and a good page description appears in the search result instead of a random sentence.

The third is **consistency**. If every heading on a site is marked as a heading, then changing every heading at once is one small edit in a style sheet. If headings were faked by making text large, every one of them would have to be changed by hand.

The fourth is **maintenance by other people**. A page written with clear labels can be read by a stranger, or by you in two years, without guessing what each part was supposed to be.

### 1.6 Where you already meet all of this

HTML is not an abstract topic. You meet it several times an hour.

The name on the browser tab is the title element. The address you click to move from one page to another is an anchor element. The text that appears in place of a picture when the picture fails to load is the alternative text attribute. The menu that collapses into a button on a phone is a consequence of the viewport declaration and a style sheet. The bulleted list of ingredients on a recipe page is an unordered list. When a page opens scrolled down to the section you clicked, the address in the bar has a fragment on the end, and the page contains an element whose identifier matches it.

None of these behaviours needs programming. They are all consequences of correct markup, which is why this topic rewards precision rather than cleverness.

## 2. Data, Syntax, and Core Concepts

### 2.1 The anatomy of a tag

An HTML tag is a special name enclosed in angle brackets, which are the characters that look like less-than and greater-than signs. The name inside the brackets is the element name, and it is written in lowercase by convention. The tag that begins a piece of content is the opening tag, for example the three characters for a paragraph opening. The tag that ends it is the closing tag, which is the same name with a forward slash in front of it. Between the two sits the content.

An **element** is the whole thing: opening tag, content and closing tag together. This distinction is worth holding onto, because examiners and colleagues use the words precisely. A tag is a piece of punctuation. An element is a complete unit of structure. So a paragraph element consists of a paragraph opening tag, the words of the paragraph, and a paragraph closing tag.

```html
<p>Lucky sleeps on the warmest chair in the house.</p>
```

Read that line as a sentence about grammar: the element is the sentence, the tags are the capital letter at the start and the full stop at the end, and the content is the words in between. Everything else in HTML is a variation on that pattern.

Elements nest. That means one element can sit entirely inside another, and the inner one must close before the outer one does. The following is correct, because the emphasis element both opens and closes inside the paragraph element:

```html
<p>Lucky is <strong>very</strong> fond of that chair.</p>
```

Written the wrong way round, the closing tag of the emphasis element ends up after the closing tag of the paragraph, so the emphasis appears to end outside the element that contains its text. Nothing is gained by typing it that way, and the browser has to decide what was meant.

Browsers are forgiving about such mistakes and will usually repair them, but the page no longer means what its author intended, and the repair is not guaranteed to match between browsers. Think of nesting as putting boxes inside boxes. A box that is inside another box cannot have its lid taped shut after the outer box has already been sealed.

### 2.2 Attributes, the extra information inside a tag

Most elements accept extra information written inside the opening tag. Each such piece is an **attribute**, and it has a name and a value joined by an equals sign. The value is written inside quotation marks. In modern HTML the quotation marks may in principle be left out when the value contains no spaces, but they should always be used, because a value with a space in it breaks without them and because unquoted values are a common source of quiet errors.

```html
<a href="https://www.example.com/">Visit the example site</a>
```

Here the element name is the anchor, the attribute name is `href`, and the attribute value is the address. The attribute sits inside the opening tag, never in the closing tag, and never between the tags. A useful way to remember the layout is that the opening tag is a small form with fields, and attributes are the field values.

A few attributes need no value at all; they are either present or absent. The most common example is `disabled` on a form control. Everything else follows the name and value pattern.

Three rules prevent almost every beginner error with attributes. First, the attribute name goes before the equals sign and the value after it, never the other way round. Second, the value goes in quotes, and the quotes must match. Third, an element may carry several attributes, separated from each other by spaces, in any order, but each name may appear only once.

```html
<img src="images/lucky.jpg" alt="Lucky asleep on a chair" width="320" height="240">
```

That single tag carries four attributes and no closing tag. Section 2.10 explains why it needs no closing tag.

### 2.3 The declaration that must come first

The very first line of a modern page is not a tag at all. It is the document type declaration, written as an exclamation mark, the word `DOCTYPE` in capitals, the word `html`, and nothing else:

```html
<!DOCTYPE html>
```

Its purpose is historical but its effect is practical. In the 1990s there were several versions of HTML, and browsers had to guess which one a page had been written for so that they could reproduce the older rendering behaviour for old pages. The guess was based on this declaration. Pages that declared a recognised version were rendered in standards mode; pages without one were rendered in quirks mode, which imitates the inconsistent behaviour of very old browsers. Modern HTML has a single declaration, and its only job is to put the browser into standards mode, where the rules you learn here are the rules that apply.

Leaving the declaration out is one of the most common causes of a page that "looks slightly wrong for no reason": boxes are a few pixels wider than expected, or spacing differs from another page. The page is not broken; it is being rendered by a compatibility mode that was designed for documents written before the rules were agreed.

Older documents used long, complicated declarations that pointed at a written specification. Those were necessary when there were several competing versions. Only one form is needed today, and it is the one shown above.

### 2.4 The document skeleton

A page is built from four elements that every document needs, and they always appear in the same order.

The **root element** is the one named `html`. It encloses everything else, which is why it is called the root: it is the trunk, and every other element is a branch on it. There is exactly one per document. It usually carries the `lang` attribute, which states the language of the content using a short code such as `en` for English or `sw` for Kiswahili. That attribute costs nothing and helps screen readers pronounce the text with the right voice.

Inside the root there are exactly two children. The first is the **head element**, which holds information about the document. The second is the **body element**, which holds everything the reader sees. This division is the most important idea in the whole topic: the head is for machines, and the body is for people.

The head contains a handful of elements. The most important is the **title element**, which gives the page its name. The name is shown on the browser tab, is saved when the reader bookmarks the page, and is used as the clickable line in search results. Every page must have exactly one title, and it should describe that page specifically rather than repeating the site name alone.

The head also holds **meta elements**, which carry information that is not displayed at all, and **link elements**, which attach outside resources such as a style sheet. Both are explored in Section 2.5.

The body holds headings, paragraphs, links, pictures and lists. In a complete document it appears after the head and closes before the root does.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Notes on Keeping a Cat</title>
  </head>
  <body>
    <h1>Notes on Keeping a Cat</h1>
    <p>A short record of one household and one very determined animal.</p>
  </body>
</html>
```

Read that from the outside in. The declaration comes first. The root opens. The head opens, does its work, and closes. The body opens, presents the content, and closes. The root closes. Nothing overlaps and nothing is left open.

### 2.5 Metadata, the information that is not displayed

**Metadata** means data about data. In a web page it is the information that describes the page rather than forming part of its visible text. All of it lives in the head, and none of it is drawn on the screen.

The single most important piece of metadata is the **character encoding**, declared with the `charset` attribute on a meta element:

```html
<meta charset="utf-8">
```

Character encoding is the agreement about how the bytes that arrive over the network map onto written characters. There are many possible encodings, and they disagree about the meaning of bytes above the basic English range. If a page is saved in one encoding and the browser assumes another, apostrophes turn into rubbish and non-English letters become question marks or odd symbols. The encoding named `utf-8` is Unicode Transformation Format, 8-bit, and it covers essentially every character used by every living language, plus emoji, which makes it the correct choice for new pages. The declaration should appear early in the head, near the top, so the browser meets it before it has to interpret any text. If you have ever opened a page and seen a strange symbol where an apostrophe should be, you have met a mismatch between encoding and declaration.

The second important piece is the **viewport declaration**, which matters only on phones and tablets but matters enormously there:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without it, a phone browser pretends to be a desktop browser with a screen about a thousand pixels wide, renders the page at that width, and then shrinks the result until it fits the phone. Everything becomes tiny. With it, the browser is told to use the real width of the device, and the page can lay itself out for a narrow screen. If a site looks perfectly readable on a laptop and microscopically small on a phone, the viewport declaration is usually the missing line.

The third important piece is the **page description**, which is a sentence or two summarising the page for search engines and for link previews:

```html
<meta name="description" content="A short record of one household, one cat, and the mice who did not survive it.">
```

Search engines frequently quote this description under the page title in their results. It should be written as a sentence a person would want to read, not as a pile of keywords. It has no effect on how the page looks.

A fourth common piece of metadata attaches an outside style sheet, which is the file that controls colours, fonts and spacing:

```html
<link rel="stylesheet" href="css/style.css">
```

That line has no closing tag. It says that the document is linked to a style sheet at the given address, and it is the whole mechanism by which one file of styling rules can serve every page on a site.

### 2.6 Headings and the hierarchy

HTML provides six heading elements, numbered one to six. The first, `h1`, is the most important, and each following number is a level lower. They form a hierarchy, which means an outline with ranks, not a list of font sizes that happen to differ.

A correct page uses one first-level heading that names the page. Each major section inside the page gets a second-level heading. Each subsection of those gets a third-level heading, and so on, down to the sixth level. The levels must not be skipped: a third-level heading should not appear directly under a first-level heading, because that leaves a gap in the outline that a screen reader reports as a broken structure.

```html
<h1>Notes on Keeping a Cat</h1>
<h2>Feeding</h2>
<p>Lucky eats twice a day, and complains about both meals.</p>
<h3>Wet food</h3>
<p>She prefers the fish flavour and will not touch the chicken.</p>
<h3>Dry food</h3>
<p>A bowl is left out overnight, which the mice have learned about.</p>
<h2>Sleeping</h2>
<p>Any chair that a person has just left is immediately occupied.</p>
```

The single most common mistake with headings is choosing the number by the size of the text you want. A first-level heading is large and a fourth-level heading is small, so it is tempting to use `h4` for a minor label that should look small. That inverts the purpose. Choose the level by rank in the outline, then adjust the appearance with a style sheet. Size is decoration; rank is structure.

The second common mistake is using several first-level headings on one page, one per section. A page has one name, so it should have one first-level heading. Sections inside it are second-level.

Headings also do real work for readers who cannot see the page. A screen reader can list every heading on a page as a table of contents and jump between them. A page with careful headings is navigable in seconds; a page with no headings must be read from the beginning.

### 2.7 Paragraphs and the flow of text

The paragraph element is the workhorse of written content. Every distinct block of prose belongs in its own paragraph, and the browser typically separates consecutive paragraphs with a vertical gap.

```html
<p>Lucky has lived in this house for six years.</p>
<p>In that time she has brought in four mice, two birds and one very surprised frog.</p>
```

The guidance worth following is one idea per paragraph. If a paragraph changes subject halfway through, split it. This is not a matter of taste: a paragraph is a unit of meaning, and both readers and machines use it that way.

A very common beginner mistake is to produce visual line breaks by stacking empty paragraphs or by repeated line-break elements. Both are wrong for the same reason. They produce the appearance of spacing without producing structure, and when the page is read aloud the reader hears meaningless pauses. If two ideas are separate, they are two paragraphs. If a line must break inside one idea, as in a postal address or a poem, a line-break element is correct, and Section 2.8 explains how it is written.

Blank lines in the source file have no effect on the rendered page. A paragraph written across five lines in the editor is still one paragraph, because the browser treats any run of whitespace as a single space. Structure comes from elements, never from the shape of the source text.

### 2.8 Void elements and the elements with no closing tag

A small number of elements contain nothing. They mark a position or insert an object rather than enclosing text, so there is nothing between an opening and a closing tag. These are called **void elements**, and the standard says they have no closing tag and must not be given one.

The two that appear in ordinary page structure are the line break and the thematic break.

The line-break element forces the text to continue on the next line without starting a new paragraph. It is written as a single tag and nothing else:

```html
<p>Lucky<br>4 Mouse Lane<br>Nairobi</p>
```

That is one paragraph containing three lines, which is exactly right for an address: it is a single unit of content, displayed on separate lines.

The thematic break element draws a horizontal rule across the page. It marks a change of topic, such as a shift in a long narrative or a separation between the end of an article and the notes that follow it. It is also written as a single tag:

```html
<p>That was the last of the mice.</p>
<hr>
<p>Six months later, the frog returned.</p>
```

Because the rule is decorative, it is easy to misuse. It should not be used to draw a line for visual effect alone; that is a styling job. Its purpose is the meaning, which is "the subject changes here".

Older material sometimes shows these elements written with a slash before the closing bracket, which is the style required by Extensible HyperText Markup Language, abbreviated XHTML. In version 5 of HTML, usually written HTML5, that trailing slash is tolerated but does nothing, and the standard describes it as unnecessary. Writing it is harmless; writing a real closing tag is an error, because there is nothing to close.

```html
<p>First line<br>Second line</p>
```

That is the modern form and the one to use. The full list of void elements is short and worth recognising: `area`, `base`, `br`, `col`, `hr`, `img`, `input`, `link`, `meta`, `track` and `wbr`. The image and meta elements appear in this topic, and they too are written without any closing tag.

### 2.9 Emphasis and the reason for choosing meaningful elements

Two inline elements mark importance rather than appearance. The strong element marks content of strong importance, and the emphasis element marks stress emphasis. Browsers usually render the first in bold and the second in italic, but the rendering is a side effect and not the point. The point is the meaning, which assistive technology can convey.

```html
<p>Lucky is <strong>not</strong> allowed on the kitchen table.</p>
```

That sentence is not merely bold. It carries a different meaning from the same words without the strong element, and a reader who hears the page can be told that the word is emphasised. The lesson generalises to the whole language: choose the element that describes what the content is, and let the appearance follow.

### 2.10 Hyperlinks and the anchor element

The anchor element creates a hyperlink, and it is the element that makes the web a web rather than a collection of separate documents. It wraps the content that should be clickable, and it carries the destination in its `href` attribute. The letters stand for hypertext reference.

```html
<p>Read more about <a href="feeding.html">Lucky's feeding routine</a>.</p>
```

Everything between the tags becomes clickable, and that content should describe the destination. "Click here" tells a reader nothing, and a blind user who lists every link on a page hears a list of identical phrases. "Lucky's feeding routine" tells everyone exactly what will happen.

The value of `href` can take several forms, and the differences matter.

An **absolute** address states the whole location, including the scheme and the host name. It works from anywhere, including from a page on a different site:

```html
<a href="https://www.example.com/about.html">About the example site</a>
```

A **relative** address states only the part that differs from the current page's location. It is resolved against the address of the page that contains it, which is why the same relative link works on a laptop and on a live server:

```html
<a href="feeding.html">Feeding</a>
<a href="pages/sleeping.html">Sleeping</a>
```

A relative address beginning with a slash is resolved from the root of the site rather than from the current folder:

```html
<a href="/contact.html">Contact</a>
```

A **fragment** begins with a hash mark and points at an element inside a page rather than at another page. The target element must carry an identifier equal to the name after the hash:

```html
<p><a href="#feeding">Jump to feeding</a></p>
<h2 id="feeding">Feeding</h2>
```

When such a link is followed, the browser jumps to the element with that identifier. A fragment can also be appended to another page's address, which opens that page already scrolled to the right place.

Two other forms are worth recognising. A link beginning with `mailto:` opens the reader's mail program with a new message addressed to the given address, and a link beginning with `tel:` starts a call on a phone. Both are ordinary anchor elements with an unusual scheme.

### 2.11 Images and the alternative text

The image element places a picture on the page. It is a void element, so it has no closing tag. It requires two attributes: `src`, which gives the address of the image file, and `alt`, which gives a text replacement.

```html
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden chair" width="480" height="360">
```

The `src` attribute works exactly like the `href` of a link, and it accepts absolute and relative addresses in the same way. A relative address is resolved against the address of the page, so `images/lucky.jpg` means a folder called images beside the page.

The `alt` attribute is not optional, and it is not decoration. It is read aloud by screen readers in place of the picture, and it is displayed by any browser that cannot load the image. A good description says what the picture conveys: "Lucky asleep across a wooden chair" tells a listener what sighted readers see. A poor description says "image" or "photo of a cat", which adds nothing. If the picture is purely decorative and the surrounding text already conveys everything, the correct value is an empty one, `alt=""`, which tells assistive technology to skip it entirely. Leaving the attribute out is different from leaving it empty: the first is an error, and the second is a deliberate statement.

The `width` and `height` attributes give the size in pixels, written as plain numbers with no unit. Their real value is that the browser can reserve the correct space before the picture arrives, so the text does not jump down the page as images load. That jump is one of the most irritating experiences on a slow connection, and two attributes prevent it.

### 2.12 Lists and their structure

HTML has two list types in everyday use, and both are built from list item elements.

An **unordered list** is a list in which the order does not carry meaning, such as a shopping list or a set of features. It is written with the `ul` element, and each item is an `li` element inside it.

```html
<ul>
  <li>Cat food</li>
  <li>Cat litter</li>
  <li>A new scratching post</li>
</ul>
```

An **ordered list** is a list in which the sequence matters, such as steps in a procedure or a ranking. It is written with the `ol` element, and the browser numbers the items automatically.

```html
<ol>
  <li>Fill the bowl with water.</li>
  <li>Add the dry food.</li>
  <li>Call the cat, twice, then a third time.</li>
</ol>
```

The structure rules are strict and simple. A list may contain only list items as direct children. A list item may contain text, paragraphs, links, images, and even another whole list. That last point is how nesting works: to place a sub-list inside a list, the inner list goes inside the list item it belongs to, not between two list items.

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

Note carefully where the closing tags fall. The inner list is complete before the outer list item closes, and the outer list item closes before the next item begins. Putting the inner list between two items instead is the most common nesting error, and browsers repair it in ways that change the outline the reader hears.

### 2.13 Block and inline, two kinds of flow

Every element behaves in one of two broad ways.

A **block-level** element occupies its own horizontal band on the page. It begins on a new line, takes the full width available to it, and the next element starts below it. Headings, paragraphs, lists, list items and the horizontal rule are block-level.

An **inline** element lives inside a line of text. It begins and ends wherever it occurs and does not break the line. Links, images, strong text and emphasis are inline.

The rule that follows from this is easy to state and easy to break: a block-level element may contain inline elements and other block-level elements, but an inline element should not contain a block-level element. A link inside a paragraph is normal. A paragraph inside a link is not, because the paragraph would need its own band while the link is trying to stay inside a line.

The practical consequence appears when a layout looks wrong for no visible reason. A heading that refuses to sit beside some text, or a link that breaks oddly onto a new line, is usually a block-and-inline mismatch rather than a styling problem.

### 2.14 Characters with special meanings

Three characters cannot be typed literally in text content, because the language uses them as punctuation. The angle brackets open and close tags, and the ampersand begins the codes used to write the special characters themselves. Each has a written substitute, called a character reference, that begins with an ampersand and ends with a semicolon.

| Character | Reference | Where it is needed |
| --- | --- | --- |
| Less than | `&lt;` | Anywhere the character must be shown as text |
| Greater than | `&gt;` | Anywhere the character must be shown as text |
| Ampersand | `&amp;` | Anywhere a literal ampersand is required |
| Quotation mark | `&quot;` | Inside an attribute value delimited by the same mark |
| Non-breaking space | `&nbsp;` | Where two words must not be split across lines |

A page that teaches programming has to show these constantly, because a tutorial about tags must display tags as text rather than letting the browser treat them as markup. In code examples that are typeset on the page, the angle brackets of every sample tag are written with references, which is why such pages look so noisy in their source.

## 3. Methods and Operations

### 3.1 The method for starting a page

Writing a page is a sequence, and following the sequence avoids most errors.

1. Create a file whose name ends in `.html`, in the folder where the page belongs.
2. Write the document type declaration as the first line.
3. Open the root element, and give it a language attribute.
4. Open the head. Add the encoding declaration first, then the title, then the viewport declaration and the description, then any link to a style sheet.
5. Close the head and open the body.
6. Add the single first-level heading that names the page.
7. Add the sections below it, each with a heading, and each containing paragraphs, lists or links as the content requires.
8. Close the body and then the root.
9. Save the file with the encoding that the declaration names, which in practice means saving as UTF-8.
10. Open it in a browser and read it as a stranger would.

The ordering in step 4 is not arbitrary. The encoding declaration must be met by the browser early, before it has to interpret any text that depends on it, so it goes as close to the top of the head as possible.

### 3.2 The method for writing headings and paragraphs

The temptation is to type the content first and add markup afterwards. The reliable method is the opposite, because structure decided while writing is structure that matches the meaning.

1. Write down the single sentence that names the page, and mark it as a first-level heading.
2. List the major sections of the page. Each becomes a second-level heading, in the order a reader should meet them.
3. For each section, list its subsections. Each becomes a third-level heading.
4. Write the prose, one idea per paragraph.
5. Re-read the headings alone, as an outline. If the outline makes sense on its own, the structure is right. If two headings at the same level overlap, one of them should be a subsection of the other.

That fifth step is the real test, and it takes less than a minute.

### 3.3 The method for building a list

1. Decide whether order carries meaning. If it does, the list is ordered; if it does not, it is unordered.
2. Open the list element.
3. Write one list item per entry, with the whole entry inside the item.
4. If an entry has sub-entries, close its text, then open the inner list inside the same list item, build it, and close both.
5. Check that no text sits directly inside the list, outside an item.

The last check catches almost every list error. Text that is a direct child of a list is not valid, and browsers move it out of the list silently, which changes what a screen reader announces.

### 3.4 The method for adding a link

1. Decide what the reader should click, and write words that describe the destination.
2. Wrap those words in an anchor element.
3. Choose the address form. Use a relative address for a page on the same site, an absolute address for another site, a slash-prefixed address for a page at a fixed place on this site, and a fragment for a position inside a page.
4. Test the link by clicking it, not by reading it. A relative address that looks correct is resolved against the page's own address, and that resolution is where errors hide.
5. Check the link text alone. If it does not say where it goes, rewrite it.

### 3.5 The method for adding an image

1. Put the image file in the project, in a folder that has a name describing its contents.
2. Reference it with a relative address from the page that uses it.
3. Write the alternative text as a description of what the image conveys, in a sentence fragment without the words "image of".
4. Decide whether the image is decorative. If it is, use an empty alternative text and no more.
5. Give the width and height in pixels so the page does not shift while loading.
6. Load the page with the image deliberately renamed, and confirm that the alternative text appears and reads sensibly. That test is the only reliable proof that the description works.

### 3.6 The method for verifying the markup

1. Open the page in a browser and read it. Does the outline make sense? Do the links go where they claim?
2. Open the page source, which is the raw file the browser received, and compare it with what you wrote. If the browser has moved anything, the markup was not valid.
3. Run the file through the validator published by the World Wide Web Consortium, abbreviated W3C, which reports every departure from the standard with a line number.
4. Fix errors from the top down, because one unclosed element causes a cascade of later complaints.
5. Re-run the validator until it reports no errors. Warnings about style are advisory; errors are not.

## 4. Worked Implementation from the Notes

### 4.1 Task: assemble a complete page about a cat, one layer at a time

### 4.2 Implementation: build the skeleton, then add content in layers

Step 1. Write the document declaration and the skeleton. This is the smallest file that a browser will treat as a document rather than as a fragment of text.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lucky the Cat</title>
  </head>
  <body>
  </body>
</html>
```

Step 2. Add the metadata that is not displayed. The encoding is declared first because the browser must know it before it interprets the title; the viewport declaration comes next so a phone uses its real width; the description is written as a sentence for search results.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lucky the Cat</title>
  <meta name="description" content="A short record of one cat, her habits, and the animals she brings home.">
  <link rel="stylesheet" href="css/style.css">
</head>
```

Step 3. Add the heading structure. There is one first-level heading because the page has one name, and two second-level headings because there are two sections.

```html
<body>
  <h1>Lucky the Cat</h1>
  <h2>Who she is</h2>
  <h2>What she does</h2>
</body>
```

Step 4. Fill each section with paragraphs, one idea per paragraph.

```html
<h2>Who she is</h2>
<p>Lucky is a small grey cat with one white paw and no interest in being picked up.</p>
<p>She has lived in this house for six years and has never once used the bed that was bought for her.</p>
```

Step 5. Add an ordered list for the sequence of events on a hunting morning, and an unordered list for her preferred sleeping places. The ordered list is numbered automatically; the unordered list is bulleted.

```html
<h2>What she does</h2>
<p>Her morning follows a fixed order:</p>
<ol>
  <li>Wake the household at five.</li>
  <li>Demand food, then refuse it.</li>
  <li>Patrol the hedge.</li>
</ol>
<p>Her preferred chairs are:</p>
<ul>
  <li>The warmest one</li>
  <li>The one a person has just left</li>
</ul>
```

Step 6. Add an inner list inside the second bullet, to show a sub-list in its correct position, inside the list item rather than between items.

```html
<ul>
  <li>The warmest one</li>
  <li>The one a person has just left
    <ul>
      <li>Especially the desk chair</li>
      <li>Especially during a call</li>
    </ul>
  </li>
</ul>
```

Step 7. Add the links. One is relative and points at a page beside this one, one is absolute and points at another site, and one is a fragment pointing at the second heading, which therefore needs an identifier.

```html
<p>Read the <a href="feeding.html">feeding routine</a> or the <a href="https://www.example.com/cats/">general guide to cats</a>.</p>
<p><a href="#what-she-does">Skip to what she does</a></p>
<h2 id="what-she-does">What she does</h2>
```

Step 8. Add the image with its alternative text and its dimensions, and finish the section with a thematic break and a closing remark.

```html
<p>Here she is, occupying the chair again.</p>
<img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
<hr>
<p>No mice were harmed in the writing of this page, though two were inconvenienced.</p>
```

Step 9. Read the whole file from top to bottom and check three things: every element that opened has closed, every void element stands alone, and every attribute value is in quotes.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Lucky the Cat</title>
    <meta name="description" content="A short record of one cat, her habits, and the animals she brings home.">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <h1>Lucky the Cat</h1>
    <h2>Who she is</h2>
    <p>Lucky is a small grey cat with one white paw and no interest in being picked up.</p>
    <p><a href="#what-she-does">Skip to what she does</a></p>
    <h2 id="what-she-does">What she does</h2>
    <ol>
      <li>Wake the household at five.</li>
      <li>Demand food, then refuse it.</li>
      <li>Patrol the hedge.</li>
    </ol>
    <img src="images/lucky.jpg" alt="Lucky asleep across a wooden desk chair" width="480" height="360">
    <hr>
    <p>Read the <a href="feeding.html">feeding routine</a> next.</p>
  </body>
</html>
```

Step 10. Open the page and confirm the expected results. The tab shows the title. The first-level heading is large and stands alone. The three list entries are numbered one to three by the browser, without any number having been typed. The link marked with a fragment scrolls the page to the second heading when clicked. The horizontal rule appears as a line across the page. Nothing needed a closing tag that does not exist.

### 4.3 Task: prove that the alternative text is doing its work

### 4.4 Implementation: break the image on purpose, then read the page without it

Step 1. Rename the image file so the address no longer resolves, then reload. The browser draws a broken-image indicator and displays the alternative text in its place.

```text
Lucky asleep across a wooden desk chair
```

Step 2. Interpret what this proves. A reader on a slow connection, a reader using a text-only browser, and a reader using a screen reader all receive the sentence in the space where the picture would be. If the attribute were absent, the browser would show either nothing or the file name, and a listener would be told only that there is an image.

Step 3. Confirm the dimensions are doing their own job. In the browser's developer tools, throttle the connection and reload. The space for the image is reserved before the file arrives, so the paragraphs below do not jump. Remove the width and height attributes, reload, and the jump returns; restore them, and it disappears.

### 4.5 Task: show what a missing declaration does to a page

### 4.6 Implementation: compare two identical pages with and without the declaration

Step 1. Save the page twice, once with the document type declaration and once without it, and give the second file a different name. The two files are then identical below the first line.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Declaration test</title>
  </head>
  <body>
    <h1>Declaration test</h1>
    <p>This page exists to show what the declaration does.</p>
  </body>
</html>
```

Step 2. Open both and compare the spacing around the heading and the width of the body. In standards mode, which the declaration triggers, the layout follows the rules in the standard. Without it the browser falls back to a compatibility mode that imitates the inconsistent behaviour of very old browsers, and small differences appear that no style rule explains.

Step 3. State the lesson plainly. The declaration is one line, it is easy to forget, and its absence produces symptoms that look like styling problems. If a page behaves inexplicably, check the first line before changing anything else.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to know you have understood this topic

You can explain, without notes, why HTML is a markup language rather than a programming language. You can point at any line of a simple page and name the element, the attribute, the attribute value and the content. You can write the skeleton from memory in the right order. You can say what belongs in the head and what belongs in the body, and why the division exists. You can write a heading outline that does not skip a level. You can explain why a line-break element has no closing tag. You can give one example each of an absolute address, a relative address, a root-relative address and a fragment. You can write an image element with a useful alternative text, and you can say what should be there when the image is decorative. You can build a nested list with the inner list inside the correct list item. If all of that is comfortable, the topic is learned.

### 5.2 Beginner misconceptions, and the correction for each

- **"HTML is a programming language."** It has no variables, no decisions and no arithmetic. It labels content. Programming is a different activity in a different language.
- **"The browser shows exactly what I typed."** The browser parses the source into a tree and renders the tree. Invalid nesting is silently repaired, and the repair may not be what you meant.
- **"Blank lines in the file create space on the page."** All runs of whitespace collapse to a single space. Spacing comes from elements and style sheets.
- **"Repeated line breaks are a good way to space out a page."** They create meaningless structure and meaningless pauses for a listener. Use paragraphs and styling.
- **"Heading numbers are font sizes."** They are ranks in an outline. Choose by rank, then style.
- **"Every image needs a description."** Decorative images need an empty alternative text so they can be skipped. Every image needs the attribute; not every image needs words.
- **"A closing tag is needed for every tag."** Void elements have no closing tag at all. Writing one is an error.
- **"The trailing slash is required."** It is an XHTML requirement. In HTML5 it is tolerated and unnecessary.
- **"Quotes around attribute values are optional."** They are optional only in narrow circumstances and always cost nothing. Use them.
- **"A link to a page in the same folder needs the whole address."** A relative address is resolved against the current page and is usually the better choice.
- **"The description meta element makes text appear on the page."** It never appears on the page. It is read by search engines and link previews.
- **"Metadata is optional decoration."** Without the encoding declaration the page may display rubbish; without the viewport declaration it may be unreadable on a phone.

### 5.3 Reading a page you have just written

Interpretation is a skill separate from writing. When a page loads, ask four questions in order.

Does the tab show the title I intended? If not, the title element is missing, empty, or in the wrong place.

Does the outline, read as a list of headings, describe the page sensibly? If a heading level jumps, a reader who navigates by headings will be told that the structure is broken.

Do the links go where they claim, in a browser, from the page as published? A relative address that works locally usually works in place, but a root-relative address that works locally may break if the site is served from a subfolder.

Can the page be understood with the images switched off? If the alternative text reads as a sensible sentence in each gap, the descriptions are doing their job.

### 5.4 A checklist to run before publishing

| Check | What a failure looks like |
| --- | --- |
| First line is the document declaration | Layout differs slightly from other pages for no reason |
| The root element states the language | Screen reader uses the wrong pronunciation |
| Exactly one title, describing this page | Tab shows the file name or a repeated site name |
| Encoding declared early in the head | Apostrophes and non-English letters display as rubbish |
| Viewport declared | Page is tiny on a phone |
| One first-level heading | The page has no clear name in an outline |
| No skipped heading levels | Outline reports an unexplained gap |
| Every image has an alternative text | A broken image shows nothing useful |
| Every attribute value is quoted | An address containing spaces breaks |
| Void elements have no closing tag | Validator reports an unexpected closing tag |
| Lists contain only list items | Browser silently moves stray text |
| Every link text describes its destination | A list of links reads as repeated "click here" |

### 5.5 Why this becomes the foundation for everything else

Every later topic in web development rests on the structure described here. A style sheet selects elements by the names and attributes introduced in this note, so a page with meaningless elements cannot be styled precisely. A script reaches into the document through the same tree, so a page with broken nesting offers the script a different structure from the one the author imagined. A search engine ranks a page partly on the outline its headings produce. An assistive technology builds its entire navigation from these elements.

The reason is that HTML is not a way of describing appearance. It is a way of describing meaning, and every other tool in the browser reads that meaning. A student who treats markup as a decoration step will spend the rest of the subject fighting the tools. A student who treats it as a description of structure will find that styling, scripting and accessibility all become straightforward, because the page already says what it is.
