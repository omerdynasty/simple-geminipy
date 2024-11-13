import pathlib
import textwrap
import json
import re
import os
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
with open('api_key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read().strip()

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

question = input("You: ")

response = model.generate_content(question)

text_response = response.text

text_without_markdown = re.sub(r'[*#]', '', text_response)

print("Gemini: " + text_without_markdown)