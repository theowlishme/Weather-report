import requests
API_KEY = "c1e60d0837cf47029c887d1f1bfedfe6"
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print("error")
        return
    data = response.json()
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
city_name = input("Enter city name: ")
get_weather(city_name)
