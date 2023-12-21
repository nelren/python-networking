##################
# For this mailling client to work, if the mail account is a google account, first make 
# sure that the 2 step verification is enable (https://support.google.com/accounts/answer/185839?sjid=15619175640662600021-EU)
# and the app password is generated (https://support.google.com/accounts/answer/185833?sjid=15619175640662600021-EU#zippy=%2Cwhy-you-may-need-an-app-password%2Capp-passwords-revoked-after-password-change)
##################

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

msg_to = input("Write email account to send meesage:")

def login_mta(username, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    try:
        server.login(username, password)
        print("Login successful!")
        return server
    except smtplib.SMTPAuthenticationError as e:
        print(f"Login failed. SMTP Authentication Error: {e}")

#Message headers
def compose_message():
    msg = MIMEMultipart()
    msg['From'] = 'Nelson Allauca' 
    msg['To'] = msg_to
    msg['Subject'] = 'This is a test email about python.'
    return msg

# Text message to be sent
def attach_text_message(msg):
    with open('attachment.txt', 'r') as file:
        message = file.read()
    msg.attach(MIMEText(message, 'plain'))
    return msg

# Attach an image file
def attach_image(msg):
    img_file = 'coding.jpeg'
    with open(img_file, 'rb') as file:
        img_attachment = file.read()
    
     #Create payload object and attach
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload(img_attachment)
    encoders.encode_base64(payload) #use encoders
    payload.add_header('Content-Disposition', f'attachment; filename={img_file}')
    msg.attach(payload)
    return msg

#Send email to receipient
def send_email():
    username = 'nelson.allauca@ecreationmedia.tv'
    with open('pass.txt', 'r') as file:
        password = file.read().strip()

    server = login_mta(username, password)

    #if login is correct attach message, file and send.
    if server:
        msg = compose_message()
        msg = attach_text_message(msg)
        print(msg)
        msg = attach_image(msg)
        text = msg.as_string()
        server.sendmail('Nelson Allauca',msg_to, text)
        server.quit() # Close the connection

if __name__ == "__main__":
    send_email()
