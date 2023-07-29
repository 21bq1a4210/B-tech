import pandas as pd

data = pd.read_csv('Data/sales.csv')

print(data.columns)
'''output:
Index(['State', 'Total Expenses', 'Product', 'Sales', 'Market Size', 'Profit',
       'Market', 'Marketing', 'Product Type', 'Inventory', 'Type'],
      dtype='object')
'''

print(data.Product)
'''output:
0             Amaretto
1            Green Tea
2          Caffe Mocha
3       Decaf Espresso
4            Chamomile
             ...      
4236        Darjeeling
4237        Darjeeling
4238         Earl Grey
4239         Earl Grey
4240         Earl Grey
Name: Product, Length: 4241, dtype: object
'''

'''
print(data.Product Type) 
gives an err cuz pandas doesnt accept space between the column value.
we can avoid that by replacing the ' ' with '_' 
'''
print(data.columns.str.replace(' ', '_'))
'''output:
Index(['State', 'Total-Expenses', 'Product', 'Sales', 'Market-Size', 'Profit',
       'Market', 'Marketing', 'Product-Type', 'Inventory', 'Type'],
      dtype='object')
'''
data.columns = data.columns.str.replace(' ', '_')
print(data.Product_Type)
'''output:
0           Coffee
1              Tea
2         Espresso
3         Espresso
4       Herbal Tea
           ...    
4236           Tea
4237           Tea
4238           Tea
4239           Tea
4240           Tea
Name: Product_Type, Length: 4241, dtype: object
'''

data.rename(columns={'Marketing': 'Trade'}, inplace=True)

#modify value:
data.loc[2, 'Total_Expenses'] = 500
print(data)

data.at[2, 'Total_Expenses'] = 707
print(data)