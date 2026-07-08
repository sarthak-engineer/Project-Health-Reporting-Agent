# AI Project Health Reporting Agent

An AI-powered project health reporting system that automatically analyzes Microsoft Project plans, determines project health using a deterministic RAG scoring engine, and generates AI-powered executive reports and presentations.

This project was developed as part of the AI Engineer Intern Technical Assignment.

---

# Features

- Reads Microsoft Project Excel plans automatically.
- Cleans and validates project data.
- Extracts project health metrics.
- Calculates deterministic RAG (Red-Amber-Green) scores.
- Uses Groq Llama 3.3 for executive reasoning.
- Generates weekly project health reports.
- Creates monthly executive PowerPoint presentations.
- Handles incomplete project data gracefully.

---

# System Workflow

```text
Excel Project Plan
        │
        ▼
Data Cleaning
        │
        ▼
Metrics Extraction
        │
        ▼
Deterministic RAG Engine
        │
        ▼
Project Context Builder
        │
        ▼
Groq Llama 3.3
        │
        ▼
Weekly Reports
        │
        ▼
Executive PowerPoint
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Excel Parsing | OpenPyXL |
| AI Model | Groq Llama 3.3 70B |
| Reporting | Markdown |
| Presentation | python-pptx |
| Environment | Python Virtual Environment |

---

# Project Structure

```text
Project-Health-Reporting-Agent/

├── data/
├── docs/
├── output/
│   ├── weekly_reports/
│   └── presentations/
├── src/
├── .env
├── requirements.txt
├── main.py
└── README.md
```

---

# Installation

```bash
git clone <repository-url>

cd Project-Health-Reporting-Agent

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key
```

---

# Run

```bash
python main.py
```

---

# Outputs

The system automatically generates:

- Weekly Markdown Project Reports
- Executive PowerPoint Presentation
- AI-generated Executive Summaries
- Risk Analysis
- Actionable Recommendations