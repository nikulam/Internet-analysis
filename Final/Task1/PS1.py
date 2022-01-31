import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
import datetime


df = pd.read_csv('PS1.csv', delimiter=',')

valueCounts = df['SourcePort'].value_counts()
print(len(valueCounts))
'''plt.scatter(valueCounts.index, valueCounts.values)
plt.xlabel('source port number')
plt.ylabel('number of packets')
##df2 = pd.DataFrame({'port': valueCounts.index, 'packets': valueCounts.values})
##df2.to_csv('table.csv')'''

#packet length distribution
length = df['Length']
'''plt.hist(list(length), bins=1514, color='orange', edgecolor='black')
plt.xlabel('packet length (bytes)')
plt.ylabel('number of packets')
plt.plot(np.sort(length), np.linspace(0, 1, len(length)))
plt.xlabel('packet length (bytes)')
plt.ylabel("x100% of total number of packets")
print(np.percentile(length, 30))
print(stats.median(length))
print(max(length))'''


seconds = df['Time']
plt.hist(list(map(lambda n: n / 600, seconds)), bins=12, color='orange', edgecolor='black')
plt.xlabel('time from start (10min)')
plt.ylabel('number of packets')

#plt.hist(list(map(lambda n: n / (60*9), seconds)), bins=10, color='orange', edgecolor='black')


plt.show()

