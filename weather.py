import requests

url = "http://api.weatherapi.com/v1/current.json?key=53b4c65060f64cb4bc1150430231809&q=63088&aqi=no"
response = requests.get(url)
weather_json = response.json()

print(weather_json)
