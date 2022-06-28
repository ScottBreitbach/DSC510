'''import JSON data'''
'''doesn't seem to work but it sounds like we'll do more JSON in the future'''

import requests
import json

url = "https://haveibeenpwned.com/api/v2/breaches?domain=adobe.com"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "abd8a247-803a-45bd-9996-7c51b462c3d6"
    }

response = requests.request("GET", url, data=payload, headers=headers)
parsed = json.loads(response.txt)
print(json.dumps(parsed, indent=4, sort_keys=True))
