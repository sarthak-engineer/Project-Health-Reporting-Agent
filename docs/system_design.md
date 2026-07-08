# AI Project Health Reporting Agent

## Objective

Build an AI-powered Project Health Reporting Agent that automatically analyzes project plans, determines project health (Red, Amber, Green), explains the reasoning, identifies emerging risks, and generates executive-level weekly and monthly reports.

---

## System Architecture

Excel Project Plans
        │
        ▼
Project Parser
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Signal Extraction
        │
        ▼
Project Metrics Generator
        │
        ▼
RAG Decision Engine
        │
        ▼
LLM Reasoning Engine (Groq Llama 3.3 70B)
        │
        ▼
Weekly Project Health Report
        │
        ▼
Executive Presentation Generator
