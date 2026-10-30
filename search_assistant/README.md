# DeepSeek Flash Web Radar ⚡

A high-speed, local Streamlit dashboard that gives **DeepSeek Flash** live internet search capabilities.

## What it does
- **Natural Language Search**: Type whatever you want to find (jobs, news, 3D/animation updates, tools, movies).
- **Multi-Source Web Engine**: Queries live web & news feeds (with authentic URL decoding), GitHub repositories, and Wikipedia.
- **DeepSeek Flash Synthesis**: Automatically synthesizes findings into structured cards: **Role / Title**, **Concise Summary**, and **Direct Clickable Links**.
- **Zero Config**: Automatically reads `DEEPSEEK_API`, `DEEPSEEK_BASE_URL`, and `DEEPSEEK_CHAT_MODEL` from your project's `.env`.

## How to Run

### Option 1: Double click
Double-click `run.bat` in this folder.

### Option 2: Terminal
```powershell
cd C:\Users\adm\.vscode\Products\EduAI\search_assistant
streamlit run app.py
```
Then open `http://localhost:8501` in your browser.
