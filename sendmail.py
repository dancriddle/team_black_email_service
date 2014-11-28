import smtplib

def send_mail_function(address, subject, message):
    
    print "Start sendmail"
    
    # Email sending parameters
    
    SERVER = "smtp.gmail.com:587"
    user = "jplservice00@gmail.com"
    password = "t3stjpl3tter"
    FROM = "jplservice00@gmail.com"
    
    # Old parameters
    #TO = ["jplservice00@gmail.com"] # must be a list
    #SUBJECT = "Hello!"
    #TEXT = "JPL restriction message."
    
    # Read parameters into variables
    TO = [address] # must be a list
    SUBJECT = subject
    TEXT = message
    
    # Prepare actual message
    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    #print "Printing message"
    #print message
    #print "EOM"
    
    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.starttls() # from https://www.pythonanywhere.com/forums/topic/450/
    server.login(user,password) # from https://www.pythonanywhere.com/forums/topic/450/
    server.sendmail(FROM, TO, message)
    server.quit()
    
    print "End sendmail"
