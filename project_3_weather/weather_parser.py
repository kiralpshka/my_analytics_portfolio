import requests
from datetime import datetime

print(" Погода в Воронеже")
print("")

url = "https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6173&current_weather=true"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        current = data['current_weather']
        temperature = current['temperature']
        wind_speed = current['windspeed']
        
        print(f"Дата и время: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
        print(f" Температура:   {temperature}°C")
        print(f" Ветер:         {wind_speed} м/с")
        print("")
        print("Данные успешно получены через Open-Meteo API")
    else:
        print(" Ошибка при получении данных")

except requests.exceptions.ConnectionError:
    print("Нет подключения к интернету")
except Exception as e:
    print(f"Ошибка: {e}")