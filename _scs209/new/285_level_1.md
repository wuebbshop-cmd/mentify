## 1. Concept and Use Case

### 1.1 A room, a shelf, and a form on the wall

Imagine you are arranging a small office. A bookshelf claims a whole wall, standing alone, and nothing else may stand in that space. A row of framed photographs hangs along one shelf, side by side, sharing the same space politely. On the desk lies a printed sheet with boxes to tick, a line for your name, and a slot for the finished sheet to be posted. Three very different arrangements, three very different jobs, one room.

A page on the web is arranged in exactly that way, and the three arrangements have direct counterparts. Some pieces of content occupy a whole "wall": they begin on a fresh line and stretch across the available width. Other pieces flow along a "shelf" in the middle of a sentence, taking only the room their words need. Data that belongs in a grid is written into rows and columns, like an accounts ledger. Information that must be collected from a visitor is written into boxes on a sheet, with a fixed destination for the finished answers.

The technical name for the language that performs these three jobs is HyperText Markup Language, usually shortened to HTML. It is the language that describes the structure of a page: which parts are headings, which are paragraphs, which are items in a grid, and which are boxes waiting for input. It does not decide the colours or the fonts on its own; a companion language, Cascading Style Sheets, abbreviated CSS, does that. Nor does HTML process the answers a visitor types; a program on a server does that after the browser sends them.

This topic is therefore about the furniture of a page rather than its paint. It covers the two display behaviours that decide whether content stands alone or flows in a line, the two plain containers used to group content, the two attributes used to label that content for styling and scripting, the grid used for data, and the sheet used for collecting answers.

### 1.2 Three jobs, one document

Every page you have ever used is doing one or more of the following three jobs, and the elements in this topic exist to serve them.

**Arranging content.** A news site has a masthead at the top, a navigation strip beneath it, a column of articles in the middle, and a footer at the bottom. Each of those regions contains other things. Something has to hold a region together so that a rule about the masthead does not accidentally apply to the footer. Generic containers do that holding, and their display behaviour decides whether the held content stacks vertically or sits inside a sentence.

**Presenting data.** A bank statement, a timetable, a price list and a set of examination results all share a shape: labels across the top, records down the side, and a value at each crossing. That shape is a grid, and HTML has a dedicated family of elements for it. Using the grid family means the browser can align columns, repeat a header on a printed page, and announce row and column labels to a screen reader.

**Collecting answers.** A login box, a search field, a booking form and a feedback survey all ask the visitor to supply values and then send them somewhere. The form family provides the paper, the boxes, the labels and the postal address.

The three jobs are separable. A page can present a table without collecting anything, and can collect answers without a table. But most real pages combine all three, which is why the last subtopic of this topic is the assembly of a complete page from every element studied along the way.

### 1.3 Why the browser has to be told

A browser does not guess the arrangement. It obeys two sets of instructions, and the interaction between them explains most beginner confusion.

The first set is the browser's own built-in rules, sometimes called the user agent stylesheet. Those rules say that a heading starts on a new line with space above and below, that a paragraph starts on a new line, that a link inside a sentence does not, that a table cell has a thin border and a little space around its text, that a text box is about twenty characters wide. You did not write them, and you cannot see them in your file, yet they are the reason an unformatted page still looks readable.

The second set is the rules you write yourself, in CSS. Your rules override the built-in ones because of the order of precedence in the cascade: an author rule outranks a browser rule for the same property on the same element.

Everything in the first two subtopics of this topic is a consequence of the first set. Some elements are declared by default to occupy their own line and fill the width available. Others are declared to sit within a line of text. Once you know which element belongs to which group, the layout behaviour stops being mysterious, and the rules about what may be placed inside what become obvious rather than arbitrary.

### 1.4 Words you will meet, spelled out

Technical writing is dense with abbreviations, so here they are in one place, each expanded the first time it matters.

**HTML** is HyperText Markup Language. "HyperText" means text that can link to other text; "markup" means that the text is annotated with labels rather than executed as instructions.

**CSS** is Cascading Style Sheets. A style sheet is a list of rules that say how elements should look, and "cascading" refers to the defined order in which conflicting rules win.

**URL** is Uniform Resource Locator, the address of a resource, such as the page a form sends its answers to.

**HTTP** is HyperText Transfer Protocol, the request-and-response protocol a browser uses to fetch pages and to submit forms. **HTTPS** is the same protocol carried inside an encrypted connection, and the extra letter stands for Secure.

**DOM** is the Document Object Model, the tree of objects a browser builds from your markup. When a script "changes the page", it is changing this tree, and the structure of the tree is decided by the parser as much as by what you typed.

**W3C** is the World Wide Web Consortium, and **WHATWG** is the Web Hypertext Application Technology Working Group. The second now maintains the living standard for HTML, while the first publishes many of the related specifications.

**ARIA** is Accessible Rich Internet Applications, a set of attributes that add meaning for assistive technology when the plain elements are not enough.

