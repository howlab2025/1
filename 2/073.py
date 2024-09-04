import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# SMTP 서버 접속 - TLS 방식
smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_server.ehlo()
smtp_server.starttls()   # TLS Encription 동작

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
smtp_server.login(user=my_addr, password=my_pw)

# 이메일 베이스 객체 (본문 메시지 + 첨부 파일)
my_msg = MIMEBase('multipart', 'mixed')

# 이메일 메시지 구성
subject = '파일 첨부 테스트'
body = '''
파일 첨부를 위한 테스트입니다.

첨부 파일을 확인해 주세요. 

감사합니다. 

'''

recipients = 'python100@naver.com'

my_msg.attach(MIMEText(body, 'plain', 'utf-8'))
my_msg['Subject'] = subject
my_msg['To'] = recipients


# 첨부 파일 구성
file_name = 'financials.xlsx'
file_path = os.path.join(os.getcwd(), 'data', file_name)

my_attach = MIMEBase('application', 'octet-stream')
my_attach.set_payload(open(file_path, 'rb').read())
encoders.encode_base64(my_attach)
my_attach.add_header('Content-Disposition', 'attachment; filename=%s' % file_name)
my_msg.attach(my_attach)

# 이메일 발송
smtp_server.sendmail(from_addr=my_addr,        
                     to_addrs=recipients, 
                     msg=my_msg.as_string())          

# 이메일 서버 종료하기
smtp_server.quit()
print("%s 님에게 이메일을 발송하였습니다." % recipients)