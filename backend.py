import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    generation_config=generation_config,
)

def GenerateResponse(input_text):
    response = model.generate_content([
    "input: who are you,",
    "output: I am Chiki-Chetah, your friendly chatbot.",
    "input: What all can you do?",
    "output: I can help you with any basic day-to-day problems that you might be facing! How can i help?",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text


# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ", GenerateResponse(string))