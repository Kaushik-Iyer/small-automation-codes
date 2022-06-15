import smtplib
import ssl
from email.message import EmailMessage
import requests
import geocoder

g = geocoder.ip('me')

API_KEY = 'User API Key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

subject = 'Email from Python'
body = "Test email"
sender = 'kushlaser@gmail.com'
receiver = 'sohamprabhu999@gmail.com'
password = 'sender email password'

print("Choose an option:")
print("1.Choose a city")
print("2.Send data of city you are in")
print("3.Send custom message")
choice = int(input())

if choice == 1:
    city = input("Enter a city name: ")
    req_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(req_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        print(f'The weather is {weather}')
        print(temperature)
        subject = f'The weather is {weather} and the temperature is currently {temperature} Celsius'
    else:
        print("Error")

elif choice == 2:
    city = g.city
    req_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(req_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        print(f'The weather is {weather}')
        print(temperature)
        subject = f'The weather is {weather} and the temperature is currently {temperature} Celsius'
    else:
        print("Error")

elif choice == 3:
    print("Enter message to be sent: ")
    subject = input()

message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("Success")
