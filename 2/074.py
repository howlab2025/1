import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import pandas as pd


def send_gmail_tls(recipient_email, title_text='', body_text='', attach_file_name=None):

    if not recipient_email:
        print("수신자 이메일이 입력되지 않았습니다...")
        
    else:            
        # 이메일 베이스 객체 (본문 메시지 + 첨부 파일)
        my_msg = MIMEBase('multipart', 'mixed')
        
        # 이메일 메시지 구성
        subject = title_text
        body = body_text
        
        recipients = recipient_email
        
        my_msg.attach(MIMEText(body, 'plain', 'utf-8'))
        my_msg['Subject'] = subject
        my_msg['To'] = recipients
        
        
        try:
            # 첨부 파일 구성
            file_name = attach_file_name
            file_path = os.path.join(os.getcwd(), 'data', file_name)
            
            my_attach = MIMEBase('application', 'octet-stream')
            my_attach.set_payload(open(file_path, 'rb').read())
            encoders.encode_base64(my_attach)
            my_attach.add_header('Content-Disposition', 'attachment; filename=%s' % file_name)
            my_msg.attach(my_attach)
        
        except:
            pass
        
        # 이메일 발송
        smtp_server.sendmail(from_addr=my_addr,        
                             to_addrs=recipients, 
                             msg=my_msg.as_string())          
        
        print("%s 님에게 이메일을 발송하였습니다." % recipients)



if __name__ == "__main__": 

    # SMTP 서버 접속 - TLS 방식
    smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp_server.ehlo()
    smtp_server.starttls()   # TLS Encription 동작
    
    # 이메일 서버 로그인 - 이메일 주소, 앱 비밀번호 입력
    my_addr = '이메일_아이디@gmail.com'
    my_pw = '앱 비밀번호'
    smtp_server.login(user=my_addr, password=my_pw)
    
    
    # 이메일 발송 리스트 가져오기
    mail_list_file = 'sendmail_list.xlsx'
    mail_list_path = os.path.join(os.getcwd(), 'data', mail_list_file)
    mail_list = pd.read_excel(mail_list_path)
    
    # 이메일 발송하기
    for idx in mail_list.index:
        recipient_email = mail_list.loc[idx, 'email']
        title_text = mail_list.loc[idx, 'title']
        body_text = mail_list.loc[idx, 'body']
        attach_file_name = mail_list.loc[idx, 'attach']
        
        send_gmail_tls(recipient_email, title_text, body_text, attach_file_name)
        
    # 이메일 서버 종료하기
    smtp_server.quit()
