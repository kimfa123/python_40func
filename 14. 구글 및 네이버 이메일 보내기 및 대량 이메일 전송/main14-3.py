import smtplib
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText

send_email = "kimfa123@naver.com"
send_pwd = "rlawlgns123!@#"

recv_email = "kimvz2002@hanmail.net"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = 'html로 보내는 메일 입니다.'
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #0000ff;">글자의 색상을 지정하거나</span></p>
<h1><span style="color: #000000;">크기를 조정할수 있습니다.</span></h1>
<p><span style="color: #000000;">표도 만들수 있습니다.</span></p>
<table style="height: 101px;" width="528">
<tbody>
<tr>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
<td style="width: 125px;">&nbsp;</td>
</tr>
</tbody>
</table>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

# html 형식 메일 보내는 코드 만들기