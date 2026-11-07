## 1. Concept and Use Case

### 1.1 What this topic is examined for

Every question on this topic is testing one of five competences, and recognising which one is being tested is most of the work.

The first is **classification**: given an element, state its default display behaviour and the consequences of that behaviour. The command words are "state", "identify" and "give the default".

The second is **diagnosis**: given markup, say what is wrong with it and why the browser behaves as it does. The command words are "explain why", "identify the error" and "state the effect".

The third is **construction**: given a described data set or a described form, write the markup. The command word is "write" or "construct", and the marking is against a list of required elements and required attributes.

The fourth is **comparison**: set two things side by side and justify a choice for a stated requirement. This is where `get` against `post` and `class` against `id` are examined, and where a bald definition earns less than a justified recommendation.

The fifth is **calculation**: account for columns in a table with spans, or count the pairs a form will submit. The arithmetic is trivial and the mark is lost through carelessness, not difficulty.

### 1.2 The scope, reduced to one page

The topic contains eight examinable areas, and they connect in a way worth holding in mind during revision.

Display semantics decide whether an element occupies its own line or flows inside one, and therefore decide whether width, height and vertical margins take effect. Nesting rules follow from display behaviour and from the content models attached to element names. The two generic containers, `div` and `span`, exist at the block and inline levels respectively, and they carry no meaning of their own. The two naming attributes, `class` and `id`, are the hooks that style sheets, scripts, links and labels use to reach elements.

Tables then apply block structure to rectangular data: a caption, a head, a body, rows, header cells and data cells, with spanning to express values that apply to several columns or rows. Forms apply block structure to collection: a target, a method, and a set of named controls whose values are collected into a single submission.

The last area, the complete semantic layout, is where the examiner checks whether you can place all of it in one coherent document with regions, headings, a table and a form, without any of the earlier errors.

### 1.3 Where the marks sit

Marks are not distributed evenly, and the pattern is stable across papers.

| Area | Typical weight | Usual command word | Where marks are lost |
|---|---|---|---|
| Block against inline | Six to ten | Explain, compare | Naming the behaviour without stating its consequence |
| Nesting legality | Four to six | Identify the error, explain | Describing the visual symptom without naming the content model |
| `div` and `span` | Two to four | State the difference, choose | Saying only that one is block-level and the other inline |
| `class` and `id` | Four to six | Distinguish, justify | Missing the uniqueness rule or the linking role of `id` |
| Table architecture | Four to eight | Write the markup | Omitting the caption or the header cells |
| Spanning | Four to eight | Complete the table, count the columns | Forgetting that a spanned cell replaces cells |
| Forms and methods | Six to ten | Compare, justify | Listing differences without saying which requirement selects which method |
| Controls | Four to eight | Write the form, name the value sent | Confusing the roles of `name` and `id` |

### 1.4 The question stems you will meet

Six stems account for almost every question set on this material.

"State three differences between block-level and inline elements." A three-mark question that wants three separate behaviours, each with its consequence.

"Explain why the following markup does not produce the expected layout." A diagnosis question, marked for naming the rule violated and for describing what the browser does instead.

"Write the HTML for a table that shows the following data, merging the cells that repeat." A construction question, marked for the container, the caption, the header cells, the row count and the span arithmetic.

"Distinguish between the `class` and `id` attributes, and state one use of each." A comparison question with a compulsory example.

"Compare `get` and `post`, and state which is appropriate for the described form, with a reason." A comparison plus a recommendation, and the reason carries a mark of its own.

"Design a page containing a header, navigation, a data table and a form, using appropriate elements." A synthesis question marked against a checklist of required elements and required attributes.

### 1.5 The vocabulary that earns marks

Certain words signal that the answer is technical rather than descriptive. Using them precisely is worth more than writing at length.

**Default display behaviour** is the value in the user agent style sheet, not a value you chose.

**Content model** is the set of categories an element may contain. Saying "the content model of `p` is phrasing content" earns a mark that "you cannot put that there" does not.

**Block formatting context** is the layout context in which block boxes stack vertically.

**Line box** is the box that contains a run of inline content on one line.

**Unique identifier** is the precise description of `id`, and the word "unique" is usually one of the marks.

**Successful control** is the standard term for a control whose value is included in a submission. It is the precise answer to "which values are sent".

**Query string** is the part of the address after the question mark; **message body** is the part of the request after the headers. These two terms carry the `get` against `post` answer.

**Occupied slot** is the way to describe a grid position covered by a span, and using it makes the counting question auditable.

### 1.6 The scenarios the questions are built from

Examiners rarely invent abstract questions; they wrap them in a scenario, and the scenario tells you which facts to bring.

A **student records system** produces tables with a merged header and a merged summary row, and questions about which cell should carry `scope`.

A **login page** produces the question about `post`, password fields and the absence of encryption in the field itself.

A **product listing** produces the question about `colspan` in a header and `rowspan` for a repeated category.

A **navigation bar** produces the question about why `span` is the wrong container for a horizontal menu.

A **registration form** produces the question about radio groups, checkboxes, `name` attributes and the reset button.

