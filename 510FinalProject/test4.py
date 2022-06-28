'''automatically check if letters or numbers entered'''

'''outline of program'''

import requests
import json

def req(url):
    response = requests.request("GET", url)
    # print(response) # tells response code (200 = success)
    resString = json.loads(response.text)
    # print(resString)    # returns json string
    # print("It is currently", resString['main']['temp'], u"\b\N{DEGREE SIGN}F with", resString['weather'][0]['description'])
    prettyPrint(resString)

def byCity(city):
    print("Getting", city.title(), "...")
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    api_key = "&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
    url = base_url+city+api_key
    req(url)

def byZip(zip):
    print("Getting", zip, "...")
    base_url = "http://api.openweathermap.org/data/2.5/weather?zip="
    api_key = "&appid=b1e5c368120adc33cee07aad2dcdc946&units=imperial"
    url = base_url+zip+api_key
    req(url)

def allDone():
    done = input("\nWould you like to search again? "
                 "[\033[1mY\033[0m/\033[1mN\033[0m] >> ")
    if done.lower() == "y":
        main()
    elif done.lower() == "n":
        print("Okay, have a great day!")
        exit()
    else:
        print('Sorry, "'+done+'"', "is not recognized.")
        allDone()

def prettyPrint(resString):
    city = resString['name'].upper()
    temp = f"\033[1m{resString['main']['temp']:.0f}\N{DEGREE SIGN}F\033[0m"
    hi_temp = f"{resString['main']['temp_max']:.0f}\N{DEGREE SIGN}"
    lo_temp = f"{resString['main']['temp_min']:.0f}\N{DEGREE SIGN}"
    feels_like = f"{resString['main']['feels_like']:.0f}\N{DEGREE SIGN}F"
    weather = resString['weather'][0]['main']
    conditions = resString['weather'][0]['description']
    wind_dir = windDirection(resString['wind']['deg'])
    wind_mph = f"{resString['wind']['speed']:.0f}"

    print(f'\n={city}= {temp} (hi {hi_temp}/lo {lo_temp})\n'
          f'Feels like: {feels_like}\n'
          f'Currently: {weather} ({conditions})\n'
          f'With {wind_dir} winds at {wind_mph} mph')

def windDirection(wind_dir):
    if wind_dir <= 22.5:
        direction = 'N'
    elif wind_dir <= 67.5:
        direction = 'NE'
    elif wind_dir <= 112.5:
        direction = 'E'
    elif wind_dir <= 157.5:
        direction = 'SE'
    elif wind_dir <= 202.5:
        direction = 'S'
    elif wind_dir <= 247.5:
        direction = 'SW'
    elif wind_dir <= 292.5:
        direction = 'W'
    elif wind_dir <= 337.5:
        direction = 'NW'
    else:
        direction = 'N'
    return direction

def main():
    city_or_zip = input("Please enter \033[1mcity name\033[0m "
                        "or \033[1mzip code\033[0m: >> ")
    if city_or_zip.isalpha() == True:
        byCity(city_or_zip)
    elif city_or_zip.isdecimal() == True:
        byZip(city_or_zip)
    else:
        print('Sorry, "'+city_or_zip+'"', "is not recognized.")
        main()
    allDone()

if __name__ == '__main__':
    print("Welcome to the weather thing!\n")
    main()
