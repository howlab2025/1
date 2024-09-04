import googlemaps
import webbrowser

my_key = "----발급받은 API 키를 입력-----"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)

# 장소명 또는 주소
place = "교보문고 광화문점"

# 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
geo_location = maps.geocode(place)[0].get('geometry')

lat = geo_location['location']['lat']
lng = geo_location['location']['lng']

# 웹브라우저에 구글 지도 실행하기
zoom=17
google_map_url = "https://www.google.co.kr/maps/@"+str(lat)+","+str(lng)+","+str(zoom)+"z?hl=ko"
print(google_map_url)

webbrowser.open(google_map_url)
