'''downloading and unzipping files'''

import gzip
import requests
import json
import os
import sys

url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
req = requests.get(url)

# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# with open(os.path.join(__location__, 'city.list.json.gz'), 'wb') as f:
#     f.write(req.content)

f = gzip.open('city.list.json.gz', 'rb')
file_content = f.read()
list = open('city.list.json', 'wb')
list.write(file_content)
f.close()
list.close()

# print(file_content)


# # print(file_content)
#
# # response = requests.request("GET", url)
# #
# # print(response)
# #
# # # resString = json.loads(response.text)
# # resString = json.load(response)
# #
# # print(resString)
#
# # with open(sys.path[0])
#
# # with open('/Users/micha/PycharmProjects/510FinalProject/city.list.json.gz', 'wb') as f:
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# # __location__ = os.path.realpath(os.path.join(sys.path[0], os.path.dirname('city.list.json.gz')))
# # f = open(os.path.join(__location__, 'city.list.json.gz'), 'wb')
#
# with open(os.path.join(__location__, 'city.list.json.gz'), 'wb') as f:
# # # with open(os.path.join(sys.path[0], 'city.list.json.gz')) as f:
#     f.write(req.content)
# # f.write(req.content)

print(req.status_code)
print(req.headers['content-type'])
print(req.encoding)

# f = gzip.open('city.list.json.gz', 'rb')
# file_content = f.read()
# f.close()
#
# print(file_content)

