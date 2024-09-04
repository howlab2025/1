from selenium import webdriver 

driver = webdriver.Chrome("./Selenium/chromedriver") 
driver.implicitly_wait(3)
driver.get("https://www.danawa.com/") 

# 다나와 메인화면의 로그인 버튼을 누르는 작업 실행
login = driver.find_element_by_css_selector('li.my_page_service > a')
login.click()
driver.implicitly_wait(3)

# 아이디/비밀번호를 입력하고 로그인하기 버튼을 누르는 작업 실행
my_id = "----본인 아이디 입력하세요----"
my_pw = "----본인 패스워드 입력하세요----"

driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(my_pw)
driver.implicitly_wait(2)
driver.find_element_by_css_selector('button.btn_login').click()
driver.implicitly_wait(2)

# 관심상품 목록 HTML 페이지 가져오기
wishlist = driver.find_element_by_css_selector('li.interest_goods_service > a').click()
driver.implicitly_wait(2)
html_src = driver.page_source
driver.close()
print(html_src[:500])
print("\n")

# 관심상품 목록 HTML 페이지를 BeautifulSoup으로 파싱하기
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_src, 'html.parser')

wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
wish_items = wish_table.select('tbody tr')

for item in wish_items:
    title = item.find('div', {'class':'tit'}).text
    price = item.find('span', {'class':'price'}).text
    link = item.find('a', href=re.compile('prod.danawa.com/info/')).get('href')
    print(title)
    print(price)
    print(link)
    print("\n")