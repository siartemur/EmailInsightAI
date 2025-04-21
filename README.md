# 🤖 EmailInsightAI

**EmailInsightAI** is an AI-powered data processing system that automatically generates **Question-Answer (Q&A) pairs** from email content.  
The system extracts structured insights (e.g., dates, meetings, decisions) from unstructured emails and formats them for **LLM (Large Language Model)** training and fine-tuning.

---

## 🎯 Project Goals

- 💬 Automatically generate Q&A pairs from email content using AI  
- 🧠 Prepare high-quality data for **LLM fine-tuning and training**  
- 🔁 Build an **automated infrastructure** that continuously checks for new emails  
- 🧼 Follow SOLID principles with a modular, testable and maintainable architecture  

---

## ✅ What Problem Does It Solve?

📧 Corporate emails often contain valuable but unstructured information.  
**EmailInsightAI** helps you:

- 📝 Convert email bodies into structured Q&A pairs  
- 📦 Export clean datasets in JSON and CSV formats  
- 🔁 Process emails automatically as they arrive  
- 📅 Normalize relative date expressions to boost data quality

---

## ⚙️ Features

| Feature                              | Description |
|--------------------------------------|-------------|
| 🧠 AI-powered Q&A generation         | Generates a meaningful question and answer from each email |
| 📨 Batch processing of seed emails   | Quickly test with sample `.txt` email files |
| 🔁 Automation system                 | Simulated hourly email polling and processing |
| 🧾 JSON + CSV export support         | Easily reusable training datasets |
| 📅 Date normalization                | Converts terms like "tomorrow" or "Monday" into actual dates |
| 🧪 Unit testing support              | Built-in testing with `pytest` |
| 🧼 Clean, SOLID-based architecture   | Clear separation of concerns with service layers |

---
