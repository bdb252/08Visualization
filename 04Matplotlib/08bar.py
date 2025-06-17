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

col_years = list(map(str, range(2010,2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# 데이터프레임 전치한다. 즉 행과 열을 바꾼다.
df4 = df4.transpose()
plt.style.use('ggplot')
# 데이터프레임의 인덱스를 정수형으로 변경(map함수의 첫번째 인수로 int함수 사용)
df4.index = df4.index.map(int)
# 막대그래프를 세로형(수직방향)으로 생성. 막대의 두께와 색깔 설정
df4.plot(kind='bar', figsize=(20,10), width=0.7, color=['orange', 'green', 'skyblue', 'blue'])

# 그래프의 제목, 라벨 등을 설정
plt.title('서울 -> 타시도 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.ylim(5000,30000)
plt.legend(loc='best', fontsize=15)

plt.show()