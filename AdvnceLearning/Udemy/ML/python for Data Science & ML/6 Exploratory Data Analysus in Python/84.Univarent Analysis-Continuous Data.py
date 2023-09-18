import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
print(df.columns.tolist())
#output:
# ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
#print(df)
x_axis = df.index
y_axix = df['PetalLengthCm']
sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', hue='Species', data=df)
plt.show()

sns.scatterplot(x=df["Species"], y=df['PetalLengthCm'])
plt.show()

sns.displot(df['PetalLengthCm'])
plt.show()

plt.hist(df['PetalLengthCm'])
plt.show()

sns.boxplot(x=df["PetalLengthCm"])
plt.show()