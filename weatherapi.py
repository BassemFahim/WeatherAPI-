import requests
import json
key  ="d2c9ab493f246ecfa28c57b33c577494"
url  = "https://api.openweathermap.org/data/2.5/weather?"
while True:
        name = input("enter country: ").strip()
        if name == 'q':
                break
        params = {
        "appid" : key,
        "q":name
        }
        res = requests.get(url, params=params)
        res = json.loads(res.content)
        print(res['weather'][0]['description'])
