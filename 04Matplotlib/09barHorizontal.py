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

# 연도를 2010~2017까지로 설정
col_years = list(map(str, range(2010,2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

'''
앞에서 적용한 연도 사이에 이동한 인구수를 각 도별로 합산하여 새로운 열을
추가한다. '''
df4['합계']=df4.sum(axis=1)
print(df4)
'''
새롭게 생성한 '합계'열을 오름차순으로 정렬하여 변수에 저장한다. '''
df_total = df4[['합계']].sort_values(by='합계', ascending=True)
# 그래프 스타일 설정
plt.style.use('ggplot')
# 수평 형태의 막대그래프 생성(kind='barh')
df_total.plot(kind='barh', figsize=(10,5), width=0.5, color='cornflowerblue')

plt.title('서울 -> 타시도 이동')
plt.ylabel('전입지', )
plt.xlabel('이동 인구 수')

plt.show()