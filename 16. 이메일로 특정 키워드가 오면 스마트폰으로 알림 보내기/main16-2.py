from base64 import encode
import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encdoe = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = ''
pw = ''
imap.login(id, pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'ALL')
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_mesaage = email.message_from_bytes(raw_email, policy=policy.default)

    print('='*70)
    print('FROM:', email_mesaage['FROM'])
    print('SENDER:', email_mesaage['Sender'])
    print('TO:', email_mesaage['To'])
    print('DATE:', email_mesaage['Date'])
    subject, encode = find_encoding_info(email_mesaage['Subject'])
    print('SUBJECT:', subject)

    print('[CONTENT]')
    message =''
    if email_mesaage.is_multipart():
        for part in email_mesaage.get_payload():
            if part.get_content_type() == 'text/plain':
                bytes = part.get_playload(decode=True)
                encode = part.get_content_charset()
                message = message + str(bytes, encode)
            
    print(message)
    print('='*70)

imap.close()
imap.logout()

# 이메일 본문 내용을 읽는 코드 만들기