**XML** is Extensible Markup Language, a stricter cousin of HTML; it is mentioned here only because you will meet self-closing syntax such as a slash before the closing angle bracket, which is not required in HTML.

### 1.5 Where this appears in ordinary life

You already rely on this topic many times a day, usually without noticing.

When you search for a flight, the results arrive as a grid of times, airlines and prices, with a header row that tells you which column is which, and often a merged row at the bottom that says "taxes included". That is a data table with spanning cells.

When you log in to a student portal, the page asks for a username and a masked password, and the browser offers to remember them. That is a form with text and password fields, submitted by a method that keeps the values out of the address bar.

When you tick "remember me" and choose between "full time" and "part time", you are using a checkbox and a group of radio buttons, and the difference between them is one of the misconceptions this note corrects.

When a page shows a highlighted product name in the middle of a sentence, or a price in a different colour, a generic inline container is probably doing the work. When a page shows a banner, a sidebar and a footer, generic block containers or their semantic replacements are holding each region together.

### 1.6 The single sentence that holds the topic together

If you remember one sentence from this section, remember this one: HTML gives you two display behaviours, two plain containers, two labelling attributes, one grid family and one form family, and every page you will build in this course is a combination of them arranged in a sensible order.

## 2. Data, Syntax, and Core Concepts

### 2.1 Block-level elements: the bookshelf

A block-level element is one whose default display behaviour is to stand alone. It begins on a new line, even if there is space to its left, and it occupies the full width available to it unless you tell it otherwise. Its height is decided by its content unless you set one.

The block-level elements you will use most are these:

- `div`, the generic block container
- `p`, a paragraph
- `h1` to `h6`, the six heading levels
- `ul` and `ol`, unordered and ordered lists, and `li`, a list item
- `blockquote`, a long quotation
- `pre`, preformatted text in which whitespace is preserved
- `table`, and the form element, despite the form being invisible
- `header`, `nav`, `main`, `section`, `article`, `aside` and `footer`, the semantic regions

Because a block element takes the whole width, two block elements placed one after another always appear stacked. You do not need a line break between them, and adding one changes nothing except, sometimes, an extra gap.

```html
<div>First block</div>
<div>Second block</div>
```

Both lines above start at the left edge of the page, one beneath the other, even though they are short. That is the defining behaviour, and it is worth seeing once in a browser because it explains the default look of every unformatted page you have ever met.

### 2.2 Inline elements: the framed photographs on the shelf

An inline element is one whose default behaviour is to sit inside a line of text. It does not force a new line before or after itself, and it takes only as much width as its content needs. A sentence containing several inline elements still reads as one sentence.

The inline elements you will use most are these:

- `span`, the generic inline container
- `a`, a link
- `strong` and `em`, for importance and emphasis
- `b`, `i` and `u`, for visual distinction without importance
- `code`, for a fragment of computer code
- `small`, `sub` and `sup`
- `abbr`, for an abbreviation with its expansion
- `label`, `input`, `select`, `textarea` and `button`, the form controls
- `br`, a line break, and `img`, an image

Some of these are called replaced elements, because the browser replaces the element with something it draws itself: an image, a text box, a button. A replaced inline element behaves a little like a small block in the middle of a line: it has an intrinsic size, and text flows around it.

The practical consequence is that you cannot rely on an inline element to create a new line, and you cannot rely on it to honour a width you set. If you want a new line, use a block element or a break; if you want an inline fragment to accept a width, you must change its display behaviour explicitly.

### 2.3 The nesting rule in plain words

The nesting rule follows directly from the two behaviours. Block-level elements may contain inline elements, and they may also contain other block-level elements. Inline elements may contain only inline content, which means text and other inline elements.

Stated as a slogan: a big box may hold small things and other big boxes, but a small thing may hold only smaller things.

```html
<div>
  <p>A paragraph inside a block container, with <span>a highlighted word</span> in it.</p>
</div>
```

The example above is legal at every level. A `div` holds a `p`, and the `p` holds text and a `span`. The reverse arrangement, a `span` holding a `p`, is not legal, and browsers will quietly rebuild the tree to something they consider acceptable, which is how pages break in ways the author cannot see in the source.

There is one useful modern exception worth knowing early: a link, `a`, is allowed to wrap block-level content in current HTML if the surrounding context allows block-level content. That is why a whole card of a website can be clickable. The exception is specific to `a`, and it does not extend to `span`.

### 2.4 `div`: the plain box

The `div` element is a generic block-level container. It carries no meaning of its own: it does not say "this is a header" or "this is a sidebar". It says only "these things belong together".

That plainness is its value. When you have several paragraphs and a heading that together form a promotional panel, you can wrap them in a `div` and give the `div` a label. Then a single CSS rule can draw a border around the panel, and a single script can hide or show it, without touching any of the paragraphs inside.

Typical uses for a `div` are a page masthead, a column of content, a sidebar, a highlighted box in the middle of an article, and an advertising slot. Since the arrival of the semantic region elements, it is better style to use `header`, `nav`, `main`, `aside` and `footer` where one of those meanings genuinely applies, and to reserve `div` for grouping that has no better name.

