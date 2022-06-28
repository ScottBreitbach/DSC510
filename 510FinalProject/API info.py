
openweathermap.orgopenweathermap.org
Current weather data

Send to Kindle
We provide 40-year Historical weather data for ANY location. The price is highly competitive - only 10$ per location! Learn more
Call current weather data for one location
Please remember that all Examples of API calls that listed on this page are just samples and do not have any connection to the real API service!
By city name
Description:
You can call by city name or city name, state code and country code. API responds with a list of weather parameters that match a search request.
API call:
api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={your api key}

api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={your api key}

Parameters:
q city name, state code and country code divided by comma, use ISO 3166 country codes. You can specify the parameter not only in English. In this case, the API response should be returned in the same language as the language of requested location name if the location is in our predefined list of more than 200,000 locations.

Examples of API calls:
api.openweathermap.org/data/2.5/weather?q=London

api.openweathermap.org/data/2.5/weather?q=London,uk

By city ID
Description:
You can call by city ID. API responds with exact result.
We recommend to call API by city ID to get unambiguous result for your city.

List of city ID city.list.json.gz can be downloaded here http://bulk.openweathermap.org/sample/

API call:
api.openweathermap.org/data/2.5/weather?id={city id}&appid={your api key}

Parameters:
id City ID
Examples of API calls:
api.openweathermap.org/data/2.5/weather?id=2172797

By geographic coordinates
API call:
api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}

Parameters:
lat, lon coordinates of the location of your interest
Examples of API calls:
api.openweathermap.org/data/2.5/weather?lat=35&lon=139

API response:
{"coord": { "lon": 139,"lat": 35},
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 281.52,
    "feels_like": 278.99,
    "temp_min": 280.15,
    "temp_max": 283.71,
    "pressure": 1016,
    "humidity": 93
  },
  "wind": {
    "speed": 0.47,
    "deg": 107.538
  },
  "clouds": {
    "all": 2
  },
  "dt": 1560350192,
  "sys": {
    "type": 3,
    "id": 2019346,
    "message": 0.0065,
    "country": "JP",
    "sunrise": 1560281377,
    "sunset": 1560333478
  },
  "timezone": 32400,
  "id": 1851632,
  "name": "Shuzenji",
  "cod": 200
}
Description:
Please note if country is not specified then the search works for USA as a default.

API call:
api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}

Parameters:
zip zip code

Examples of API calls:
api.openweathermap.org/data/2.5/weather?zip=94040,us

API response:
{
  "coord": {"lon": -122.08,"lat": 37.39},
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
}

Cities within a rectangle zone
Description:
JSON returns the data from cities within the defined rectangle specified by the geographic coordinates.

Parameters:
bbox bounding box [lon-left,lat-bottom,lon-right,lat-top,zoom]

callback javascript functionName

cluster use server clustering of points. Possible values ​​are [yes, no]

lang language [ru, en ... ]

Examples of API calls:
http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10
Cities in cycle
Description:
JSON returns data from cities laid within definite circle that is specified by center point ('lat', 'lon') and expected number of cities ('cnt') around this point. The default number of cities is 10, the maximum is 50.

Parameters:
lat latitude

lon longitude

callback functionName for JSONP callback.

cluster use server clustering of points. Possible values ​​are [yes, no]

lang language [en , ru ... ]

cnt number of cities around the point that should be returned

Examples of API calls:
http://api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10

Call for several city IDs
Parameters:
id City ID
Examples of API calls:
http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric


We provide number of bulk files with current weather and forecasts.
More information is on the Bulk page.

Examples of bulk files:
http://bulk.openweathermap.org/sample/


Example of API response:
{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
}

Parameters:
coord
coord.lon City geo location, longitude
coord.lat City geo location, latitude
weather (more info Weather condition codes)
weather.id Weather condition id
weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
weather.description Weather condition within the group. You can get the output in your language. Learn more
weather.icon Weather icon id
base Internal parameter
main
main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
main.humidity Humidity, %
main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.sea_level Atmospheric pressure on the sea level, hPa
main.grnd_level Atmospheric pressure on the ground level, hPa
wind
wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
wind.deg Wind direction, degrees (meteorological)
clouds
rain
rain.1h Rain volume for the last 1 hour, mm
rain.3h Rain volume for the last 3 hours, mm
snow
snow.1h Snow volume for the last 1 hour, mm
snow.3h Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
sys.type Internal parameter
sys.id Internal parameter
sys.message Internal parameter
sys.country Country code (GB, JP etc.)
sys.sunrise Sunrise time, unix, UTC
sys.sunset Sunset time, unix, UTC
timezone Shift in seconds from UTC
id City ID
name City name
cod Internal parameter

