import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---" 

# 검색기간 설정하기
now = dt.datetime.now()    
search_period = dt.timedelta(days=30)   
now_date = now.strftime('%Y%m%d')
start_date = (now-search_period).strftime('%Y%m%d')   
page_set = 10 

# DART 상세점보 접속 URL
crp_cd = "005380"
url = "http://dart.fss.or.kr/api/search.xml?auth="+my_auth_key+"&crp_cd="+crp_cd\
      +"&page_set="+str(page_set)+"&start_dt="+start_date


# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  
print(str(soup)[:500])

search_result = pd.DataFrame()
items=soup.find_all('list')
print(len(items))

for item in items:
    temp_dataframe=pd.DataFrame(([[item.crp_cls.text, item.crp_nm.text, item.crp_cd.text,
                                   item.rpt_nm.text, item.rcp_no.text, item.flr_nm.text,
                                   item.rcp_dt.text, item.rmk.text]]),
    columns=["crp_cls","crp_nm","crp_cd","rpt_nm","rcp_no","flr_nm","rcp_dt","rmk"])
    search_result=pd.concat([search_result,temp_dataframe])

print(search_result)