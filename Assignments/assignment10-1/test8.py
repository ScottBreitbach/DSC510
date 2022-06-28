'''internet try / requests'''

try:
    response = requests.request("GET", base_url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("broken internet maybe?")     # can get this error by using wrong URL(city/zip/state)or wrong api key
        print(e)                            # "couldn't find <city/state/zip>; check your spelling and try again"
    except Exception as e:
        print("something else going on here:")
        print(e)                            # can't make this one happen, but keep just in case?
    else:
        try:
            resString = json.loads(response.text)
            print(resString)
            print("success!")
        except Exception as e:
            print("that didn't work, here's why:")
            print(e)
except Exception as e:
    print("What's going on here?")          # <airplane mode> "check your internet connection"
    print(e)


# '''clear screen test'''
# # This doesn't seem to work in PyCharm :(
#
# import os
# from os import system, name
#
# def cls():
#     # os.system('cls' if os.name=='nt' else 'clear')
#     if name == 'nt':
#         _ = system('cls')
#     else:
#         _ = system('clear')
#
# print('test')
# cls()
# print('test2')
# os.system('cls')
