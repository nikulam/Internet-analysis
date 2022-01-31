import statistics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import scipy.stats
from collections import Counter


#3
class Server:
    def __init__(self, name, DNStimes, pingTimes, lost):
        self.name = name
        self.DNStimes = DNStimes
        self.pingTimes = pingTimes
        self.lost = lost
    
    def median(self):
        both = self.DNStimes + self.pingTimes
        if len(both) < self.lost:
            return float('inf')
        elif len(both) == 0:
            return 0
        elif lost == 0:
            return(statistics.median(both))
        else:
            for i in range(0, self.lost):
                both.append(float('inf'))
            return statistics.median(both)
    
    def mean(self):
        both = self.DNStimes + self.pingTimes
        if len(both) == 0:
            return 0
        else:
            return statistics.mean(both)
    
    def lossRatio(self):
        both = self.DNStimes + self.pingTimes
        if len(both) == 0 and self.lost != 0:
            return 1
        elif len(both) == 0 and self.lost == 0:
            return float('inf')
        else:
            return self.lost / len(both)

    def spread(self):
        both = self.DNStimes + self.pingTimes
        if len(both) == 0 or lost / len(both) > 0.25:
            return float('inf')
        else:
            return np.percentile(both, 75) - np.percentile(both, 25)

    def normPing(self):
        l = [n if n < 1000 else 1000 for n in self.pingTimes]
        for i in range(0, int(self.lost)):
            l.append(1000)

        return l    
            
    def normDNS(self):
        l = [n if n < 1000 else 1000 for n in self.DNStimes]
        for i in range(0, int(self.lost)):
            l.append(1000)
        
        return l

        


nameserver1 = Server('nameserver1', [], [], 0)
nameserver2 = Server('nameserver2', [], [], 0)
nameserver3 = Server('nameserver3', [], [], 0)

with open('task3/Week2/ns.txt') as nsfile:
    lines = nsfile.readlines()



#nameserver1
ns1dns = lines[2::14]
for dnstime in ns1dns:
    nameserver1.DNStimes.append(float(dnstime.split(' ')[3]))

ns1ping = lines[3::14]
for pingtime in ns1ping:
    nameserver1.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))

ns1lost = lines[4::14]
for line in ns1lost:
    transmitted = float(line.split(' ')[0])
    received = float(line.split(' ')[3])
    lost = transmitted - received
    nameserver1.lost += lost

#nameserver2
ns2dns = lines[6::14]
for dnstime in ns2dns:
    nameserver2.DNStimes.append(float(dnstime.split(' ')[3]))

ns2ping = lines[7::14]
for pingtime in ns2ping:
    nameserver2.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))

ns2lost = lines[8::14]
for line in ns1lost:
    transmitted = float(line.split(' ')[0])
    received = float(line.split(' ')[3])
    lost = transmitted - received
    nameserver2.lost += lost

#nameserver3
ns3dns = lines[10::14]
for dnstime in ns3dns:
    nameserver3.DNStimes.append(float(dnstime.split(' ')[3]))

ns3ping = lines[11::14]
for pingtime in ns3ping:
    nameserver3.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))

ns3lost = lines[12::14]
for line in ns1lost:
    transmitted = float(line.split(' ')[0])
    received = float(line.split(' ')[3])
    lost = transmitted - received
    nameserver3.lost += lost



researchserver1 = Server('researchserver1', [], [], 0)
researchserver2 = Server('researchserver2', [], [], 0)
researchserver3 = Server('researchserver3', [], [], 0)

with open('task3/Week2/rs.txt') as rsfile:
    line = rsfile.readline()
    
    while line:
        #researchserver1
        if '--- pna' in line:
            line = rsfile.readline()
            transmitted = float(line.split(' ')[0])
            received = float(line.split(' ')[3])
            lost = transmitted - received
            researchserver1.lost += lost
            line = rsfile.readline()
        elif 'PING pna' in line:
            line = rsfile.readline()
            while line != '\n':
                researchserver1.pingTimes.append(float(line.split('time=')[1].split(' ')[0]))
                line = rsfile.readline()
        #researchserver2
        elif '--- hlz' in line:
            line = rsfile.readline()
            transmitted = float(line.split(' ')[0])
            received = float(line.split(' ')[3])
            lost = transmitted - received
            researchserver2.lost += lost
            line = rsfile.readline()
        elif 'PING hlz' in line:
            line = rsfile.readline()
            while line != '\n':
                researchserver2.pingTimes.append(float(line.split('time=')[1].split(' ')[0]))
                line = rsfile.readline()
        #researchserver3
        elif '--- jfk' in line:
            line = rsfile.readline()
            transmitted = float(line.split(' ')[0])
            received = float(line.split(' ')[3])
            lost = transmitted - received
            researchserver3.lost += lost
            line = rsfile.readline()
        elif 'PING jfk' in line:
            line = rsfile.readline()
            while line != '\n':
                researchserver3.pingTimes.append(float(line.split('time=')[1].split(' ')[0]))
                line = rsfile.readline()
        else:
            line = rsfile.readline()
            

