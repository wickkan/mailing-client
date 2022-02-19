import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('throwaway197256@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'John'
msg['To'] = 'testmails@spam1.de'
msg['Subject'] = 'Test Project'

with open('msg.txt', 'r') as f:
    msg = f.read()

msg.attach()