A **news page layout** produces the question about `div` against `header`, `nav`, `main`, `aside` and `footer`.

## 2. Data, Syntax, and Core Concepts

### 2.1 High-yield facts and what each is worth

The following facts are the currency of this topic. Each is written as a claim precise enough to be marked, followed by the mark value it typically carries.

A block-level element starts on a new line and occupies the full available width unless a width is set. **Two marks**, one for the new line and one for the width.

An inline element flows within a line of text, occupies only the width of its content, and does not accept `width` or `height`. **Three marks**, one per clause.

Vertical margins do not apply to a non-replaced inline element, and vertical padding on an inline element paints without increasing the line box height. **Two marks**, and this is the discriminating fact that separates a good answer from a memorised one.

The content model of `p` is phrasing content, so a block-level element such as `div` may not be nested inside it. **Two marks**.

The content model of `span` is phrasing content, so it may contain text and inline elements only. **One mark**.

`div` is a generic block-level container with no semantic meaning; `span` is the generic inline container with no semantic meaning. **Two marks**, one for each definition, and a third if the absence of semantics is stated as the reason they are generic.

`id` must be unique within a document and may not contain whitespace. **Two marks**, one for uniqueness and one for the no-space rule.

`id` is used as a fragment target for links, as the lookup key for `getElementById`, and as the association target for `label for`. **Three marks**, one per use.

`class` may be shared by many elements, and one element may carry several class values separated by spaces. **Two marks**.

An identifier selector outranks a class selector, which outranks a type selector. **One mark** for the ordering, occasionally two when an example is required.

A table must contain a caption as its first child, and every row must account for the same number of columns. **Two marks**.

`th` marks a header cell and accepts `scope`; `td` marks a data cell. **Two marks**, one for each definition, and a third when the accessibility purpose of `scope` is given.

`colspan` sets how many columns a cell covers, and `rowspan` sets how many rows it covers; both default to one. **Two marks**.

`border`, `cellpadding` and `cellspacing` are presentational attributes replaced in modern practice by `border`, `padding` and `border-spacing` in CSS. **Three marks**, one per replacement.

`cellpadding` is the space between a cell's border and its content; `cellspacing` is the gap between adjacent cells. **Two marks**, and reversing them is the single most common error in the table section.

A form requires an `action` naming the target and a `method` naming the technique; the method defaults to `get`. **Two marks**.

`get` places the data in the query string of the address and is limited in practice by address length; `post` places the data in the message body and carries no architectural size limit. **Two marks**.

A control without a `name` attribute is not submitted. **One mark**, and frequently the whole difference between a correct and an incorrect form.

An unchecked checkbox submits nothing, and a group of radio buttons shares one `name` so that only one value is sent. **Two marks**.

A password field masks the characters on screen but does not encrypt them. **One mark**.

A reset control restores the form to its declared values and submits nothing. **One mark**.

### 2.2 Display semantics, stated for the mark scheme

The block and inline distinction is examined through its consequences, and the consequences come in a fixed order. Learn them in that order and the answer writes itself.

The first consequence is line placement. A block-level box is placed on a line of its own; an inline-level box is placed inside a line box with the surrounding text.

The second is width resolution. A block-level box with `width: auto` resolves its width against the containing block, so it fills the available space; an inline-level box is as wide as its content and ignores a declared width.

The third is vertical geometry. A block-level box accepts height, and its vertical margins participate in margin collapsing with its neighbours; an inline-level box ignores height, ignores vertical margins, and its vertical padding does not change the line box height.

The fourth is nesting capacity. A block-level container may hold block-level and inline-level content; an inline container may hold only inline content.

The fifth is the exception that must not be forgotten. An inline element that is replaced, such as an input control or an image, does accept width and height, because the browser draws an object with an intrinsic size rather than laying out child content. And an element with `display: inline-block` is inline on the outside and block on the inside, so it accepts width and height while remaining in the line.

### 2.3 Nesting facts, stated for the mark scheme

A nesting question is marked for naming the correct content model and for stating the parser's response.

The content model of `p` is phrasing content. The parser closes an open paragraph when it encounters a start tag for `div`, `p`, `ul`, `ol`, `table`, `form`, `section`, `article`, `header`, `footer`, `nav` or `blockquote`. The consequence is that the offending element becomes a sibling of the paragraph, and the trailing text becomes a new paragraph.

The content model of `span` is phrasing content. A `span` containing a `div` is invalid, and the parser's repair produces a tree in which the division is no longer inside the span.

The content model of a list is one or more list items. A paragraph placed directly inside a `ul` is invalid, and the parser moves it outside the list.

The content model of a table begins with an optional caption, then optional column groups, then an optional head, then body rows, then an optional foot. A cell placed directly inside a table acquires anonymous row and row-group boxes, which is why the page can look plausible while the markup is wrong.

The content model of a form may not include another form. The parser terminates the outer form when it meets a nested one, which is why a form inside a table cell usually breaks the page.

