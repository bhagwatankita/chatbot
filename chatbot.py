import nltk
import spacy
from nltk.chat.util import Chat, reflections

nlp = spacy.load("en_core_web_sm")


pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What's on your mind?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!", "You can call me NLPBot."]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm here to help!", "I'm functioning perfectly, thanks for asking!"]
    ],
    [
        r"what can you do?",
        ["I can answer your queries, chat with you, and provide information.", 
         "Feel free to ask me anything!"]
    ],
    [
        r"bye|goodbye|see you",
        ["Goodbye! Have a great day!", "See you later! Take care."]
    ],
]

def spacy_chatbot_response(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    print("Processed Tokens:", tokens)

    if "weather" in tokens:
        return "I can't provide live weather updates, but you can check weather apps."
    elif "time" in tokens:
        return "I can't tell you the time, but I suggest looking at a clock."
    else:
        return "I'm not sure about that. Could you ask me something else?"

chatbot = Chat(pairs, reflections)

print("Chatbot: Hi there! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    elif user_input.strip() != "":
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:

            print(f"Chatbot: {spacy_chatbot_response(user_input)}")
