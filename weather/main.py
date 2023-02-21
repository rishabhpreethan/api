import datetime as d
import requests

base_url="https://api.openweathermap.org/data/2.5/weather?"

# api key from https://home.openweathermap.org/api_keys
api_key="enter api key here"
city=input("enter your city\n")
# city="Bangalore"

url=base_url+"appid=" + api_key+"&q="+city

response=requests.get(url).json()

# print(response)

# function to covert kelvin into celcius and fahrenheit
def k_to_c_and_f(k):
    c=k-273.15
    f=c*(9/5)+32
    return f,c

# extracting temperature from the json formatted response
temp_k=response['main']['temp']
# using the function to convert the kelvin to celcius and fahrenheit
temp_c,temp_f=k_to_c_and_f(temp_k)


# extracting the feels like temperature which is in kelvin
feels_like_k=response['main']['feels_like']
# coverting that into celsuis and fahrenheit
feels_like_c,feels_like_f=k_to_c_and_f(feels_like_k)

wind_speed=response['wind']['speed']

humidity=response['main']['humidity']

# it is a list of dictionaries 
# print line 12 to see the data in json
description=response['weather'][0]['description']

sunrise=d.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset=d.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# printing all the data
print("temp in celsius",temp_c,"C")
print("temp in f",temp_f,"F")
print("feels like ",feels_like_c,"C")
print("wind speed",wind_speed,"kmph")
print("humididty",humidity,"%")
print("description",description)
print("sunrise",sunrise,"local time")
print("sunset",sunset,"local time")