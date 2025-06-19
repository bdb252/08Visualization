import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글깨짐처리를 위해 폰트매니저 임포트
font_path='../resData/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터에서 주소와 업종만 뽑아서 종로구 치킨집 찾기
df = pd.read_excel('../resData/서울특별시_일반음식점.xlsx', engine='openpyxl',
                   usecols=['소재지전체주소','업태구분명'])
find_str = '종로구'
mask = (
    df['소재지전체주소'].str.contains(find_str, na=False)  &
    ((df['업태구분명'] == '통닭(치킨)') | (df['업태구분명'] == '호프/통닭'))
)
df_jongro = df[mask]
# print(df_jongro.head())
# print(df_jongro)

#주소에서 동만 추출
df_jongro['dong_nm']=df_jongro['소재지전체주소'].str.split().str[2]
# df_jongro.columns=['addr1', 'addr2', 'menutype']
# print(df_jongro)
# csv 파일로 저장
df_jongro.to_csv('../saveFiles/치킨집가공.csv')
################################################################################
# 위 내용은 주피터 노트북에서 실행

# 저장한 csv 파일 불러오기
df_chicken = pd.read_csv('../saveFiles/치킨집가공.csv')

df_chicken['dong_nm'].value_counts()

dong_count = df_chicken['dong_nm'].value_counts().to_frame()

dong_count = dong_count.reset_index().rename(columns={"index":"dong_nm","count":"count"})
print(dong_count)

plt.style.use('ggplot')
font_name=(font_manager.FontProperties(fname='../resData/malgun.ttf').get_name())
rc('font', family=font_name)

dong_count['label'] = dong_count['dong_nm'] + '('+dong_count['count'].astype(str) + ')'
squarify.plot(sizes=dong_count['count'], label=dong_count['label'], alpha=0.8)
plt.axis('off')
plt.show()