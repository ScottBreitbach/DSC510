'''try to search city.list.json; download and unzip if not available'''

import gzip
import requests
import json
import os

try:
    with open('city.list.json', 'r', encoding='utf-8') as file:
        test_list = json.load(file)

    city = input("Enter city name: >> ")

    res = None
    for sub in test_list:
        if sub['name'] == city.title():
            res = sub
            break

    # printing result
    print("The filtered dictionary value is : " + str(res))
except:
    # url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
    # url = "http://bulk.openweathermap.org/snapshot/city.list.json.gz"
    url = "http://bulk.openweathermap.org/snapshot/city.list.json.gz?appid=b1e5c368120adc33cee07aad2dcdc946"
    req = requests.get(url)

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'city.list.json.gz'), 'wb') as f:
        f.write(req.content)

    f = gzip.open('city.list.json.gz', 'rb')
    file_content = f.read()
    list = open('city.list.json', 'wb')
    list.write(file_content)
    f.close()
    list.close()

    # print(file_content)
    '''this part should be in a function or something'''
    with open('city.list.json', 'r', encoding='utf-8') as file:
        test_list = json.load(file)

    city = input("Enter city name: >> ")

    res = None
    for sub in test_list:
        if sub['name'] == city.title():
            res = sub
            break

    # printing result
    print("The filtered dictionary value is : " + str(res))

# url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
# req = requests.get(url)
#
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# with open(os.path.join(__location__, 'city.list.json.gz'), 'wb') as f:
#     f.write(req.content)
#
# f = gzip.open('city.list.json.gz', 'rb')
# file_content = f.read()
# list = open('city.list.json', 'wb')
# list.write(file_content)
# f.close()
# list.close()
#
# # print(file_content)
#
# with open('city.list.json', 'r', encoding='utf-8') as file:
#     test_list = json.load(file)
#
# city = input("Enter city name: >> ")
#
# res = None
# for sub in test_list:
#     if sub['name'] == city.title():
#         res = sub
#         break
#
# # printing result
# print("The filtered dictionary value is : " + str(res))







