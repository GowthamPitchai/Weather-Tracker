import html
from twilio.rest import Client
import requests
API_KEY = "d02282b70d628339e28edc9882c191df"
API = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = "ACbc668805ee5e5590dfec3591177be358"
AUTH_TOKEN = "2dd0aa4d23647d22987e9b662fb694c4"

parameters = {
    "lat": 10.95,
    "lon": 78.0833,
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
        from_='+18126134243',
        to='+918870264633'
    )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="No Rain Enjoy Your Day..!!",
        from_='+18126134243',
        to='+918870264633'
    )

# print(data["hourly"][0]["weather"])