### 2.5 `span`: the highlighter pen

The `span` element is a generic inline container. It also carries no meaning. It says only "this run of words is one thing".

You reach for a `span` when a piece of text inside a sentence needs its own identity: a product name that should be styled consistently, a price that must change colour when it drops, a word that a script must find and replace. The text stays in the flow of the sentence; only the label is added.

```html
<p>Our best sellers are the <span class="product">SuperWidget</span> and the <span class="product">MegaWidget</span>.</p>
```

The paragraph still reads as one sentence. The two spans give CSS a handle, and they give a script a way to select exactly those words.

### 2.6 `class` and `id`: a reusable label and a name tag

Both `class` and `id` are global attributes, which means they may be written on any element. They are how CSS and scripts find things. They are not interchangeable, and the difference is worth learning properly now.

An `id` is a name tag for one specific element. It must be unique within the document: no two elements may share the same `id` value. It may not contain spaces. You use it when there is exactly one such thing on the page, such as the main content area, the search box, the site footer, or the heading of a section that a link should jump to.

A `class` is a reusable label. Many elements may share the same class value, and one element may carry several class values at once, separated by spaces. You use it when a rule should apply to a whole family of things: every price, every warning message, every row that is currently selected.

```html
<p id="intro">The <span class="product featured">SuperWidget</span> is on offer.</p>
<p>The <span class="product">MegaWidget</span> arrives in June.</p>
```

Here the first paragraph has a unique name tag, while both product names share the reusable label `product`, and the first one also carries `featured`. A CSS rule for `.product` styles both, a rule for `.featured` styles only the first, and a rule for `#intro` styles only that paragraph.

A simple way to choose between them: if you can imagine a second one appearing, use a class. If the page would become meaningless with two, use an `id`.

### 2.7 The table family: `table`, `caption`, `tr`, `th`, `td`

A table is declared with the `table` element, and it is built from rows. Inside the table are rows, declared with `tr`, which stands for table row. Inside each row are cells. A cell that holds a label for its column or row is a table header cell, declared with `th`. A cell that holds data is a table data cell, declared with `td`.

```html
<table>
  <caption>Class grades</caption>
  <tr>
    <th scope="col">Student</th>
    <th scope="col">Subject</th>
    <th scope="col">Grade</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>Mathematics</td>
    <td>A</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>Science</td>
    <td>B</td>
  </tr>
</table>
```

The `caption` element gives the table a title. It must be the first thing inside the `table`, and it is announced to assistive technology, which is why it matters more than a heading placed above the table by coincidence.

The `scope` attribute on a `th` states whether that header labels a column, a row, a group of columns, or a group of rows. It costs a few characters and it makes the table readable by a screen reader, which cannot see the grid the way you can. In an examination answer, mentioning `scope` is usually worth a mark.

### 2.8 Cell alignment

By default, a `th` is centred and bold, and a `td` is left aligned, because those are the browser's built-in rules for the two elements. You change alignment with CSS, not with the old presentational attributes.

```css
th {
  text-align: left;
}

td.number {
  text-align: right;
}
```

Horizontal alignment uses `text-align`, with the values `left`, `right`, `center` and `justify`. Vertical alignment inside a cell uses `vertical-align`, with the values `top`, `middle`, `bottom` and `baseline`. A sensible convention, and one examiners like to see stated, is to centre the header labels, left align text values and right align numbers so that digits line up by place value.

### 2.9 Borders, cell padding and cell spacing

Three pieces of a table's appearance are worth separating, because beginners merge them into one idea and therefore cannot fix a table that looks cramped or gappy.

A **border** is the line drawn around the table and around each cell. There is an old attribute called `border` on the `table` element that takes a width in pixels, and there is a modern CSS property with the same name. The attribute still works in browsers, but it is obsolete, so the property is the correct answer in an examination.

**Cell padding** is the space between a cell's border and the text inside it. It is the cushion that stops text from touching the line. The old attribute is `cellpadding`, and the modern equivalent is the `padding` property applied to the `th` and `td` elements.

**Cell spacing** is the gap between one cell and the next. It is the moat between neighbours. The old attribute is `cellspacing`, and the modern equivalent is the `border-spacing` property on the table, which only has any effect while the table is using the separate borders model.

```html
<table border="1" cellpadding="10" cellspacing="6">
  <caption>Legacy presentation attributes</caption>
  <tr>
    <th scope="col">Item</th>
    <th scope="col">Cost</th>
  </tr>
  <tr>
    <td>Notebook</td>
    <td>120</td>
  </tr>
</table>
```

That markup produces a visible result, but the same result is better written in CSS, where the three ideas stay separate and can be changed without touching the markup. The three attributes above are obsolete in the current standard; they are shown because legacy pages and older examination questions still use them, and because recognising them is how such a page is converted to CSS.

```css
table {
  border-collapse: separate;
  border-spacing: 6px;
}

th,
td {
  border: 1px solid #999;
  padding: 10px;
}
```

