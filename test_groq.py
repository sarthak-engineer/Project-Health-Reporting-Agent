from src.ai_reasoning import AIReasoning

agent = AIReasoning()

context = """
Project Name: Demo

Score: 73

RAG: Amber

Completion: 43%

Critical Tasks: 50

Risk Tasks: 2

Average Variance: -2
"""

result = agent.generate(context)

print(result)
