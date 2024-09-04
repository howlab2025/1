import pandas as pd

# 예제 017의 CSV 파일을 다시 활용하여, 데이터프레임으로 변환
df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)  
print(df.head())
print('\n')

df.columns = ['year', 'CD_rate', 'change']  # 열 이름 변경
df.set_index('year', inplace=True)   # year 열을 행 인덱스로 설정
print(df.head())
df.to_csv('./data/bok_statistics_CD_2.csv')
print('\n')

# 선 그래프 그리기
df.plot()

df['CD_rate'].plot()
df['change'].plot()

