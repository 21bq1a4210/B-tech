import pandas as pd

data = pd.read_csv('Data/sales.csv')
null_sum = data.isnull().sum()
print(null_sum)
'''output:
State             0
Total Expenses    3
Product           0
Sales             2
Market Size       0
Profit            6
Market            0
Marketing         0
Product Type      0
Inventory         1
Type              0
dtype: int64
'''

data.dropna(inplace=True)
print(data.isnull().sum())
'''output:
State             0
Total Expenses    0
Product           0
Sales             0
Market Size       0
Profit            0
Market            0
Marketing         0
Product Type      0
Inventory         0
Type              0
dtype: int64
'''

data.to_csv('Data/modified.cssv')