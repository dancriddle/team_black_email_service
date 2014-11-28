import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object('config')

def send_mail_function(address, subject, message):
    
    print "Start sendmail"
    
    # Email sending parameters from config file
    EMAIL_SERVER = app.config['EMAIL_SERVER']
    EMAIL_USER = app.config['EMAIL_USER']
    EMAIL_PASSWORD = app.config['EMAIL_PASSWORD']
    EMAIL_FROM_ADDRESS = app.config['EMAIL_FROM_ADDRESS']
    
    
    # Email parameters from web service call
    TO = address
    SUBJECT = subject
    TEXT = message
    
    # Prepare actual message
    message = MIMEText(TEXT, 'html')
    message['From']=EMAIL_FROM_ADDRESS
    message['To']=TO
    message['Subject']=SUBJECT
    
    #print "Printing message"
    #print message.as_string()
    #print "EOM"
    
    # Send the mail
    server = smtplib.SMTP(EMAIL_SERVER)
    server.starttls()
    server.login(EMAIL_USER,EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM_ADDRESS, TO, message.as_string())
    server.quit()
    
    print "End sendmail"