Changing `display` in CSS never changes a content model, because content models are checked against element names during parsing. This sentence is worth memorising verbatim; it answers a recurring two-mark part.

### 2.4 `div` and `span`, stated for the mark scheme

`div` is a generic block-level container. It is used to group flow content that belongs together, to give that group a single box for layout, and to provide a hook for styling or scripting. It has no semantic meaning, which is both its strength and the reason a page built only from divisions is inaccessible.

`span` is a generic inline container. It is used to give a run of phrasing content a single box, a class or an identifier, so that a fragment inside a sentence can be styled or selected. It also has no semantic meaning.

The distinction is asked in three forms. "State the difference" wants block against inline, with the width consequence. "Give an example of each" wants a grouping of paragraphs for `div` and a highlighted word for `span`. "Why is `div` preferred for layout and `span` for text" wants the statement that containers should match the display level of their content.

A four-mark answer adds the semantic replacements, because the current standard prefers a named element where one exists: `header`, `nav`, `main`, `section`, `article`, `aside` and `footer` for regions, and `strong`, `em` and `code` for text-level meaning.

### 2.5 `class` and `id`, stated for the mark scheme

| Property | `id` | `class` |
|---|---|---|
| Number per document | Exactly one element | Any number of elements |
| Number per element | At most one value | Any number of space-separated values |
| Whitespace in value | Not permitted | Not permitted inside a single token |
| Reusable across pages | Possible but discouraged | Yes, this is the normal use |
| Selector syntax | Hash sign followed by the value | Full stop followed by the value |
| Specificity weight | Higher than any number of classes | Lower than any identifier |
| Link target | Yes, through the fragment form of a link | No |
| Direct script lookup | Yes, `getElementById` | No, a collection lookup is required |
| Label association | Yes, through `label for` | No |
| Styling role | Discouraged as a primary hook | The recommended primary hook |

Four facts about this pair are examined more than the rest.

The uniqueness rule is absolute: an identifier value may appear once per document. Duplicates are a conformance error, and every lookup that uses the value silently resolves to the first element in tree order.

`id` is the only attribute that can serve as a fragment target for a link, which is why "jump to section" links require identifiers.

`class` is a token set, so `class="panel panel-wide"` gives the element membership of two families, and a rule for either family applies.

Specificity makes identifiers a poor styling hook: an identifier rule cannot be overridden by a class rule, so styling with identifiers leads to escalating selectors.

### 2.6 Table facts, stated for the mark scheme

The elements and their roles are examined as a matched list.

- `table` declares the grid.
- `caption` names the table and must be its first child.
- `thead` groups the header rows so they can repeat on a printed page.
- `tbody` groups body rows, and more than one body is permitted.
- `tfoot` groups the footer rows and must follow the body.
- `tr` declares a row and may contain only cells.
- `th` declares a header cell and accepts `scope` and `abbr`.
- `td` declares a data cell.
- `colgroup` and `col` group columns for styling, with `span` on `col`.

Cell alignment is examined as a CSS question. `text-align` handles horizontal alignment with `left`, `right`, `center` and `justify`; `vertical-align` handles vertical alignment with `top`, `middle`, `bottom` and `baseline`. The default is bold and centred for `th`, plain and left aligned for `td`, both from the user agent style sheet.

The convention worth stating in a design answer is that text is left aligned, numbers are right aligned so that digits align by place value, headers are centred or left aligned consistently with their column, and vertical alignment is `top` so that a multi-line cell does not displace the values beside it.

### 2.7 Span arithmetic, stated for the mark scheme

The rule is one sentence: a spanning cell is declared once, at the position where it starts, and the slots it covers are simply not declared again.

The arithmetic has three parts, and showing all three is what earns full marks on a counting question.

The first part is the grid width, taken from the header row and constant for the table. The second part is the sum, for each row, of the `colspan` values of the cells declared in that row. The third part is the addition of the slots in that row already occupied by a `rowspan` that began above. The three must agree with the grid width for every row.

A worked instance makes the rule concrete. In a four-column timetable, a cell with `rowspan="2"` declared in the second row removes one slot from the third row, so the third row declares three cells rather than four. A cell with `colspan="2"` declared in the second row covers two columns there, so the second row declares three cells rather than four. Neither span changes the grid width, which remains four.

Two values need a note. `rowspan="0"` means the cell extends to the end of its row group and is valid; `colspan="0"` is not valid in the current standard.

### 2.8 Form facts, stated for the mark scheme

A form is defined by three attributes and one content rule.

`action` is the target address, defaulting to the current document. `method` is `get` or `post`, defaulting to `get`. `enctype` is the encoding, defaulting to `application/x-www-form-urlencoded`, with `multipart/form-data` required for file uploads. The content rule is that a form may not contain another form.

The submission collects successful controls, which are controls that have a `name`, are not disabled, and are either not a checkbox or radio button or are checked, and are not a button other than the one used to submit. Each successful control contributes one name-value pair; a select with `multiple` contributes one pair per selected option.

The four attributes that are confused with one another are examined as a set. `name` is the key sent to the server. `id` is the local identity used by labels and scripts. `value` is the data sent for that control. `placeholder` is a hint shown in an empty field and is never sent.

