import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics

df = pd.read_csv('./WEEK4/0.t3', delimiter='\t')

df['pair'] = df['src'].astype(str) + ' ' + df['dst'].astype(str)

pairs = df['pair'].value_counts()[0:100].index.tolist()

#print(df.loc[df['pair'] == pairs[0]]['flows'].sum())


'''print(
    df['flows'].sum(), 
    min(df['bytes']),
    statistics.median(df['bytes']),
    max(df['bytes']),
    statistics.mean(df['bytes']),
    min(df['pkts']),
    statistics.median(df['pkts']),
    max(df['pkts']),
    statistics.mean(df['pkts']),
    )'''

'''flows = []
for i in range(0, 100):
    flows.append(int(df.loc[df['pair'] == pairs[i]]['flows'].sum()))

order = range(0,100)

flows = list(map(lambda n: math.log(n), flows))
plt.scatter(order, flows, c='orange')
plt.xlabel('nth most common pair')
plt.ylabel('flows')
plt.show()'''