If you set `border-collapse: collapse` on the table, neighbouring borders merge into one line and the spacing is ignored, because there is no gap left for a moat. That single switch explains why two tables with the same borders can look so different: one is drawing each cell's four edges separately, and the other is drawing shared edges once.

### 2.10 Spanning: `colspan` and `rowspan`

Sometimes one cell must cover more than one column or more than one row. The attribute `colspan` sets how many columns a cell covers, and `rowspan` sets how many rows it covers. Both default to one, and both accept a positive whole number.

```html
<table>
  <caption>Term marks for one student</caption>
  <tr>
    <th scope="col">Student</th>
    <th scope="col">Term 1</th>
    <th scope="col">Term 2</th>
  </tr>
  <tr>
    <th scope="row" rowspan="2">Alice</th>
    <td>70</td>
    <td>75</td>
  </tr>
  <tr>
    <td>80</td>
    <td>85</td>
  </tr>
</table>
```

The second row declares three cells: the name, which covers two rows, and two marks. The third row declares only two cells, because the space under the name is already taken. This is the single most important habit to build: a spanned cell is declared once, in the row where it starts, and every row it covers must simply leave that space empty.

Counting is the safeguard. The table above has three columns. Row one declares one plus one plus one, three. Row two declares one plus one plus one, three. Row three declares two, and the third space is occupied by the row span from row two. Every row accounts for three columns, so the grid is sound.

### 2.11 The form family: `form`, `action` and `method`

A form is a region of a page that collects values from the visitor and sends them to a program. It is declared with the `form` element, which is invisible by default but behaves as a block-level container.

Two attributes decide where the answers go and how they travel.

The `action` attribute holds the URL of the program that will receive the answers. Without it, the browser sends the answers back to the same address the page came from.

The `method` attribute chooses between two submission techniques, `get` and `post`. With `get`, the answers are appended to the address as a query string, which you have seen many times as the part of a web address after a question mark. With `post`, the answers travel in the body of the request message and do not appear in the address.

```html
<form action="/search" method="get">
  <label for="q">Search the catalogue</label>
  <input type="text" id="q" name="q">
  <input type="submit" value="Search">
</form>
```

If the visitor types the word algebra and submits, the browser requests the address `/search?q=algebra`. A colleague can bookmark that address and get the same result, which is exactly why searching uses `get`.

### 2.12 The controls: boxes on the sheet

Inside a form, the visitor interacts with controls. Each control has a `name`, which is the label used when the value is sent, and usually an `id`, which is how a `label` element and a script refer to it. The `name` is what the server sees; the `id` is what the page uses. Confusing the two is common and always produces a form that submits nothing.

- A text field, `input` with `type="text"`, accepts one line of text.
- A password field, `input` with `type="password"`, accepts one line and displays dots or asterisks. It hides the characters from onlookers only; it does not encrypt anything, so a secure connection is still required.
- A checkbox, `input` with `type="checkbox"`, is an independent switch that is either ticked or not.
- A radio button, `input` with `type="radio"`, is one of a group from which exactly one may be chosen. All the buttons in one group share the same `name`.
- A submit button, `input` with `type="submit"`, sends the form.
- A reset button, `input` with `type="reset"`, restores every control to its initial value and sends nothing.
- A text area, `textarea`, accepts several lines of text.
- A drop-down list, `select`, contains `option` elements, one of which may be marked `selected`.

```html
<form action="/enrol" method="post">
  <p>
    <label for="full-name">Full name</label>
    <input type="text" id="full-name" name="full_name" required="required">
  </p>
  <p>
    <label for="pin">Password</label>
    <input type="password" id="pin" name="pin">
  </p>
  <p>
    <input type="radio" id="mode-full" name="mode" value="full_time" checked="checked">
    <label for="mode-full">Full time</label>
    <input type="radio" id="mode-part" name="mode" value="part_time">
    <label for="mode-part">Part time</label>
  </p>
  <p>
    <input type="checkbox" id="newsletter" name="newsletter" value="yes">
    <label for="newsletter">Send me the newsletter</label>
  </p>
  <p>
    <label for="campus">Campus</label>
    <select id="campus" name="campus">
      <option value="main">Main campus</option>
      <option value="north" selected="selected">North campus</option>
    </select>
  </p>
  <p>
    <input type="submit" value="Send application">
    <input type="reset" value="Clear form">
  </p>
</form>
```

Notice that each `label` points at a control by matching its `for` attribute to the control's `id`. That association means clicking the word focuses or toggles the control, and it gives a screen reader the name of the field. A form without labels is technically usable by a mouse and unusable by many other people, which is a point examiners reward.

### 2.13 Putting the pieces together: the semantic layout

A complete page is not a random pile of containers. It has a conventional order, and HTML provides elements whose names describe that order: `header` for the masthead, `nav` for the navigation links, `main` for the unique content of the page, `section` for a titled part of that content, `article` for something that could stand alone, `aside` for a related side note, and `footer` for the closing information.

