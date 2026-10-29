import random
from datetime import datetime

print("=" * 35)
print("       PYTHON CHATBOT 🤖")
print("=" * 35)

print("Chatbot: Hello! I'm your chatbot.")
print("Chatbot: What's your name?")

name = input("You: ")

print(f"Chatbot: Nice to meet you, {name}!")
print("Chatbot: You can talk to me.")
print("Chatbot: Type 'bye' to exit.")

responses = {
    "hello": ["Hello!", "Hey there!", "Hi! How are you?"],
    "how are you": [
        "I'm doing great!",
        "I'm functioning perfectly!",
        "I'm ready to chat!"
    ],
    "what is your name": [
        "I'm PythonBot!",
        "You can call me PythonBot."
    ],
    "what can you do": [
        "I can chat with you and answer simple questions."
    ],
    "who created you": [
        "You created me using Python!"
    ]
}

while True:
    user_message = input(f"{name}: ").strip().lower()

    if user_message == "bye":
        print(f"Chatbot: Goodbye, {name}! See you next time! 👋")
        break

    elif user_message == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: The current time is {current_time}.")

    elif user_message in responses:
        print("Chatbot:", random.choice(responses[user_message]))

    else:
        print("Chatbot: I'm not sure how to answer that yet.")
        print("Chatbot: I'm still learning!")

