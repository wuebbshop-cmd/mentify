## 1. Concept and Use Case

### 1.1 Display is a layout contract, not a decoration

Every element in a document generates one or more boxes, and every box takes part in a formatting context that decides how it is positioned relative to its neighbours. The `display` property states which kind of box is generated, and the value used when the author writes nothing comes from the user agent stylesheet. Because that value is attached to the element name, choosing an element is choosing a layout strategy. A `div` is not merely "a thing you can style"; it is a promise that the element will participate in block layout, that it will start on a new line, and that its width will resolve against its containing block unless overridden.

Three outer display behaviours matter for this topic. An element with a block-level outer display participates in a block formatting context: it is placed on a line of its own, and vertical stacking is the only arrangement available unless an ancestor introduces flex or grid layout. An element with an inline-level outer display participates in an inline formatting context: it is placed inside a line box, flows with the text, and may be split across several lines. An element with `display: none` generates no box at all and therefore affects nothing.

There is also a hybrid that appears in this topic because it is the honest answer to "I want this fragment to accept a width": `display: inline-block` generates an inline-level box whose interior is a block container, so the box sits in a line yet honours width and height.

### 1.2 The browser's sequence, and why the order matters

The order in which a browser processes a document explains nearly every confusing behaviour in this topic.

The first stage is parsing. The markup is tokenised and assembled into a tree of objects, the Document Object Model. This stage includes error recovery, and error recovery is not passive: the parser inserts missing elements, closes elements that cannot contain what follows, and moves content. A `div` written inside a `p` is not stored as written; the parser closes the paragraph first, then appends the division as a sibling. Nothing you write in CSS can undo that, because the tree was already rebuilt before any style was considered.

The second stage is box generation. Each node in the tree generates a principal box according to its computed `display`, and the layout engine inserts anonymous boxes where a table or a block container needs an intermediate wrapper it was not given. A `td` placed directly inside a `table` acquires an anonymous table row and an anonymous row group, which is why the page can look acceptable while the markup is wrong.

The third stage is layout. Block-level boxes are stacked and their widths resolved; inline content is broken into line boxes; tables are laid out on a grid derived from the maximum number of columns in any row; floats and out-of-flow boxes are placed.

The fourth stage is painting. Colours, borders and backgrounds are drawn in the order defined by the stacking rules.

The practical conclusion is stated once and used throughout the rest of this note: nesting legality is decided at the first stage and layout behaviour at the third, so a styling fix can never repair an illegal nesting, while a nesting choice always constrains the styling that follows.

### 1.3 The three contracts this topic is really about

The elements in this topic are governed by three separate contracts, and examination questions are usually testing one of them.

The **display contract** says whether an element generates a block-level or an inline-level box by default. It determines whether content starts on a new line, whether width and height apply, and whether vertical margins have any effect.

The **structure contract** is the content model of each element: which categories of content it may contain. A paragraph may contain only phrasing content, so it may not contain a division, a list, or a table. A list may contain only list items, so a stray paragraph inside a `ul` is invalid. A table has a prescribed order of children.

The **naming contract** governs the two global attributes used as hooks. An `id` names exactly one element in the document. A `class` names a set of elements. The first is an identity, the second is a membership.

Tables and forms then add local contracts of their own: a table's cells must form a rectangle, and a form's controls must each carry a name before their values can be submitted.

### 1.4 Where the rigour pays

Four situations in ordinary development make the difference between a page that works and a page that needs to be rewritten.

Choosing a container for navigation. A navigation strip built from `span` elements with a link inside each cannot be given a height, cannot be given vertical padding that pushes other content away, and cannot be laid out as a set of buttons without changing `display`. The same strip built from list items, or from a flex container of links, behaves predictably.

Choosing between a division and a region element. The choice is invisible on screen and highly visible to assistive technology, to search engines, and to the next developer. A page of nested divisions with class names describing their appearance carries no structure; the same page with `header`, `nav`, `main` and `footer` gives a screen reader user a landmark list and a way to skip repeated content.

Using a table for layout. A layout table imposes a reading order that follows the grid rather than the content, so a screen reader reads cell by cell across a design that has no tabular meaning. It also refuses to reflow sensibly at narrow widths, because a grid with a fixed column count cannot become a single column without abandoning the grid.

Choosing a form method. A search form sent with `post` cannot be bookmarked and cannot be refreshed without a warning; a login form sent with `get` writes the credentials into the address bar, the browser history, and the server's access log.

### 1.5 The eight subtopics, mapped to the contracts

The material divides cleanly, and the division is worth carrying into revision.

| Subtopic | Contract it belongs to | Practical consequence |
|---|---|---|
| Block versus inline display semantics | Display | Predicts new lines, width resolution and margin behaviour |
| Nesting rules that follow | Structure | Decides which markup the parser accepts unaltered |
| `div` and `span` | Display plus structure | Generic grouping at block and inline level |
| `class` and `id` | Naming | Reachability from CSS, scripts and links |
| Table architecture | Structure | Rectangular data with captions and headers |
| Table attributes and spanning | Structure plus layout | Grid geometry and border rendering |
| Form architecture and methods | Protocol | Where values travel and whether repetition is safe |
| Controls | Protocol plus accessibility | Which values are successful and how they are named |

### 1.6 The one-sentence statement of the topic

HTML layout containers, tables and forms are three applications of one idea: the element you choose fixes the box the browser generates, the content model fixes what may legally sit inside it, and the attributes you add fix how style sheets, scripts and servers can reach it.

## 2. Data, Syntax, and Core Concepts

### 2.1 The CSS box model, stated precisely

Every box has four concentric regions. The **content box** holds the text, the image, or the child boxes. The **padding box** surrounds the content box with the element's own background. The **border box** surrounds the padding with a border. The **margin box** surrounds the border with transparent space that separates the element from its neighbours.

By default, the `width` and `height` properties set the content box, which is the behaviour named `box-sizing: content-box`. The space an element occupies horizontally is therefore the sum of its content width, its left and right padding, its left and right border, and its left and right margin. Setting `box-sizing: border-box` makes `width` include padding and border, which is why many style sheets begin with a universal reset to that value.

Two details are easy to miss and are examined often. Percentage padding resolves against the **width** of the containing block, including for `padding-top` and `padding-bottom`, not against its height. And margins never accept the element's own background, so a margin is always transparent, whereas padding is painted with the element's background.

