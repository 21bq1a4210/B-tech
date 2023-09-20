import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("Titanic.csv")
print(df.columns.tolist())
# output:
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

survied_ratio = df[['Pclass', 'Survived']].groupby('Pclass').sum()
print(survied_ratio)
# output:
#         Survived
# Pclass
# 1            136
# 2             87

sns.boxplot(x=survied_ratio.index, y=survied_ratio['Survived'])
plt.show()