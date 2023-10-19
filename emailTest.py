from email.message import EmailMessage
import ssl
import smtplib
import certifi

print(certifi.where())
print("``````````")

sender = "mmmkmmkk1234@gmail.com"
password = "tkvfonxxipoevrar"
receiver = "maxwangko1@gmail.com"

subject = "Email Test"
body = """
Body of my email test
"""

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

#Set security
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())