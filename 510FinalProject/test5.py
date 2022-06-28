'''play with URL requests'''

import requests
import json

# base_url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
# base_url = "http://api.openweathermap.org/data/2.5/weather?zip=98166"
base_url = "http://api.openweathermap.org/data/2.5/weather?id=5072006&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
# base_url = "http://api.openweathermap.org/data/2.5/onecall?lat=40.8&lon=-96.67&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
# base_url = "http://api.openweathermap.org/data/2.5/weather?q=lincoln&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
# api_key = "&appid=b1e5c368120adc33cee07aad2dcdc946"

# response = requests.request("GET", base_url+api_key)
# response = requests.request("GET", base_url)

try:
    response = requests.request("GET", base_url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("broken internet maybe?")     # can get this error by using wrong URL(city/zip/state)or wrong api key
        print(e)                            # "couldn't find <city/state/zip>; check your spelling and try again"
    except Exception as e:
        print("something else going on here:")
        print(e)                            # can't make this one happen, but keep just in case?
    else:
        try:
            resString = json.loads(response.text)
            print(resString)
            print("success!")
        except Exception as e:
            print("that didn't work, here's why:")
            print(e)
except Exception as e:
    print("What's going on here?")          # <airplane mode> "check your internet connection"
    print(e)
# print(response)
# if response.status_code == 200:
#     print("success!")
#     resString = json.loads(response.text)
# else:
#     print("lets try something else")
#     # do something else
# print(resString)

# if resString['cod'] == '200':
#     print("success!")
# else:
#     print("lets try something else")

# city_name = input("enter city name: ")
# response = requests.request("GET", base_url+"q="+city_name+api_key)
# print(response) # tells response code (200 = success)
# resString = json.loads(response.text)
# print(resString)    # returns json string

    # {
    # "id": 5072006,
    # "name": "Lincoln",
    # "state": "NE",
    # "country": "US",
    # "coord": {
    #   "lon": -96.666962,
    #   "lat": 40.799999
    # }
