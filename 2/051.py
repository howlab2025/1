import pandas as pd
import folium

pd.set_option('display.max_columns', 30)

# 서울시 환승주차장 리스트를 데이터프레임 변환
df = pd.read_csv('./data/parking.csv')
df = df[['주차장명', '주차장 위치 좌표 위도', '주차장 위치 좌표 경도', '주차 면(주차 가능 차량 수)']]
df.columns = ['명칭', '위도', '경도', '대수']
df = df.dropna(axis=0)
print(df.head())
print("\n")

# 서울 지도 만들기
parking_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

# 위치정보를 Marker로 표시
for name, lat, lng in zip(df.명칭, df.위도, df.경도):
    folium.Marker([lat, lng],
                  icon=folium.Icon(color='red',icon='info-sign'),
                  popup=name).add_to(parking_map)

# 지도를 HTML 파일로 저장하기
parking_map.save('./output/parking_map.html')