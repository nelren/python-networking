##################
# For this mailling client to work, if the mail account is a google account, first make 
# sure that the 2 step verification is enable (https://support.google.com/accounts/answer/185839?sjid=15619175640662600021-EU)
# and the app password is generated (https://support.google.com/accounts/answer/185833?sjid=15619175640662600021-EU#zippy=%2Cwhy-you-may-need-an-app-password%2Capp-passwords-revoked-after-password-change)
##################
import smtplib
from email import encoders
from email.mime.text import MIMEText #Ordinary test to use
from email.mime.base import MIMEBase #For attachment
from email.mime.multipart import MIMEMultipart #Fro the hole thing

# Connect to the SMTP server using TLS
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()

with open('pass.txt', 'r') as file: #open pass.tx as "file" alias
    password = file.read()

try:
    # Log in to the mail server
    server.login('nelson.allauca@ecreationmedia.tv', password)
    print("Login successful!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Login failed. SMTP Authentication Error: {e}")

#Define message (Header)
msg = MIMEMultipart()
msg['From'] = 'Nelson Allauca'
msg['To'] = 'nallauca@protonmail.com'
msg['Subject'] = 'This is a test email about python.'

#Load the message
with open('attachment.txt', 'r') as file:
    message = file.read()

print(message)

# Attach something to the message
msg.attach(MIMEText(message, 'plain'))

# Attach an image file
img_file = 'coding.jpeg' #sometimes the whole path is needed here

img_attachment = open(img_file, 'rb') #rb = read byte codes

#Create payload object
payload = MIMEBase ('application','octet-stream')
payload.set_payload (img_attachment.read())

#use encoders
encoders.encode_base64(payload)
payload.add_header ('Content-Disposition', f'attachment; filename={img_file}')
msg.attach(payload)

text = msg.as_string() #Finaly got everything as string
server.sendmail('Nelson Allauca','nallauca@protonmail.com',text)

# Close the connection
server.quit()