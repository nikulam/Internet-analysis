import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

df1 = pd.read_csv('distr_a.txt')
df2 = pd.read_csv('distr_b.txt')
df3 = pd.read_csv('distr_c.txt')

#list(map(lambda n: math.log(n), df2['x']))
plt.hist(df2['x'], bins=30, color='orange', edgecolor='black')
plt.show()