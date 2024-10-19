from chatterbot.trainers import ListTrainer

custom_conversations = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing well, thank you!",
    "What is your name?",
    "I am an enhanced chatbot.",
]

list_trainer = ListTrainer(chatbot)
list_trainer.train(custom_conversations)
