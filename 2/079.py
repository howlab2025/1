import imaplib
import datetime
import imapclient

# IMAP 서버 접속 - SSL 방식
imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com', port='993')

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
imap_server.login(user=my_addr, password=my_pw)

# 받는 편지함('INBOX') 선택
mailbox = "INBOX"
mailbox_code = imap_server.select(mailbox)

# 받는 편지함('INBOX')에서 특정 날짜 이전의 편지를 삭제하기
before_date = datetime.date(2019, 10, 15).strftime('%d-%b-%Y')
code1, mails = imap_server.search(None, 'BEFORE', before_date)
print(mails, '\n')

# 메일 삭제하기 (1) - 휴지통으로 이동
imap_server.store('%s:%s' % (mails[0].split()[0].decode('utf-8'), mails[0].split()[-1].decode('utf-8')), '+X-GM-LABELS', '\\Trash')

# 메일 삭제하기 (2) - 휴지통 비우기
trash = imap_server.select(imapclient.imap_utf7.encode('[Gmail]/휴지통'))
print(trash)

imap_server.store('1:*', '+FLAGS', '\\Deleted')
print(trash)

imap_server.expunge()
print(trash)               

# 이메일 서버 종료하기
imap_server.close()