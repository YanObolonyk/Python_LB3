import requests
from datetime import datetime
import pytz  # замість zoneinfo

API_KEY = "b52de3195d8a397bfc0bdfd3f911d754"
BASE_URL = "https://api.openweathermap.org/data/2.5/"
CITY = "Харків"

def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric&lang=ua"
    response = requests.get(url)

    if 200 <= response.status_code < 300:
        data = response.json()

        # часовий пояс України 
        ua_time = pytz.timezone("Europe/Kiev")

        return {
            "Погода в місті": data["name"],
            "Температура": f"{data['main']['temp']}°C",
            "Опис": data["weather"][0]["description"].capitalize(),
            "Координати": f"Широта: {data['coord']['lat']}, Довгота: {data['coord']['lon']}",
            "Вітер": f"{data['wind']['speed']} м/с, напрямок {data['wind']['deg']}°",
            "Атмосферний тиск": f"{data['main']['pressure']} hPa",
            "Вологість": f"{data['main']['humidity']}%",
            "Схід сонця": datetime.fromtimestamp(data["sys"]["sunrise"], ua_time).strftime('%H:%M:%S'),
            "Захід сонця": datetime.fromtimestamp(data["sys"]["sunset"], ua_time).strftime('%H:%M:%S')
        }
    else:
        return f"Помилка: {response.status_code}, {response.text}"

# перетворюємо у рядок
def format_weather_info(info):
    if isinstance(info, str):
        return info
    return "\n".join([f"{key}: {value}" for key, value in info.items()])

weather_info = get_weather(CITY)
print(format_weather_info(weather_info))