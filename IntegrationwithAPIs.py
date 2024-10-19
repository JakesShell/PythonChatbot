import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        return f"The weather in {city} is {data['weather'][0]['description']}."
    else:
        return "Sorry, I couldn't fetch the weather data."
