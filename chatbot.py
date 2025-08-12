# Simple Rule-Based Chatbot using if-else

print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! How can I help you today?")
    elif user_input in ["how are you", "how are you doing"]:
        print("Chatbot: I'm just a program, but I'm doing great!")
    elif "your name" in user_input:
        print("Chatbot: I'm a simple Python chatbot created using if-else.")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif "help" in user_input:
        print("Chatbot: Sure! I can answer greetings, tell you about myself, and say goodbye.")
    else:
        print("Chatbot: Sorry, I don't understand that.")
