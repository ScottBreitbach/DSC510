'''different way to URL requests'''

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather"

zipCode = input("What is your zip code? ")

querystring = {"zip":zipCode,
               "appid":"d5751b1a9e2e4b2b8c7983646072da8b",
               "units":"imperial"}

headers = {'cache-control':'no-cache'}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

resString = json.loads(response.text)
print(resString)

#
# base_url = "http://api.openweathermap.org/data/2.5/weather?q=portlando&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
#
# try:
#     response = requests.request("GET", base_url)
#     try:
#         response.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print("broken internet maybe?")     # can get this error by using wrong URL(city/zip/state)or wrong api key
#         print(e)                            # "couldn't find <city/state/zip>; check your spelling and try again"
#     except Exception as e:
#         print("something else going on here:")
#         print(e)                            # can't make this one happen, but keep just in case?
#     else:
#         try:
#             resString = json.loads(response.text)
#             print(resString)
#             print("success!")
#         except Exception as e:
#             print("that didn't work, here's why:")
#             print(e)
# except Exception as e:
#     print("What's going on here?")          # <airplane mode> "check your internet connection"
#     print(e)
