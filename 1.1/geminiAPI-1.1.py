import os
import google.generativeai as genai

with open('api_key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read().strip()

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
    ]
)

while 1 == 1:
    response = chat_session.send_message(str(input("You: ")))
    print("Gemini 1.5 (Flash): " + str(response.text))
