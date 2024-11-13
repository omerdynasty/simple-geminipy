# Simple Gemini-PY
A very simple script to use Gemini API with python.

I tried my best to make it as user friendly as possible, you can look below for detailed explanations of the code or other information, but if you just want to use it, you don't need to tinker much...

Elbette, bu kodun ne yaptığını kısaca İngilizce olarak açıklayabilirim:

**English Explanation:**

This Python code interacts with Google's Generative AI to provide text-based responses to user queries. Here's a breakdown of its primary functions:

- AI EXPLANATION -
- 
1. **Import Necessary Libraries:** Imports modules for various tasks, including file operations, text manipulation, regular expressions, and interaction with the Google Generative AI API.
2. **Read API Key:** Reads the API key from a file named 'api_key.txt' which is required to authenticate with the Google AI service.
3. **Configure API:** Sets up the Google Generative AI environment using the obtained API key.
4. **Create Model:** Instantiates a 'gemini-1.5-flash' model, which is a language model capable of generating text.
5. **Prompt User:** Asks the user to input a question or prompt.
6. **Generate Response:** Sends the user's input to the model and receives a generated text response.
7. **Remove Markdown:** Removes any Markdown formatting (like headings, lists) from the generated response to get plain text.
8. **Print Response:** Prints the final, cleaned-up response from the model.

**In essence, this code acts as a simple chatbot, using Google's AI to generate text responses based on user prompts.** 

**Would you like me to explain any specific part of the code in more detail?** 

For instance, I can provide a more in-depth explanation of:

* How the API key is used to authenticate with the Google AI service.
* The purpose of the `to_markdown` function and why it's not used in this specific example.
* What regular expressions are and how `re.sub` is used to remove Markdown formatting.

Just let me know!

