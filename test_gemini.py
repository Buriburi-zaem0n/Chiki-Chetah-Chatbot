import google.generativeai as genai

print("google-generativeai version:", genai.__version__)

genai.configure(api_key="AIzaSyDNQF3-kP9WZOd6kxs6WJ9fNP_GpXX6pik")

print("Available models:")
for m in genai.list_models():
    print("-", m.name)
