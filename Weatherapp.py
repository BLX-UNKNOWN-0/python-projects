# BLX-UNKNOWN-0
# PROJECT 10 // WEATHER APP
#I don't know viewr's what went wrong i tried a lot but it didn't run and yeah here is not any api keys cause i already tried it but in my laptop it doesn't worked so i left only code here, if you want you can check may in your laptop it will run!

import requests

API_KEY = "paste_your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q"       : city,
            "appid"   : API_KEY,
            "units"   : "metric"  # celsius
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        name    = data["name"]
        country = data["sys"]["country"]
        temp    = data["main"]["temp"]
        feels   = data["main"]["feels_like"]
        humidity= data["main"]["humidity"]
        desc    = data["weather"][0]["description"]

        print(f"\n--- Weather in {name}, {country} ---")
        print(f"  Condition : {desc}")
        print(f"  Temp      : {temp}°C")
        print(f"  Feels like: {feels}°C")
        print(f"  Humidity  : {humidity}%")

    except requests.exceptions.ConnectionError:
        print("No internet connection!")

def menu():
    print("...WEATHER APP...")

    while True:
        city = input("\nEnter city (or 0 to quit): ").strip()
        if city == "0":
            print("Bye!")
            break
        get_weather(city)

menu()