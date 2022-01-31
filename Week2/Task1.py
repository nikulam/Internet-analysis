import statistics
import pandas as pd
import numpy as np

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


nameserver1 = Server('nameserver1', [], [], 0)
nameserver2 = Server('nameserver2', [], [], 0)
nameserver3 = Server('nameserver3', [], [], 0)

with open('ns.txt') as nsfile:
    lines = nsfile.readlines()

#nameserver1
ns1dns = lines[2::14]
for dnstime in ns1dns:
    nameserver1.DNStimes.append(float(dnstime.split(' ')[3]))
ns1ping = lines[3::14]

for pingtime in ns1ping:
    nameserver1.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))

#nameserver2
ns2dns = lines[6::14]
for dnstime in ns2dns:
    nameserver2.DNStimes.append(float(dnstime.split(' ')[3]))
ns2ping = lines[7::14]

for pingtime in ns2ping:
    nameserver2.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))

#nameserver3
ns3dns = lines[10::14]
for dnstime in ns3dns:
    nameserver3.DNStimes.append(float(dnstime.split(' ')[3]))

ns3ping = lines[11::14]
for pingtime in ns3ping:
    nameserver3.pingTimes.append(float(pingtime.split('time=')[1].split(' ')[0]))



researchserver1 = Server('researchserver1', [], [], 0)
researchserver2 = Server('researchserver2', [], [], 0)
researchserver3 = Server('researchserver3', [], [], 0)

with open('rs.txt') as rsfile:
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

with open('is.txt') as isfile:
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


servers = [
    nameserver1,
    nameserver2,
    nameserver3,
    researchserver1,
    researchserver2,
    researchserver3,
    iperfserver1,
    iperfserver2
]

names = []
medians = []
means = []
lossRatios = []
spreads = []


for server in servers:
    names.append(server.name)
    medians.append(server.median())
    means.append(server.mean())
    lossRatios.append(server.lossRatio())
    spreads.append(server.spread())

data = {'ServerName':names, 'Median':medians, 'Mean':means, 'LossRatio':lossRatios, 'Spreads':spreads}

df = pd.DataFrame(data)

df.to_csv('task1.csv')