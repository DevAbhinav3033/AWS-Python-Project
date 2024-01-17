
import requests

def get_weather(api_key,city):
    base_url="http://api.openweathermap.org/data/2.5/weather"
    params={
        "q" : city,
        "appid" : api_key
    }

    res=requests.get(base_url,params=params)
    data=res.json()
    return data

