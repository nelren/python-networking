import smtplib
from email import encoders
from email.mime.text import MIMEText #Ordinary test to use
from email.mime.base import MIMEBase #For attachment
from email.mime.multipart import MIMEMultipart #Fro the hole thing

server = smtplib.SMTP('smtp.gmail.com',465) #Specify the smtp server hostname and port

server.ehlo

with open('pass.txt', 'r') as file: #open pass.tx as "file" alias
    password = file.read()

#log in to the mail server
server.login('datanetec@gmail.com', password)

#Define message (Header)
msg = MIMEMultipart()
msg['From'] = 'Test Sender'
msg['To'] = 'nallauca@tutanota.com'
msg['Subject'] = 'This is a test email about python.'

#Load the message
with open('attachment.txt', 'r') as file:
    message = file.read

#something to attach to the message
msg.attach(MIMEText(message,'plain')) #attach file as plain text