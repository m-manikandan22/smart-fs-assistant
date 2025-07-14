import os
import openai
from config.settings import API_KEY

openai.api_key = API_KEY
client = openai.OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1")

def get_llm_response(prompt):
    system_prompt = open("prompts/system_prompt.txt").read()

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # or other model you're using
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
