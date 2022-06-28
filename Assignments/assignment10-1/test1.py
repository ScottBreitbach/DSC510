'''API example from slides'''

import requests
import json

url = "https://api.chucknorris.io/jokes/random"

response = requests.request("GET", url)
res = json.loads(response.text)
print('Just the "joke":', res['value'])

'''ignore the rest of this probably'''
# response = requests.request("GET", url)
# # print("response type", type(response))
#
# # print(response.text)
# # print("response.text type", type(response.text))
#
# testString = response.text
#
# res = json.loads(testString)
# # print("res type:", type(res))
# # print(res)
#
# print('Just the "joke":', res['value'])
#
# # jokeDict = dict()
# # jokeDict = response.text
# #
# # print("jokeDict type:", type(jokeDict))
# # print(jokeDict['value'])
#
# # joke = response['value']
# # print(joke)
#
# #
# # # This is the query string that we're going to submit to the URL.
# # # Notice that this is a dictionary with key value pairs.
# # querystring = {"zip":"68522",
# #                "APPID":"d5751b1a9e2e4b2b8c7983646072da8b"}
# # # This is used to submit any headers we need for the HTTP Request.
# # # Notice that the headers are a dictionary.
# # headers = {'cache-control':'no-cache'}
# #
# # # This is where the real magic occurs. We're going to submit all of our data to the URL in order to get
# # # data back in the form of JSON data. Keep in mind that the data you get back depends on the webservice
# # # that you interact with
# # response = requests.request("GET", url, headers=headers, params=querystring)
# # print(response.text)