Example of API response:
<current>
<city id="0" name="Mountain View">
<coord lon="-122.09" lat="37.39"/>
<country>US</country>
<timezone>-28800</timezone>
<sun rise="2020-01-07T15:22:59" set="2020-01-08T01:05:37"/>
</city>
<temperature value="278.07" min="273.15" max="282.59" unit="kelvin"/>
<feels_like value="275.88" unit="kelvin"/>
<humidity value="86" unit="%"/>
<pressure value="1026" unit="hPa"/>
<wind>
<speed value="0.93" unit="m/s" name="Calm"/>
<gusts/>
<direction value="23" code="NNE" name="North-northeast"/>
</wind>
<clouds value="1" name="clear sky"/>
<visibility value="16093"/>
<precipitation mode="no"/>
<weather number="800" value="clear sky" icon="01n"/>
<lastupdate value="2020-01-07T11:33:40"/>
</current>
Parameters:
city
city.id City ID
city.name City name
city.coord
city.coord.lon City geo location, longitude
city.coord.lat City geo location, latitude
city.country Country code (GB, JP etc.)
timezoneShift in seconds from UTC
city.sun
city.sun.rise Sunrise time
city.sun.set Sunset time
temperature
temperature.value Temperature
temperature.min Minimum temperature at the moment of calculation. This is minimal currently observed temperature (within large megalopolises and urban areas), use this parameter optionally.
temperature.max Maximum temperature at the moment of calculation. This is maximal currently observed temperature (within large megalopolises and urban areas), use this parameter optionally.
temperature.unit Unit of measurements. Possilbe valure is Celsius, Kelvin, Fahrenheit.
feels_like
feels_like.value Temperature. This temperature parameter accounts for the human perception of weather.
feels_like.unit Unit of measurements. Possilbe valure is Celsius, Kelvin, Fahrenheit. Unit Default: Kelvin
humidity
humidity.value Humidity value
humidity.unit Humidity units, %
pressure
pressure.value Pressure value
pressure.unit Pressure units, hPa
wind
wind.speed
wind.speed.value Wind speed
wind.speed.unit Wind speed units, m/s
wind.speed.name Type of the wind
wind.direction
wind.direction.value Wind direction, degrees (meteorological)
wind.direction.code Code of the wind direction. Possilbe value is WSW, N, S etc.
wind.direction.name Full name of the wind direction.
clouds
clouds.value Cloudiness
clouds.name Name of the cloudiness
visibility
visibility.value Visibility, meter
precipitation
precipitation.value Precipitation, mm
precipitation.mode Possible values are 'no", name of weather phenomena as 'rain', 'snow'
weather
weather.number Weather condition id
weather.value Weather condition name
weather.icon Weather icon id
lastupdate
lastupdate.value Last time when data was updated

List of weather condition codes
List of weather condition codes with icons (range of thunderstorm, drizzle, rain, snow, clouds, atmosphere including extreme conditions like tornado, hurricane etc.)


Min/max temperature in current weather API and forecast API
Example of current weather API response:
"main":{
"temp":306.15, //current temperature
"pressure":1013,
"humidity":44,
"temp_min":306, //min current temperature in the city
"temp_max":306 //max current temperature in the city
},
For comparison look at example of daily forecast weather API response:
"dt":1406080800,
"temp":{
        "day":297.77,  //daily averaged temperature
        "min":293.52, //daily min temperature
        "max":297.77, //daily max temperature
        "night":293.52, //night temperature
        "eve":297.77, //evening temperature
        "morn":297.77}, //morning temperature

Format
Description:
JSON format is used by default. To get data in XML or HTML formats just set up mode = xml or html.

Parameters:
mode - possible values are xml and html. If mode parameter is empty the format is JSON by default.
Examples of API calls:
JSON api.openweathermap.org/data/2.5/weather?q=London

XML api.openweathermap.org/data/2.5/weather?q=London&mode=xml

HTML api.openweathermap.org/data/2.5/weather?q=London&mode=html

Description:
Standard, metric, and imperial units are available.

Parameters:
units metric, imperial. When you do not use units parameter, format is Standard by default.

Examples of API calls:
standard api.openweathermap.org/data/2.5/find?q=London

metric api.openweathermap.org/data/2.5/find?q=London&units=metric

imperial api.openweathermap.org/data/2.5/find?q=London&units=imperial

You can use lang parameter to get the output in your language.
Translation is applied for the city name and description fields.

API call:
http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&appid={your api key}&lang={lang}
Parameters:
lang language code
Examples of API calls:
http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&lang=zh_cn We support the following languages that you can use with the corresponded lang values:
#	Language code	Language
1	af	Afrikaans
2	al	Albanian
3	ar	Arabic
4	az	Azerbaijani
5	bg	Bulgarian
6	ca	Catalan
7	cz	Czech
8	da	Danish
9	de	German
10	el	Greek
11	en	English
12	eu	Basque
13	fa	Persian (Farsi)
14	fi	Finnish
15	fr	French
16	gl	Galician
17	he	Hebrew
18	hi	Hindi
19	hr	Croatian
20	hu	Hungarian
21	id	Indonesian
22	it	Italian
23	ja	Japanese
24	kr	Korean
25	la	Latvian
26	lt	Lithuanian
27	mk	Macedonian
28	no	Norwegian
29	nl	Dutch
30	pl	Polish
31	pt	Portuguese
32	pt_br	Português Brasil
33	ro	Romanian
34	ru	Russian
35	sv, se	Swedish
36	sk	Slovak
37	sl	Slovenian
38	sp, es	Spanish
39	sr	Serbian
40	th	Thai
41	tr	Turkish
42	ua, uk	Ukrainian
43	vi	Vietnamese
44	zh_cn	Chinese Simplified
45	zh_tw	Chinese Traditional
46	zu	Zulu
Description:
To use JavaScript code you can transfer callback functionName to JSONP callback.
Examples of API calls:
api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test

