import imaplib
import email
from email import policy
import requests
import json
import time

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSalckWebhook(strText):
    headers = {
        "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "OK"
    else:
        return "ERROR"

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = ''
pw = ''
imap.login(id, pw)

send_list =[]

while True:
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'ALL')
        all_email = data[0].split()
        last_email = all_email[-5:]

        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default)

            emain_from = str(email_message['From'])
            emain_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)

            if subject_str.find("결과") >= 0:
                slack_send_message = emain_from + '\n' + emain_date + '\n' + subject_str
                if slack_webhook_url not in send_list:
                    sendSalckWebhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message)
        
        time.sleep(30)
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()

# 이메일로 특정 키워드가 오면 스마트폰으로 알림 보내기