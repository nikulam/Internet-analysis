from datetime import datetime
import pandas as pd
import random
import matplotlib.pyplot as plt
import math
import statistics

df = pd.read_csv('flowdata.txt', delimiter='\t',)

#1000 random
'''
rows = []
for i in range(0,1000):
    index = random.randint(0, 10000)
    rows.append(df.loc[[index]])

df2 = pd.concat(rows)[['pro', 'ok', 'sport', 'dport', 'pkts', 'bytes', 'flows']]
'''
#port80
'''df2 = df[df['sport'] == 80][['pro', 'ok', 'dport', 'pkts', 'bytes', 'flows']]

df2.insert(0, 'index', list(range(0,493)), True)
pd.plotting.parallel_coordinates(df2, 'index')'''

#bytes vs pkts
'''
plt.scatter(
    list(map(lambda n: math.log(n), df['pkts'])),
    list(map(lambda n: math.log(n), df['bytes'])), 
    c='orange'
    )
plt.ylabel('bytes log')
plt.xlabel('pkts log')
'''
#Throughputs
'''tps = []
for index, row in df.iterrows():
    time = (datetime.fromtimestamp(row['latest']) - datetime.fromtimestamp(row['first']))
    seconds = time.total_seconds()
    if seconds > 0:
        tp = float(row['bytes']) / float(seconds)
        tps.append(tp)

print(statistics.mean(tps))'''