```html
<body>
  <header>
    <h1>Mentify Prep</h1>
  </header>
  <nav>
    <a href="#grades">Grades</a>
    <a href="#enrol">Enrol</a>
  </nav>
  <main>
    <section id="grades">
      <h2>Grades</h2>
    </section>
    <section id="enrol">
      <h2>Enrol</h2>
    </section>
  </main>
  <footer>
    <p>Copyright 2026</p>
  </footer>
</body>
```

Each region can still contain a `div` where no better name exists, and each `id` gives the navigation links a target. This is the shape that the last worked example of this note builds and tests.

## 3. Methods and Operations

### 3.1 A procedure for choosing a container

The same five questions answer almost every container decision, and asking them in order prevents most broken layouts.

Step 1. Ask whether the group must stand on its own or sit inside a line. A masthead, a column, a panel and a footer stand alone, so the container must be block-level. A highlighted word, a price or a product name sits in a sentence, so the container must be inline.

Step 2. Ask whether an existing element already means what you mean. If the group is the top of the page, `header` says so. If it is a set of links, `nav` says so. If it is the unique body of the page, `main` says so. Use the meaningful element first, and fall back to `div` or `span` only when no element carries the meaning.

Step 3. Give the container a name. If there will be one of them, use an `id`. If there may be many, use a `class`. Never invent two elements with the same `id`.

Step 4. Write the CSS rule that targets that name, and put the appearance there rather than in attributes on the element. This keeps the markup describing structure and the style sheet describing looks, which is the separation the course keeps returning to.

Step 5. Open the page and check. Use the browser's inspector to see which box a rule actually landed on, because a selector that matches nothing produces no error message and no visible change.

### 3.2 Writing the three kinds of selector

CSS can reach an element in three ways that correspond exactly to the three ways of naming it.

```css
p {
  line-height: 1.6;
}

.warning {
  color: #a33;
  font-weight: bold;
}

#site-footer {
  border-top: 1px solid #ccc;
}
```

The first rule selects every paragraph by its element name. The second selects every element whose class list contains `warning`. The third selects the single element whose `id` is `site-footer`. A class selector is written with a leading full stop, and an `id` selector with a leading hash sign; forgetting the sign is a common cause of rules that never apply.

When two rules set the same property on the same element, the more specific one wins. An `id` selector is more specific than a class selector, and a class selector is more specific than an element selector. That ordering is the reason styling is normally done with classes: a class is easy to override later, while an `id` rule is stubborn and tends to be defeated only by adding more rules rather than by editing the right one.

### 3.3 Building a table in five steps

Step 1. Write the `table` element and put a `caption` immediately inside it. The caption names the table for a reader who cannot see it.

Step 2. Write the header row as the first `tr`, using `th` cells and a `scope` attribute on each. If the header row is long, wrap it in `thead` so that a printed page can repeat it.

Step 3. Write one `tr` per record, with one `td` per value, in the same order as the header row.

Step 4. If a cell must cover several columns or rows, add `colspan` or `rowspan` to it and remove the cells it replaces from the rows below or beside it.

Step 5. Move alignment and borders into CSS. Set `border-collapse: collapse` on the table so that neighbouring borders become one line, add padding to the cells so the text does not touch the border, and align numbers to the right.

```css
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #999;
  padding: 8px 12px;
}

th {
  background-color: #eef;
  text-align: left;
}
```

### 3.4 Merging cells without breaking the grid

Before typing `colspan` or `rowspan`, count the columns in the header row. That number is the width of the grid, and it never changes.

Then, for every row, add up the spans declared in that row and add the number of spaces already taken by a cell that started in an earlier row. The total must equal the width of the grid. If a row totals less, the browser invents an empty cell at the end; if a row totals more, the browser pushes the extra cell onto a new row. In both cases the visible result is a table that looks subtly wrong in a way that is hard to trace, which is why the count is worth doing by hand.

A second habit helps: draw the grid on paper first, marking the merged rectangle, and only then write the rows. Merging is much easier to reason about as a picture of occupied squares than as a list of tags.

### 3.5 Building a form in six steps

Step 1. Write the `form` element with an `action` naming the program that will receive the answers, and a `method` chosen from the comparison in the next subsection.

Step 2. Group related controls with `fieldset` and give each group a `legend`. A long form with no groups is tiring to complete and impossible to describe to a screen reader user.

Step 3. For each control, write a `label` whose `for` attribute equals the control's `id`, then write the control with a `name` attribute. The `name` is what the server receives; without it, the value is discarded silently.

Step 4. Choose the control type that matches the answer: one line of text, a masked secret, a single choice from several, any number of independent choices, a long comment, or a choice from a list.

Step 5. Add a submit control, and a reset control only if clearing the form is genuinely useful, because a reset destroys everything the visitor has typed.

Step 6. Test by submitting, then inspect what actually arrived. Look at the address bar for a `get` form, and at the request details in the browser's network panel for a `post` form.

### 3.6 Choosing between `get` and `post`

