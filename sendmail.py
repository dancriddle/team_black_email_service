import smtplib
from email.mime.text import MIMEText

def send_mail_function(address, subject, message):
    
    print "Start sendmail"
    
    # Email sending parameters
    
    SERVER = "smtp.gmail.com:587"
    user = "jplservice00@gmail.com"
    password = "t3stjpl3tter"
    FROM = "jplservice00@gmail.com"
    
    # Read parameters into variables
    TO = address
    SUBJECT = subject
    TEXT = message
    
    # Prepare actual message
    message = MIMEText(TEXT, 'html')
    message['From']=FROM
    message['To']=TO
    message['Subject']=SUBJECT
    
    #print "Printing message"
    #print message.as_string()
    #print "EOM"
    
    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.starttls() # from https://www.pythonanywhere.com/forums/topic/450/
    server.login(user,password) # from https://www.pythonanywhere.com/forums/topic/450/
    server.sendmail(FROM, TO, message.as_string())
    server.quit()
    
    print "End sendmail"
