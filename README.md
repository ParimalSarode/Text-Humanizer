# 🧠 AI Text Humanizer

A fast, lightweight, open-source tool that rewrites text to sound more natural, clear, and human-edited — built with Streamlit and modern LLM APIs.

### ⭐ If you find this useful, consider starring the repo.

---

## ✨ Why This Project Exists

Most *“AI humanizer”* tools:

* make unrealistic promises
* chase unreliable AI detectors
* hide their limitations

This project takes a different approach.

It focuses on what actually matters:

* readability
* tone
* clarity
* human-editor style rewrites

**No gimmicks. No false guarantees.**

---

## 🚀 Features

* ✍️ Rewrite text to sound more natural and human-edited
* 🎭 Style options:

  * Friendly
  * Casual
  * Professional
* ⚡ Extremely fast inference using Groq-hosted LLMs
* 🖥️ Simple, clean Streamlit UI
* ☁️ Deployable on Streamlit Cloud
* 🧩 Clean, beginner-friendly architecture
* 🔌 Optional FastAPI backend for API usage

---

## 🏗️ Architecture (Simple & Robust)

```
Browser
  ↓
Streamlit UI
  ↓
humanizer.py (Prompt + Logic)
  ↓
Groq API (LLM Inference)
```

### Optional API Mode

```
Client / curl / app
  ↓
FastAPI
  ↓
humanizer.py
  ↓
Groq API
```

### Why this design?

* No backend servers required for UI
* No local model hosting
* No RAM or disk pressure
* Stable repeated usage
* Easy deployment
* This mirrors how real-world AI tools are built

---

## 📁 Project Structure

```
dummy__humanizer/
├─ streamlit_app.py   # Streamlit UI
├─ humanizer.py       # Core logic + Groq API
├─ api.py             # Optional FastAPI backend
├─ requirements.txt   # Dependencies
└─ README.md
```

---

## 🧪 What This Tool Is (and Isn’t)

### ✅ This tool DOES:

* Improve tone and flow
* Preserve meaning
* Act like a human editor
* Help with emails, posts, explanations, UX copy

### ❌ This tool DOES NOT:

* Guarantee “100% human” detector results
* Bypass AI detection systems
* Detect AI-written text
* Claim authorship certainty

> AI detectors are inconsistent and unreliable.
> This project intentionally does **not** optimize for them.

---

## ⚙️ Getting Started (Streamlit UI)

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start the Streamlit app

```bash
python -m streamlit run streamlit_app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 🔐 API Key

Create a free account at:
👉 [https://console.groq.com](https://console.groq.com)

Generate a **Groq API key**, then paste it into the app sidebar.

* The key is stored **only for the session**
* It is **never written to disk**
* It is **not committed to GitHub**

---

## 🎭 Styles Available

| Style        | Behavior                                |
| ------------ | --------------------------------------- |
| Professional | Formal, clear, neutral tone             |
| Casual       | Relaxed, conversational                 |
| Friendly     | Warm, approachable, slightly expressive |

> Styles affect **tone**, not model intelligence.

---

## 🤖 Models Available

| Label            | Model ID                  | Use case                       |
| ---------------- | ------------------------- | ------------------------------ |
| Fast & Efficient | `llama-3.1-8b-instant`    | Default, fast rewrites         |
| High Quality     | `llama-3.3-70b-versatile` | Richer phrasing, better nuance |

> Model availability depends on Groq.
> Larger models may be slower and consume more free-tier quota.

---

## 🔌 FastAPI Usage (Optional)

The project includes an optional FastAPI backend for programmatic use.

### Start the API server

```bash
uvicorn api:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📄 FastAPI Request Schema

```json
{
  "text": "string",
  "style": "string",
  "api_key": "string",
  "model": "string"
}
```

### Field details

* **text** – Input text to rewrite
* **style** – `professional` | `casual` | `friendly`
* **api_key** – User’s Groq API key
* **model** – Model ID (see Models section)

---

## 🧪 Example FastAPI Request (curl)

For terminal-focused users who don’t want Swagger:

```bash
curl -X POST http://127.0.0.1:8000/humanize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The system encountered an unexpected error during processing.",
    "style": "friendly",
    "api_key": "gsk_your_groq_key_here",
    "model": "llama-3.1-8b-instant"
  }'
```

### Example response

```json
{
  "output": "Looks like something hiccupped while we were processing this. Give it another try in a bit — we’re on it!"
}
```

---

## 📦 Deployment

### Streamlit Cloud

This project is Streamlit Cloud–ready.

**Steps:**

1. Push the repo to GitHub
2. Deploy on Streamlit Cloud
3. No secrets configuration required

Users provide their own API key via UI.

---

## 🔍 Lessons Learned

During development, this project demonstrated that:

* AI detectors frequently contradict each other
* “Human vs AI” classification is unreliable
* Writing quality ≠ detector approval

As a result, this tool focuses on **usefulness**, not broken metrics.

---

## 🛠️ Future Ideas

* Model selection expansion
* Output history
* File upload support
* Desktop packaging
* Optional local + API hybrid mode

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## ⭐ Final Note

This project is intentionally:

* honest
* minimal
* practical
* educational

If you’re learning applied AI engineering or want a clean text-rewriting tool, this repo is a solid reference.

---

## 🙌 Contributing

Issues, ideas, and improvements are welcome.
If this helped you learn something — a GitHub star goes a long way ⭐

---


