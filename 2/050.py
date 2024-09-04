import folium

# 서울 지도 만들기
seoul_map1 = folium.Map(location=[37.55,126.98], zoom_start=12)

seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=9)

seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', 
                        zoom_start=15)

# 지도를 HTML 파일로 저장하기
seoul_map1.save('./output/seoul1.html')
seoul_map2.save('./output/seoul2.html')
seoul_map3.save('./output/seoul3.html')