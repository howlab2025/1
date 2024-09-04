import pandas as pd

# 예제 025에서 저장한 CSV 파일을 불러와서 데이터프레임으로 변환
df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=0, index_col=0)  
print(df.head())
print('\n')

# 히스토그램
df['CD_rate'].plot(kind='hist')

df['change'].plot(kind='hist')

