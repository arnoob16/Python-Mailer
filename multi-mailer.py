import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("Enter the email from which you want to send mails. Please make sure that you've enabled 'Less Secure' apps in your account settings.")
senderMail = input()

print("Enter the count of your mail list: \n")
count = int(input())

print("Enter the maillist: \n")
maillist = []
for i in range(0,count):
    maillist.append(input())

password = input("Type your password. : \n")

for receiverMail in maillist:
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Mail Subject"
    message["From"] = senderMail
    message["To"] = receiverMail

    html = """\
    <html>
        <head>
            <style>
                h5{
                    color: #fca400;
                }
            </style>
        </head>
        <body>
            <h1>Hey there LearnYuva Members</h1>
            <h5>Here's a mail made in HTML, which was sent to you using python.</h5>
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