### 2.9 `get` against `post`, stated for the mark scheme

| Feature | `get` | `post` |
|---|---|---|
| Location of data | Query string in the request address | Body of the request message |
| Visibility | Visible in the address bar | Not visible in the address |
| History and bookmarks | Retained with the data | Address retained without the data |
| Caching | Permitted by default | Not cached by default |
| Repetition | Safe, produces the same result | Unsafe, may repeat an effect |
| Size | Limited by address length | Limited only by server configuration |
| Encoding of files | Not possible | Possible with the multipart encoding |
| Suitability for secrets | Unsuitable | Suitable, over a secure connection |
| Typical use | Search, filtering, pagination | Login, registration, payment, upload |

The mark scheme for a comparison question usually awards one mark per matched pair of differences, up to a stated maximum, and then one mark for a justified recommendation. A recommendation without a reason scores the comparison marks and loses the justification mark, which is a needless loss.

### 2.10 Controls, stated for the mark scheme

| Control | Markup | Value submitted |
|---|---|---|
| Single-line text | `input type="text"` | The text entered |
| Masked text | `input type="password"` | The text entered, unmasked in transit |
| Independent switch | `input type="checkbox"` | The `value` when checked, nothing when unchecked |
| Single choice in a group | `input type="radio"` | The `value` of the checked member of the named group |
| Submission trigger | `input type="submit"` | Its own name and value, only when it triggered submission |
| Restore defaults | `input type="reset"` | Nothing |
| Multi-line text | `textarea` | The text content between the tags |
| Choice list | `select` with `option` children | The `value` of each selected option, or its text if no value is given |
| Grouping | `fieldset` with `legend` | Nothing; both are structural |
| Caption for a control | `label` with `for` | Nothing; it names the control for users and assistive technology |

Three control facts are worth separate memorisation because they are examined as one-mark parts. A `textarea` takes its initial text from its content, not from a `value` attribute, and it is not a void element. A group of radio buttons is defined by a shared `name`, not by proximity or by a shared class. A control hidden with `display: none` is still submitted, because it is not disabled; hiding is a visual operation and disabling is a submission operation.

### 2.11 Definitions worth a mark each

**Element.** A node in the document tree defined by a start tag and an end tag, with content between them.

**Void element.** An element that cannot have content and therefore has no end tag, such as `input`, `br` or `meta`.

**Attribute.** A name-value pair written inside a start tag that modifies the element.

**Global attribute.** An attribute permitted on every element, which is the category that `class` and `id` belong to.

**Content model.** The set of content categories an element is permitted to contain.

**Phrasing content.** The category of text-level content, including spans, links, emphasis and form controls.

**Flow content.** The category of everything permitted in the body, including block-level structures.

**Semantic element.** An element whose name states its role, such as `nav` or `caption`, as opposed to a generic container whose name states only its display behaviour.

**Landmark.** A region of a page announced to assistive technology so that a user can jump to it, produced by `header`, `nav`, `main`, `aside` and `footer`.

### 2.12 Counts and defaults worth memorising

Six heading levels exist. A table has one caption at most. A row may declare any number of cells provided the totals agree. A form has one action and one method. A radio group has one shared name. A select may be multiple or single, and single by default. The default method is `get`. The default encoding is `application/x-www-form-urlencoded`. The default `colspan` and `rowspan` are both one. The default display of `div` is block, of `span` is inline, of `li` is list-item, of `th` and `td` is table-cell, and of `input` is inline-block.

Those defaults are the answer to a surprising number of short questions, and they cost almost nothing to learn.

## 3. Methods and Operations

### 3.1 The six question shapes and how each is marked

**Shape one: list differences.** A three-mark or four-mark question wants one sentence per difference, each naming a behaviour and its effect. Write them as separate numbered points, never as one long paragraph, because a marker looking for three separate ideas will not hunt for the second inside the first.

**Shape two: diagnose the markup.** The marks are for the rule that was broken and for the browser's response. A diagnosis that says only "it looks wrong" scores nothing, and a diagnosis that names the content model and describes the parser's repair scores fully.

**Shape three: construct the markup.** The marks are attached to elements and attributes, not to elegance. A table without a caption loses its caption mark however tidy it is; a form control without a `name` loses its submission mark however well labelled it is.

**Shape four: compare and recommend.** The comparison marks come in pairs, and the recommendation mark requires the requirement to be named. "Use `post` because it is safer" is weak; "use `post` because the submission creates a record and repeats would duplicate it, and because the password must not appear in the address" is complete.

**Shape five: count.** Show the arithmetic per row. Even when the answer is right, a bare number can lose the method mark on a question that says "show your working".

**Shape six: design a page.** Marked against a checklist. Work through the checklist deliberately: document type, language, encoding, title, regions, a single main, heading order, a table with a caption and scoped headers, a form with a method and labelled controls, and styling separated into a style sheet.

### 3.2 Recipe cards

