'''textwrap and bold'''

import requests
import json
import textwrap

url = "https://api.chucknorris.io/jokes/random"

response = requests.request("GET", url)
print(response)
res = json.loads(response.text)
print('\033[1m'+"Here's your joke:\n"+'\033[0m',
      textwrap.indent(textwrap.fill(res['value'], width=50), prefix='\t'))

# textwrap.fill(res['value'], width=50)
# textwrap.wrap()
