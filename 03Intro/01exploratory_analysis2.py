import pandas as pd
import numpy as np

# csv파일을 데이터프레임으로 변환1
# df = pd.read_csv('../resData/auto-mpg.csv', header=None)

# csv파일을 데이터프레임으로 변환2 : na_values 옵션으로 결측치 ?를 NaN으로 대체 후 변환
df = pd.read_csv('../resData/auto-mpg.csv', header=None, na_values='?')
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 상위 5개의 데이터 출력하기
print(df.head())
# 출력 컬럼만 출력하기
print(df['horsepower'])

# 문자형 데이터가 포함되어있으므로 에러가 발생함
# name컬럼은 자동차의 이름이므로 평균을 계산할 수 없다.
# print(df.mean()) #예외발생.

print('수치형 열만 선택 후 평균 출력', '='*30)
# numpy 모듈의 number를 이용해서 숫자형인 열만 선택한다.
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.mean())
'''
horsepower 컬럼은 변환1에서는 출력안됨. ?를 문자로 인식하기 때문
하지만 변환2에서는 NaN으로 변경했으므로 컬럼을 숫자형으로 인식해서
포함되어 출력된다.
'''
print('연비의 평균 출력', '='*30)
print(df['mpg'].mean())
# print(df['name'].mean()) #에러발생. String은 수치데이터가 아님

print('연비와 무게 평균 출력', '='*30)
print(df[['mpg', 'weight']].mean())

print('중간값', '='*30)
# print(df.median()) #에러발생. String은 수치데이터가 아님
print('연비', df['mpg'].median())
print('제조국가', df['origin'].median())

# 최대값
print('최대값', '='*30)
print(df.max())
print('연비', df['mpg'].max())
print('제조국가', df['origin'].max())

# 최소값
print('최소값', '='*30)
print(df.min())
print('연비', df['mpg'].min())

# 표준편차
print('표준편차', '='*30)
# print(df.std()) #에러발생
print(df['mpg'].std())

print('상관계수', '='*30)
# print(df.corr()) #에러발생
print(df[['mpg', 'weight']].corr())