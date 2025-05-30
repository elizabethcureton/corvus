from ai_client import ask_ai

print("Ask the AI a question. Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ("exit", "quit"):
        break
    print(f"AI: {ask_ai(prompt)}\n{'-'*40}")