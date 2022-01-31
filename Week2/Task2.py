import matplotlib.pyplot as plt
import statistics
import pandas as pd

with open('sm.txt') as smfile:
    lines = smfile.readlines()


upload = lines[17::42]
uloads = []

for line in upload:
    uloads.append(float(line.split('Bytes')[1].split(' ')[3]))

download = lines[37::42]
dloads = []

for line in download:
    dloads.append(float(line.split('Bytes')[1].strip().split(' ')[0]))


iperfUp = [
    statistics.mean(uloads),
    statistics.median(uloads),
    min(uloads),
    max(uloads),
    pd.Series(uloads).mad()
]

iperfDown = [
    statistics.mean(dloads),
    statistics.median(dloads),
    min(dloads),
    max(dloads),
    pd.Series(dloads).mad()
]

with open('ft.txt') as ftfile:
    lines = ftfile.readlines()

goodLines = lines[5::8]
speeds = []
for line in goodLines:
    speeds.append(float(line.split('\n')[0]) * 8 / 1000)

HTTP = [
    statistics.mean(speeds),
    statistics.median(speeds),
    min(speeds),
    max(speeds),
    pd.Series(speeds).mad()
]
print(HTTP)

speedtestUp = [407,251,337,448,398]
speedtestDown = [450,397,444,437,457]

stUp = [
    statistics.mean(speedtestUp),
    statistics.median(speedtestUp),
    min(speedtestUp),
    max(speedtestUp),
    pd.Series(speedtestUp).mad()
]

stDn = [
    statistics.mean(speedtestDown),
    statistics.median(speedtestDown),
    min(speedtestDown),
    max(speedtestDown),
    pd.Series(speedtestDown).mad()
]

data = {'HTTP':HTTP, 'iperf up':iperfUp, 'iperf dn':iperfDown, 'ST up':stUp, 'ST dn':stDn}
df = pd.DataFrame(data)

df.to_csv('task2.csv')