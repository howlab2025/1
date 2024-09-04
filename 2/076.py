import imaplib

# IMAP 서버 접속 - SSL 방식
imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com', port='993')

# 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
my_addr = '이메일_아이디@gmail.com'
my_pw = '앱 비밀번호'
imap_server.login(user=my_addr, password=my_pw)

# 받은 편지함('INBOX') 선택
mailbox = 'INBOX'
mailbox_code = imap_server.select(mailbox)

# 받은 편지함('INBOX')에서 편지 검색 - 모든 편지
code1, mail_all = imap_server.search(None, 'ALL')
print('모든 편지 리스트: ')
print(code1)
print(mail_all)
print('\n')

# 읽지 않은 편지
code2, mail_unseen = imap_server.search(None, 'UNSEEN')
print('읽지 않은 편지 리스트: ')
print(code2)
print(mail_unseen)
print('\n')

# 제목에 '첨부' 문자열이 포함된 편지
search1 = '첨부'.encode('utf-8')
imap_server.literal = search1
code3, mail_subject = imap_server.search('utf-8', 'SUBJECT')
print('제목에 특정 단어가 있는 편지 리스트: ')
print(code3)
print(mail_subject)
print('\n')

# 본문에 '엑셀' 문자열이 포함된 편지
search2 = '엑셀'.encode('utf-8')
imap_server.literal = search2
code4, mail_body = imap_server.search('utf-8', 'BODY')
print('본문에 특정 단어가 있는 편지 리스트: ')
print(code4)
print(mail_body)

# 이메일 서버 종료하기
imap_server.close()
