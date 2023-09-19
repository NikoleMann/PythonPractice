import requests

zipcode = input("What zipcode are you hiking in?")
url = "http://api.weatherapi.com/v1/current.json?key=53b4c65060f64cb4bc1150430231809&q=" + zipcode + "aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")
preciptation = weather_json.get("current").get("precip_in")

is_hiking = ""
if temp < 55.0 or temp > 80.0 or preciptation > 1.0:
    is_hiking = "Not Good for hiking"
else: is_hiking = "Good weather for hiking. "

print("The temprature is", temp, "and the weather is", description, "\n", is_hiking)