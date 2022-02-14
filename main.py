import html
from twilio.rest import Client
import requests
API_KEY = "your's API-key"
API = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = "your's account-id"
AUTH_TOKEN = "your's authentication-token"

parameters = {
    "lat": your's lat,
    "lon": your's long,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(API, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False
for data in weather_slice:
    condition_code = data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Rain Rain On The Way.. Stay Safe..!!",
        from_='from phone no.',
        to='to phone no'
    )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="No Rain Enjoy Your Day..!!",
        from_='from phone no.',
        to='to phone no'
    )
