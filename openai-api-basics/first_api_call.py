import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

# if not api_key:
#     print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
# elif not api_key.startswith("sk-proj-"):
#     print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
# elif api_key.strip() != api_key:
#     print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
# else:
#     print("API key found and looks good so far!")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a 1 sentence cold email for a job for the position of 'AI Engineer'"}
]

openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

print(response.choices[0].message.content)