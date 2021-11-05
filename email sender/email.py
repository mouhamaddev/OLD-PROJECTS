import ssl, smtplib

port = 465


email = input("Enter your email: ")

password = input("Enter your password: ")


recipient = input("Enter the email address to send the email to: ")

subject = input("What is the subject of the email: ")

text = input("Type your email here: ")

message = "Subject: {}\n\n{}".format(subject, text)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as servers:

        server.login(email,password)

        server.sendmail(email, recipient,message)