**Recipe for a display comparison.** State the block behaviour in three clauses: new line, full available width, accepts height and vertical margins. State the inline behaviour in the matching three clauses: flows in the line, content width only, ignores height and vertical margins. Add the nesting consequence and one example of each. Add the caveat that `display` can change the visual behaviour without changing the content model.

**Recipe for a nesting diagnosis.** Name the parent, name its content model, name the child and its category, state that the child is not permitted, then state the parser's action and the resulting tree, then state the visible consequence.

**Recipe for a table.** Column count first, then caption, then head with scoped headers, then body rows, then spans declared once at their start, then a per-row count, then the CSS for borders and alignment.

**Recipe for a form.** Purpose, then method with its justification, then action, then fieldsets with legends, then for each control the type, the `name`, the `id` and the `label`, then the submit control, then a statement of what will be submitted.

**Recipe for a naming answer.** Uniqueness for `id`, multiplicity for `class`, selector syntax, specificity, three uses of `id`, two uses of `class`, and the recommendation to style with classes and identify with identifiers.

### 3.3 The trap table

This table lists the statements that appear in weak answers, together with the correction that earns the mark. Read it the night before the examination.

| Tempting statement | Why it is wrong | What to write instead |
|---|---|---|
| A `div` may be placed anywhere because it has no meaning | It has no meaning, but it is flow content and `p` accepts only phrasing content | A `div` may not be inside a `p`; the parser closes the paragraph first |
| A `span` can hold a `div` if it is styled as a block | Content models are checked against element names, not display values | A `span` may contain phrasing content only |
| Two elements may share an `id` if they are styled the same | Identifiers must be unique; lookups return only the first | Use one identifier per element and a class for shared styling |
| `class` and `id` are interchangeable | `id` is unique and is the only fragment and lookup target | `id` identifies one element; `class` labels a family |
| `colspan="2"` means the next two cells are merged | It means this cell covers two columns | The cell covers two columns, and the cells it replaces are not declared |
| A rowspan requires an empty cell below it | The span already occupies the slot | The covered row simply declares one fewer cell |
| `cellpadding` sets the gap between cells | Padding is inside the cell; spacing is between cells | `cellpadding` is internal, `cellspacing` is external |
| The `border` attribute is the modern way to draw rules | It is obsolete; CSS replaces it | Use `border` in CSS with `border-collapse: collapse` |
| `get` is limited to 255 characters by HTTP | HTTP defines no such limit; browser and server limits differ | `get` is limited in practice by address length limits |
| `get` and `post` are both acceptable for a login | `get` writes the password into the address and history | A login must use `post` over a secure connection |
| A password field encrypts what is typed | It masks the characters on screen only | The field masks display; transport protection needs a secure connection |
| An unchecked checkbox sends the value `false` | Unchecked controls are not successful and send nothing | Nothing is submitted for an unchecked checkbox |
| Radio buttons in the same area form a group | The group is defined by a shared `name`, and only that | Radios share one `name` to form one group |
| `name` and `id` on a control do the same job | `name` is the submitted key; `id` is the local identity | `name` submits, `id` labels and scripts |
| A reset button clears the server record | It restores the form on screen and submits nothing | Reset restores declared values locally |
| A control hidden with `display: none` is not submitted | It is still successful because it is not disabled | Only the `disabled` attribute removes a control from submission |
| An inline element cannot have padding | Horizontal padding applies; vertical padding paints without growing the line | Vertical padding on an inline box overlaps adjacent lines |
| Tables may be used to lay out a page | It breaks reading order and cannot reflow | Use grid or flex for layout and reserve tables for data |
| A `table` cell may be placed directly inside `table` | It is invalid and acquires anonymous row and group boxes | Rows must be declared explicitly with `tr` |
| `section` is the correct wrapper for any styled block | `section` is a thematic grouping and needs a name | Use `div` for grouping without meaning |

### 3.4 Laying out a comparison answer

A comparison earns marks in pairs, and the pairing is visible to the marker only when the answer is structured.

Use one of two layouts. The first is a two-column list of matched statements: one line for the first item, the immediately following line for the corresponding behaviour of the second. The second is a table with the criterion in the first column and the two items in the next two. Both make the pairing explicit; a prose paragraph usually hides it.

Never write two consecutive paragraphs, one describing the first item in full and the other describing the second. The marker then has to match them up, and unmatched statements are where marks disappear.

Finish with a short recommendation paragraph that names the requirement, names the choice, and gives the reason. One sentence is enough: because the submission changes stored data and carries a password, `post` is required.

### 3.5 Answering an invalidity question

An invalidity question nearly always reads "explain why the following markup is invalid" or "explain why the page does not display as intended". Both want the same four sentences in the same order.

Sentence one names the parent and its content model. Sentence two names the child and its category. Sentence three states that the child is not permitted, and therefore that the nesting is invalid. Sentence four states what the parser does, which is to close the open parent and insert the child as a sibling, and what the visible result is.

For the paragraph and division case, the four sentences are: a paragraph's content model is phrasing content; a division is flow content and not phrasing content; the division may not therefore appear inside the paragraph; the parser closes the paragraph when it sees the division, so the division becomes a sibling and the trailing text becomes a new paragraph.

