# course: DSC510
# assignment: 12.1 Final Project
# date: 29-May-2020
# name: Scott Breitbach
# description: pulls weather forecast for city or zip query

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather"
appid = "b1e5c368120adc33cee07aad2dcdc946"
units = "imperial"

def byCity(city):
    '''provides url parameters for search by city name'''
    print("Getting", city.title(), "...")
    querystring = {"q":city,
                   "appid":appid,
                   "units":units}
    return querystring

def byCityState(city, state):
    '''provides url parameters for search by city and state'''
    print("Getting", city.title(), state.upper(), "...")
    location = city+","+state+",us"
    querystring = {"q":location,
                   "appid":appid,
                   "units":units}
    return querystring

def byZip(zip):
    '''provides url parameters for search by zip code'''
    print("Getting", zip, "...")
    querystring = {"zip":zip,
                   "appid":appid,
                   "units":units}
    return querystring

def req(querystring, cityZip):
    '''assembles url and requests information from openweathermap'''
    headers = {'cache-control':'no-cache'}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:\n", e)
            print(f"\n\033[1m ** Sorry, we couldn't find '{cityZip}'. **\n"
                  f"Please check your spelling and try again.\033[0m\n")
            main()
        except Exception as e:
            print("Error:\n", e)
            print("\n\033[1m ** Sorry, it seems something went awry. **\033[0m")
            allDone()
        else:
            resString = json.loads(response.text)
    except Exception as e:
        print("Error:\n", e)
        print("\n\033[1m ** Please check your internet connection. **\033[0m")
        allDone()
    return resString

def prettyPrint(resString, state):
    '''prints weather results for queried location'''
    city = resString['name'].upper()
    state = state.upper()
    temp = f"{resString['main']['temp']:.0f}\N{DEGREE SIGN}F"
    hi_temp = f"{resString['main']['temp_max']:.0f}\N{DEGREE SIGN}"
    lo_temp = f"{resString['main']['temp_min']:.0f}"
    feels_like = f"{resString['main']['feels_like']:.0f}\N{DEGREE SIGN}F"
    weather = resString['weather'][0]['main']
    conditions = resString['weather'][0]['description']
    wind_dir = windDirection(resString['wind']['deg'])
    wind_mph = f"{resString['wind']['speed']:.0f}"

    if state == "":
        print(f'\n\t ==== {city} ====')
    else:
        print(f'\n\t ==== {city}, {state} ====')
    print(f'\tTemperature: {temp} ({lo_temp}-{hi_temp})\n'
          f'\tFeels like: {feels_like}\n'
          f'\tCurrently: {weather} ({conditions})\n'
          f'\t{wind_dir} winds at {wind_mph} mph')
    moreDetail(resString)

def moreDetail(resString):
    '''provides addional weather details upon request'''
    moreDeets = input("\nWould you like more detail? "
                      "[\033[1mY\033[0m/\033[1mN\033[0m] >> ")
    if moreDeets.lower() == "y":
        pressure = f"{resString['main']['pressure']:.0f}"
        humidity = f"{resString['main']['humidity']:.0f}"
        cloudCvr = f"{resString['clouds']['all']:.0f}"

        print(f'\n\tPressure: {pressure} mmHg\n'
              f'\tHumidity: {humidity}%\n'
              f'\tCloud cover: {cloudCvr}%')
        # main()
    elif moreDeets.lower() == "n":
        # print("\n === \033[1mOkay, have a great day!\033[0m ===")
        pass
    else:
        print('\nSorry, "'+moreDeets+'"', "is not recognized.")
        moreDetail(resString)

def windDirection(wind_dir):
    '''returns cardinal direction given azimuth direction'''
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

def allDone():
    '''allows user to continue or exit'''
    done = input("\nWould you like to search again? "
                 "[\033[1mY\033[0m/\033[1mN\033[0m] >> ")
    if done.lower() == "y":
        main()
    elif done.lower() == "n":
        print("\n === \033[1mOkay, have a great day!\033[0m ===")
        exit()
    else:
        print('\nSorry, "'+done+'"', "is not recognized.")
        allDone()

def main():
    '''requests location query from user and calls relevant functions'''
    state = ""
    city_or_zip = input("\nPlease enter \033[1mcity name\033[0m "
                        "or \033[1mzip code\033[0m: >> ")
    if city_or_zip.isdecimal() == True:
        querystring = byZip(city_or_zip)
    else:
        state = input("Please enter the \033[1mstate abbreviation\033[0m, or hit enter: >> ")
        if state == "":
            querystring = byCity(city_or_zip)
        else:
            querystring = byCityState(city_or_zip, state)

    resString = req(querystring, city_or_zip)
    prettyPrint(resString, state)
    allDone()

if __name__ == '__main__':
    print("Welcome to Scott's pretty okay weather thing!")
    main()
