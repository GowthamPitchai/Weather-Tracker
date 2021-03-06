import html
from twilio.rest import Client
import requests
API_KEY = "your's api-key"
API = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = "your's account-sid"
AUTH_TOKEN = "your's auth-token"

parameters = {
    "lat": your's lat,
    "lon": your's lon,
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
        from_='yours from no',
        to='yours to no'
    )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="No Rain Enjoy Your Day..!!",
        from_='yours from no',
        to='yours to no'
    )