Adding that CSS cannot repair this, because `display` does not change a content model, is usually a fifth mark on a longer question.

### 3.6 Answering the counting question

Three lines earn the method mark.

Line one states the grid width, taken from the row with the most declared slots or from the header row. Line two gives the per-row total, counting each `colspan` as its width and adding the slots already occupied by row spans from above. Line three states that every total equals the grid width.

Then state the consequence of a mismatch, because a question that asks you to count usually also asks what happens if the count is wrong: fewer slots produce anonymous empty cells at the end of the row, and more slots push the surplus onto a new row.

### 3.7 Budgeting words per mark

A written answer under examination conditions should give roughly one sentence per mark for a recall question, and roughly two sentences per mark for an explanation question. A ten-mark comparison therefore needs about ten to fifteen sentences, which is a page of handwriting rather than three.

Two budgeting errors are common. The first is writing a long definition when the question asked for three differences, which leaves no time for the third difference. The second is writing nothing for a construction question because the markup feels too long, when a correct five-line table would have earned most of the marks.

Divide the time in proportion to the marks. If a section carries twenty marks and the section lasts thirty-six minutes, each mark is worth under two minutes, and a four-mark part should take about seven minutes including reading.

## 4. Worked Implementation from the Notes

### 4.1 Task: a ten-mark question on block-level and inline elements

Question: "Compare block-level and inline elements, stating three differences and explaining how each affects the layout of a page. (10 marks)"

### 4.2 Implementation: model answer as six numbered steps

Step 1. Define the block behaviour. A block-level element is one whose default display value is block, so it begins on a new line and occupies the full width of its containing block unless a width is set. **2 marks**, one for the new line and one for the width.

Step 2. Define the inline behaviour. An inline element has a default display value of inline, so it flows inside a line of text and occupies only the width of its content. **2 marks**, one for the flow and one for the content width.

Step 3. Give the first difference with its consequence. A block element accepts `width` and `height`, so a declared size is honoured, and its vertical margins separate it from its neighbours; an inline element ignores `width` and `height` and ignores vertical margins, so its size is decided by its text. **2 marks**.

Step 4. Give the second difference with its consequence. A block element's vertical margins collapse with its neighbours, so two stacked panels with 24-pixel margins are separated by 24 rather than 48; an inline element's vertical padding paints outside the line box without increasing its height, so generous padding overlaps adjacent lines. **1 mark**.

Step 5. Give the third difference with its consequence. A block container may hold both block-level and inline content, so a division may contain paragraphs and spans; an inline container may hold only phrasing content, so a span may not contain a paragraph or a division. **2 marks**.

Step 6. Close with the qualifying statement. The display value can be changed, since `display: inline-block` makes an element accept width and height while remaining in the line, and since `display: block` on a span makes it occupy its own line; however, changing display never changes the content model, so an illegally nested element remains illegal. **1 mark**.

The steps total ten marks. The answer names three differences, attaches a layout consequence to each, and closes with the qualification that distinguishes a full-mark answer.

### 4.3 Task: an eight-mark question requiring a table with a merged header and a merged footer

Question: "Write the HTML for a table showing unit results by department for semester one, with a merged heading over the unit and pass columns and a merged summary row. (8 marks)"

### 4.4 Implementation: model answer built from the column count

Step 1. Fix the column count before writing any markup. The table needs a department, two semester columns and a total, so the grid is four columns wide. **1 mark** for a stated column count.

Step 2. Write the table with a caption. **2 marks**, one for the `table` element and one for the `caption`.

Step 3. Write the head with the merged heading. The department header and the total header each span two rows, and the semester heading spans two columns. **2 marks**, one for `rowspan` and one for `colspan`, and both must be declared in the correct row.

```html
<table>
  <caption>Unit results by department, semester one</caption>
  <thead>
    <tr>
      <th scope="col" rowspan="2">Department</th>
      <th scope="colgroup" colspan="2">Semester 1</th>
      <th scope="col" rowspan="2">Total</th>
    </tr>
    <tr>
      <th scope="col">Units</th>
      <th scope="col">Passes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Computing</th>
      <td>12</td>
      <td>10</td>
      <td>22</td>
    </tr>
    <tr>
      <td colspan="3">Institution total</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
```

Step 4. Verify the arithmetic row by row. The first head row declares one, two and one, which is four. The second head row declares two cells and inherits two occupied slots from the row spans above, which is four. The first body row declares four single cells. The summary row declares a cell spanning three columns plus one cell, which is four. **1 mark** for the verification.

Step 5. Add the styling that replaces the presentational attributes. **1 mark** for collapsed borders and cell padding.

```css
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #778;
  padding: 8px 12px;
}

th {
  background-color: #eef;
  text-align: left;
}

td {
  text-align: right;
}
```

Step 6. State what the markup demonstrates. The two `rowspan="2"` declarations remove one slot from the second head row, which is why that row declares only two cells; the `colspan="2"` on the semester heading covers the unit and pass columns; and the summary row's `colspan="3"` plus one cell completes the four-column grid. **1 mark** for the explanation.

