from flask_mail import Mail, Message
import json
from modules import app
def sendMail(senderEmail, data):
    mail = Mail(app)
    msg = Message(subject = "This is the data for which you had queried in the form.", sender=app.config['MAIL_USERNAME'], recipients=[senderEmail])
    msg.body = "Hello Flask message sent from Flask-Mail" + json.dumps(data["data"]["DATA"])
    mail.send(msg)
    print("sent Successfully!!!!")