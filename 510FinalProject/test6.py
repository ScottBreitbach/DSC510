# city_or_zip.isalpha()
print("new hampton".isalpha())

# # Python3 code to demonstrate working of
# # Find dictionary matching value in list
# # Using loop
#
# # # Initialize list
# # test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
# # 			{'it' : 5, 'is' : 7, 'best' : 8},
# # 			{'CS' : 10}]
# #
# # # Printing original list
# # print("The original list is : " + str(test_list))
#
# import requests
# import json
#
# # base_url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
# # api_key = "&appid=b1e5c368120adc33cee07aad2dcdc946"
# # with open(base_url, 'r', encoding='utf-8') as f:
# #     test_list = json.load(f)
#
# with open('city.list.json', 'r', encoding='utf-8') as f:  # these two rows work
#     test_list = json.load(f)
#
# # response = requests.request("GET", base_url)
# # print(response)
# # self.encoder = json.load(open(vocab_file, 'r', encoding='utf-8'))
# # test_list = json.loads(open(response.text, 'r', encoding='utf-8'))
# # print(resString)
#
# # Using loop
# # Find dictionary matching value in list
# res = None
# for sub in test_list:
#     if sub['name'] == 'Lincoln':
#         res = sub
#         break
#
# # printing result
# print("The filtered dictionary value is : " + str(res))