The choice is not a matter of taste. It follows from what the submission does to the server and from whether the visitor might want to repeat or share the result.

| Property | `get` | `post` |
|---|---|---|
| Where the values appear | Appended to the address as a query string | In the body of the request |
| Visible to an onlooker | Yes, in the address bar and in browser history | No, not in the address |
| Can be bookmarked | Yes, the address holds the whole request | No, the address alone is not the request |
| Safe to repeat | Yes, it is meant for retrieval | No, repeating may create a duplicate record |
| Suitable for passwords | No | Yes, and always with a secure connection |
| Suitable for file uploads | No | Yes, with the multipart encoding |
| Practical size limit | Small, because addresses are limited | Large, set by the server configuration |

The rule of thumb that covers every examination question: use `get` when the submission only asks for information, and use `post` when it changes something or carries something private.

### 3.7 Testing a layout in the browser

Testing a page is not the same as reading its source. Three checks catch almost every mistake in this topic.

First, check the rendered page: does each block element start on a new line, and does each inline fragment stay inside its sentence?

Second, right-click the thing that looks wrong and choose the option that inspects it. The inspector shows the element the browser actually built, which may differ from what you typed if you nested something illegally.

Third, submit the form and look at what left the browser. For a `get` form the address bar shows the query string, which makes missing `name` attributes obvious: a control with no name contributes nothing, so the pair simply is not there.

## 4. Worked Implementation from the Notes

### 4.1 Task: a two-column page skeleton built from generic containers

### 4.2 Implementation: one `div` per region, one `span` for a highlighted word

Step 1. Write the two regions as block containers, each with a class, and put a paragraph in each.

```html
<div class="layout">
  <div class="main-column">
    <h1>Student portal</h1>
    <p>The <span class="highlight">registration deadline</span> is Friday.</p>
  </div>
  <div class="side-column">
    <h2>Notices</h2>
    <p>Library closes at six.</p>
  </div>
</div>
```

Step 2. Explain the structure. The outer `div` groups the two columns. The inner `div` elements are block-level, so each begins on its own line, one below the other, before any styling is applied. The `span` inside the paragraph is inline, so it takes only the width of the phrase and does not break the sentence. Nothing here has meaning beyond grouping, so `div` and `span` are the correct choices.

Step 3. Place the two columns side by side with CSS, using a grid on the outer container.

```css
.layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

.highlight {
  background-color: #ffd;
  font-weight: bold;
}
```

Step 4. State what the result demonstrates. The grid declaration changes the arrangement of the outer container's children only; it does not change what the elements mean, and it does not change their nesting. The `span` still sits inside a paragraph and still cannot contain a paragraph of its own.

Step 5. Confirm the display behaviour by predicting before you look. If the `grid` line is removed, the two columns stack; if `display: inline` were forced onto the `span` in an experiment, it would still not be allowed to hold block content.

### 4.3 Task: a grade table with a merged summary row

### 4.4 Implementation: caption, header row with scopes, data rows, and a `colspan` footer

Step 1. Count the columns first. The header names four things: student, subject, score and grade. The grid is four columns wide.

Step 2. Write the table with a caption and a header row.

```html
<table>
  <caption>Semester one results</caption>
  <thead>
    <tr>
      <th scope="col">Student</th>
      <th scope="col">Subject</th>
      <th scope="col">Score</th>
      <th scope="col">Grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>Mathematics</td>
      <td>78</td>
      <td>A</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>Science</td>
      <td>65</td>
      <td>B</td>
    </tr>
    <tr>
      <td colspan="4">Average score: 71.5</td>
    </tr>
  </tbody>
</table>
```

Step 3. Verify the count row by row. The header row declares one plus one plus one plus one, which is four. The first data row declares four. The second data row declares four. The summary row declares a single cell spanning four. Every row accounts for four columns, so no invented cells and no overflow.

Step 4. Explain why the summary row declares only one cell. A cell spanning four columns has already taken the four spaces, so writing three more cells would force the browser to start a fifth column or wrap the extras onto a new row. The declaration is one cell, not five.

Step 5. Add the styling that turns the grid into a readable table: collapsed borders, padding, a tinted header, and right-aligned scores.

```css
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #999;
  padding: 8px 12px;
}

th {
  background-color: #eef;
  text-align: left;
}

td:nth-child(3) {
  text-align: right;
}
```

Step 6. Interpret the outcome. Borders touch instead of doubling because the table has collapsed its border model, text no longer touches the cell edge because of the padding, and the scores line up on the right so that magnitudes are comparable at a glance.

### 4.5 Task: an enrolment form with every control type studied

### 4.6 Implementation: labelled controls, a radio group, a checkbox, a list and two buttons

Step 1. Write the form element with a `post` method, because the form creates a record rather than retrieving one.