```css
.card {
  box-sizing: border-box;
  width: 320px;
  padding: 16px;
  border: 2px solid #345;
  margin: 12px;
}
```

The rule above produces a border box of 320 pixels, because `border-box` makes the declared width include padding and border, and with 24 pixels of horizontal margin its footprint in a row is 344 pixels. Without the `border-box` declaration, the content width would remain 320 while padding and border were added outside it, giving a border box of 356 pixels and a row footprint of 380.

### 2.2 Block box geometry

A block-level, non-replaced element in normal flow is laid out by a single constraint: the sum of its horizontal margin, border, padding and width must equal the width of its containing block. The layout engine resolves whichever of those values is `auto`.

When `width` is `auto`, which is the initial value, the used width is whatever remains after margins, borders and padding are subtracted. That is why a `div` with no width fills the available space, and why adding a border to it does not make it overflow: the content shrinks to compensate.

When `width` is specified and the sum exceeds the containing block, the box overflows if the margins were specified, because over-constrained values are resolved by ignoring the right margin in left-to-right writing modes.

Vertical geometry is different. A block box's height is `auto` by default, which means it is exactly tall enough to contain its in-flow children. Padding and border add to that height. Adjacent vertical margins between sibling block boxes collapse: instead of adding, the larger of the two margins is used, and if one is negative the result is the sum of the largest positive and the most negative. Margin collapsing is suppressed inside flex containers, grid containers, and any box that establishes a new block formatting context, such as one with `overflow: hidden` or `display: flow-root`.

```css
.panel {
  margin-top: 24px;
  margin-bottom: 24px;
}

.panel + .panel {
  margin-top: 24px;
}
```

Two consecutive panels in the rule above are separated by 24 pixels, not 48, because their adjoining margins collapse. A student who measures the gap and expects 48 has discovered the single most commonly examined consequence of block layout.

### 2.3 Inline box geometry

An inline-level, non-replaced box behaves under different rules, and the differences are all consequences of one fact: an inline box lives inside a line box whose height is decided by the line, not by the element.

`width` and `height` do not apply to a non-replaced inline box. Setting them has no effect at all; the box is as wide as its content and as tall as the font's content area. Horizontal `margin-left`, `margin-right`, `padding-left`, `padding-right` and horizontal borders do apply, and they push the neighbouring content along the line. Vertical padding and vertical borders are painted but do not change the height of the line box, so they overlap the lines above and below. Vertical margins do not apply at all.

The height of a line box is determined by the `line-height` of the inline boxes in it and by the strut, the invisible zero-width inline box that carries the block container's font and line height. This is why `line-height` is the correct tool for spacing lines of text and why adding `margin-top` to a `span` never moves anything.

An inline box that reaches the end of a line is split into fragments. Horizontal margins, borders and padding are applied at the start of the first fragment and the end of the last fragment only, so a wrapped inline element does not acquire padding at every line break.

```css
.mark {
  background-color: #ffd;
  padding: 6px 2px;
  margin-top: 30px;
  width: 400px;
}

p {
  line-height: 1.5;
}
```

In the rule above, the 30-pixel top margin is ignored, the 400-pixel width is ignored, and the six-pixel vertical padding paints outside the line box and can overlap the previous line. The background makes the overlap visible, which is exactly why inline elements are unsuitable for boxes that must push other content away.

### 2.4 Replaced inline elements and `inline-block`

An image, an input control, a select list, a text area and a button are replaced elements: the browser draws something with an intrinsic size rather than laying out child content. A replaced inline element honours `width` and `height`, and it contributes its margin box to the line box height. This is why a text field can sit in a sentence at a sensible size while a `span` beside it cannot be given one.

`display: inline-block` produces a box that participates in inline layout on the outside and contains block layout on the inside. It accepts width and height, keeps its children in normal block flow, and sits on the baseline of the line unless `vertical-align` says otherwise. It was the standard technique for horizontal navigation before flexbox, and it survives because it answers a genuinely awkward requirement: a fragment that must flow with text yet behave like a box.

```css
.badge {
  display: inline-block;
  min-width: 48px;
  padding: 4px 8px;
  border-radius: 4px;
  background-color: #234;
  color: #fff;
  text-align: center;
}
```

Modern layout has absorbed most of the legitimate uses of `inline-block`. A row of navigation links is a flex container; a page divided into regions is a grid container; a card with a fixed width in a text flow is still well served by `inline-block`.

### 2.5 Content models: flow content and phrasing content

The HTML standard groups elements into categories and states, for each element, which categories it may contain. Two categories carry this topic.

**Flow content** is the broad category of everything that may appear in the body of a document: divisions, paragraphs, headings, lists, tables, forms, and the semantic region elements.

**Phrasing content** is the narrower category of text-level content: spans, links, emphasis, code fragments, images, and the form controls.

The rules that follow are direct consequences. An element whose content model is flow content may contain phrasing content, because every phrasing element is also flow content. An element whose content model is phrasing content may contain only phrasing content. A `div` is flow content; a `span` is phrasing content; a `p` is flow content whose content model is phrasing content; a `li` is flow content whose content model is flow content.

```html
<ul>
  <li>A list item may contain a paragraph.
    <p>Like this one.</p>
  </li>
</ul>
```

The example above is legal. The paragraph is inside the list item, and the list item accepts flow content. The reverse, a paragraph directly inside a `ul`, is not legal: a list accepts only list items and script-supporting elements, so the parser will move the paragraph outside the list.

### 2.6 Why a `div` cannot legally sit inside a `p`

This is the question that separates memorised answers from understood ones, and it has three layers.

The first layer is the content model. The `p` element's content model is phrasing content, and `div` is flow content that is not phrasing content. Writing a division inside a paragraph therefore violates the specification at the point where the element is declared, regardless of how it looks.

The second layer is the parser. When the tokeniser meets a start tag for `div` while a `p` element is open, the tree construction stage runs a rule that closes the open paragraph before inserting the division. The set of tags that trigger this behaviour includes `div`, `p`, `ul`, `ol`, `table`, `form`, `section`, `article`, `header`, `footer`, `nav` and `blockquote`. The result is that the source you typed and the tree the browser builds are different documents.

```html
<p>First sentence.
<div>A division that was written inside the paragraph.</div>
Second sentence.</p>
```

