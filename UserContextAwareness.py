user_context = {}

def get_response(user_input, user_id):
    # Store user preferences or previous questions
    if user_input.startswith("My name is "):
        name = user_input.split("My name is ")[1]
        user_context[user_id] = {'name': name}
        return f"Nice to meet you, {name}!"
    # Add more context handling as needed
    response = chatbot.get_response(user_input)
    return response