```html
<form action="/enrol" method="post">
  <fieldset>
    <legend>Applicant</legend>
    <p>
      <label for="full-name">Full name</label>
      <input type="text" id="full-name" name="full_name" required="required">
    </p>
    <p>
      <label for="pin">Password</label>
      <input type="password" id="pin" name="pin">
    </p>
  </fieldset>
  <fieldset>
    <legend>Study mode</legend>
    <p>
      <input type="radio" id="mode-full" name="mode" value="full_time" checked="checked">
      <label for="mode-full">Full time</label>
      <input type="radio" id="mode-part" name="mode" value="part_time">
      <label for="mode-part">Part time</label>
    </p>
    <p>
      <input type="checkbox" id="newsletter" name="newsletter" value="yes">
      <label for="newsletter">Send me the newsletter</label>
    </p>
  </fieldset>
  <p>
    <label for="campus">Campus</label>
    <select id="campus" name="campus">
      <option value="main">Main campus</option>
      <option value="north" selected="selected">North campus</option>
    </select>
  </p>
  <p>
    <label for="comments">Anything we should know</label>
    <textarea id="comments" name="comments" rows="4" cols="40"></textarea>
  </p>
  <p>
    <input type="submit" value="Send application">
    <input type="reset" value="Clear form">
  </p>
</form>
```

Step 2. Show why the radio buttons work as a group. Both carry the same `name`, `mode`, and different `value` attributes. The browser therefore treats them as one control that can hold a single value, and the form will send either `mode=full_time` or `mode=part_time`, never both.

Step 3. Show why the checkbox is different. It has its own name, `newsletter`, so it is independent of the radio group. Ticked, it sends `newsletter=yes`; unticked, it sends nothing at all. That absence is not a bug, and it explains why a server program must treat a missing checkbox as "no".

Step 4. Point out the `name` and `id` division of labour. The `id` values let each `label` point at its control with `for`, so clicking the words works and a screen reader can name the field. The `name` values are what travel to the server. A control with an `id` but no `name` is beautifully labelled and sends nothing.

Step 5. Explain the two buttons. The submit control triggers the submission and, because it has no `name`, adds nothing to the data. The reset control restores every control to the state declared in the markup, so the name field empties, the password field empties, the first radio button is chosen again and the checkbox is unticked. It sends nothing to the server.

Step 6. Contrast the same form with `method="get"`. The address would then contain `full_name=Alice&mode=full_time&campus=north`, which puts a password in the browser history, in the server logs and in any shared link. That single observation is the reason the form uses `post`.

### 4.7 Task: assemble a complete page from every element studied

### 4.8 Implementation: semantic regions holding a table, a form and a styled panel

Step 1. Write the document skeleton with the required declarations, so that the page declares its character encoding and its language.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Student portal</title>
  <link rel="stylesheet" href="portal.css">
</head>
<body>
  <header>
    <h1>Student portal</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#results">Results</a></li>
      <li><a href="#enrol">Enrolment</a></li>
    </ul>
  </nav>
  <main>
    <section id="results">
      <h2>Results</h2>
      <table>
        <caption>Semester one results</caption>
        <thead>
          <tr>
            <th scope="col">Student</th>
            <th scope="col">Subject</th>
            <th scope="col">Grade</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Alice</td>
            <td>Mathematics</td>
            <td>A</td>
          </tr>
          <tr>
            <td>Bob</td>
            <td>Science</td>
            <td>B</td>
          </tr>
        </tbody>
      </table>
    </section>
    <section id="enrol">
      <h2>Enrolment</h2>
      <form action="/enrol" method="post">
        <p>
          <label for="portal-name">Full name</label>
          <input type="text" id="portal-name" name="full_name" required="required">
        </p>
        <p>
          <input type="submit" value="Enrol">
        </p>
      </form>
    </section>
  </main>
  <aside>
    <h2>Notice</h2>
    <p>The <span class="highlight">deadline</span> is Friday.</p>
  </aside>
  <footer>
    <p>Student services, 2026.</p>
  </footer>
</body>
</html>
```

Step 2. Check the nesting at every level. `header` contains a heading, which is legal. `nav` contains a list, which contains list items, which contain links, all legal. `main` contains two sections, each with a heading and either a table or a form. The form contains paragraphs, and each paragraph contains a label, an input and text, all of which are inline content. The `span` in the aside sits inside a paragraph and holds text only.

Step 3. Verify the table count again. Three header cells, and three cells in each data row, so the grid is three wide throughout and needs no spanning at all.

Step 4. Add the layout rules that give the page its regions shape.

```css
body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
}

header,
nav,
main,
aside,
footer {
  padding: 16px 24px;
}

header {
  background-color: #234;
  color: #fff;
}

nav ul {
  display: flex;
  gap: 16px;
  list-style: none;
  padding: 0;
}