The markup above is invalid, and the browser constructs three siblings: an empty paragraph, the division, and a second paragraph containing the trailing text. The visual effect is an unexplained gap where the first paragraph should have been, and a closing `</p>` that ends a paragraph the browser had already closed.

The third layer is the styling route, and this is the trap. Adding `div { display: inline }` or `p { display: block }` does not make the nesting legal, because content models are checked against element names, not against computed display values. A division displayed inline is still a division, and it still may not appear inside a paragraph. CSS describes how boxes are drawn; it does not amend the grammar.

The correct alternatives are simple. If the intent is a block-level grouping inside a section, put the paragraph and the division side by side inside a container that accepts flow content. If the intent is to style a run of text, use a `span`, which is phrasing content and therefore legal inside a paragraph.

```html
<section>
  <p>First sentence.</p>
  <div>A division beside the paragraph, not inside it.</div>
  <p>Second sentence.</p>
</section>
```

### 2.7 `div` and `span` as transparent generic containers

Both elements are defined as having no semantics beyond their display behaviour: they represent their children, and their only purpose is to give a group a single box and a single place to hang attributes. The standard calls this being a generic container.

A `div` is therefore appropriate when a group of flow content needs one box, one class, and one position in the layout, and no existing element carries the meaning. A `span` is appropriate when a run of phrasing content needs one box so that a style or a script can reach it.

Both become inappropriate the moment a better element exists. A masthead is a `header`, a set of navigation links is a `nav`, the unique content is `main`, a self-contained composition is an `article`, a titled division of a document is a `section`, tangential content is an `aside`, and the closing information is a `footer`. A quotation is a `blockquote`, an emphasised word is `em`, a strong word is `strong`, and a fragment of code is `code`. Every one of those replacements adds meaning to the accessibility tree at no cost.

There is one caveat about `section`: it is not a generic wrapper for styling. A `section` is a thematic grouping and should normally have an accessible name, usually from a heading inside it. A page divided into anonymous blocks of styling is better served by `div`.

### 2.8 `id`: identity, uniqueness, and resolution order

The `id` attribute assigns a document-unique identifier. Three rules govern it.

The value must be unique in the document. Duplicate identifiers are a conformance error, and every consumer resolves the ambiguity in the same silent way: it uses the first element in tree order. `document.getElementById` returns that first element, fragment navigation scrolls to it, and a `label` with a matching `for` associates with it. The second element carrying the same value is unreachable by any of those mechanisms.

The value must not contain ASCII whitespace. An identifier with a space is not one identifier; the attribute value is simply invalid, and selectors referencing it must escape the space, which is a reliable sign that the value should be changed instead.

The value is matched case-sensitively in an HTML document. `#Main` and `#main` are different identifiers, and a selector written with the wrong case silently matches nothing.

The legitimate jobs of an `id` are narrow and each one is a real requirement rather than a styling convenience. It is a fragment target for a link. It is the lookup key for `getElementById`. It is the association target for `label for`, for `aria-labelledby` and `aria-describedby`, and for the `form` attribute that lets a control live outside its form element. It is the target for `headers` on a table cell. None of those can be done with a class.

Styling by identifier is legal but usually unwise. An identifier selector carries a specificity of one hundred in the familiar three-part count, which makes it hard to override from a class later, and it cannot be reused, which is the opposite of what a style sheet normally needs.

### 2.9 `class`: a token set, and the arithmetic of specificity

The `class` attribute holds a set of space-separated tokens. An element may carry many, and a token may appear on many elements. Two elements with the same tokens are members of the same family and are styled by the same rule.

Class values are matched case-sensitively in standards mode. A class whose value contains characters that are not valid in a CSS identifier, such as a slash or a leading digit, must be escaped in a selector, which is a strong argument for restricting class names to letters, digits, hyphens and underscores.

Specificity is arithmetic on three components: the number of identifier selectors, the number of class, attribute and pseudo-class selectors, and the number of type and pseudo-element selectors. A rule with one identifier outranks a rule with any number of classes. A rule with one class outranks a rule with any number of type selectors. A declaration in a `style` attribute outranks every selector, and a declaration marked `!important` outranks both.

```css
p { color: #333; }                 /* specificity 0,0,1 */
.note { color: #066; }            /* specificity 0,1,0 */
#intro { color: #900; }           /* specificity 1,0,0 */
```

A paragraph carrying `id="intro"` and `class="note"` is coloured by the third rule, because one identifier outranks one class. This is precisely why identifiers are a poor styling hook: they win arguments that the author later wants to lose.

### 2.10 Reaching elements from scripts

The naming contract exists because two consumers outside the style sheet need to find things.

The `id` route is a direct lookup: `document.getElementById("intro")` returns the element or null, in constant time. The `class` route is a collection: `document.getElementsByClassName("note")` returns a live collection, and `document.querySelectorAll(".note")` returns a static list of matches for any selector.

Mutating the class list is a first-class operation. The `classList` property exposes `add`, `remove`, `toggle` and `contains`, each of which manipulates the token set without producing doubled spaces or clobbering unrelated tokens.

```javascript
const panel = document.getElementById("intro");
panel.classList.add("is-open");
console.log(panel.classList.contains("is-open"));
```

The output is `true`. Doing the same job by assigning to `className` works only if the author remembers to preserve the tokens that were already there, which is exactly the bug `classList` exists to prevent.

### 2.11 Table architecture

A table is a rectangular structure, and the elements describe its parts rather than its appearance.

The `table` element is the container. The `caption` element names the table and must be its first child; it is not a heading placed above the table by coincidence, it is part of the table and is announced with it.

The `colgroup` and `col` elements group columns so that a rule can be applied to a whole column without repeating it in every cell. A `col` may carry a `span` attribute naming how many columns it covers.

The `thead`, `tbody` and `tfoot` elements are row groups. They exist so that a long table can repeat its header across printed pages, so that a footer can be kept with the table, and so that a script or a style sheet can address a group as a unit. A `tbody` may begin with a `tr`, and a table may contain more than one `tbody`, which is how a single table presents several blocks of records under one heading.

The `tr` element is a row, and it may contain only cells. The `th` element is a header cell and the `td` element is a data cell. A `th` accepts a `scope` attribute naming whether it labels a column, a row, a column group or a row group, and an `abbr` attribute holding a short form for a screen reader that reads the header repeatedly.

