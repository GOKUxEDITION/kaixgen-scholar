from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(prompt, board):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful 11th class teacher for {board} board. Explain clearly with step-by-step solution."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
