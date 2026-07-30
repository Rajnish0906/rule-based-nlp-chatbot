import json
import random
import re
from typing import Dict, List

# 1. Custom Chatbot Class for Clean OOP Architecture
class RuleBot:
    def __init__(self):
        # Memory to keep track of user context
        self.user_name = None
        
        # Defining Intents & Dynamic Patterns
        self.rules: Dict[str, Dict] = {
            "greeting": {
                "patterns": [r"\b(hi|hello|hey|greetings|hola|ssup|wassup)\b"],
                "responses": [
                    "Hey there! What's up?",
                    "Hello! Great to meet you.",
                    "Hey! How can I assist you today?"
                ]
            },
            "name_ask": {
                "patterns": [r"\b(your name|who are you|what should i call you)\b"],
                "responses": [
                    "I am RuleBot 2.0, your friendly neighborhood AI!",
                    "Call me RuleBot!"
                ]
            },
            "set_name": {
                "patterns": [r"\bmy name is ([a-zA-Z]+)\b", r"\bcall me ([a-zA-Z]+)\b"],
                "responses": [
                    "Nice to meet you, {name}!",
                    "Got it! I'll call you {name} from now on."
                ]
            },
            "how_are_you": {
                "patterns": [r"\b(how are you|how do you do|hows it going)\b"],
                "responses": [
                    "Running at 100% CPU efficiency! How about you?",
                    "Doing awesome! Hope you are having a killer day!"
                ]
            },
            "bye": {
                "patterns": [r"\b(bye|goodbye|see ya|exit|quit|tata)\b"],
                "responses": [
                    "Catch ya later!",
                    "Goodbye! Have a productive day ahead!"
                ]
            }
        }

    def process_input(self, user_input: str) -> str:
        clean_text = user_input.strip().lower()

        # Check for name extraction (Context Handling)
        for pattern in self.rules["set_name"]["patterns"]:
            match = re.search(pattern, clean_text)
            if match:
                self.user_name = match.group(1).capitalize()
                resp = random.choice(self.rules["set_name"]["responses"])
                return resp.format(name=self.user_name)

        # Match general intents using Regex
        for intent, data in self.rules.items():
            if intent == "set_name":
                continue  # Already handled above

            for pattern in data["patterns"]:
                if re.search(pattern, clean_text):
                    resp = random.choice(data["responses"])
                    # If user name is remembered, add a personal touch
                    if self.user_name and random.choice([True, False]):
                        resp += f" (by the way, {self.user_name})"
                    return resp

        # Smart Fallback Response
        return "Hmm, I didn't get that. Try asking something else or type 'help'!"

    def run(self):
        print("=" * 60)
        print("🚀 RuleBot 2.0 Active! Type 'exit' or 'bye' to terminate.")
        print("=" * 60 + "\n")

        while True:
            try:
                user_input = input("👤 You: ")
                if not user_input.strip():
                    continue

                bot_response = self.process_input(user_input)
                print(f"🤖 Bot: {bot_response}\n")

                # Check termination
                if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
                    break

            except KeyboardInterrupt:
                print("\n🤖 Bot: Force exit detected. Bye!")
                break

if __name__ == "__main__":
    bot = RuleBot()
    bot.run()