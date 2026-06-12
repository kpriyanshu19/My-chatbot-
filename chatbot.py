from groq import Groq
client = Groq(api_key="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")
print("Chatbot (Groq Streaming): Type 'quit', 'exit' or 'bye' to stop\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit","bye"]:
        print("\n Chatbot: Goodbye!")
        break
    print("Chatbot : ", end="", flush=True)
    
    stream = client.chat.completions.create(
        model="groq/compound",
        messages=[
            {"role": "system","content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
            
        ],
        stream=True
        
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="",flush=True)
    print()