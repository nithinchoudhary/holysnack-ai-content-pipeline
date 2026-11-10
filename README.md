# ⚡ Holy Snack — Serverless AI Content & Compliance Pipeline

A self-sustaining, **$0/month** AI workflow automation, regulatory compliance, and publishing pipeline built during my Industry Internship (ICT803, Project `2026S2_02`) for **Holy Snack**, a Melbourne-based direct-to-consumer (D2C) snack brand.

---

## 📌 Overview & Problem Statement

Small consumer brands face two major operational risks when scaling digital content with Generative AI:
1. **Manual Bottlenecks:** Writing captions, formatting assets, and scheduling posts across multiple platforms takes hours of repetitive work every week.
2. **Regulatory & Brand Risk:** Unfiltered Large Language Models (LLMs) frequently hallucinate medical, nutritional, or therapeutic claims that violate **Food Standards Australia New Zealand (FSANZ)** and back-of-pack **Nutrition Information Panel (NIP)** rules.

### What I Built
As Team Leader for a 5-member cross-functional group, I architected a **Human-in-the-Loop AI Content & Publishing Engine** connecting Google Sheets, Google Apps Script, the Google Gemini API, Python, and Make.com webhooks. The system automates draft generation and compliance filtering while enforcing mandatory human approval before any asset is published.

---

## ✨ Key Features

* **1-Click Cloud Automation (`pipeline.gs`):** Bound directly to Google Sheets with a custom UI menu (`⚡ Holy Snack AI`), calling the **Google Gemini 3.5 Flash Lite API** via `UrlFetchApp` to turn raw calendar topics (`Draft`) into compliant captions (`Pending Approval`).
* **20-Point FSANZ & NIP Compliance Firewall:** Enforces verified product attributes (popped water lily seeds, 60g pouches, roasted never fried, plant-based, gluten-free across *Himalayan Salt*, *Peri Peri*, and *Thai Sweet Chilli*) while blocking prohibited health or weight-loss claims.
* **Human-in-the-Loop Gate & Master Kill Switch:** Prevents unauthorized automated posting. Rows must be manually switched from `Pending Approval` to `Approved` before triggering the Make.com / Instagram Business webhook. Includes an emergency Kill Switch in Cell `Q1` (`ACTIVE` / `PAUSE`).
* **Automated CDN Media Transformation:** Automatically extracts Google Drive file IDs from Column O (`Asset_Link`) and converts PNG links into Instagram-compatible JPEG CDN streams (`lh3.googleusercontent.com/d/{id}=w1080`) prior to webhook dispatch.
* **Local Python Engine (`brain_and_qa.py` & `visual_factory.py`):**
  * `brain_and_qa.py`: Standalone Python CLI module for local terminal prompt execution and compliance QA testing.
  * `visual_factory.py`: Python **Pillow (PIL)** script designed to dynamically overlay hooks and CTAs onto clean 1080×1350 and 1080×1920 background templates with safe-zone padding.

---

## 🛠️ Tech Stack

* **Languages & Scripting:** Python 3, JavaScript (Google Apps Script)
* **AI & LLM Integration:** Google Gemini API (Gemini 3.5 Flash Lite via Google AI Studio), OpenAI ChatGPT, Prompt Engineering
* **Automation & APIs:** Make.com Webhooks, Meta Graph API (Instagram Business), Telegram Bot API, REST APIs, JSON
* **Database & Cloud Storage:** Google Sheets (State Machine & Queue), Google Drive
* **Libraries:** Python Pillow (`PIL`), `requests`, Google `UrlFetchApp`

---

## 🔄 System Architecture & Workflow

```text
[ Master Google Sheet Calendar (26 Mapped Posts) ]
                        │
                        ▼  (Status = "Draft" | Click: 1️⃣ Generate AI Drafts)
[ Google Apps Script (pipeline.gs) + Gemini 3.5 Flash Lite API ]
                        │  (Applies 20-Point FSANZ/NIP Compliance Firewall)
                        ▼
[ Google Sheet Queue (Column L Updated | Status = "Pending Approval") ]
                        │
                        ▼  (Human Review & Sign-Off -> Status = "Approved")
[ Click: 2️⃣ Publish Approved Posts -> Make.com Webhook Bridge ]
                        │  (Converts Drive Asset to CDN Stream + Maps Caption)
                        ▼
[ Published to Instagram Business Grid | Status = "Published" ]
```

---

## 🚀 How to Run It

### Option A: Cloud Pipeline (Google Sheets + Apps Script)
1. Create a Google Sheet with operational columns (`Post_ID`, `Proposed_Publish_Date`, `Platform`, `Format`, `Main_Pillar`, `Publish_Ready_Caption` in Column L, `Asset_Link` in Column O, and `Approval_Status` in Column P).
2. Set Cell `Q1` to `ACTIVE` (Master Kill Switch).
3. In the Google Sheet top menu, click **Extensions > Apps Script**, paste the contents of `pipeline.gs`, and insert your `GEMINI_API_KEY` (from Google AI Studio) and `MAKE_WEBHOOK_URL`.
4. Reload the Google Sheet, set any row's Column P to `Draft`, and click **⚡ Holy Snack AI → 1️⃣ Generate AI Drafts**.
5. Review the generated caption in Column L, change Column P to `Approved`, and click **⚡ Holy Snack AI → 2️⃣ Publish Approved Posts**.

### Option B: Local Python Scripts
```bash
# Install dependencies
pip install pillow requests

# Run local CLI caption generator and compliance checker
python brain_and_qa.py

# Run batch image text-overlay renderer
python visual_factory.py
```

---

## 🧠 What I Learned

* **LLM Input Validation & Guardrails:** Designing deterministic prompt constraints and compliance checklists is essential when deploying generative AI in regulated consumer industries.
* **Serverless Cost & Reliability Engineering:** Building on native Google Apps Script (`UrlFetchApp`), Google AI Studio's free tier (1,500 RPD), and webhook bridges allowed us to deliver an enterprise-grade workflow with $0/month recurring overhead.
* **Cross-Functional Technical Leadership:** Coordinating a 5-person team taught me how to standardize cloud file naming schemas, image safe zones, and spreadsheet data structures so creative deliverables integrate cleanly with automation code.

---

## 🤝 AI Tools & Learning Attribution

During this internship, I used **Google Gemini** and **OpenAI ChatGPT** both as core API components of the automated pipeline and as collaborative coding and documentation assistants to accelerate Google Apps Script and Python prototyping. All code, API payloads, and regulatory compliance rules were manually tested, audited, and verified in a live staging environment prior to client handover.
