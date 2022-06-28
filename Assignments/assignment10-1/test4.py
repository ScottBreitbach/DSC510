'''check if nsfw returned'''

import requests
import json

url = "https://api.chucknorris.io/jokes/random"

response = requests.request("GET", url)
res = json.loads(response.text)
# test = 'golf balls'
nsfwList = ["piss", "ass", "balls", "shit", "damn", "fuck", "cunt", # capital
            # Shit, words containing *ass*
            "8=D", "climax", "sodomize", "bitch", "sex", "erection",
            "dick", "penis", "cock", "vagina", "sperm", "rape",
            "masterbat", "masturbat", "condom", "hung"]
# if any(word in test for word in nsfwList):
if res["categories"] == ["explicit"]:
    print('Sorry, this joke is explicit:\n', res['value'])
elif any(word in res['value'] for word in nsfwList):
    print('Sorry, this joke is NSFW:\n', res['value'])
else:
    print(response.text)
    print('Heres the "joke":', res['value'])
