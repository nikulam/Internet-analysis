import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
import datetime
import math
from geolite2 import geolite2
from collections import Counter


df = pd.read_csv('PS2.t2', delimiter='\t')


#2.1
valueCounts = df['sport'].value_counts()
'''plt.scatter(valueCounts.index, list(map(lambda n: math.log(n), valueCounts.values)))
plt.xlabel('source port number')
plt.ylabel('number of packets')'''
#plt.show()
#df2 = pd.DataFrame({'port': valueCounts.index, 'packets': valueCounts.values})
#df2.to_csv('table2.csv')

#1.5


#1.6 countries by source ip
'''
sourceIP = df['src']
ints = ['0','1','2','3','4','5','6','7','8','9']
src = list(filter(lambda n: n[0] in ints, sourceIP))
countries = []
reader = geolite2.reader()

for ip in src:
    match = reader.get(ip)
    if match:
        if 'country' in match:
            countries.append(match['country']['iso_code'])

c = Counter(countries)

labels, values = (zip(*c.items()))

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width, color='green', edgecolor='black')
plt.xticks(indexes + width * 0.5, labels)
plt.ylabel('number of flows')
plt.xlabel('country')
print(len(countries))
print(len(set(src)))'''

#by pairs
'''
df['pair1'] = df['src'] + df['dst']
df['pair2'] = df['dst'] + df['src']
vc = df['pair1'].value_counts()
print(vc.head(10))
'''

#1.8
'''
ints = ['0','1','2','3','4','5','6','7','8','9']
bytes = df['bytes']
length = list(filter(lambda n: isinstance(n, str), bytes))
length = list(filter(lambda n: n[0] in ints, length))
length = list(map(lambda n: math.log(int(n)), length))

#l = [min(length), np.percentile(length, 25), stats.mean(length), np.percentile(length, 75), max(length)]
plt.hist(length, bins=30, color='orange', edgecolor='black')
plt.xlabel('flow length log(bytes) ')
plt.ylabel('number of flows')
plt.plot(np.sort(length), np.linspace(0, 1, len(length)))
plt.xlabel('flow length log(bytes)')
plt.ylabel("x100% of total number of flows")'''


#1.5

times = df['first']
ints = ['0','1','2','3','4','5','6','7','8','9']
times = list(filter(lambda n: isinstance(n, str), times))
times = list(filter(lambda n: n[0] in ints, times))
times = list(map(lambda n: float(n), times))
times = list(map(lambda n: datetime.datetime.fromtimestamp(n), times))
first = times[0]

seconds = []
for time in times:
    seconds.append((time - first).total_seconds() / (600))

plt.hist(seconds, bins=12, color='orange', edgecolor='black')

plt.xlabel('time from start (10min)')
plt.ylabel('number of flows')

plt.show()
