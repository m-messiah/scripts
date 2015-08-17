#!/usr/bin/python
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.Utils import formatdate
import smtplib


msg = MIMEMultipart(
    From=settings.EMAIL,
    To="support@esetnod32.ru",
    Subject="Potential malware",
    Date=formatdate(localtime=True)
)
msg.attach(
    MIMEText("Additional information at "
             "http://cuckoo.skbkontur.ru/analysis/%s/" % task_id))
with open(filename, "rb") as archive:
    msg.attach(MIMEApplication(
        archive.read(),
        Content_Disposition='attachment; filename="%s"'
                            % file_info["sha256"] + ".zip",
        Name=file_info["sha256"] + ".zip"
    ))
smtp = smtplib.SMTP("smtp")
smtp.sendmail(settings.EMAIL, "support@esetnod32.ru", msg.as_string())
smtp.close()
