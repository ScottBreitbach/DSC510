'''working on errors for web call'''

import requests
import json

url = "https://api.chucknorris.io/jokes/random"

response = requests.request("GET", url)
# print(response.raise_for_status())
print(response)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
else:
    try:
        res = json.loads(response.text)
        print('<The "joke">:', res['value'])
    except Exception as e:
        print('res exception', e)


# print(response)
# res = json.loads(response.text)
# print(res)
# print('<The "joke">:', res['value'])
