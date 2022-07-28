import smtplib
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText
from email.mime.application import MIMEApplication

send_email = "kimfa123@naver.com"
send_pwd = "rlawlgns123!@#"

recv_email = "kimvz2002@hanmail.net"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = '첨부파일 테스트 입니다.'
msg['From'] = send_email
msg['To'] = recv_email

text = """
첨부파일 메일 테스트 내용 입니다.
감사합니다.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'/Users/jihoonkim/Desktop/python_40functions/14. 구글 및 네이버 이메일 보내기 및 대량 이메일 전송/첨부파일.txt'
with open(etc_file_path, 'rb') as f :
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment',filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login( send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

#네이버 이메일 보내기 및 대량 이메일 전송 