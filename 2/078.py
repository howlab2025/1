import imaplib
import email
import os
from email.header import decode_header

# IMAP 서버 접속 - SSL 방식
imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com', port='993')

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
imap_server.login(user=my_addr, password=my_pw)

# 받는 편지함('INBOX') 선택
mailbox = "INBOX"
mailbox_code = imap_server.select(mailbox)

# 받는 편지함('INBOX')에서 모든 편지 검색
code1, mail_all = imap_server.search(None, 'ALL')
print(mail_all, '\n')

# 첨부 파일 저장하기
mail_ids = mail_all[0].split()
print(mail_ids)
      
for mid in mail_ids:
    code2, data = imap_server.fetch(mid, '(RFC822)')
    mail = {}
        
    msg = email.message_from_string(data[0][1].decode('utf-8')) 

    if msg.is_multipart():
        for part in msg.walk():       
            if part.get_content_type().startswith('application/'):
#
                filename = decode_header(part.get_filename())[0][0].decode('utf-8')
                download_path = os.path.join(os.getcwd(), 'output', mid.decode('utf-8') + filename)

                fp = open(download_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
               
    
# 이메일 서버 종료하기
imap_server.close()

