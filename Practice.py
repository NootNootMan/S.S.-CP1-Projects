import os
from google import genai

# 1. Initialize the client with your API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

print("🤖 AI Bot initialized! Type 'quit' to exit.\n")

# 2. Start a continuous conversation loop
while True:
    # Get what you want to say to the AI
    user_input = input("You: ")
    
    # Check if you want to stop the program
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    # 3. Send your message to the Gemini model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
    )
    
    # 4. Print the AI's response
    print(f"AI: {response.text}\n")