from matplotlib import pyplot as plt
import numpy as np

bytes = []
indices = []
i = 0

with open('Week3/data/flows.txt') as file:
    for line in file:
        bytes.append(int(line))
        indices.append(i)
        i += 1


##bytes = list(filter(lambda n: n < 200,bytes))

##bytes = list(map(lambda n: math.log(n), bytes))

'''print(np.percentile(bytes, 70))
print(statistics.mean(bytes))
print(max(bytes))'''

plt.plot(np.sort(bytes), np.linspace(0, 1, len(bytes)))
##plt.hist(bytes, bins=30, color='orange', edgecolor='black')
##plt.scatter(indices, bytes, c='orange')
##plt.boxplot(bytes)
plt.xlabel('bytes')
plt.ylabel('number of observations')
plt.show()
