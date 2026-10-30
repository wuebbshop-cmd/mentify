"""
search_assistant/app.py

Streamlit Internet Search Dashboard powered by DeepSeek Flash.
General-purpose web intelligence agent with deep content reading and full answers.
"""
import concurrent.futures
import json
import re
import time
from datetime import datetime
from pathlib import Path
import streamlit as st

from deepseek_client import generate_search_queries, get_deepseek_config, stream_synthesis
from search_engine import (
    extract_urls_from_text,
    scrape_domain_jobs,
    scrape_page_content,
    search_github,
    search_web,
    search_wikipedia,
)

# Page configuration
st.set_page_config(
    page_title="DeepSeek Flash Web Radar",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Obsidian / Cyber Teal Minimalist UI)
st.markdown(
    """
    <style>
    /* Dark Theme Core */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #111827 0%, #080c14 100%);
        color: #e2e8f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Header styling */
    .hero-container {
        padding: 1.5rem 0 1rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1.5rem;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(0, 210, 157, 0.12);
        color: #00d29d;
        border: 1px solid rgba(0, 210, 157, 0.25);
        border-radius: 9999px;
        padding: 4px 12px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 0.4rem 0;
    }
    .hero-desc {
        color: #94a3b8;
        font-size: 0.95rem;
        margin: 0;
    }

    /* Sidebar Clean styling */
    section[data-testid="stSidebar"] {
        background-color: #0c1017;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Metric / Status widget */
    .status-pill {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        border-radius: 8px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #00d29d;
        box-shadow: 0 0 8px #00d29d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "search_history" not in st.session_state:
    st.session_state.search_history = []
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# Sidebar Controls
with st.sidebar:
    st.markdown("### ⚡ System Status")
    cfg = get_deepseek_config()
    if cfg["api_key"]:
        st.markdown(
            f"""
            <div class="status-pill">
                <div class="status-dot"></div>
                <div>
                    <strong style="color: #f8fafc;">DeepSeek Flash</strong><br>
                    <span style="color: #64748b; font-size: 0.75rem;">Model: {cfg['model']} &bull; Connected</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("❌ DeepSeek API key not found in `.env`.")

    st.markdown("---")
    st.markdown("### 🔍 Search Configuration")

    time_filter_label = st.selectbox(
        "Search Horizon",
        options=["Anytime", "Past 24 Hours", "Past 7 Days", "Past 30 Days"],
        index=0,
        help="Filter live web articles by publication window.",
    )
    time_filter_map = {
        "Anytime": "any",
        "Past 24 Hours": "day",
        "Past 7 Days": "week",
        "Past 30 Days": "month",
    }
    selected_time_filter = time_filter_map[time_filter_label]

    max_results = st.slider(
        "Sources to Scout",
        min_value=4,
        max_value=16,
        value=8,
        step=2,
        help="Number of web sources retrieved per query.",
    )

    deep_read = st.checkbox(
        "Deep Page Reading",
        value=True,
        help="Reads inside the actual web pages (extracting lists, ratings, tables, and full body text).",
    )

    include_github = st.checkbox("Include GitHub Repos", value=True, help="Scouts code repositories when questions relate to software/tools.")
    include_wiki = st.checkbox("Include Wikipedia Knowledge", value=False, help="Pulls encyclopedia context for conceptual definitions.")

    st.markdown("---")
    st.markdown("### 🕒 Recent Searches")
    if st.session_state.search_history:
        for idx, past_query in enumerate(reversed(st.session_state.search_history[-8:])):
            if st.button(f"🔍 {past_query[:30]}...", key=f"hist_{idx}"):
                st.session_state.pending_prompt = past_query
                st.rerun()
    else:
        st.caption("No searches yet in this session.")

    if st.button("🗑️ Clear Chat & History", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.search_history = []
        st.rerun()

# Main Header
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-badge">⚡ Real-Time Web Intelligence</div>
        <h1 class="hero-title">DeepSeek Flash Web Radar</h1>
        <p class="hero-desc">Ask anything. The assistant autonomously searches the live internet, reads web pages deeply, extracts facts and rankings, and delivers complete answers.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display existing conversation history
for msg in st.session_state.chat_history:
    role = msg["role"]
    content = msg["content"]
    sources = msg.get("sources", [])

    with st.chat_message(role):
        st.markdown(content)
        if sources:
            with st.expander(f"📚 Verified Sources ({len(sources)})", expanded=False):
                for s in sources:
                    date_badge = f" ({s.get('pub_date')})" if s.get('pub_date') else ""
                    st.markdown(f"- **[{s.get('title')}]({s.get('link')})** &bull; `{s.get('source')}`{date_badge}")


# Process User Input (either from chat_input or a past history item)
user_prompt = st.chat_input("Ask DeepSeek to search, scout, or extract anything...")
if st.session_state.pending_prompt:
    user_prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    if user_prompt not in st.session_state.search_history:
        st.session_state.search_history.append(user_prompt)

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        status_box = st.status("🔍 Scouting live web sources...", expanded=True)

        all_results = []
        seen_urls = set()

        detected_urls = extract_urls_from_text(user_prompt)
        prompt_lower = user_prompt.lower()

        # 1. If user gave direct URLs, scrape them immediately
        for u in detected_urls:
            status_box.write(f"🌐 Deep-reading URL: `{u[:60]}...`")
            page_data = scrape_page_content(u, max_chars=4000)
            if page_data.get("success"):
                all_results.append(
                    {
                        "title": page_data.get("title") or u,
                        "link": u,
                        "source": "Direct URL",
                        "pub_date": "Current",
                        "snippet": page_data.get("text", "")[:250],
                        "content": page_data.get("text", ""),
                    }
                )
                seen_urls.add(u)

        # 2. Site-specific detection (e.g., job portals or specific platforms)
        if "myjobmag" in prompt_lower or "brightermonday" in prompt_lower:
            portal = "myjobmag" if "myjobmag" in prompt_lower else "brightermonday"
            status_box.write(f"💼 Scouting live postings on **{portal.title()}**...")
            kw = re.sub(r"https?://[^\s]+", "", user_prompt)
            kw = re.sub(r"\b(find|search|me|latest|roles|jobs|in|kenya|from|at|on|the)\b", " ", kw, flags=re.I)
            kw = re.sub(r"\s+", " ", kw).strip()
            job_results = scrape_domain_jobs(portal, kw or "software data", max_results=max_results)
            for j in job_results:
                if j["link"] not in seen_urls:
                    seen_urls.add(j["link"])
                    all_results.append(j)

        # 3. Web Search with Deep Reading
        status_box.write("⚡ DeepSeek Flash generating optimized web queries...")
        search_queries = generate_search_queries(user_prompt)
        status_box.write(f"🎯 Search queries: `{'` &bull; `'.join(search_queries)}`")

        def fetch_web_query(q):
            return search_web(q, time_filter=selected_time_filter, max_results=max_results, deep_fetch_content=deep_read)

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            batches = list(executor.map(fetch_web_query, search_queries))

        for batch in batches:
            for item in batch:
                link = item.get("link", "")
                if link and link not in seen_urls:
                    seen_urls.add(link)
                    all_results.append(item)

        # 4. Optional GitHub Search
        if include_github and any(k in prompt_lower for k in ["code", "repo", "model", "tool", "github", "framework", "library", "software"]):
            status_box.write("🐙 Searching GitHub repositories...")
            gh_items = search_github(search_queries[0], max_results=4)
            for it in gh_items:
                if it["link"] not in seen_urls:
                    seen_urls.add(it["link"])
                    all_results.append(it)

        # 5. Optional Wikipedia Search
        if include_wiki:
            wiki_items = search_wikipedia(search_queries[0], max_results=2)
            for it in wiki_items:
                if it["link"] not in seen_urls:
                    seen_urls.add(it["link"])
                    all_results.append(it)

        status_box.write(f"✅ Retrieved {len(all_results)} verified sources. Synthesizing full answer...")
        status_box.update(label=f"Retrieved {len(all_results)} sources &bull; Ready", state="complete", expanded=False)

        # Display expandable source preview
        if all_results:
            with st.expander(f"📚 Verified Sources & Links ({len(all_results)})", expanded=False):
                for r in all_results:
                    date_badge = f" ({r.get('pub_date')})" if r.get('pub_date') else ""
                    st.markdown(f"- **[{r.get('title')}]({r.get('link')})** &bull; `{r.get('source')}`{date_badge}")

        # Step 4: Stream DeepSeek Flash synthesis (with auto-continuation for long responses)
        response_placeholder = st.empty()
        full_response = ""

        conversation_context = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.chat_history[:-1]
        ]

        for token in stream_synthesis(user_prompt, all_results, conversation_context):
            full_response += token
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

        # Save assistant message to chat history
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": full_response,
                "sources": all_results,
            }
        )
