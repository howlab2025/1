import smtplib
from email.mime.text import MIMEText

# SMTP 서버 접속 - TLS 방식
smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_server.ehlo()
smtp_server.starttls()   # TLS Encription 동작

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
smtp_server.login(user=my_addr, password=my_pw)

# 이메일 메시지 구성
subject = '제목 테스트'
body = '본문 테스트'

recipients = 'python100@naver.com'

my_msg = MIMEText(body)
my_msg['Subject'] = subject
my_msg['To'] = recipients

# 이메일 발송
smtp_server.sendmail(from_addr=my_addr,        
                     to_addrs=recipients, 
                     msg=my_msg.as_string())          

# 이메일 서버 종료하기
smtp_server.quit()
print("%s 님에게 이메일을 발송하였습니다." % recipients)
