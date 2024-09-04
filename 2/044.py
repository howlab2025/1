import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---" 

# 기업개황 정보 접속 URL
crp_cd = "005380"
url = "http://dart.fss.or.kr/api/company.xml?auth="+my_auth_key+"&crp_cd="+crp_cd

# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  

crp_nm = soup.find('crp_nm').text
crp_nm_e = soup.find('crp_nm_e').text
crp_nm_i = soup.find('crp_nm_i').text
stock_cd = soup.find('stock_cd').text
ceo_nm = soup.find('ceo_nm').text
crp_cls = soup.find('crp_cls').text
crp_no = soup.find('crp_no').text
bsn_no = soup.find('bsn_no').text
adr = soup.find('adr').text
hm_url = soup.find('hm_url').text
ir_url = soup.find('ir_url').text
phn_no = soup.find('phn_no').text
fax_no = soup.find('fax_no').text
ind_cd = soup.find('ind_cd').text
est_dt = soup.find('est_dt').text
acc_mt = soup.find('acc_mt').text

company_info = {'crp_nm':crp_nm,
                'crp_nm_e':crp_nm_e,
                'crp_nm_i':crp_nm_i,
                'stock_cd':stock_cd,
                'ceo_nm':ceo_nm,
                'crp_cls':crp_cls,
                'crp_no':crp_no,
                'bsn_no':bsn_no,
                'adr':adr,
                'hm_url':hm_url,
                'ir_url':ir_url,
                'phn_no':phn_no,
                'fax_no':fax_no,
                'ind_cd':ind_cd,
                'est_dt':est_dt,
                'acc_mt':acc_mt,                
                }

print(company_info)