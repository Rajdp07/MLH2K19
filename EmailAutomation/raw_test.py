import smtplib
from email.mime.multipart import MIMEMultipart
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imghdr
from pathlib import Path

class Sender:
    def __init__(self,receivers,subject, body):
        self.sender = 'debjit16.dc@gmail.com'
        self.passwrd = 'uudmhbjprlxrcycy'
        self.receivers = receivers
        self.subject = subject
        self.body = body

    def sendEmails(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender, self.passwrd)
            try:
                for emails in self.receivers:
                    msg = MIMEMultipart()
                    msg['To'] = emails
                    msg['From'] = self.sender
                    msg['Subject'] = self.subject
                    text = MIMEText(self.body, 'plain')
                    msg.attach(text)
                    part = MIMEBase('application', "octet-stream")
                    with open('attachment.jpg', 'rb') as f:
                        part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition','attachment; filename="{}"'.format(Path('attachment.jpg').name))
                    msg.attach(part)                 

                    my_msg = msg.as_bytes().decode()
                    smtp.sendmail(self.sender, emails, my_msg)
                    # print('Email Successfully sent to {}'.format(emails))
            except Exception as e:
                print(e)

