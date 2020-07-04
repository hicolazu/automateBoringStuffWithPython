# pip install imapclient
# pip install pyzmail
from datetime import date
import imapclient
import pyzmail

gmail_user = 'python.fortest123@gmail.com'
gmail_password = 'fortestpython123'


def printemailmessages(emailmessages):
    for emailmessage in emailmessages:
        print(str(emailmessage.get_addresses('from')) + "\n", str(emailmessage.get_addresses('to')) + "\n",
              emailmessage.get_subject() + "\n", emailmessage.text_part.get_payload().decode('UTF-8'))


def getmessages(server):
    UIDs = server.search(['SINCE', date(2020, 7, 3)])
    rawMessage = server.fetch(UIDs, ['BODY[]', 'FLAGS'])
    messages = []
    for uid in UIDs:
        messages.append(pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]']))
    return messages


try:
    client = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    client.login(gmail_user, gmail_password)
    client.select_folder('INBOX', readonly=True)
    printemailmessages(getmessages(client))
except ValueError as valerr:
    print('Something went wrong...')
    print(valerr)
