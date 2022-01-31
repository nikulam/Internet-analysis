import pandas as pd

df = pd.read_csv('./data/flowdata_unclean.txt', sep='\t')

indices = []
column = []
for index, row in df.iterrows():
    if row.isnull().sum() > 0:
        indices.append(index)
        print(index)
    else:
        value = 0 if row['bytes'] < 50 else 1
        column.append(value)

df.drop(labels=indices, axis=0, inplace=True)
df['Y'] = column
df.to_csv('Task5.csv')




