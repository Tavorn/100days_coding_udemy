import requests
from datetime import datetime as dt


SUNSET_SUNRISE_API = "https://api.sunrise-sunset.org/json"
MY_LAT = 13.756331
MY_LONG = 100.501762

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(SUNSET_SUNRISE_API, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.now()
print(time_now.hour)


# endpoint = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=endpoint)
# response.raise_for_status()
# data = response.json()
# print(data)
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
#
#
# iss_position = (latitude, longitude)
#
# print(iss_position)


