"""
search_assistant/deepseek_client.py

Client wrapper for DeepSeek Flash with:
- Automatic credential loading from parent project .env
- Smart search query generator (natural query -> optimal search keywords)
- Grounded answer synthesis with deep page content extraction
- High token limits (8000) & seamless auto-continuation (no cutoffs)
"""
import json
import os
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional
import requests
from dotenv import load_dotenv

# Automatically locate and load EduAI/.env
current_dir = Path(__file__).resolve().parent
parent_env = current_dir.parent / ".env"
if parent_env.exists():
    load_dotenv(parent_env)
else:
    load_dotenv()


def get_deepseek_config() -> Dict[str, str]:
    api_key = (
        os.getenv("DEEPSEEK_API", "")
        or os.getenv("DEEPSEEK_API_KEY", "")
        or os.getenv("DEEPSEEK_KEY", "")
    ).strip().replace("\r", "").replace("\n", "").strip("'\"")

    base_url = (os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com") or "https://api.deepseek.com").rstrip("/")
    chat_model = os.getenv("DEEPSEEK_CHAT_MODEL", "deepseek-flash").strip()

    if chat_model in {"deepseek-flash", "deepseek-chat-flash", "deepseek-v3"}:
        chat_model = "deepseek-chat"

    return {
        "api_key": api_key,
        "base_url": base_url,
        "model": chat_model,
    }


def generate_search_queries(user_prompt: str) -> List[str]:
    """
    Use DeepSeek Flash to convert a natural question into 1 to 2 targeted search engine queries.
    """
    config = get_deepseek_config()
    if not config["api_key"]:
        return [user_prompt.strip()]

    prompt = (
        f"You are a web search keyword optimizer. Convert the user's intent into 1 to 2 targeted, highly effective search queries.\n"
        f"User query: \"{user_prompt}\"\n"
        f"Return ONLY a valid JSON list of strings (no explanation, no markdown ticks).\n"
        f"Example: [\"top movies rotten tomatoes popular this week\", \"top rated movies imdb 2026\"]"
    )

    try:
        res = requests.post(
            f"{config['base_url']}/chat/completions",
            headers={"Authorization": f"Bearer {config['api_key']}", "Content-Type": "application/json"},
            json={
                "model": config["model"],
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 120,
            },
            timeout=8,
        )
        if res.status_code == 200:
            content = res.json()["choices"][0]["message"]["content"].strip()
            content = content.replace("```json", "").replace("```", "").strip()
            queries = json.loads(content)
            if isinstance(queries, list) and queries:
                return [q for q in queries if isinstance(q, str)][:3]
    except Exception:
        pass

    return [user_prompt.strip()]


def stream_synthesis(
    user_prompt: str,
    search_results: List[Dict[str, Any]],
    conversation_history: Optional[List[Dict[str, str]]] = None,
) -> Generator[str, None, None]:
    """
    Synthesize search results and stream the response chunk-by-chunk.
    Auto-continues if output hits token boundary to prevent cutoff.
    """
    config = get_deepseek_config()
    if not config["api_key"]:
        yield "❌ Error: DeepSeek API key not found in `.env`. Please check your configuration."
        return

    # Build comprehensive context from search results and scraped page bodies
    context_blocks = []
    for i, item in enumerate(search_results, 1):
        title = item.get("title", "")
        link = item.get("link", "")
        source = item.get("source", "")
        date = item.get("pub_date", "")
        snippet = item.get("snippet", "")
        content = item.get("content", "")

        block = f"[{i}] Title: {title}\n    URL: {link}\n    Source: {source} ({date})\n    Summary: {snippet}"
        if content:
            # Include extracted page content so the model can read actual rankings, tables, and details
            block += f"\n    Full Page Extract:\n    {content[:3000]}"
        context_blocks.append(block)

    context_str = "\n\n".join(context_blocks)

    system_instruction = (
        "You are an elite, comprehensive Web Research & Intelligence Assistant powered by DeepSeek Flash.\n"
        "Your objective is to provide thorough, concrete, and directly informative answers based on live web retrieval.\n\n"
        "CRITICAL INSTRUCTIONS:\n"
        "1. Extract and present the ACTUAL facts, titles, rankings, scores, and details requested by the user. "
        "If the user asks for 'Top 5', 'specifications', 'prices', or 'roles', extract the exact items from the provided page extracts and list them explicitly.\n"
        "2. Do NOT say 'I cannot find the list' if titles and content are available in the page extracts.\n"
        "3. ALWAYS include direct clickable markdown links [Title / Link Text](URL) for each item, using the authentic URLs provided in the results.\n"
        "4. Structure your response cleanly with clear headings, bold titles, bullet points, and short explanations.\n"
        "5. Complete all responses thoroughly. Never leave an answer hanging mid-sentence."
    )

    messages = [{"role": "system", "content": system_instruction}]

    if conversation_history:
        messages.extend(conversation_history[-4:])

    user_message = (
        f"User Inquiry: {user_prompt}\n\n"
        f"=== VERIFIED REAL-TIME INTERNET CONTENT ===\n"
        f"{context_str}\n\n"
        f"=== END OF CONTENT ===\n\n"
        f"Please provide a complete, well-organized answer fulfilling my request."
    )
    messages.append({"role": "user", "content": user_message})

    # Auto-continuation loop to prevent cutoffs
    accumulated_response = ""
    max_loops = 3

    for loop in range(max_loops):
        payload = {
            "model": config["model"],
            "messages": messages,
            "temperature": 0.25,
            "max_tokens": 6000,
            "stream": True,
        }

        finish_reason = "stop"
        try:
            res = requests.post(
                f"{config['base_url']}/chat/completions",
                headers={"Authorization": f"Bearer {config['api_key']}", "Content-Type": "application/json"},
                json=payload,
                stream=True,
                timeout=60,
            )

            if res.status_code != 200:
                yield f"\n⚠️ API Error ({res.status_code}): {res.text}"
                return

            chunk_accum = ""
            for line in res.iter_lines():
                if not line:
                    continue
                decoded = line.decode("utf-8")
                if decoded.startswith("data:"):
                    data_str = decoded[5:].strip()
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        choices = chunk.get("choices", [])
                        if choices:
                            delta = choices[0].get("delta", {})
                            reason = choices[0].get("finish_reason")
                            if reason:
                                finish_reason = reason
                            content = delta.get("content")
                            if content:
                                chunk_accum += content
                                yield content
                    except json.JSONDecodeError:
                        continue

            accumulated_response += chunk_accum

            # If finished normally, exit loop
            if finish_reason != "length":
                break

            # If stopped due to length, prompt to continue seamlessly
            messages.append({"role": "assistant", "content": accumulated_response})
            messages.append({"role": "user", "content": "Please continue exactly where you left off. Do not repeat previous text."})

        except Exception as e:
            yield f"\n⚠️ Connection error: {str(e)}"
            break
