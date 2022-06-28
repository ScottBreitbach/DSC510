'''yahoo finance api that converts USD to other currency;
let's pull down data, convert JSON to Python object and parse out some info'''

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

# print(source)
data = json.loads(source)
# print(json.dumps(data, indent=2))       # prints more nicely formatted
# print(len(data['list']['resources']))   # to verify actually 188 resources in list

for item in data['list']['resources']:
    # print(item)
    name = item['resource']['fields']['name']   # might have to dig down a bit to get what you're looking for
    price = item['resource']['fields']['price']
    print(name, price)          # should print just the name and the price


'''use these conversion rates to convert USD to a specific currency'''
# create a new dictionary w/names as key and conversion rates as value
usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']   # might have to dig down a bit to get what you're looking for
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(usd_rates['USD/EUR'])     # would print: 0.846500
# to convert 50 USD to EUR:
print(50 * float(usd_rates['USD/EUR']))     # would print: 42.325
