import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
import math
from collections import Counter
from datetime import datetime


#2.1 Plot traffic volume

df = pd.read_csv('task2/FS2.t2', delimiter='\t')
'''
length = df['bytes']

#print(len(list(filter(lambda n: n < 96, length))))

length = list(map(lambda n: math.log(n), length))

plt.hist(list(length), bins=30, color='orange', edgecolor='black')
plt.xlabel('flow length (bytes)')
plt.ylabel('number of flows (log(bytes))')

plt.plot(np.sort(length), np.linspace(0, 1, len(length)))
plt.xlabel('flow length (log(bytes))')
plt.ylabel("x100% of total number of flows")

print(np.percentile(length, 30))
print(stats.mean(length))
print(max(length))

c = Counter(length)
print(c)
'''
#2.2 Per user data volume
'''uniq = list(set(list(df['src'].unique()) + list(df['dst'].unique())))
users = list(filter(lambda n: '133.60.172' in n, uniq))
userTraffic = []

for user in users:
    bytes = []
    print(user)
    for index, row in df.iterrows():
        if user in row['src'] or user in row['dst']:
            bytes.append(row['bytes'])
    
    userTraffic.append(sum(bytes))

pd.DataFrame({'bytes': userTraffic}).to_csv('task2/bytes.csv')'''

'''df2 = pd.read_csv('task2/bytes.csv')

plt.bar(df2['i'], df2['bytes'], 1, color='orange')
plt.xlabel('user')
plt.ylabel('data volume (bytes)')'''

#2.3 ipv4 & ipv6

'''df4 = pd.read_csv('task2/ipv4_filtered.t2', delimiter='\t')
df6 = pd.read_csv('task2/ipv6.t2', delimiter='\t')

length = df6['bytes']

#length = list(map(lambda n: math.log(n), length))
#length = list(filter(lambda n: n < 2000, length))

plt.hist(list(length), bins=30, color='orange', edgecolor='black')
plt.xlabel('flow length (bytes)')
plt.ylabel('number of flows')

plt.plot(np.sort(length), np.linspace(0, 1, len(length)))
plt.xlabel('flow length log(bytes)')
plt.ylabel("x100% of total number of flows")
print(stats.median(length))
print(stats.mean(length))
print(len(list(filter(lambda n: n > 2000, length))))'''

#time scales
length = df['bytes']
times = df['first']
times = list(map(lambda n: datetime.fromtimestamp(n), times))
first = times[0]
seconds = []
for time in times:
    seconds.append((time - first).total_seconds() / 600)

plt.hist(seconds, bins=6, color='orange', edgecolor='black')
plt.xlabel('time from start (10min)')
plt.ylabel('number of flows')
plt.show()

#port application analysis
port = df['sport'].value_counts()
print(port.head(10))
