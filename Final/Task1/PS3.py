import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import statistics as stats
from datetime import datetime
import matplotlib.dates

df = pd.read_csv('PS3.csv', delimiter=',')

first = df['first_packet']
latest = df['last_packet']

#print((datetime.datetime.fromtimestamp(1638456038.26163) - datetime.datetime.fromtimestamp(1638455746.578940)).total_seconds())

#df['rtts'] = str((datetime.fromtimestamp(df['last_packet']) - datetime.fromtimestamp(df['first_packet'])).total_seconds())

rtts = []

for i in range(0, len(first)):
    rtt = datetime.fromtimestamp(float(latest[i])) - datetime.fromtimestamp(float(first[i]))
    rtts.append(rtt.total_seconds())


print(df.columns)

#plt.show()
