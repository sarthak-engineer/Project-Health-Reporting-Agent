import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class AIReasoning:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

    def generate(self, context):

        prompt = f"""
You are a Senior PMO Executive.

Analyze the following project.

Rules:

- Use ONLY the provided project metrics.
- Do NOT assume missing information.
- Do NOT invent facts.
- Keep the response concise and executive friendly.

Return ONLY valid JSON.

Schema:

{{
    "executive_summary": "",
    "key_risks": [
        "",
        "",
        ""
    ],
    "recommendations": [
        "",
        "",
        ""
    ]
}}

Project:

{context}
"""

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            response_format={
                "type": "json_object"
            }

        )

        text = response.choices[0].message.content

        return json.loads(text)
