import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROK_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client=Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

# message={
#     "role":"user",
#     "content":"Who is virat kohli?"
# }
# messages=[message]

messages = [
    {
        "role": "user",
        "content": """
        Answer all questions separately:

        1. Who is Elon Musk?
        2. Give me 10 Hindu goddess names.
        3. What is the capital of France?
        4. What is the square root of 144?
        """
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)
print(response.choices[0].message.content)
