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

# 엑셀파일에서 강원도 > 서울로 이동한 데이터만 추출
mask = (df['전출지별']=='강원도') & (df['전입지별']!='강원도')
df_kangwon_seoul = df[mask]
df_kangwon_seoul = df_kangwon_seoul.drop(['전출지별'], axis=1)
df_kangwon_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_kangwon_seoul.set_index('전입지', inplace=True)

sr_one = df_kangwon_seoul.loc['서울특별시']
print("sr_one")
print(sr_one)
# new_one = df_kangwon_seoul.loc['서울특별시', '1980':]
new_one = sr_one.drop(sr_one.index[0:10])
print("new_one")
print(new_one)

# 그래프 스타일 설정
plt.style.use('ggplot')

fig=plt.figure(figsize=(20,5))
ax1=fig.add_subplot(2,1,1)
ax1.plot(new_one, marker='o', markersize=10, markerfacecolor='orange',
         color='olive', linewidth=2, label='강원도->서울')
ax1.legend(loc='best')
ax1.set_ylim(0,100000)
ax1.set_title('강원 -> 서울 인구 이동', size=20)
ax1.set_xlabel('기간', size=12)
ax1.set_ylabel('이동인구수', size=12)
ax1.set_xticklabels(new_one.index, rotation=75)

ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)

plt.show()