The document order of the row groups is fixed: the caption, then any column groups, then the head, then the body or bodies, then the foot. Writing the foot before the body was permitted in older versions of the language and is not permitted now.

```html
<table>
  <caption>Unit results by department</caption>
  <colgroup>
    <col>
    <col span="2">
    <col>
  </colgroup>
  <thead>
    <tr>
      <th scope="col">Department</th>
      <th scope="col">Units</th>
      <th scope="col">Passes</th>
      <th scope="col">Completion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Computing</th>
      <td>12</td>
      <td>10</td>
      <td>83 per cent</td>
    </tr>
  </tbody>
</table>
```

### 2.12 Table attributes and their replacements

Older HTML carried presentational attributes on the `table` element. They still function in browsers for compatibility, but the standard marks them as obsolete and provides CSS equivalents. Knowing both is necessary because legacy pages use the attributes and modern answers must recommend the CSS.

The `border` attribute set a border width in pixels on the table and its cells. The replacement is the `border` property applied to the table and the cells.

The `cellpadding` attribute set the space between a cell's border and its content. The replacement is the `padding` property on the `th` and `td` elements.

The `cellspacing` attribute set the gap between adjacent cells. The replacement is the `border-spacing` property on the table, which applies only in the separate borders model.

The `border-collapse` property decides which of two border models is used. In the default, `separate`, every cell draws its own four borders and `border-spacing` sets the gaps between them. In `collapse`, adjacent borders are merged into a single line and `border-spacing` is ignored, which is the model that produces the familiar ruled grid.

| Legacy attribute | Effect | Modern replacement |
|---|---|---|
| `border` | Draws a border of the given width | `border` on the table and cells |
| `cellpadding` | Space inside a cell, around its content | `padding` on `th` and `td` |
| `cellspacing` | Gap between neighbouring cells | `border-spacing` on the table |
| `width` | Table width in pixels or percent | `width` on the table |
| `align` | Horizontal placement of the table | `margin-left` and `margin-right` auto |

```css
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #8a8;
  padding: 10px 14px;
  vertical-align: top;
}

td.amount {
  text-align: right;
}
```

The rule above replaces every attribute in the comparison table at once: collapsed borders, one-pixel rules, ten pixels of internal padding, top vertical alignment, and right alignment for an amount column so that digits align on their place value.

### 2.13 `colspan` and `rowspan` as a grid computation

The two spanning attributes do not add cells; they make one cell occupy several grid slots. `colspan` states how many columns the cell covers, and `rowspan` states how many rows it covers. Both are positive integers, and one is the default. The special value zero on `rowspan` means the cell extends to the end of its row group; zero on `colspan` is not permitted.

The grid is derived from the widest row, and every row must account for exactly that width. The accounting is a small algorithm, and running it by hand is the only reliable way to avoid a broken table.

For each row, start at column one. If the current slot is already occupied by a cell that began in an earlier row, move to the next slot. Otherwise place the next declared cell at the current slot, mark its rectangle of slots as occupied, and move past its `colspan`.

Two failures follow from breaking the rule. A row that accounts for fewer slots than the grid is wide receives anonymous empty cells at the end, which appear as unexplained blank columns. A row that accounts for more slots overflows, and the extra cells are pushed onto a new row, shifting everything after them.

```html
<table>
  <caption>Weekly laboratory timetable</caption>
  <thead>
    <tr>
      <th scope="col">Period</th>
      <th scope="col">Monday</th>
      <th scope="col">Tuesday</th>
      <th scope="col">Wednesday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">09:00</th>
      <td colspan="2">Laboratory</td>
      <td>Mathematics</td>
    </tr>
    <tr>
      <th scope="row">10:00</th>
      <td>English</td>
      <td rowspan="2">Physics</td>
      <td>Art</td>
    </tr>
    <tr>
      <th scope="row">11:00</th>
      <td>History</td>
      <td>Music</td>
    </tr>
    <tr>
      <td colspan="4">Lunch, 12:00 to 13:00</td>
    </tr>
  </tbody>
</table>
```

The grid is four columns wide. Row one declares a period plus a laboratory covering Monday and Tuesday plus Mathematics, accounting for one, two and one, four in total. Row two declares a period, English, Physics covering two rows, and Art, accounting for one, one, one and one, again four. Row three declares a period, History and Music, accounting for three slots, and the fourth slot is already taken by Physics, so the row is complete. Row four declares one cell covering four columns. Every row accounts for four, so the table is sound.

### 2.14 Form architecture and the submission algorithm

A form is a set of controls plus a target and a method. The `form` element's `action` attribute holds the target address and defaults to the address of the current document. The `method` attribute names a submission technique and defaults to `get`. The `enctype` attribute names an encoding and defaults to `application/x-www-form-urlencoded`; `multipart/form-data` is required when a form uploads files, and `text/plain` exists mainly for debugging.

Submission proceeds in a fixed order. The browser collects the controls whose form owner is this form. It discards any control that is disabled, any control without a `name`, any checkbox or radio button that is not checked, any button that is not the one that triggered the submission, and any control inside a disabled `fieldset`. What remains is the set of successful controls, and only those contribute entries. Each entry is the control's name paired with its current value. The entry list is then encoded according to the `enctype`, and the encoded result is placed in the query string for `get` or in the message body for `post`.

Two consequences are examined repeatedly. A control with an `id` but no `name` is perfectly labelled and completely absent from the submission. A control that is disabled is absent, so a script that disables a field while waiting must also be aware that its value will not be sent.

### 2.15 The precise difference between `get` and `post`

The two methods differ in the shape of the request, in the guarantees that follow from that shape, and in what a repeat submission means.

With `get`, the encoded entry list replaces the query component of the target address, and the browser issues a request whose request line contains the whole address and whose body is empty. Because the entire request is in the address, it can be bookmarked, copied into a message, cached, and found in the server's access log. Because it is in the address, it is also limited in practice by browser and server limits on address length, and it is visible to anyone who can see the screen, the history, or the log.

With `post`, the encoded entry list is the body of the request message, and the target address stays unchanged. The body is not part of the address, so it is not bookmarked, not stored in history, and not written to access logs by default. HTTP imposes no architectural limit on the size of a body, though servers impose their own. A `post` request is not safe to repeat blindly, because repeating it may create a second record, so browsers warn before re-sending one.

