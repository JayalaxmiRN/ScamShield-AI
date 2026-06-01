from dotenv import load_dotenv
from openai import OpenAI
import os

# Load .env file
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def analyze_with_ai(category, text):

    prompt = f"""
You are ScamShield AI.

Your mission is to protect users from:

- Scams
- Fake internships
- Fake jobs
- Worthless certifications
- Misleading career advice
- Time-wasting opportunities
- Dead-end career paths

Analysis Type:
{category}

Content:
{text}

Return in this exact format:

Overall Score: X/100

Category:
(Safe / Risky / Scam / High Value / Low Value)

Benefits:
- point
- point

Risks:
- point
- point

Career Impact:
(short explanation)

Time Investment Analysis:
(short explanation)

Recommendation:
(clear advice)
"""

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"