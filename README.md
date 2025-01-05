# Gemini (with Python)

A very simple script to use the Gemini API with Python. Designed to be user-friendly and easy to set up. Below, you'll find detailed explanations and instructions, but if you just want to use it, follow the quick setup guide. 🚀

---

## Before Starting ⚠

*Version 1.1* was developed to be more **user friendly**, if you just want to use Gemini with python (or in the console interface) you can use the bat scripts I wrote. *Version 1.1B* is a simpler version for those who are curious about the code, you can import it into your own projects. *Version 1.0* is a version written with less concern for Google documentation and the bat script is very simple, **not recommended for use**, but if you want to tinker with it, why not

# ❗ This section is for those more unfamiliar with computers, see below for better explanations.

## How to Use 📖 (USER FRIENDLY)

### 1. Install Required Libraries

Run the following commands to install the necessary libraries:
```bash
pip install google-cloud-aiplatform
pip install -q -U google-generativeai
```

### 2. Get Your API Key

1. Obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. With 1.1, use the bat script (writekey.bat) to write the API KEY to the file.

### 3. Run the Script

Just run the bat script (start.bat).

---

## How to Use 📚

### 1. Install Required Libraries

Run the following commands to install the necessary libraries:
```bash
pip install google-cloud-aiplatform
pip install -q -U google-generativeai
```

### 2. Get Your API Key

1. Obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Save your key in a file named `api_key.txt` in the same directory as the script.

### 3. Run the Script

Simply execute the script:
```bash
python gemini_chat.py
```

Type your input, and Gemini will respond! To exit, type `exit`.

---

## Developer Notes 😋

- **Python Version:** The script was developed using Python 3.12.4 but should work with other versions.
- **No Environment Variables:** The script reads the API key from a plaintext file (`api_key.txt`). While simple, this is not recommended for production. For better security, consider using environment variables.

Example for environment variables:
```python
import os
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GOOGLE_API_KEY:
    print("Error: API key not found in environment variables.")
    exit(1)
```

---

## What is Gemini? 🤔

Gemini is a product of Google AI that provides powerful language models for various applications, such as text generation, summarization, and chat interfaces. This project demonstrates how to interact with the Gemini API for creating a chatbot.

### Key Features:
1. **Text Generation:** Generate coherent and contextually relevant responses.
2. **Customizable Settings:** Adjust temperature, top-p, and other parameters for tailored outputs.
3. **Easy Integration:** Simple setup to start using the Gemini API.

---

## Code Overview 💻

### Main Functionality

1. **Import Required Libraries:**
    - Handles file operations and interacts with the Gemini API.
2. **Read API Key:**
    - Reads the API key from a file (`api_key.txt`).
3. **Configure API:**
    - Sets up the Gemini environment with the API key.
4. **Create Model:**
    - Initializes the `gemini-1.5-flash` model for chat.
5. **Start Chat Session:**
    - Begins a chat session with the model.
6. **Interactive Chat Loop:**
    - Allows the user to send prompts and receive responses in real time.

### Example Code Snippet

```python
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    print("Processing your input... Please wait.")
    response = chat_session.send_message(user_input)
    print(f"Gemini: {response.text}\n")
```
---
This Python code creates a chat interface using Google's Generative AI (GAI) library. You can interact with a large language model called Gemini through this interface.

**Here's a breakdown of the code:**

1. **Importing Libraries:**
    * import os: Imports the os library for operating system functionalities.
    * import google.generativeai as genai: Imports the Google Generative AI library.

2. **Reading API Key (Original Version):**
    * with open('api_key.txt', 'r') as f:: Opens the file api_key.txt in read mode.
    * GOOGLE_API_KEY = f.read().strip(): Reads the content of the file and removes leading/trailing whitespaces, storing it in the GOOGLE_API_KEY variable.

3. **Configuring GAI:**
    * genai.configure(api_key=GOOGLE_API_KEY): Configures the GAI library using the API key retrieved from the file.

4. **Chat Configuration:**
    * generation_config dictionary defines settings for text generation:
        * temperature: Controls the balance between creativity and coherence in the model's responses (higher values lead to more creative but potentially less relevant outputs).
        * top_p: Influences the probability distribution of the model's next word selection (higher values favor more likely words).
        * top_k: Limits the number of words the model considers for the next word (lower values promote more diverse outputs).
        * max_output_tokens: Sets the maximum length of the model's generated response.
        * response_mime_type: Specifies the format of the model's response (here, plain text).

5. **Creating the Model:**
    * model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config): Creates a generative model named "gemini-1.5-flash" and assigns the generation_config settings to it. This model name likely refers to a specific pre-trained model within the GAI library.

6. **Starting Chat Session:**
    * chat_session = model.start_chat(history=[]): Initiates a chat session with the model. The history parameter is an empty list in this case, which means the model won't have any previous conversation context to consider during its initial responses.

7. **Main Chat Loop:**
    * while 1 == 1 creates an infinite loop.
    * print("It may take a while to receive a response, please wait."): Informs the user that processing might take some time.
    * response = chat_session.send_message(str(input("You: "))): Prompts the user for input, converts it to a string, and sends it to the model using chat_session.send_message. The model response is stored in the response variable.
    * os.system('cls'): Clears the console screen (Windows specific, for other platforms, different commands might be needed).
    * print("Gemini: " + str(response.text)): Prints the model's response, attributing it to "Gemini." 

**Summary:**

This script allows you to have a conversation with the Gemini language model through text input and output. You provide prompts or questions, and Gemini responds based on its training data and the parameters set in the configuration.
---

## Trust and Security 🔒

This script is safe to use. The `api_key.txt` file is read locally, and no data is stored or shared beyond the API calls to Gemini. For added security, consider the following:

1. Use environment variables instead of plaintext files.
2. Avoid sharing your API key publicly.

---

## Resources 📚

- [Gemini API Quick Start](https://ai.google.dev/gemini-api/docs/quickstart?hl=en&lang=python)
- [Gemini API Get Started Guide](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=en)
- [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- [API Limits](https://aistudio.google.com/plan_information)

---

Happy coding! 🚀
