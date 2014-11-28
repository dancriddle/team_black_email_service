import requests
import os
import urllib
import urllib2
from sendmail import send_mail_function

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return "Email Service Active"
  
@app.route('/test')
def test():
  send_mail_function("jplservice00@gmail.com", "Test email", "Someone hit the test URL")
  return "Test Email Sent"

@app.route('/sendmail', methods=['POST'])
def send_mail():
  print "sendmail service"
  
  # Get email parameters
  name=request.form['name'] # This is currently not used
  email=request.form['email']
  subject=request.form['subject']
  body=request.form['body']
  
  # Send mail
  send_mail_function(email, subject, body)
  return "OK"

if __name__ == '__main__':
  app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5009)))