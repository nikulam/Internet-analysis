import pandas as pd
import random
import matplotlib.pyplot as plt
import statistics
import statsmodels.api as sm
import pylab
import numpy as np


df = pd.read_csv('sampling.txt')


n = 100
means = []
for i in range(0,10000):
    samples = []
    for j in range(0, n):
        index = random.randint(0, 9999)
        samples.append(df['time'][index])
    means.append(statistics.mean(samples))


print(statistics.mean(means))
print(statistics.stdev(means))

'''
arr = np.array(means)
sm.qqplot(arr)
pylab.show()
'''

plt.hist(means, bins=25, color='orange', edgecolor='black')
plt.ylabel('samples (n)')
plt.xlabel('time (ms)')
plt.show()