The protocol vocabulary matters here. A method is **safe** if it only retrieves; `get` is safe and `post` is not. A method is **idempotent** if repeating it has the same effect as performing it once; `get` is idempotent, and `post` is generally not. A form that changes state must therefore use `post`, not because `get` is insecure in itself, but because a state-changing `get` violates the guarantee that makes prefetching, caching and link sharing safe.

### 2.16 Controls and their values

Each control type produces values in a defined way, and the definitions explain most of the surprises.

A text field sends the text it contains. A password field sends the text it contains as well; the masking is a display effect only. A checkbox that is checked sends its `value`, or the string `on` if no value is given, and an unchecked checkbox sends nothing. A radio button sends its `value` when it is the checked member of its group; the group is defined by a shared `name` within a shared form owner. A submit button sends its own name and value only when it is the button that submitted the form, which is how a form with several buttons can tell which was pressed.

A text area sends its text content between the tags, not a `value` attribute, and that text may contain newlines. A select sends the value of each selected option, and a select with the `multiple` attribute may send several entries with the same name. An option without a `value` attribute sends its text content.

A file input sends the name and content of each selected file, and it functions correctly only when the encoding is `multipart/form-data` and the method is `post`.

```html
<form action="/profile" method="post" enctype="multipart/form-data">
  <p>
    <label for="avatar">Profile picture</label>
    <input type="file" id="avatar" name="avatar" accept="image/png,image/jpeg">
  </p>
  <p>
    <input type="submit" name="intent" value="Upload">
  </p>
</form>
```

## 3. Methods and Operations

### 3.1 Choosing the container

The decision procedure is short enough to apply mechanically, and applying it mechanically is the point.

Step 1. Decide the outer display behaviour required. If the group must occupy its own line, the container is block-level. If the group must sit inside a sentence or a row of inline content, it is inline-level. If the group must flow in a line yet accept a width, it is inline-level with a block interior, which means `inline-block`, or a flex item in a row container.

Step 2. Decide whether the group has a standard meaning. Header, navigation, main content, a titled section, an independent article, tangential content, and a footer all have elements. A figure with a caption has an element. A quotation has an element. If a meaning exists, use the element that carries it and add a class for the specific styling.

Step 3. Fall back to the generic container. A `div` for block-level grouping, a `span` for inline fragments. Write it only when the answer to step 2 was "no standard meaning".

Step 4. Attach the naming hook. One instance, or an identity that links target, scripts query, and labels point at: an `id`. Many instances sharing behaviour: a `class`. Both when the element needs to be both addressable and styled, as a section usually does.

Step 5. Put appearance in a style sheet keyed to the class, and keep identifiers out of selectors unless the identifier is genuinely the subject of the rule.

### 3.2 Writing nesting that survives the parser

Because the parser repairs illegal nesting silently, the only defence is to check the content model before writing the tag. The following checks cover the situations this topic creates.

Check that a paragraph contains only phrasing content. If a division, a list, a table, a form, or a section is needed inside what you were about to call a paragraph, that element is not a paragraph.

Check that a list contains only list items. Text directly inside a `ul` is invalid; it belongs inside an `li`.

Check that a `span` contains only phrasing content. A span is never the container for a block.

Check that a table contains the caption, column groups, row groups and rows in the prescribed order, and that a row contains only cells.

Check that a `form` does not contain another `form`. Nested forms are invalid and the parser will terminate the outer one.

Check that an `a` that wraps block content has a parent that accepts flow content. The transparency of `a` means it inherits its content model from its parent; a link inside a paragraph therefore may not wrap a division, while a link directly inside a section may.

### 3.3 Naming: the identifier or the class

Four tests decide the question, and a single "yes" to the first is decisive.

Is the element the target of a link, a label, an ARIA reference, or a `getElementById` call? Then it needs an `id`, because none of those mechanisms accepts a class.

Could a second element with the same name reasonably exist on this page? If yes, it must be a class, because an identifier may not repeat.

Is the name describing a role that recurs across the site, such as every price, every warning, or every table row that is selected? Then it is a class.

Is the name describing one unique region, such as the site header of this page? Then an `id` is permitted, though a class is often still preferable if the styling is shared across pages.

### 3.4 Constructing a table on a grid

Step 1. Decide the column count from the data, not from the markup. Write it down.

Step 2. Write the caption, then the header row with a `scope` on every `th`.

Step 3. Write each record as a row with exactly the column count of cells, in header order.

Step 4. Introduce a span only where a value genuinely applies to several columns or rows. Note the row and column where it starts, and delete the cells it replaces from every row it covers.

Step 5. Verify the accounting row by row, as described next.

Step 6. Style with `border-collapse`, cell padding, header emphasis, and right alignment for numeric columns.

### 3.5 Verifying a span layout by occupancy

The verification is a table of slots. For each row, list what occupies each column. A slot is filled either by a cell declared in that row or by a cell that started above and reaches down.

Run the check in three passes.

Pass one: write the number of columns declared in each row, counting each cell's `colspan` as its full width. Pass two: add the number of slots in that row already occupied by a row span from above. Pass three: confirm that the total equals the grid width for every row, with no slot filled twice.

If any row totals less than the grid, an anonymous cell will appear. If any row totals more, the surplus will be pushed to a new row. If a slot is filled twice, the second cell is displaced and the table loses its rectangularity.

### 3.6 Constructing a form

Step 1. Decide what the submission does. If it retrieves, the method is `get`; if it creates, updates or deletes, the method is `post`.

Step 2. Name the target in `action`. Name the encoding in `enctype` only when it differs from the default, which means only for file uploads.

Step 3. Group the controls with `fieldset` and `legend` so that the form has describable parts.

Step 4. For each control, choose the type, give it a `name`, give it an `id`, and give it a `label` whose `for` matches that `id`.

Step 5. Decide which controls must be filled, and express that with `required` rather than with a script where the browser can enforce it.

Step 6. Provide one submit control. Provide a reset control only when losing the entered values is acceptable.

Step 7. Submit the form and inspect the request, confirming that every intended name appears and no unintended name does.

### 3.7 Deciding between the methods

