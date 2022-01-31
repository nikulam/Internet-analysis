import pandas as pd
from collections import Counter

df = pd.read_csv('./Week4/t4', delimiter='\t')
#df2 = pd.read_csv('./Week4/t5', delimiter='\t')

t1bytes = 242334090 + 485376
t2bytes = 3360679 + 91831
t1pkts = 240493 + 1203
t2pkts = 10194 + 200

uniques = set(df['src'].tolist() + df['dst'].tolist())
#print(len(uniques))

c = Counter(df['src'].tolist() + df['dst'].tolist())

failed = df[df['ok'] == 0]
#failed.to_csv('failed.txt', sep='\t')

topByPkts = df.sort_values(by=['pkts'])
inOrder = topByPkts['sport'].tolist()[::-1]
#print(list(dict.fromkeys(inOrder))[0:15])