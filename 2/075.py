import imaplib
import imapclient

# IMAP 서버 접속 - SSL 방식
imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com', port='993')

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
imap_server.login(user=my_addr, password=my_pw)

# 메일박스 리스트 확인
resp_list, mailbox_list = imap_server.list()
print(resp_list, '\n')
print(mailbox_list, '\n')

for mailbox in mailbox_list:
    print(imapclient.imap_utf7.decode(mailbox))

# 받는 편지함('INBOX') 선택
mailbox = "INBOX"
mailbox_code = imap_server.select(mailbox)
print('\n', mailbox_code)

# 이메일 서버 종료하기
imap_server.close()