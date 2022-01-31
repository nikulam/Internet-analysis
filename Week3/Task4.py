import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/bytes.csv')
print(df)
sns.pairplot(df)
plt.show()
