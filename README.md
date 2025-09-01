# 🧠 Learnify – AI-Powered YouTube Lecture Summarizer

> **Short on time? Learnify watches, learns, and teaches — so you don’t have to.**

Stop watching hour-long lectures.  
Let **Learnify** do it for you.

This AI agent crew watches YouTube educational videos, extracts the transcript, summarizes key insights, and delivers a **structured, markdown-formatted summary** — ready for review, sharing, or archiving.

🎯 Ideal for:  
Students • Researchers • Developers • Lifelong Learners • Knowledge Workers

---

## 🚀 What It Does

1. **📹 Input**: Provide any YouTube lecture URL  
2. **🧩 Extract**: Fetches full transcript using `youtube-transcript-api`  
3. **🧠 Summarize**: AI agent breaks it into chunks and summarizes key points  
4. **📄 Format**: Another agent compiles everything into clean Markdown  
5. **💾 Output**: Saves to `lecture_summary.md` — ready to read or export

✅ No manual note-taking  
✅ No skimming through videos  
✅ Just deep, structured insights — delivered instantly

---

## 🛠️ Tech Stack

- **Framework**: [CrewAI](https://www.crewai.com/) (Multi-Agent Orchestration)
- **Transcript Tool**: `youtube-transcript-api`
- **Agents**:  
  - `YouTube Lecture Summarizer` – Extracts and distills key ideas  
  - `Markdown Formatter` – Structures output beautifully
- **Input Validation**: Pydantic + Custom Tool Schema
- **Output**: Markdown (for Notion, Obsidian, GitHub, etc.)

---
