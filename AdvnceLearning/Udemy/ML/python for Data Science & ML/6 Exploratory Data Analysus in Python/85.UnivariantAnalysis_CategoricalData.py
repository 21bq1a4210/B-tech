import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

sns.countplot(x=df['Species'])
plt.show()

labels = df['Species'].unique()
plt.pie(df['Species'].value_counts(), labels = labels)
plt.show()