import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---" 

# 기업개황 정보 접속 URL
crp_cd = "005380"
url = "http://dart.fss.or.kr/api/company.xml?auth="+my_auth_key+"&crp_cd="+crp_cd

# BeautifulSoup으로 API가 반환하는 XML 확인
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  
print(soup)