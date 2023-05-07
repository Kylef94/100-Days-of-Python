import requests

api_key = "6b722804fc23751078c165b625a76fd4"
api = "https://api.openweathermap.org/data/3.0/onecall"

params = {
"lat" : "51.507351",
"lon" : "-0.127758",
"appid" : api_key
}

data = requests.get(url=api, params=params)
print(data)