iperfserver1 = Server('iperfserver1', [], [], 0)
iperfserver2 = Server('iperfserver1', [], [], 0)

with open('task3/Week2/is.txt') as isfile:
    line = isfile.readline()
    
    while line:
        #iperfserver1
        if '--- blr1' in line:
            line = isfile.readline()
            transmitted = float(line.split(' ')[0])
            received = float(line.split(' ')[3])
            lost = transmitted - received
            iperfserver1.lost += lost
            line = isfile.readline()
            line = isfile.readline()
            iperfserver1.DNStimes.append(float(line) * 1000)
            line = isfile.readline()
        elif 'PING blr1' in line:
            line = isfile.readline()
            while line != '\n':
                iperfserver1.pingTimes.append(float(line.split('time=')[1].split(' ')[0]))
                line = isfile.readline()
        #researchserver2
        elif '--- iperf' in line:
            line = isfile.readline()
            transmitted = float(line.split(' ')[0])
            received = float(line.split(' ')[3])
            lost = transmitted - received
            iperfserver2.lost += lost
            line = isfile.readline()
            line = isfile.readline()
            iperfserver2.DNStimes.append(float(line) * 1000)
            line = isfile.readline()
        elif 'PING iperf' in line:
            line = isfile.readline()
            while line != '\n':
                iperfserver2.pingTimes.append(float(line.split('time=')[1].split(' ')[0]))
                line = isfile.readline()
        else:
            line = isfile.readline()

#3.3 & 3.4
tp1 = []
tp2 =[]

with open('task3/Week2/ft.txt') as file:
    lines = file.readlines()

is1 = lines[2::8]
for line in is1:
    tp1.append(float(line) * 8 / 1000)

is2 = lines[5::8]
for line in is2:
    tp2.append(float(line) * 8 / 1000)

'''mean = statistics.mean(tp2)
harmonic = statistics.harmonic_mean(tp2)
geometric = statistics.geometric_mean(tp2)
median = statistics.median(tp2)
print(mean, harmonic, geometric, median)'''
s = pd.Series(tp1)

times = []
timelines = lines[0::8]
for line in timelines:
    times.append(line.split(' ')[0])

t = pd.to_datetime(times)
df = pd.DataFrame({'tp': tp2, 'times': t})

#plt.plot(df['times'], df['tp'], color='tab:red')
#plt.gca().set(title='AS2.i2', xlabel='TIme', ylabel='Throughput (Kbps)')
#plt.xticks(rotation=20)
plt.acorr(tp2, maxlags=10)
plt.xlabel('lags')
plt.title('AS2.i2')
plt.show()



#3.1 Without lost packets
#plt.boxplot(nameserver3.pingTimes)


#3.1 With lost packets
#plt.boxplot(nameserver3.normDNS())


servers = [(nameserver1, 'AS1.n1'),
            (nameserver2, 'AS1.n2'),
            (nameserver3, 'AS1.n3'),
            (researchserver1, 'AS1.r1'),
            (researchserver2, 'AS1.r2'),
            (researchserver3, 'AS1.r3'),
            (iperfserver1, 'AS1.i1'),
            (iperfserver2, 'AS1.i2'),
            (nameserver1, 'AS1.d1'),
            (nameserver2, 'AS1.d2'),
            (nameserver3, 'AS1.d3')]

l = servers[6]
    
#3.1 PDF
#plt.hist(servers[10][0].pingTimes, bins=50, color='orange', edgecolor='black')

#3.1CDF
#plt.plot(np.sort(l[0].pingTimes), np.linspace(0, 1, len(l[0].pingTimes)))

plt.ylabel("Throughput (Kbps)")
#plt.xlabel('time (ms)')
plt.title(l[1])
#plt.show()