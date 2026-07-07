# Groq Chat Completion Example (Python)

This project demonstrates how to use the **Groq Python SDK** to interact with the **Llama 3.3 70B Versatile** model by sending a prompt and receiving a response.

## Features

* Load API key securely using `.env`
* Connect to the Groq API
* Send a prompt using the Chat Completions API
* Ask multiple questions in a single prompt
* Print the model's response

---

## Project Structure

```text
project/
│
├── main.py          # Python source code
├── .env             # Stores the API key
├── requirements.txt # Python dependencies
└── README.md
```

---

## Requirements

* Python 3.9+
* Groq API Key

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2. Install dependencies

```bash
pip install groq python-dotenv
```

Or using a `requirements.txt` file:

```text
groq
python-dotenv
```

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GROK_API_KEY=your_groq_api_key_here
```

> Replace `your_groq_api_key_here` with your actual Groq API key.

---

## Example Code

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROK_API_KEY")

client = Groq(api_key=api_key)

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
    model="llama-3.3-70b-versatile",
    messages=messages
)

print(response.choices[0].message.content)
```

---

## How It Works

1. Loads the API key from the `.env` file.
2. Creates a Groq client.
3. Sends a chat completion request to the model.
4. The prompt contains multiple questions inside a single user message.
5. The model generates one response containing answers to all questions.

---

## Example Prompt

```text
Answer all questions separately:

1. Who is Elon Musk?
2. Give me 10 Hindu goddess names.
3. What is the capital of France?
4. What is the square root of 144?
```

---

## Expected Output

```text
1. Elon Musk is an entrepreneur...

2. Hindu Goddess Names:
- Durga
- Lakshmi
- Saraswati
...

3. The capital of France is Paris.

4. The square root of 144 is 12.
```

---

## Notes

* The `messages` parameter represents the conversation history.
* Each message contains:

  * `role`: Who is sending the message (`system`, `user`, or `assistant`)
  * `content`: The actual text sent to the model.
* Multiple independent questions can be included in a single `content` block if you want one combined response.

---

## Dependencies

* `groq`
* `python-dotenv`

---

## License

This project is intended for learning and educational purposes.
