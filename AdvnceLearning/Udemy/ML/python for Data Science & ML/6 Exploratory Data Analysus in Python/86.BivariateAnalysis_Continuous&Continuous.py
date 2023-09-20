import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('Titanic.csv')
print(df.columns.tolist())
#Output:
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

'''SCATTER PLOT::'''
sns.scatterplot(x=df['Fare'], y=df['Age'])
plt.title('Bivariate Analysis')
plt.show()

'''CORELATION::'''
print(df[['Fare', 'Age']].corr())
# output:
#           Fare       Age
# Fare  1.000000  0.096067
# Age   0.096067  1.000000

'''HEATMAP::'''
sns.heatmap(df[['Fare', 'Age']].corr())
plt.show()