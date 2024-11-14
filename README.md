# Gemini (with Python)

A very simple script to use Gemini API with python.

I tried my best to make it as user friendly as possible, you can look below for detailed explanations of the code or other information, but if you just want to use it, you don't need to tinker much...


# How to use? 📖

### Necessary things <br>
```
pip install google-cloud-aiplatform
```
```
pip install -q -U google-generativeai
```

Get a [key.](https://aistudio.google.com/app/apikey) <br> Then open writekey.bat, paste your key, press enter. That's it! <br>
Note: 1.1 version doesn't remove markdown, I will add soon.

# Developer Things 😋

Note: I used Python 3.12.4 to do everything, but I don't think it will be a problem with other versions.

[API DOCS/Quick Start](https://ai.google.dev/gemini-api/docs/quickstart?hl=en&lang=python) <br>
[API DOCS/Get Started](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=en) <br>
[AI STUDIO](https://aistudio.google.com/prompts/new_chat) <br>
[API LIMITS](https://aistudio.google.com/plan_information) <br>

Obviously I wanted to keep it simple, but I was trying hard not to build a cryptosystem or at least not to use environment variables (man, it's 2024, you're storing an API KEY in plaintext!) so take a look at what I said. <br>

An example: <br>
```
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')

if not GOOGLE_API_KEY:
  print("Error: API KEY not found in environment variable.")
  exit(1)
```

## What is Gemini?

Gemini is a product of Google.
This project is designed as a training tool for using the Gemini API. I do not own any rights.

## AI EXPLANATION OF CODE 1.0

1. **Import Necessary Libraries:** Imports modules for various tasks, including file operations, text manipulation, regular expressions, and interaction with the Google Generative AI API.
2. **Read API Key:** Reads the API key from a file named 'api_key.txt' which is required to authenticate with the Google AI service.
3. **Configure API:** Sets up the Google Generative AI environment using the obtained API key.
4. **Create Model:** Instantiates a 'gemini-1.5-flash' model, which is a language model capable of generating text.
5. **Prompt User:** Asks the user to input a question or prompt.
6. **Generate Response:** Sends the user's input to the model and receives a generated text response.
7. **Remove Markdown:** Removes any Markdown formatting (like headings, lists) from the generated response to get plain text.
8. **Print Response:** Prints the final, cleaned-up response from the model.

**In essence, this code acts as a simple chatbot, using Google's AI to generate text responses based on user prompts.** 

## AI EXPLANATION OF CODE 1.1 (BETTER)

This Python code creates a chat interface using Google's Generative AI (GAI) library. You can interact with a large language model called Gemini through this interface.

**Here's a breakdown of the code:**

1. **Importing Libraries:**
    * `import os`: Imports the `os` library for operating system functionalities.
    * `import google.generativeai as genai`: Imports the Google Generative AI library.

2. **Reading API Key (Original Version):**
    * `with open('api_key.txt', 'r') as f:`: Opens the file `api_key.txt` in read mode.
    * `GOOGLE_API_KEY = f.read().strip()`: Reads the content of the file and removes leading/trailing whitespaces, storing it in the `GOOGLE_API_KEY` variable.

3. **Configuring GAI:**
    * `genai.configure(api_key=GOOGLE_API_KEY)`: Configures the GAI library using the API key retrieved from the file.

4. **Chat Configuration:**
    * `generation_config` dictionary defines settings for text generation:
        * `temperature`: Controls the balance between creativity and coherence in the model's responses (higher values lead to more creative but potentially less relevant outputs).
        * `top_p`: Influences the probability distribution of the model's next word selection (higher values favor more likely words).
        * `top_k`: Limits the number of words the model considers for the next word (lower values promote more diverse outputs).
        * `max_output_tokens`: Sets the maximum length of the model's generated response.
        * `response_mime_type`: Specifies the format of the model's response (here, plain text).

5. **Creating the Model:**
    * `model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)`: Creates a generative model named "gemini-1.5-flash" and assigns the `generation_config` settings to it. This model name likely refers to a specific pre-trained model within the GAI library.

6. **Starting Chat Session:**
    * `chat_session = model.start_chat(history=[])`: Initiates a chat session with the model. The `history` parameter is an empty list in this case, which means the model won't have any previous conversation context to consider during its initial responses.

7. **Main Chat Loop:**
    * `while 1 == 1` creates an infinite loop.
    * `print("It may take a while to receive a response, please wait.")`: Informs the user that processing might take some time.
    * `response = chat_session.send_message(str(input("You: ")))`: Prompts the user for input, converts it to a string, and sends it to the model using `chat_session.send_message`. The model response is stored in the `response` variable.
    * `os.system('cls')`: Clears the console screen (Windows specific, for other platforms, different commands might be needed).
    * `print("Gemini: " + str(response.text))`: Prints the model's response, attributing it to "Gemini." 

**Summary:**

This script allows you to have a conversation with the Gemini language model through text input and output. You provide prompts or questions, and Gemini responds based on its training data and the parameters set in the configuration.

