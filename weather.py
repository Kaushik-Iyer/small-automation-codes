import requests

API_KEY='User API Key from the website'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city=input("Enter a city name: ")
req_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(req_url)
if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]['description']
    temperature=round(data['main']['temp']-273.15,2)
    print(f'The weather is {weather}')
    print(temperature)
else:
    print("Error")
