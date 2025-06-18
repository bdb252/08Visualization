import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15,5))
axe1 = fig.add_subplot(1,3,1)
axe2 = fig.add_subplot(1,3,2)
axe3 = fig.add_subplot(1,3,3)

'''
barplot : 막대그래프 생성
    x, y : x,y축에 표시할 데이터
    data : 그래프에 사용할 데이터
    dodge : 데이터에 색상을 기준으로 구분할 열 지정
    hue : 막대그래프를 나란히 배치하거나(True), 겹치도록 배치(False)
'''
sns.barplot(x='sex', y='survived', data=titanic, ax=axe1)
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=axe2)
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=axe3)


axe1.set_title('titanic survived - sex')
axe2.set_title('titanic survived - sex/class')
axe3.set_title('titanic survived - sex/class(stacked)')
plt.show()