"""
Code inspired by FreeCodeCamp: youtube.com/watch?v=FGdiSJakIS4&ab_channel=freeCodeCamp.org
"""

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('<insert gmail>', password)

msg = MIMEMultipart()
msg['From'] = 'John'
msg['To'] = '<insert email>'
msg['Subject'] = 'Test Project'

with open('msg.txt', 'r') as f:
    body = f.read()

msg.attach(MIMEText(body, 'plain'))

image = 'bridge.jpeg'
attachment = open(image, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',
             'attachment; filename = {}.format(image)')
msg.attach(p)

text = msg.as_string()
server.sendmail('<insert email>', text)