The steps total eight marks.

### 4.5 Task: an eight-mark question comparing `get` and `post` for a stated form

Question: "A college needs a form that lets applicants submit their details to create a student record. Compare `get` and `post` and recommend a method, justifying your choice. (8 marks)"

### 4.6 Implementation: model answer as matched pairs plus a recommendation

Step 1. State where the data travels in each case. With `get`, the name-value pairs are appended to the target address as a query string. With `post`, the pairs form the body of the request message. **2 marks**, one per method.

Step 2. State the visibility consequence. Data sent with `get` appears in the address bar, in the browser history, in bookmarks and in the server's access log; data sent with `post` does not appear in the address, so it is absent from the history and the log. **2 marks**.

Step 3. State the repetition consequence. A `get` request is safe and idempotent, so repeating it produces the same result and caching or prefetching is harmless. A `post` request may create a second record if it is repeated, which is why the browser warns before re-sending one. **2 marks**.

Step 4. State the practical limit. A `get` request is limited in practice by the maximum length of an address accepted by the browser and the server, whereas a `post` body has no architectural limit, with only the server's configured limit applying. **1 mark**.

Step 5. Recommend, naming the requirement. The form creates a record and therefore changes stored data, and it carries personal details, so `post` is required. **1 mark** for the recommendation with a reason.

Step 6. Add the operational detail that shows understanding. The form should also declare `action` naming the receiving program and should be served over a secure connection, because `post` prevents the values from appearing in the address but does not encrypt the message on its own. The scoring is complete at eight marks; this sentence protects the recommendation mark when the examiner looks for a reason rather than a slogan.

### 4.7 Task: a six-mark question distinguishing `class` and `id`

Question: "Distinguish between the `class` and `id` attributes and state one use of each. (6 marks)"

### 4.8 Implementation: model answer as definition, mechanism, use

Step 1. Define `id`. An `id` assigns a unique identifier to one element; the value may appear only once in a document and may not contain whitespace. **2 marks**, one for uniqueness and one for the no-whitespace rule.

Step 2. Define `class`. A `class` assigns one or more reusable labels to an element; the same value may be used on any number of elements, and one element may carry several values separated by spaces. **1 mark**.

Step 3. Contrast the mechanisms. An identifier is selected with a hash sign and a class with a full stop, and an identifier selector carries greater specificity than a class selector, so identifier rules are hard to override. **1 mark**.

Step 4. Give the use of `id`. An `id` is the target of a fragment link, the lookup key for `getElementById`, and the association target for a `label` element's `for` attribute. **1 mark**.

Step 5. Give the use of `class`. A `class` is the normal hook for a style rule that applies to a family of elements, and it is what `querySelectorAll` and the class-list operations manipulate. **1 mark**.

Step 6. State the working recommendation. Identify with `id` and style with `class`, because an identifier is unique by definition and because its specificity makes it a brittle styling hook. The six marks are already secure at step 5; this closing sentence is the difference between a correct answer and one that reads as understood.

### 4.9 Task: a twelve-mark design question

Question: "Write the HTML for a page containing a header, a navigation bar, a section of tabular results and a form for enrolling, using appropriate elements. Include the document preamble. (12 marks)"

### 4.10 Implementation: model answer as a checklist walked in order

Step 1. Write the preamble. The document type declaration, the `html` element with a language, and a head containing the character encoding, the viewport declaration, a title and a style sheet link. **2 marks**, one for the document type and one for the encoding and title.

Step 2. Write the page regions in reading order. A `header` with the page heading, a `nav` with a list of links, a `main` containing the sections, and a `footer` with the closing information. **3 marks**, one per region correctly chosen.

Step 3. Order the headings without skipping a level. The page heading is `h1` and each section heading is `h2`. **1 mark**.

Step 4. Write the results as a data table with a caption and scoped header cells. **3 marks**, one for the caption, one for `th` with `scope`, and one for a grid in which every row accounts for the same number of columns.

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
  <header>
    <h1>Department of Computing</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#results">Results</a></li>
      <li><a href="#enrol">Enrol</a></li>
    </ul>
  </nav>
  <main>
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
        </tbody>
      </table>
    </section>
    <section id="enrol">
      <h2>Enrolment</h2>
      <form action="/enrol" method="post">
        <fieldset>
          <legend>Applicant</legend>
          <p>
            <label for="full-name">Full name</label>
            <input type="text" id="full-name" name="full_name" required="required">
          </p>
        </fieldset>
        <p>
          <input type="radio" id="mode-full" name="mode" value="full_time" checked="checked">
          <label for="mode-full">Full time</label>
        </p>
        <p>
          <input type="submit" value="Submit application">
        </p>
      </form>
    </section>
  </main>
  <footer>
    <p>Student services, 2026.</p>
  </footer>
