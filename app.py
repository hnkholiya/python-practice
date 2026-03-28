import requests,json
api_key="998e2aebe559b2a59590c9899ae24c40"
base_url="https://api.openweathermap.org/data/2.5/weather?"
city_name=input("Enter city name : ")
complete_url=base_url+"appid="+api_key+"&q="+city_name
response=request.get(complete_url)
temperature=response_from_website.json()['main']['temp']
print("current temp in=",temperature["main"]["temp"]-273,"celsius",city_name)

