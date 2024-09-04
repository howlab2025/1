import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---" 

# 검색기간 설정하기
now = dt.datetime.now()    
search_period = dt.timedelta(days=5)   
now_date = now.strftime('%Y%m%d')
start_date = (now-search_period).strftime('%Y%m%d')   
page_set = 10 

# DART 상세점보 접속 URL
bsn_tp_list = [
               "D001", #주식등의대량보유상황보고서
               "D002", #임원ㆍ주요주주특정증권등소유상황보고서
               "D003", #의결권대리행사권유
               "D004", #공개매수
               ] 

bsn_tp_urls = []

for bsn_tp in bsn_tp_list:
    url = "http://dart.fss.or.kr/api/search.xml?auth="+my_auth_key+"&page_set="+str(page_set)\
           +"&start_dt="+start_date+"&bsn_tp="+bsn_tp
    bsn_tp_urls.append(url)

# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리

sum_items = []
    
for url in bsn_tp_urls:
    xml = requests.get(bsn_tp_urls[1])
    soup = BeautifulSoup(xml.text, 'html.parser')  
    items=soup.find_all('list')
    sum_items += items

print(len(sum_items))

search_result = pd.DataFrame()

for item in sum_items:
    temp_dataframe=pd.DataFrame(([[item.crp_cls.text, item.crp_nm.text, item.crp_cd.text,
                                   item.rpt_nm.text, item.rcp_no.text, item.flr_nm.text,
                                   item.rcp_dt.text]]),
    columns=["crp_cls","crp_nm","crp_cd","rpt_nm","rcp_no","flr_nm","rcp_dt"])
    search_result=pd.concat([search_result,temp_dataframe])

print(search_result.head())