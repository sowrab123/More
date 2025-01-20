# WEATHER REPORT
import requests

# 5.1 Setup Environment
API_KEY = "0233cc24641a18eb7a68b96322e51af7"                 # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" # OpenWeather API that retrieves weather data. 

# 5.3 Take the location name from the user
location = input("Enter the location (e.g., Dhaka or any city name): ") 

# 5.4 Get weather data from OpenWeather API for the given location name
try:
    response = requests.get(
        BASE_URL,
        params={
            "q": location,     # user search query
            "appid": API_KEY,  # API authencation check
            "units": "metric"  # For temperature in Celsius
        }
    )
    response.raise_for_status()    # Check for HTTP errors
    weather_data = response.json() # API response (JSON format)

    # 5.5 Print basic weather data
    print("\nWeather Report:")                                                  
    print(f"Location: {weather_data['name']}")                                  # Extracts the city name from
    print(f"Temperature: {weather_data['main']['temp']}°C")                     # Extracts the temperature in Celsius from 
    print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}") # description 
    print(f"Humidity: {weather_data['main']['humidity']}%")                     # Extracts the humidity percentage from
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")                   # Extracts the wind speed in meters/second from
    
    
# except requests.exceptions.HTTPError as http_err: # unauthorized access,
#     print(f"HTTP error occurred: {http_err}")
# except Exception as err:                          # generic error message.
#     print(f"An error occurred: {err}")
finally:
    quit()
