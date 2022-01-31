import pandas as pd

file = pd.read_csv('log_tcp_complete', delimiter=' ')


#1
total = len(file)
columns = [3, 7, 10, 17, 21, 24]
for int in columns:
    columnName = file.columns[int - 1]
    print('avg ' ,sum(file[columnName]) / total)


#2
count = 0
for index, row in file.iterrows():
    c7, c10 = row[6], row[9]

    if c7 != 0: 
        if c10 / c7 > 0.2:
            count += 1

print(count / total)



#3
columns = [3, 9, 17, 23, 31]
for int in columns:
    columnName = file.columns[int - 1]
    print('max ' ,max(file[columnName]))

