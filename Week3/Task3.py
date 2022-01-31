loads1 = []
with open('.\data\linkload-1.txt') as file:
    for line in file:
        string = line.split(' ')[1]
        loads1.append(float(string[:len(string) - 4]))

loads2 = []
with open('.\data\linkload-2.txt') as file:
    for line in file:
        string = line
        loads2.append(float(string[:len(string) - 4]))

loads3 = []
with open('.\data\linkload-3.txt') as file:
    for line in file:
        string = line.split(' ')[1]
        loads3.append(float(string[:len(string) - 4]))

loads4 = []
with open('.\data\linkload-4.txt') as file:
    for line in file:
        string = line.split(' ')[1]
        loads4.append(float(string[:len(string) - 4]))

import pandas as pd
import matplotlib.pyplot as plt


s1 = pd.Series(loads1)
pd.plotting.lag_plot(s1, lag=1, c='orange')
s2 = pd.Series(loads2)
pd.plotting.lag_plot(s2, lag=1, c='green')
s3 = pd.Series(loads3)
pd.plotting.lag_plot(s3, lag=1, c='blue')
s4 = pd.Series(loads4)
pd.plotting.lag_plot(s4, lag=1, c='pink')

plt.acorr(loads1, maxlags=1000) # or maxlags=10

plt.show()

