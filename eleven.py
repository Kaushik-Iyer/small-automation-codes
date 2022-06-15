import smtplib
import ssl
from email.message import EmailMessage
import requests

subject = '11:11'
body = "11:11"
sender = 'kushlaser@gmail.com'
receiver = ['Enter list of receiver email ids']
password = 'password of sender email id'


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