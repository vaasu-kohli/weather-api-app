import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
        else:
            print("City not found.")
            return None
    else:
        print("Error fetching coordinates.")
        return None


def get_weather(lat, lon, city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]

        print(f"\nWeather for: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
    else:
        print("Error fetching weather data.")


city = input("Enter your city name: ")
coords = get_coordinates(city)

if coords:
    lat, lon = coords
    get_weather(lat, lon, city)
