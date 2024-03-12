import requests
import json

"""
   Client.py
   - consumer of app.js weather rest api
   - provide city name via user input and display weather data for that city  
"""

### Params
API_URL = 'http://localhost:3000/weather?city='

### Utils

# kelvin to celsius converter
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# kelvin to fahrenheit converter
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# display weather data on successful request
def display_weather_data(weather_request):
    weather_data_dict = weather_request.json()
    weather_data_city_name = weather_data_dict['name']
    weather_data_city_country = weather_data_dict['sys']['country']
    weather_data_temp = weather_data_dict['main']['temp']
    weather_data_condition = weather_data_dict['weather'][0]['description']
    print('City: ' + weather_data_city_name + ', ' + weather_data_city_country)
    print('Temperature (Kelvin): ' + str(weather_data_temp))
    print('Temperature (Celsius): ' + str(kelvin_to_celsius(weather_data_temp)))
    print('Temperature (Fahrenheit): ' + str(kelvin_to_fahrenheit(weather_data_temp)))
    print('Conditions: ' + weather_data_condition)

# log weather data error for failed request
def log_weather_data_api_error(weather_request):
    if weather_request.json()['message'] == 'city not found': # handle city not found
        print('Sorry, we could not find the requested city')
    elif weather_request.status_code == 500: # handle internal server issue
        print('Internal server error:\n' + weather_request.json())
    else: # handle for unknown errors
        print('Unhandled Error:\n' + weather_request.json())

### Main
print('Welcome to Brian\'s weather reporter.')
while True:
    print('Type the name of the city (e.g. New York) to request weather data, or type exit to end the program:')
    input_city = input()
    if input_city == 'exit':
        break
    try:
        weather_request = requests.get(API_URL+input_city)
        if weather_request.status_code == 200:
            display_weather_data(weather_request)
        else:
            log_weather_data_api_error(weather_request)
        weather_request.raise_for_status()
    # generic error handling for request exceptions...
    except requests.exceptions.HTTPError as errh: 
        print("Http Error:\n",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:\n",errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:\n",errt)
    except requests.exceptions.RequestException as err:
        print("Unhandled Request Error:\n",err)
    except Exception as e:
        print("Unhandled Interal Error:\n", e)
print('stopping program')