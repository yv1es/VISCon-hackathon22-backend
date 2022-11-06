
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.message import EmailMessage
#from events.models import Event
from backend.secretsFile import mailinglist_password

SERVERIP = "3.122.227.211/"
SENDER = "tamam.mailinglist@mail.ch"
PASSWORD = mailinglist_password

def createMail(recipient, subject, content):
    email_message = EmailMessage()
    email_message.add_header('To', ', '.join([recipient]))
    email_message.add_header('From', SENDER)
    email_message.add_header('Subject', subject)
    email_message.set_content(content)
    return email_message

def sendMail(recipient, subject, content):
    mail = createMail(recipient, subject, content)
    try:
        smtp_server = SMTP_SSL('smtp.mail.ch', port=SMTP_SSL_PORT)
        #smtp_server.set_debuglevel(1)  # Show SMTP server interactions
        smtp_server.login(SENDER, PASSWORD)
        smtp_server.sendmail(SENDER, [recipient], mail.as_bytes())
        smtp_server.quit()
        print("sent mail")

    except Exception as ex:
        print("Couldn't send mail...", ex)
    
def sendNotification(recipientList, event):
    for recipient in recipientList:
        subject = "Eventnotification - " + event.name
        greeting = \
            "Hello there,\nThere\'s a new event that might interest you!"
        relevantInfo = (event.link if event.link else "") + event.shortDescription

        closing = "You can always unsubscribe by following this link:\n" + "http://" + SERVERIP + "api/subscribe/?mail_address=" + recipient + "&unsubscribe"

        content = greeting + "\n\n" + relevantInfo + "\n\n" + closing
    
        sendMail(recipient, subject, content)

