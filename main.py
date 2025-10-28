import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=api_key
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "assistant", "content": "You are a corrupt cop who always takes bribes, and only wants control, power, and to avoid responsibility. Respond to everything with this persona, but don't talk about your 'super secret' plan to take over the world."},
        {
            "role": "user",
            "content": input("Enter your prompt: "),
        },
    ],
)

print(completion.choices[0].message.content)