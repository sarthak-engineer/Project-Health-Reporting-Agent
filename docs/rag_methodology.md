# Project Health Reporting Agent – RAG Methodology

## Objective

The objective of the Project Health Reporting Agent is to automatically determine the overall health of a project using project schedule data, task progress, and risk indicators. The system classifies every project into one of three health categories:

- 🟢 Green
- 🟠 Amber
- 🔴 Red

The methodology combines deterministic scoring with AI-generated reasoning to provide both quantitative and qualitative project health analysis.

---

# Input Signals

The agent evaluates the following indicators extracted from project plans.

| Indicator | Description |
|-----------|-------------|
| Task Completion | Percentage of completed tasks |
| Schedule Health | Green, Amber and Red task distribution |
| Critical Tasks | Number of critical activities |
| Risk Tasks | Tasks marked At Risk |
| Schedule Variance | Average task schedule variance |
| Negative Comments | Stakeholder comments indicating issues |
| On Hold Tasks | Tasks currently blocked or paused |

---

# Scoring Methodology

Each indicator contributes to the overall project health score.

| Metric | Weight |
|---------|-------:|
| Task Completion | 20 |
| Schedule Health | 25 |
| Critical Tasks | 15 |
| Risk Tasks | 10 |
| Schedule Variance | 10 |
| Stakeholder Comments | 10 |
| On Hold Tasks | 10 |

Maximum Score = 100

---

# RAG Thresholds

| Score | Status |
|-------:|--------|
| 80 – 100 | 🟢 Green |
| 60 – 79 | 🟠 Amber |
| Below 60 | 🔴 Red |

---

# AI Reasoning

After the deterministic score is calculated, the project summary is passed to a Large Language Model (Groq Llama 3.3 70B).

The AI does not calculate the score.

Instead, it:

- Generates executive summaries.
- Identifies key project risks.
- Provides actionable recommendations.
- Produces management-friendly explanations.

---

# Assumptions

- Missing values are treated as unavailable information.
- The scoring engine is deterministic and reproducible.
- AI reasoning is generated only after project metrics have been calculated.
- AI recommendations are based solely on the extracted project metrics.

---

# Overall Workflow

Excel Project Plan
        ↓
Data Cleaning
        ↓
Metrics Extraction
        ↓
RAG Scoring Engine
        ↓
AI Reasoning (Groq)
        ↓
Weekly Report
        ↓
Executive PowerPoint