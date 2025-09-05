import requests


def simple_weather():
    api_key = "52292923ae35c6e490b3e355a6afaa5b"
    city = ("Tver', RU")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        data = response.json()

        print(f"Погода в {data['name']}:")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Ощущается как: {data['main']['feels_like']}°C")
        print(f"Погода: {data['weather'][0]['description']}")
        print(f"Влажность: {data['main']['humidity']}%")

    except:
        print("Не удалось получить данные о погоде")


simple_weather()