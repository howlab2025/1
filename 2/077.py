import imaplib
import email
from email.utils import parseaddr
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

# 메일 내용 파싱하기
result = {}
mail_ids = mail_all[0].split()
print(mail_ids)
    
for mid in mail_ids:
    code2, data = imap_server.fetch(mid, '(RFC822)')
    mail = {}
        
    msg = email.message_from_string(data[0][1].decode('utf-8')) 
    
    mail['From'] = parseaddr(msg['From'])[1]        
    mail['To'] = parseaddr(msg['To'])[1] 
            
    subject = decode_header(msg['Subject'])
    mail['Subject'] = subject[0][0].decode('utf-8')

    if msg.is_multipart():
        for part in msg.walk():       
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True) 
                body = body.decode()               
    else:
        body = msg.get_payload()

    mail['Body'] = body 
      
    result[int(mid.decode('utf-8'))] = mail   
        
print(result)
    
# 이메일 서버 종료하기
imap_server.close()

