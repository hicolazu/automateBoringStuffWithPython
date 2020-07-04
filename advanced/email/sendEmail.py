import smtplib

gmail_user = 'python.fortest123@gmail.com'
gmail_password = 'fortestpython123'
gmail_to = 'hicolazu22@hotmail.com'


def buildemailmessage(subject, body):
    return 'Subject: %s\n\nDear user, \n%s' % (subject, body)


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # configure the SMTP server (for Hotmail/Outlook -> smtp-mail.outlook.com)
    server.ehlo()
    server.starttls()  # starts TLS encryption
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, gmail_to,
                    buildemailmessage('Test email subject!', 'This is a test email from Python using smtplib.\n\n-Python'))
    server.quit()  # ends server
    print('Email sucessfully sent!')
except ValueError as valerr:
    print('Something went wrong...')
    print(valerr)