main {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 24px;
}
```

Step 5. Confirm the behaviour that matters. The regions stack in document order because they are block-level. The list inside the navigation becomes a horizontal row only because of the flex declaration; remove it and the items stack, which is the inline-versus-block distinction in miniature, since a list item is block-level by default.

Step 6. Test the page. Click each navigation link and confirm the browser jumps to the matching `id`. Submit the form with the name blank and confirm the browser refuses, because of the `required` attribute. Then submit with a name and confirm in the network panel that the value travelled in the request body rather than in the address.

## 5. Testing, Interpretation, and Common Errors

### 5.1 How to check that you understand the topic

You have understood this topic when you can do all of the following without looking anything up.

- State the default display behaviour of a `div`, a `span`, a `p`, a table cell and a link, and predict which of them will start a new line.
- Explain, using the words block and inline, why a paragraph cannot contain a division.
- Choose between `div` and `span` for five described situations, and between a `class` and an `id` for five more.
- Name the five table elements studied, say what each contributes, and explain why `caption` comes first.
- Take a four-column table with one merged cell and write the rows correctly, accounting for every column in every row.
- Name every attribute a form needs, and say what happens to a control that has no `name`.
- Justify `get` or `post` for a search box, a login box, a feedback survey and a file upload.
- Describe the difference between a checkbox and a radio button in one sentence each.

### 5.2 Beginner misconceptions

These are the errors that appear most often in first attempts, each paired with the correction.

**Misconception: a `div` is the right container for everything.** It is the right container when nothing more specific applies. A page top is a `header`, a link list is a `nav`, the unique content is `main`. Using `div` everywhere produces markup that is harder to style, harder to script and invisible to assistive technology.

**Misconception: `span` and `div` differ only in name.** They differ in display behaviour. A `div` starts a new line and fills the width; a `span` stays in the sentence and takes only the width of its text. The same CSS rule applied to both produces visibly different layouts.

**Misconception: any element can go inside any other element.** Containers have content models. A paragraph may hold only inline content, so a division inside a paragraph is invalid even though the page may still appear to render.

**Misconception: `id` is just a class that you use once.** An `id` is a document-wide unique identifier with its own jobs: it is a jump target for links, it is what `getElementById` finds, and it is what a `label` points at with `for`. A class cannot do those jobs.

**Misconception: two elements may share an `id` if they look the same.** They may not. The document becomes invalid, and every feature that looks up an `id` silently finds only the first one.

**Misconception: `class` names on one element must be joined by commas.** They are separated by spaces. A comma makes one class name that contains a comma, which no sensible selector will match.

**Misconception: the `border` attribute on a table is the modern way to draw borders.** It is a presentational leftover. Borders belong in CSS, where you can also collapse them so that shared edges are drawn once.

**Misconception: `cellpadding` and `cellspacing` are the same thing.** Padding is the space between a cell's border and its text, inside the cell. Spacing is the gap between neighbouring cells, outside them. The modern equivalents are `padding` on the cells and `border-spacing` on the table.

**Misconception: a merged cell needs a matching empty cell beside it.** It does not. The span already occupies the space, so the following rows simply declare fewer cells. Writing an extra empty cell pushes the row wider and is the most common table bug in this topic.

**Misconception: `colspan` counts the cells that follow it.** It counts columns covered, starting from the cell itself. A cell spanning three columns is one cell that replaces three.

**Misconception: `name` and `id` on a form control do the same job.** The `id` links the control to its label and to scripts. The `name` is the key sent to the server. A control with no `name` is not submitted at all.

**Misconception: a password field encrypts the password.** It only masks the characters on screen. Protection in transit comes from a secure connection, and protection at rest comes from the server hashing what it stores.

**Misconception: radio buttons with different names form a group.** They form a group only when they share one `name`. With different names, each button is its own independent control and several can be selected at once, which defeats the purpose.

**Misconception: `get` and `post` are interchangeable.** They differ in where the data travels, whether the request can safely be repeated, whether it can be bookmarked, and how much data can be sent. A login form sent with `get` exposes the password in the address bar.

**Misconception: `textarea` takes its starting text from a `value` attribute.** It takes it from the text between its opening and closing tags, and that text is not a void element, so the closing tag is mandatory.

**Misconception: a reset button clears the server's record.** It only restores the form on screen to the values declared in the markup. Nothing is sent anywhere.

### 5.3 Reading a broken layout

When a page looks wrong, the symptom usually names the cause.

If two things that should sit side by side are stacked, one of them is block-level and needs an explicit layout rule, or an inline element has been given a width it cannot honour.

If a container's styling seems to leak into unrelated content, an `id` has been duplicated or a selector is broader than intended.

If a table has an extra empty column on the right, some row declares fewer cells than the header row. If a table has one row pushed sideways, a row declares more cells than the grid is wide.

If a form submits nothing, the controls have `id` attributes but no `name` attributes. If a form submits a password in the address bar, the method is `get`.

### 5.4 Key takeaways

Layout is decided by display behaviour before it is decided by any style rule. A block element stands alone and takes the available width; an inline element joins the line and takes only what it needs. Containers inherit that behaviour, so `div` groups blocks and `span` marks fragments. Labels let you reach a container from a style sheet or a script, with `id` reserved for the one and only and `class` used for the many. Tables are grids declared row by row, where every row must account for every column, and merging is a subtraction rather than an addition. Forms are sheets with a destination and a delivery method, and every control needs a name to be posted and a label to be understood.
