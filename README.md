team_black_email_service
========================
Email service.  This provides a pure web interface for sending emails.  Contains no business logic or message content/formatting.

Dependencies
========================
Flask

mime

Resolve Python dependencies by running pip install -r requirements.txt

Config File
========================
The email service requires a config file config.py.  Create this file and put in the following parameters for the email provider:

EMAIL_SERVER = email server address and port

EMAIL_USER = email login user

EMAIL_PASSWORD = email login password

EMAIL_FROM_ADDRESS = the address emails will be sent from
    
How to use it
========================
Start it by running service.py.  This recieves requests and calls send_mail_function in
sendmail.py, which creates the SMTP connection and sends the email.  Web services on the 
following URLs

https://service_address/ - URL to check if email service is running

https://service_address/test  - URL to send a test email with hard-coded parameters

https://service_address/sendmail - URL for email service. This needs a post request with the following parameters:

Parameters for email service - all POST parameters

name (currently ignored)

email - the email to send to

subject - message subject

body - subject body 
