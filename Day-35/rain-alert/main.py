import requests
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

MY_LAT = 24.093120 # Your latitude
MY_LONG = 82.651551 # Your longitude
MY_APPID = os.environ['APP_ID']

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_APPID,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# for i in range(len(weather_slice)):
#     if weather_data["hourly"][i]["weather"][0]["id"] < 700:
#         print("bring an umbrella")

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to carry an umbrella! ☂️",
        from_='*******',
        to='*****'
    )

    print(message.sid)