| Criterion | `get` | `post` |
|---|---|---|
| Position of the entry list | Query component of the target address | Message body |
| Visible in the address bar | Yes | No |
| Stored in browser history | Yes, with the values | Address only, without values |
| Cacheable and prefetchable | Yes | No, by default |
| Bookmarkable with its data | Yes | No |
| Safe to repeat | Yes, by definition | No, may duplicate an effect |
| Usable for file upload | No | Yes, with multipart encoding |
| Practical size ceiling | Address length limits set by browser and server | Body size limits set by the server |
| Appropriate for secrets | No | Yes, over a secure connection |

### 3.8 Building the semantic layout

Step 1. Open with the document type declaration, the `html` element with a `lang`, and a `head` carrying the character encoding, the viewport declaration, a title, and the style sheet link.

Step 2. Place the page-level regions in order: `header` for the masthead, `nav` for the primary links, `main` for the unique content, `aside` for tangential content, `footer` for the closing information.

Step 3. Inside `main`, divide by subject with `section` elements that each begin with a heading, and use `article` for content that would still make sense on its own.

Step 4. Use `div` inside those regions only for grouping that has no name of its own, such as a row of controls or a panel with a heading and a paragraph.

Step 5. Make the layout explicit with grid or flex on the region containers, and keep every visual rule in the style sheet.

Step 6. Confirm that the landmarks appear in the accessibility tree and that the heading order descends without skipping a level.

### 3.9 The verification workflow

Four instruments answer four different questions, and using the wrong one produces confident wrong answers.

A conformance checker answers "is this markup legal", reporting the nesting errors the parser silently repaired. The browser's element inspector answers "what tree did the browser build", which is where a displaced division becomes visible. The computed style panel answers "which declaration won", which resolves specificity disputes. The network panel answers "what was actually sent", which resolves form submissions.

```css
/* Applied in the browser console to confirm the resolved display value. */
.box {
  outline: 1px solid #c00;
}
```

The outline above is chosen deliberately: unlike a border, an outline does not change the box's dimensions, so it shows the box without altering the geometry being measured.

## 4. Worked Implementation from the Notes

### 4.1 Task: demonstrate the box-model consequence of block versus inline

### 4.2 Implementation: one markup pattern, three display values, three measured results

Step 1. Write three elements with identical content and identical class, so that only the display value differs.

```html
<div class="track">
  <div class="box block-demo">Alpha</div>
  <span class="box inline-demo">Beta</span>
  <span class="box inline-block-demo">Gamma</span>
</div>
```

Step 2. Apply a width, a height, padding and a margin to all three, so that any difference is attributable to display alone.

```css
.track {
  width: 600px;
  font: 16px/1.5 system-ui, sans-serif;
}

.box {
  width: 200px;
  height: 40px;
  padding: 10px;
  margin: 10px;
  border: 2px solid #345;
}

.block-demo {
  display: block;
}

.inline-demo {
  display: inline;
}

.inline-block-demo {
  display: inline-block;
}
```

Step 3. Measure each box with the browser's client rectangle and record what it reports.

```javascript
for (const element of document.querySelectorAll(".box")) {
  const rect = element.getBoundingClientRect();
  console.log(element.textContent, Math.round(rect.width), Math.round(rect.height));
}
```

```text
Alpha 224 64
Beta 57 43
Gamma 224 64
```

Step 4. Interpret the three numbers. Alpha reports 224 by 64 because the declared 200-pixel width and 40-pixel height set the content box, and the 20 pixels of horizontal padding and 4 pixels of border are added outside it under the default content-box model; the 600-pixel container only matters when `width` is `auto`. Beta reports 57 by 43 because width and height do not apply to a non-replaced inline box, so the declared 200 by 40 is ignored entirely and the rectangle is the word plus its horizontal padding and border, and the font's content area plus its vertical padding and border. Gamma reports the same 224 by 64 as Alpha, because `inline-block` accepts the width and height while the box still sits in the line.

Step 5. Confirm the vertical behaviour, which the rectangles hide. Alpha occupies its own line and pushes the next element down. Beta and Gamma sit on the same line as each other, and Beta's 20 pixels of vertical padding appear in its rectangle without increasing the line box height, so the padding paints over the neighbouring lines. That is the difference that causes inline boxes with generous padding to collide with the text above and below, and it is why `line-height` rather than padding is the tool for spacing lines.

### 4.3 Task: prove that the parser relocates a division written inside a paragraph

### 4.4 Implementation: compare the source with the constructed tree

Step 1. Write the illegal markup deliberately.

```html
<div class="track">
  <p>First sentence.
  <div>Relocated division.</div>
  Second sentence.</p>
</div>
```

Step 2. Read the tree the browser built, rather than the file that was served.

```javascript
const track = document.querySelector(".track");
for (const node of track.children) {
  console.log(node.tagName, JSON.stringify(node.textContent.trim()));
}
```

```text
P ""
DIV "Relocated division."
P "Second sentence."
```

Step 3. Interpret the output. Three siblings exist where the source described two. The parser closed the paragraph when it met the division, inserted the division as a sibling, and then created a new paragraph for the trailing text. The closing tag in the source had nothing left to close, and the stray one was discarded.

Step 4. Prove that styling cannot repair the structure. Apply a display override and observe that the tree does not change.

```css
p { display: block; }
div { display: inline; }
```

Step 5. State the conclusion precisely. The content model is a rule about element names, the parser enforces it during tree construction, and CSS operates on the tree afterwards. Changing `display` changes the box, never the parent-child relationship, so the nesting remains invalid and the empty first paragraph remains as a layout artefact.

Step 6. Write the legal equivalent, which is a container of flow content holding a paragraph, a division and a paragraph as siblings.

```html
<div class="track">
  <p>First sentence.</p>
  <div>Division beside the paragraph.</div>
  <p>Second sentence.</p>
</div>
```

### 4.5 Task: build a five-column table with one column span and two row spans

### 4.6 Implementation: occupancy accounting before writing the markup

Step 1. Fix the grid at five columns: category, product, size, price and stock.

Step 2. Plan the occupied slots. The category applies to three products, so it spans three rows. The size applies to two products, so it spans two rows. A footer note applies to the whole table, so it spans five columns.

| Row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|---|
| Header | Category | Product | Size | Price | Stock |
| 2 | Stationery, rows 2 to 4 | Notebook | A5 | 120 | 40 |
| 3 | occupied above | Pen | Standard, rows 3 to 4 | 30 | 120 |
| 4 | occupied above | Marker | occupied above | 90 | 15 |
| 5 | Note, spanning five columns | covered | covered | covered | covered |

