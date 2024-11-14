# Gemini (with Python)

A very simple script to use Gemini API with python.

I tried my best to make it as user friendly as possible, you can look below for detailed explanations of the code or other information, but if you just want to use it, you don't need to tinker much...


# How to use? 📖

Firstly install Gemini-API (only one time)

Necessary things
Python
`pip install google-cloud-aiplatform`
`pip install -q -U google-generativeai`

Just paste your [KEY](https://aistudio.google.com/app/apikey) in api_key.txt. That's it!

# Developer Things 😋

Once you have done that, you can use the script at any time (as long as your KEY is working).
You can just use Gemini-API.py but if you don't know how to, just use start.bat :)

Note: I used Python 3.12.4 to do everything, but I don't think it will be a problem with other versions.

### I realize I've overcomplicated things a bit, so here is version 1.1 in its simplicity.

## What is Gemini?

Gemini is a product of Google.
This project is designed as a training tool for using the Gemini API. I do not own any rights.

## AI EXPLANATION OF CODE

1. **Import Necessary Libraries:** Imports modules for various tasks, including file operations, text manipulation, regular expressions, and interaction with the Google Generative AI API.
2. **Read API Key:** Reads the API key from a file named 'api_key.txt' which is required to authenticate with the Google AI service.
3. **Configure API:** Sets up the Google Generative AI environment using the obtained API key.
4. **Create Model:** Instantiates a 'gemini-1.5-flash' model, which is a language model capable of generating text.
5. **Prompt User:** Asks the user to input a question or prompt.
6. **Generate Response:** Sends the user's input to the model and receives a generated text response.
7. **Remove Markdown:** Removes any Markdown formatting (like headings, lists) from the generated response to get plain text.
8. **Print Response:** Prints the final, cleaned-up response from the model.

**In essence, this code acts as a simple chatbot, using Google's AI to generate text responses based on user prompts.** 

