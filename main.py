
from datetime import datetime

BOT_NAME = "Keda AI"

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Welcome to Keda AI.",
    "how are you": "I am doing great! Thanks for asking.",
    "your name": "My name is Keda AI.",
    "python": "Python is a powerful programming language.",
    "help": "You can ask about my name, Python, or the current time."
}


def get_response(message, username):
    message = message.lower().strip()

    if message in ("bye", "exit", "quit"):
        return f"Goodbye, {username}! Keep coding!"

    if message == "time":
        return datetime.now().strftime("%H:%M:%S")

    if message == "date":
        return datetime.now().strftime("%Y-%m-%d")

    if message == "my name":
        return f"Your name is {username}."

    for keyword, answer in responses.items():
        if keyword in message:
            return answer

    return "I don't know that yet. Type 'help' to see what I can do."


def main():
    print("=" * 35)
    print(f"Welcome to {BOT_NAME}!")
    print("=" * 35)

    username = input("What is your name? ").strip()

    if not username:
        username = "Friend"

    print(f"\nNice to meet you, {username}!")
    print("Type 'help' for help or 'exit' to quit.\n")

    while True:
        message = input(f"{username}: ")
        reply = get_response(message, username)

        print(f"{BOT_NAME}: {reply}")

        if message.lower().strip() in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