</body>
</html>
```

Step 5. Check the form attributes. The `action` names the receiving program, the `method` is `post` because a record is created, every data control has a `name` so that it is submitted, and every data control has an `id` matched by a `label`. **2 marks**, one for the method with its justification and one for the labelled, named controls.

Step 6. Check the separation of structure from presentation. All appearance belongs in the linked style sheet, and no presentational attribute appears on the table. **1 mark**.

Step 7. Self-check the whole answer against the question. Header, navigation, results section, enrolment section, form, preamble and styling are all present; the table has a caption and scoped headers; the grid is three columns wide in every row; the form creates rather than retrieves. The steps total twelve marks.

## 5. Testing, Interpretation, and Common Errors

### 5.1 What the marker rewards

Four habits separate the upper band from the middle, and none of them requires extra knowledge.

Name the mechanism rather than the symptom. "The parser closes the paragraph" scores; "it looks broken" does not.

Attach a consequence to every claim. "Inline elements ignore width" is half an answer; "inline elements ignore width, so a highlighted phrase cannot be given a fixed width without changing its display" is the whole one.

Use the standard vocabulary. Content model, successful control, query string, message body, unique identifier, block formatting context, line box. Each of those terms is a compressed mark.

Answer the question that was asked. If the question asks for three differences, give exactly three, numbered, and stop. A fourth difference costs time and earns nothing.

### 5.2 Time strategy

Allocate by marks, not by enthusiasm. A reasonable plan for a thirty-six minute section carrying twenty marks is forty seconds per mark for reading and planning, then ninety seconds per mark for writing, with the final three minutes reserved for checking the markup questions.

Spend the first minute of each question writing the required elements as a list in the margin. For a table question that list is the column count, the caption, the head, the body and the spans. For a form question it is the method, the action, the fieldsets, the names and the labels. Working from a list prevents the omission that costs a mark for a one-line addition.

Leave construction questions until after the written ones if time is short, because a partially written table earns proportionally more per minute than a partially written essay.

If a question says "show your working", write the arithmetic even when the answer is obvious. A correct total with no method commonly scores half.

### 5.3 Revision checklist

Work through this list and tick only what you can do without notes.

- State the default display value of `div`, `span`, `p`, `li`, `th`, `td` and `input`.
- State the three layout consequences of the inline display value.
- Define content model, phrasing content and flow content.
- Explain why a `div` cannot sit inside a `p`, naming both the content model and the parser behaviour.
- Explain why changing `display` cannot repair illegal nesting.
- Define `div` and `span` and give one use of each.
- State the uniqueness rule for `id` and the no-whitespace rule.
- List three uses of `id` that a class cannot perform.
- State the specificity ordering of identifier, class and type selectors.
- Name the four parts of a table and the role of `caption`.
- State the difference between `cellpadding` and `cellspacing` and give both modern replacements.
- Explain the border-collapse models and when `border-spacing` applies.
- State what `colspan` and `rowspan` count, and the special meaning of `rowspan="0"`.
- Perform the per-row column count for a table with two spans.
- Name the three form attributes and the default of each.
- Define a successful control and list three reasons a control is not successful.
- Give four differences between `get` and `post` with the consequence of each.
- State the value submitted by a checkbox, a radio group, a select and a submit button.
- State the difference between `name`, `id`, `value` and `placeholder`.
- Name the semantic regions and the heading order rule.

### 5.4 Traps to re-read the night before

The five that cost the most marks, in order.

First, the omission of `name` on a form control. It is invisible in the rendered page and fatal to the submission.

Second, the reversal of `cellpadding` and `cellspacing`. Padding is inside the cell; spacing is between cells.

Third, the assumption that a spanned cell needs a companion empty cell. It does not, and adding one breaks the grid.

Fourth, the belief that an identifier may repeat. It may not, and duplicates silently disable every lookup after the first.

Fifth, the use of `get` for anything that changes data or carries a secret. The address bar is public, persistent and logged.

### 5.5 Rapid self-test

Answer each in one sentence, then check against the sections above.

What happens to a division written inside a paragraph, and why? Which attribute makes a form control's value reach the server? Which attribute makes a label clickable? Why does vertical padding on a span overlap the line above? For a table whose header row declares four cells, how many cells does a body row declare if one of them spans two columns? Which method should a file upload use, and which encoding? Which is more specific, `.panel` or `#panel`? What does a reset button send? Which two elements make a labelled group of controls? What is the difference between `tfoot` placement in the current standard and in older markup?

The answers are, in order: it becomes a sibling of the paragraph because the parser closes the open paragraph, since `p` accepts only phrasing content; `name`; `for`, matched to the control's identifier; because vertical padding on an inline box does not increase the line box height; three, because the cell that spans two columns covers two of the four slots and the other two cells cover the remaining two; `post` with the multipart encoding; the identifier; nothing; `fieldset` with `legend`; and the foot must follow the body in the current standard, whereas older markup allowed it before.

### 5.6 The last word

This topic rewards precision more than length. A candidate who writes four short sentences naming the content model, the parser behaviour, the resulting tree and the visible consequence will beat a candidate who writes two paragraphs describing how the page looks. Learn the vocabulary, attach a consequence to every claim, count the columns every time, and check that every control has a name.