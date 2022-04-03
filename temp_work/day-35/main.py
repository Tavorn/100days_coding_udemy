import requests
import os
from twilio.rest import Client

"""
Environment variable

$ export OWM_API_KEY=*******************************
$ export AUT_TOKEN=*******************************
"""


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = "*******************************"
auth_token = os.environ.get("AUT_TOKEN")

lat = 13.80
lon = 100.58
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    # print("Bring an umbrella.")

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_='*******************************',
            to='*******************************'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    # print("Bring an umbrella.")

    message = client.messages \
        .create(
            body="It wil not rain today. Don't bring an ☔️",
            from_='*******************************',
            to='*******************************'
    )
    print(message.status)
    # print(message.sid)

# print(hours12_list)
# print(weather_id)
#
# if weather_id <= 700:
#     print("hello World")
# else:
#     print("Ooop")
