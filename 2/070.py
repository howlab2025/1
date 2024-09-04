import smtplib

# SMTP 서버 접속 - TSL 방식
smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)

# SMTP 서버에 hello 메시지 보내기
hello_message = smtp_server.ehlo()
print(hello_message)
print("\n")

# 이메일 서버 종료하기
bye_message = smtp_server.quit()
print(bye_message)