Step 3. Write the markup from the plan, declaring each span once at its starting slot.

```html
<table>
  <caption>Stock list</caption>
  <thead>
    <tr>
      <th scope="col">Category</th>
      <th scope="col">Product</th>
      <th scope="col">Size</th>
      <th scope="col">Price</th>
      <th scope="col">Stock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="3">Stationery</th>
      <td>Notebook</td>
      <td>A5</td>
      <td>120</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Pen</td>
      <td rowspan="2">Standard</td>
      <td>30</td>
      <td>120</td>
    </tr>
    <tr>
      <td>Marker</td>
      <td>90</td>
      <td>15</td>
    </tr>
    <tr>
      <td colspan="5">Prices include tax.</td>
    </tr>
  </tbody>
</table>
```

Step 4. Verify the accounting in numbers. Row one declares five cells of one column each, five. Row two declares a category spanning three rows plus four single cells, five. Row three declares four cells plus the category already occupying column one, five. Row four declares three cells plus the category in column one and the size in column three, five. Row five declares one cell spanning five columns, five. No slot is filled twice, and every row totals five.

Step 5. Explain the `scope` choice. The category header labels a group of rows rather than a single row, which is why it carries `scope="rowgroup"`. A reader that announces the header with each cell will then repeat the correct category for all three products.

Step 6. Style the result and confirm the rules.

```css
table {
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #99a;
  padding: 8px 12px;
}

td:nth-child(n + 4) {
  text-align: right;
}
```

The numeric columns are aligned to the right so that the digits align by place value, and the collapsed border model draws shared edges once rather than twice.

### 4.7 Task: compare `get` and `post` on the wire, not in prose

### 4.8 Implementation: submit two forms and read the requests

Step 1. Write a retrieval form that uses `get`.

```html
<form action="/search" method="get">
  <p>
    <label for="query">Search</label>
    <input type="text" id="query" name="q" value="algebra">
    <input type="hidden" name="level" value="beginner">
  </p>
  <p>
    <input type="submit" value="Search">
  </p>
</form>
```

Step 2. Observe the request the browser sends. The entry list has replaced the query component of the address, and the body is empty.

```http
GET /search?q=algebra&level=beginner HTTP/1.1
Host: portal.example.org
Accept: text/html
```

Step 3. Write a creation form that uses `post`, with the default encoding.

```html
<form action="/enrol" method="post">
  <p>
    <label for="name">Full name</label>
    <input type="text" id="name" name="full_name" value="Alice Mwangi">
  </p>
  <p>
    <label for="campus-choice">Campus</label>
    <select id="campus-choice" name="campus">
      <option value="main">Main campus</option>
      <option value="north" selected="selected">North campus</option>
    </select>
  </p>
  <p>
    <input type="submit" value="Enrol">
  </p>
</form>
```

Step 4. Observe the second request. The address is unchanged, and the pairs are in the body.

```http
POST /enrol HTTP/1.1
Host: portal.example.org
Content-Type: application/x-www-form-urlencoded
Content-Length: 50

full_name=Alice+Mwangi&campus=north
```

Step 5. Read the encoding rules from the body. The space in the name became a plus sign, pairs are joined by an ampersand, and each name and value is separated by an equals sign. A character outside the plain ASCII set would be percent-encoded as its bytes, and a repeated name, as produced by a group of checkboxes, would appear once per value.

Step 6. State the operational difference the two requests prove. The first request can be pasted into a message and will reproduce the same search for anyone. The second cannot, because the address alone does not carry the data, and repeating it would create a second enrolment. This is the concrete meaning of safe and unsafe methods.

### 4.9 Task: give one element an identity and a family a reusable label

### 4.10 Implementation: one identifier, one class, two consumers

Step 1. Write an element that needs both a link target and a shared style.

```html
<section id="fees" class="panel">
  <h2>Fees</h2>
  <p class="amount">Tuition: 48,000</p>
  <p class="amount">Laboratory: 6,500</p>
</section>
```

Step 2. Reach the section from a link, which is a job only an identifier can do.

```html
<nav>
  <a href="#fees">Jump to fees</a>
</nav>
```

Step 3. Style the family with a class rule and confirm that both amounts change.

```css
.amount {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

.panel {
  border: 1px solid #ccd;
  padding: 16px;
}
```

Step 4. Reach the single section from a script, which is the second job only an identifier can do.

```javascript
const fees = document.getElementById("fees");
console.log(fees.classList.contains("panel"));
```

```text
true
```

Step 5. Explain the division of labour. The class gathers the two amounts and the panel border; the identifier gives the navigation link a destination and gives the script a constant-time lookup. Attempting the same with two classes would leave the link without a target, and duplicating the identifier would make the second copy unreachable.

Step 6. Demonstrate the specificity consequence, which is why the identifier is not used for styling.

```css
#fees .amount {
  color: #900;
}

.amount {
  color: #333;
}
```

The first rule wins for both amounts because an identifier outranks a class, and it would continue to win against any later class rule, which is the rigidity that makes identifier selectors a poor styling habit.

### 4.11 Task: assemble the complete page

### 4.12 Implementation: landmarks, a data table, a form and an explicit layout

Step 1. Write the document with its head declarations.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Department portal</title>
  <link rel="stylesheet" href="portal.css">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header>
    <h1>Department of Computing</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#results">Results</a></li>
      <li><a href="#enrol">Enrolment</a></li>
    </ul>
  </nav>
  <main id="content">
    <section id="results">
      <h2>Results</h2>
      <table>
        <caption>Unit results by department</caption>
        <thead>
          <tr>
            <th scope="col">Department</th>
            <th scope="col">Units</th>
            <th scope="col">Passes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Computing</th>
            <td>12</td>
            <td>10</td>
          </tr>
          <tr>
            <th scope="row">Mathematics</th>
            <td>9</td>
            <td>8</td>
          </tr>
        </tbody>
      </table>
    </section>
    <section id="enrol">
      <h2>Enrolment</h2>
      <form action="/enrol" method="post">
        <fieldset>
          <legend>Applicant</legend>
          <p>
            <label for="student-name">Full name</label>
            <input type="text" id="student-name" name="full_name" required="required">
          </p>
          <p>
            <label for="student-pin">Password</label>
            <input type="password" id="student-pin" name="pin" required="required">
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
        </fieldset>
        <p>
          <input type="submit" value="Submit application">
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

