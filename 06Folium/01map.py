'''
아나콘다 설치시 기본적으로 생성되는 base 가상환경에는 설치되어 있지 않으므로
다음과 같이 설치한다.
pip install folium
혹은 conda로 설치할 수 있다.
'''
import folium

'''
folium 라이브러리
    :데이터를 지도로 시각화해주는 라이브러리.
    코드를 실행하면 IDE에서 직접 지도가 표시되지 않고, HTML파일로
    저장되어 웹브라우저를 통해 확인해야 한다. 웹서버(Tomcat 등)가 있다면
    특정 경로에 저장하여 Spring(혹은 JSP)와 연동할 수 있다. 
'''

# 맵표시 : 인수로 시설물의 위도/경도와 줌 레벨을 지정
seoul_map1 = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map1.save('../saveFiles/seoul1.html')

# tiles 옵션으로 산악지형 강조, 도로망 강조와 같은 표현이 가능하다.
# (버전의 문제가 있어 확인 필요)
# seoul_map2 = folium.Map(location=[37.55, 126.98], zoom_start=12,
#                         tiles='Stamen Terrain',
#                         attr='Stamen Terrain')
# seoul_map2.save('../saveFiles/seoul2.html')
#
# seoul_map3 = folium.Map(location=[37.55, 126.98], zoom_start=12,
#                         tiles='Stamen Toner',
#                         attd='Stamen Terrain')
# seoul_map3.save('../saveFiles/seoul3.html')

# 데이터프레임 변환을 위해 판다스 임포트
import pandas as pd
# 엑셀 파일을 변환. 1행은 타이틀로 간주해서 2행부터 데이터를 가져온다.
df = pd.read_excel('../resData/서울지역_대학교_위치2.xlsx', engine='openpyxl')
# 컬럼명 추가
df.columns=['학교명', '위도', '경도']
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    # 위경도는 리스트로 부여하고, popup(풍선도움말)은 학교명 지정
    folium.Marker([lat, lng], popup=name).add_to(seoul_map1)
# 마커가 추가된 Map을 HTML 파일로 저장
seoul_map1.save('../saveFiles/seoul_colleges1.html')

# 원형 마커 및 추가 옵션 지정
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng], radius=10, color='brown', fill=True,
                        fill_color='coral', fill_opacity=0.7,
                        popup=name).add_to(seoul_map1)
seoul_map1.save('../saveFiles/seoul_colleges2.html')