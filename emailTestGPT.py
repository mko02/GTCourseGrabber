#smtplibGPT

import smtplib

sender = 'hkoscript@outlook.com'
receivers = ['maxwangko1@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
