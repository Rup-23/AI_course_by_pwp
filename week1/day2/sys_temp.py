import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
my_api_key=os.getenv("GROK_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

# System message meaning how system behave itself and reply
system_message={
    "role":"system",
    "content":"you are a brand manager who suggest name for my food company.name should be in one word. suggest one name only"
}

message={
    "role":"user",
    "content":"Suggest a name for my cloth company"
}
messages=[system_message,message]

# Temperature work between (0-2) and 0 meaning safe and 2 meaning creative 
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)
# print(response)
# print("####################################################")

print(response.choices[0].message.content)
