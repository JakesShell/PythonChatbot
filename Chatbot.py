from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Create a new chatbot instance
chatbot = ChatBot(
    'EnhancedBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',  # Responds with the current time
    ],
    database_uri='sqlite:///database.db'  # Save conversations in a SQLite database
)

# Set up the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with English corpus data
trainer.train("chatterbot.corpus.english")

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Function to save conversation history
def save_conversation(user_input, bot_response):
    with open('conversation_history.txt', 'a') as f:
        f.write(f"You: {user_input}\nEnhancedBot: {bot_response}\n")

if __name__ == "__main__":
    print("Hello! I am EnhancedBot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("EnhancedBot: Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"EnhancedBot: {response}")
        
        # Save the conversation
        save_conversation(user_input, response)