Step 2. Audit the structure against the content models. `header` holds a heading. `nav` holds a list of list items holding links. `main` holds two sections, each named by a heading. Each section holds either a table whose every row accounts for three columns, or a form whose controls are grouped and labelled. `aside` holds a heading and a paragraph. `footer` holds a paragraph. The only `span` contains text inside a paragraph, which is legal phrasing content.

Step 3. Give the page its layout without altering the document order.

```css
body {
  margin: 0;
  font: 16px/1.6 system-ui, sans-serif;
}

main {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 24px;
  padding: 24px;
}

nav ul {
  display: flex;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 12px 24px;
}

.skip {
  position: absolute;
  left: -9999px;
}

.skip:focus {
  left: 0;
  background-color: #ffd;
}
```

Step 4. Explain why each rule is placed where it is. The grid on `main` turns the page body into two columns without moving any element in the document, so the reading order stays masthead, navigation, results, enrolment, notice, footer. The flex row on the list makes the navigation horizontal without changing the list items from block-level elements. The skip link is moved out of view rather than removed, so it remains reachable by the keyboard.

Step 5. Verify the interactive behaviour. Tabbing from the top of the page reaches the skip link first and reveals it. Clicking a navigation link moves focus to the matching section. Submitting the form with either required field empty is refused by the browser before any request is made, which is the constraint validation built into the `required` attribute.

Step 6. Verify the submission. With both fields filled and one radio button chosen, the request body contains three pairs: the name, the password and the mode. The submit control contributes nothing, because a button without a `name` is not part of the entry list even when it is the button that triggered the submission.

## 5. Testing, Interpretation, and Common Errors

### 5.1 Validation and what it cannot tell you

A conformance checker reads the source and reports violations of the content models, duplicate identifiers, unknown attributes and unclosed elements. It is the correct instrument for the illegal-nesting class of error, because a browser will not report those: it repairs them instead.

Validation cannot tell you whether the layout is what you intended, whether a class is doing any work, or whether the form submits the right pairs. Those require the rendering engine, the computed style panel and the network panel respectively.

One limitation is worth stating because it causes false confidence. A validator judges the source as text. A browser judges the tree it builds, and the tree can differ. A page can therefore pass validation and still behave unexpectedly if a script later moves nodes, and a page can fail validation while rendering acceptably because error recovery has produced a workable tree.

### 5.2 Reading computed values correctly

Three quantities are routinely confused. The declared value is what the style sheet says. The computed value is what results after relative units are resolved. The used value is what the layout engine actually applied after resolving `auto` against the containing block.

The distinction explains a common puzzle: a block element declared with `width: 50%` reports a used width that includes no padding when `box-sizing` is `content-box`, so two such elements with padding overflow their parent even though the percentages sum to one hundred. Switching to `border-box` makes the declared width the full footprint, and the overflow disappears.

### 5.3 Errors, symptoms and corrections

| Symptom | Likely cause | Correction |
|---|---|---|
| An unexplained empty line appears before a panel | A division was written inside a paragraph and the parser split it | Move the division beside the paragraph |
| Two elements that should sit side by side are stacked | Both are block-level and no layout container arranges them | Use flex or grid on the parent |
| Setting `width` on a highlighted phrase changes nothing | The element is a non-replaced inline box | Use `inline-block`, or move the box outside the sentence |
| Vertical padding on a phrase overlaps the line above | Padding on an inline box does not grow the line box | Use `line-height`, or convert the phrase to `inline-block` |
| A style rule for a class is beaten by another rule | An identifier selector or an inline style outranks it | Lower the winning specificity rather than adding more rules |
| Only the first of two elements with the same identifier responds | Identifiers must be unique and lookups return the first | Convert the repeated identifier into a class |
| A table has a blank column on the right | One row declares fewer slots than the grid width | Count the row and supply the missing cell or span |
| A merged cell pushes a row sideways | The spanned cell was declared again in a covered row | Delete the duplicate cell from the covered row |
| Cells are separated by gaps that will not close | The separate border model is in use | Apply `border-collapse: collapse` |
| A control's value never reaches the server | The control has no `name`, or it is disabled | Add a `name` and stop disabling it during submission |
| Only one option of a radio group can be selected | Every radio in the group shares one name, by design | Use checkboxes for independent choices |
| A password appears in the address bar | The form method is `get` | Change the method to `post` and serve the page over a secure connection |
| A file upload arrives empty | The encoding was left at the default | Add `enctype="multipart/form-data"` and use `post` |
| A form inside a form behaves erratically | Nested forms are invalid and the parser closes the outer one | Move the inner form outside, or use the `form` attribute on its controls |

### 5.4 Edge cases worth knowing

A link may wrap block-level content because `a` is a transparent element: its content model is inherited from its parent. This is why a whole card can be clickable in current HTML, and why the same construct inside a paragraph is still invalid.

A `rowspan` of zero means "extend to the end of this row group". It is useful when the number of rows is not known in advance, and it is not the same as omitting the attribute, which means one row.

A `fieldset` that is disabled disables every control inside it, including controls that carry no `disabled` attribute of their own. Nothing inside will be submitted.

A `label` may associate with a control either by a matching `for` attribute or by wrapping the control. Wrapping is convenient for checkboxes and radios; the `for` form is clearer when the label and the control are separated by other markup.

An `option` without a `value` attribute submits its text content, which is convenient for short lists and a source of surprise when the visible text is translated or edited.

A `select` with `multiple` submits one entry per selected option, all with the same name, so the server must expect a list rather than a single value.

### 5.5 The invariants to memorise

Block boxes stack and resolve `auto` width against the containing block; inline boxes flow in lines and ignore width, height and vertical margins. Nesting is governed by content models, checked before any style is applied, so a paragraph can never contain a division. An `id` is one per document and is the only hook that links, labels and direct lookups accept; a `class` is many per document and is the right hook for styling. A table is a rectangle whose every row must account for the full column count, and a span replaces cells rather than adding them. A form is a set of named controls plus a target and a method, and only successful controls are submitted. `get` puts the entry list in the address and is safe to repeat; `post` puts it in the body and is not.
