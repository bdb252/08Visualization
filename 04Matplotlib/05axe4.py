import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from setuptools.command.rotate import rotate

# 폰트 설정
font_path='../resData/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터프레임 만들기
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')

# 엑셀파일에서 서울 > 경기도로 이동한 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# range 함수로 1970~2017까지를 반환하면 str함수를 통해 문자열로 변경한 후 리스트로 생성한다.
col_years = list(map(str, range(1970,2018)))
# 연도를 지정한 후 각 4개의 도를 선택하여 데이터 추출
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# 그래프 사이즈 지정
fig=plt.figure(figsize=(20,10))
# Axe객체 생성 2행 2열의 첫번째부터 순서대로 그래프의 영역을 설정
axe1=fig.add_subplot(2,2,1)
axe2=fig.add_subplot(2,2,2)
axe3=fig.add_subplot(2,2,3)
axe4=fig.add_subplot(2,2,4)

# 각 Axe객체에 plot 함수로 그래프를 출력
'''
x축은 1970~2017까지의 연도를 설정. y축은 각 전출지의 전체 데이터를 설정.
나머지는 마커, 컬러, 두께 등을 설정한다. '''
axe1.plot(col_years, df4.loc['충청남도',:], marker='o', markersize=10, markerfacecolor='green',
         color='olive', linewidth=2, label='서울->충남')
axe2.plot(col_years, df4.loc['경상북도',:], marker='o', markersize=10, markerfacecolor='blue',
         color='skyblue', linewidth=2, label='서울->경북')
axe3.plot(col_years, df4.loc['강원도', :], marker='o', markersize=10, markerfacecolor='red',
         color='magenta', linewidth=2, label='서울->강원')
axe4.plot(col_years, df4.loc['전라남도',:], marker='o', markersize=10, markerfacecolor='orange',
         color='yellow', linewidth=2, label='서울->전남')

# 범례 설정
axe1.legend(loc='best')
axe2.legend(loc='best')
axe3.legend(loc='best')
axe4.legend(loc='best')

# 타이틀 설정
axe1.set_title('서울 -> 충남 인구 이동', size=15)
axe2.set_title('서울 -> 경북 인구 이동', size=15)
axe3.set_title('서울 -> 강원 인구 이동', size=15)
axe4.set_title('서울 -> 전남 인구 이동', size=15)

# x축 눈금, 회전 설정
axe1.set_xticklabels(col_years, rotation=90)
axe2.set_xticklabels(col_years, rotation=90)
axe3.set_xticklabels(col_years, rotation=90)
axe4.set_xticklabels(col_years, rotation=90)

plt.show()