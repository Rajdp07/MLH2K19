import smtplib
from email.mime.multipart import MIMEMultipart
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imghdr
from pathlib import Path
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import font

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

## Utility Functions
def sendEmails(email_subject, receivers, email_body):
    try:
        s = Sender(receivers, email_subject, email_body)
        s.sendEmails()
        # print('All Emails sent Successfully!!!!')
        receiver_entry.delete('1.0', tk.END)
        subject_box.delete('1.0', tk.END)
        body_box.delete('1.0', tk.END)
        tkMessageBox.showinfo("Success", "All Emails sent Successfully!!!!")
    except Exception as e:
        # print('Some Error Occurred!!!')
        receiver_entry.delete('1.0', tk.END)
        subject_box.delete('1.0', tk.END)
        body_box.delete('1.0', tk.END)
        tkMessageBox.showinfo('Failure', e)

def getInput():
    email_inp = receiver_entry.get("1.0","end-1c").split()
    email_subject = subject_box.get("1.0","end-1c")
    email_body = body_box.get("1.0","end-1c")
    sendEmails(email_subject, email_inp, email_body)


if __name__ == "__main__":
    H = 500
    W = 1100
    root = tk.Tk()
    root.title('Custom Mailing Software')
    canvas = tk.Canvas(root, height = H, width = W)
    canvas.pack()

    top_frame = tk.Frame(root, bd=5, bg='#6CB484')
    top_frame.place(anchor = 'n', relx=0.5, rely=0, relheight = 0.1, relwidth=0.75)

    head_label = tk.Label(top_frame, text = 'Custom Mailing System',font = ('Courier', 20))
    head_label.place(relheight=1, relwidth=1)

    bottom_frame = tk.Frame(root, bd=7, bg='#6CB484')
    bottom_frame.place(relx=0.5, rely = 0.15, relheight=0.84, relwidth = 0.75, anchor = 'n')

    recipients_label = tk.Label(bottom_frame, text='Receipients', font=('Courier', 15))
    recipients_label.place(relx=0, rely = 0.1, relheight=0.1, relwidth = 0.3)

    receiver_entry = tk.Text(bottom_frame, font=('Courier', 10), bd=2)
    receiver_entry.place(relx=0.35, rely=0, relheight=0.3, relwidth=0.6)

    subject_label = tk.Label(bottom_frame, text='Subject', font=('Courier', 15))
    subject_label.place(relx=0, rely = 0.38, relheight=0.1, relwidth = 0.3)

    subject_box=tk.Text(bottom_frame, height=2, width=10)
    subject_box.place(relx=0.35, rely = 0.38, relheight = 0.1, relwidth=0.6)


    body_label = tk.Label(bottom_frame, text='Body', font=('Courier', 15))
    body_label.place(relx=0, rely = 0.58, relheight=0.1, relwidth = 0.3)

    body_box=tk.Text(bottom_frame, height=2, width=10)
    body_box.place(relx=0.35, rely = 0.58, relheight = 0.3, relwidth=0.6)

    send_mail = tk.Button(bottom_frame, text = 'Send Mail', font=('Courier', 15),
    command = lambda : getInput())
    send_mail.place(relx=0.3, rely=0.9, relwidth=0.3, relheight=0.1)
    root.mainloop()











