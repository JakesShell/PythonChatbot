from textblob import TextBlob

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0:
        return "I'm glad to hear that!"
    elif analysis.sentiment.polarity < 0:
        return "I'm sorry to hear that."
    return "Thank you for sharing!"
