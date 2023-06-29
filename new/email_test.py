# the email address to send the email
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

'''
This script sends email to committer about the comparison figure of different test.
, the result YML file and the workflow link for quick access.
'''
# TODO: set up your email address and server
server = 'smtp.outlook.com'
port = 587
username = ''
password = ''
msg = MIMEMultipart()
to_email = 'Cyrusiris@outlook.com'
from_email = username
with open("example output/result.yml", "rb") as attachment:
    part = MIMEApplication(
        attachment.read(),
        Name=basename("result.yml")
    )
    attachment.close()
part['Content-Disposition'] = 'attachment; filename="%s"' % basename("result.yml")
msg.attach(part)

# Send the email using the SMTP server
msg.attach(MIMEText(f"Workflow link "))
msg['Subject'] = "test"
msg['From'] = from_email
msg['To'] = to_email
with smtplib.SMTP(server, port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()