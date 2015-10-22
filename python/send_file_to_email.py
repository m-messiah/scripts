#!/usr/bin/python
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

filename="269.zip"
email="malware-report@example.com"
msg = MIMEMultipart(
    From=email,
    To="test@example.com",
    Subject="Potential malware",
    Date=formatdate(localtime=True)
)
msg.attach(MIMEText("Additional information"))
with open(filename, "rb") as archive:
    msg.attach(MIMEApplication(
        archive.read(),
        Content_Disposition='attachment; filename="269.zip"',
        Name="269.zip"
    ))

smtp = smtplib.SMTP("smtp")
smtp.sendmail(email, "test@example.com", msg.as_string())
smtp.close()
