import pandas as pd
import statistics
import matplotlib.pyplot as plt
import numpy as np

bitrates = []
bytes = []
retries = []
dates = []
stamps = []

with open('iperfresults.txt') as file:

    for row in file:
        if 'sender' in row:
            bitrates.append(float(row.split('GBytes   ')[1].split(' ')[0]))
            bytes.append(float(row.split('sec  ')[1].split(' ')[0]))
            retries.append(float(row.split('sec    ')[1].split(' ')[0]))

        elif 'EEST' in row:
            dates.append(row.split('T')[1].split(' ')[0])
        
        elif 'timestamp' in row:
            stamps.append(row.split(':')[1].splitlines()[0])
    

data = {'timestamp':stamps, 'time':dates, 'bytes transferred(GB)':bytes, 'bitrate(Gb/s)':bitrates, 'retries':retries}

df = pd.DataFrame(data)

avgBitrate = sum(bitrates) / len(bitrates)
minBitrate = min(bitrates)
maxBitrate = max(bitrates)
medianBitrate = (statistics.median(bitrates))

print(avgBitrate, minBitrate, maxBitrate, medianBitrate)

plt.plot(retries, bitrates)
plt.show()

df.to_csv('iperfresults.csv')