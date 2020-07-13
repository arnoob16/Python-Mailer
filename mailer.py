import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

senderMail = "arnab4srk@gmail.com"
receiverMail = "arnabdeep6@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Mail Subject"
message["From"] = senderMail
message["To"] = receiverMail

html = """\
<html>
    <body>
        <h1>Hey there aspiring Web Developers</h1>
        <h5>Here's a mail made in HTML</h5>
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Adipisci delectus eaque omnis voluptate voluptatum ab similique sapiente, 
            rem harum mollitia reprehenderit iste illo cumque totam at tempora, 
            perspiciatis ullam deleniti.
        </p>
  </body>
</html>
"""

messageMail = MIMEText(html, "html")
message.attach(messageMail)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(senderMail, password)
    server.sendmail(
        senderMail, receiverMail, message.as_string()
    )