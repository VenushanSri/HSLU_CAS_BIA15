import requests
from datetime import datetime
#import pandas as pd

#API Key from OpenWeather
apiKey = '<5be1bbb289a67600ba770ccbb9233209>'

def getResponse(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print(e)  
        raise

def getTargetCities():
    cityList = ([
                    "Rotkreuz",
                    "Oberrüti",
                    "Luzern",
                    "Zürich",
                    "Bern",
                    "Genf",
                    "Basel",
                    "London",
                    "Paris",
                    "Chicago",
                    "Rom",
                    "Amsterdam",
                    "Berlin",
                    "Budapest",
                    "Copenhagen",
                    "Dublin",
                    "Helsinki",
                    "Madrid",
                    ])
    return cityList

try:
    utcTimestamp = datetime.utcnow()   
    cityList = getTargetCities()
    
    for city in cityList:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric'
        response = getResponse(url)
        jsonResponse = response.content
        print(jsonResponse)
        print("#######################################")

except Exception as e:
    print(e)  
    raise
