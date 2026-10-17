import re


_GENERIC_TOPIC_TERMS = {
    "about", "and", "application", "applications", "basics", "course", "concept",
    "a", "about", "after", "all", "also", "an", "and", "any", "are", "as", "at",
    "basic", "basics", "be", "because", "been", "being", "both", "between", "by", "can", "course",
    "concept", "concepts", "could", "definition", "definitions", "does", "each", "economic",
    "economics", "for", "from", "has", "have", "how", "if", "in", "into", "introduction",
    "is", "it", "its", "may", "more", "most", "of", "on", "one", "or", "other", "our",
    "overview", "principle", "principles", "same", "such", "than", "that", "the", "their",
    "them", "then", "there", "these", "they", "this", "those", "through", "to", "topic",
    "understanding", "unit", "using", "was", "were", "what", "when", "which", "while", "who",
    "will", "with", "within", "would",
}
_GENERIC_TOPIC_ANCHORS = {"demand", "equilibrium", "price", "supply"}


def _tokens(text):
    tokens = []
    for raw_token in re.findall(r"[A-Za-z0-9]+", str(text or "")):
        token = raw_token.casefold()
        if len(token) <= 2 or token in _GENERIC_TOPIC_TERMS:
            continue
        if token.endswith("opolistic"):
            token = token[:-9] + "opoly"
        elif token.endswith("ies") and len(token) > 5:
            token = token[:-3] + "y"
        elif token.endswith("s") and not token.endswith(("ss", "us", "is")) and len(token) > 4:
            token = token[:-1]
        tokens.append(token)
    return tokens


def _topic_value(topic, name, default=None):
    if isinstance(topic, dict):
        return topic.get(name, default)
    return getattr(topic, name, default)


def map_pdf_topic_sections(text, topics):
    """Map PDF pages to explicitly headed syllabus sections and flag split pages."""
    page_header = re.compile(r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$")
    explicit_heading = re.compile(
        r"^\s*(?:#{1,6}\s*)?(?:(?:unit|module|chapter|topic|lesson|part|section)\s+)?"
        r"(?:(?:\d+(?:\.\d+)*)|(?:one|two|three|four|five|six|seven|eight|nine|ten|[ivxlc]+))\s*[.:)\-]?\s+(.*?)\s*$",
        re.IGNORECASE,
    )

    title_lookup = {}
    topic_distinctive_tokens = {}
    all_topic_tokens = []
    for topic in topics:
        title = str(_topic_value(topic, "title", "") or "")
        normalized = " ".join(re.findall(r"[a-z0-9]+", title.casefold()))
        if normalized and normalized not in title_lookup:
            title_lookup[normalized] = topic
        all_topic_tokens.append(set(_tokens(title)))

    for i, topic in enumerate(topics):
        unique_tokens = all_topic_tokens[i].copy()
        for j, other_tokens in enumerate(all_topic_tokens):
            if i != j:
                unique_tokens -= other_tokens
        topic_distinctive_tokens[id(topic)] = unique_tokens or all_topic_tokens[i]

    page_matches = list(page_header.finditer(str(text or "")))
    page_numbers = [int(match.group(1)) for match in page_matches]
    headings_by_page = {}
    for index, page_match in enumerate(page_matches):
        p_num = int(page_match.group(1))
        end = page_matches[index + 1].start() if index + 1 < len(page_matches) else len(text)
        page_text = str(text or "")[page_match.end():end]
        for line in page_text.splitlines():
            clean_line = line.strip()
            if not clean_line or len(clean_line) > 120 or clean_line.endswith("."):
                continue
            heading_match = explicit_heading.match(clean_line)
            heading_text = heading_match.group(1).strip() if heading_match else clean_line.lstrip("# ")
            normalized = " ".join(re.findall(r"[a-z0-9]+", heading_text.casefold()))
            is_heading = bool(
                heading_match
                or clean_line.startswith("#")
                or (clean_line.isupper() and sum(char.isalpha() for char in clean_line) >= 8)
            )
            topic = title_lookup.get(normalized) if is_heading else None
            if not topic and is_heading:
                # Check distinctive title tokens
                heading_tokens = set(_tokens(heading_text))
                for top in topics:
                    dist = topic_distinctive_tokens.get(id(top), set())
                    if dist and dist.issubset(heading_tokens):
                        topic = top
                        break
            if not topic and is_heading:
                candidate, score, margin, evidence = score_topic_context(heading_text, topics)
                if candidate and ((score >= 6 and margin >= 3) or (score >= 10 and margin >= 5)):
                    topic = candidate
            if topic:
                page_topics = headings_by_page.setdefault(p_num, [])
                if not page_topics or _topic_value(page_topics[-1], "title") != _topic_value(topic, "title"):
                    page_topics.append(topic)

    page_sections = {}
    ambiguous_pages = set()
    active_topic = None
    for page_number in page_numbers:
        page_headings = headings_by_page.get(page_number, [])
        if len(page_headings) > 1:
            ambiguous_pages.add(page_number)
            active_topic = None
        elif page_headings:
            active_topic = page_headings[-1]
        if active_topic and page_number not in ambiguous_pages:
            page_sections[page_number] = active_topic
    return page_sections, ambiguous_pages


def score_topic_context(context, topics):
    """Rank topic objects against source-page evidence; return best match and margin."""
    source = " ".join(_tokens(context))
    source_tokens = set(_tokens(context))
    topic_phrases = []
    term_topic_counts = {}
    for topic in topics:
        phrases = [_topic_value(topic, "title", "")]
        subtopics = _topic_value(topic, "subtopics", [])
        if isinstance(subtopics, list):
            phrases.extend(subtopics)
        filtered_phrases = []
        topic_all_tokens = set()
        for phrase in phrases:
            phrase_tokens = _tokens(phrase)
            if not phrase_tokens:
                continue
            filtered_phrases.append((" ".join(phrase_tokens), phrase_tokens))
            topic_all_tokens.update(phrase_tokens)
        topic_phrases.append((topic, filtered_phrases))
        for token in topic_all_tokens:
            term_topic_counts[token] = term_topic_counts.get(token, 0) + 1

    scores = []
    for topic, phrases in topic_phrases:
        score = 0
        matched = set()
        title_tokens = set(_tokens(_topic_value(topic, "title", "")))
        if title_tokens and title_tokens.issubset(source_tokens):
            score += 15
            matched.update(title_tokens)

        for phrase, phrase_tokens in phrases:
            if len(phrase_tokens) >= 2 and re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", source):
                score += 4 + len(set(phrase_tokens))
                matched.update(phrase_tokens)
            elif (
                len(phrase_tokens) == 1
                and phrase_tokens[0] not in _GENERIC_TOPIC_ANCHORS
                and term_topic_counts.get(phrase_tokens[0]) == 1
                and re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", source)
            ):
                score += 12
                matched.update(phrase_tokens)
        for token in {token for _, tokens in phrases for token in tokens}:
            if re.search(rf"(?<!\w){re.escape(token)}(?!\w)", source):
                score += 3 if term_topic_counts.get(token) == 1 else 1
                matched.add(token)
        scores.append((topic, score, sorted(matched)))

    ranked = sorted(scores, key=lambda item: item[1], reverse=True)
    if not ranked or ranked[0][1] == 0:
        return None, 0, 0, []
    best_topic, best_score, best_evidence = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else 0
    return best_topic, best_score, best_score - second_score, best_evidence