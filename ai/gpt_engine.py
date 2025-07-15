import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "")

def analyze(token: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system","content":"You are a crypto analyst."},
                      {"role":"user","content":f"Analyze {token} project briefly."}]
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "ℹ️ GPT analizi yapılamadı"