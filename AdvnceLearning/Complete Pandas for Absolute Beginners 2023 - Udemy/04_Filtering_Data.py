import pandas as pd

data = pd.read_csv('Data/sales.csv')

high_sales = (data['Sales'] > 300)
#print(high_sales)
'''output:
0       False
1       False
2       False
3        True
4       False
        ...  
4236    False
4237    False
4238    False
4239    False
4240    False
Name: Sales, Length: 4241, dtype: bool
'''

#print(data.loc[high_sales])
'''output:
           State  Total Expenses  ... Inventory     Type
3     California           113.0  ...    1744.0    Decaf
5     California            99.0  ...    1268.0    Decaf
9     California           142.0  ...    2067.0  Regular
10    California           166.0  ...    2617.0  Regular
11    California           139.0  ...    2580.0  Regular
...          ...             ...  ...       ...      ...
3932  Washington            71.0  ...     932.0    Decaf
3933  Washington            73.0  ...    1119.0    Decaf
4004  Washington            75.0  ...     961.0    Decaf
4122   Wisconsin           149.0  ...     705.0  Regular
4213   Wisconsin           139.0  ...     705.0  Regular

[669 rows x 11 columns]
'''

#print(data.loc[high_sales, ['Product', 'Profit', 'Sales']])
'''output:
             Product  Profit  Sales
3     Decaf Espresso   216.0  576.0
5              Lemon   291.0  582.0
9          Columbian   364.0  687.0
10         Columbian   508.0  902.0
11         Columbian   349.0  664.0
...              ...     ...    ...
3932       Chamomile   171.0  329.0
3933       Chamomile   171.0  334.0
4004       Chamomile   179.0  347.0
4122       Columbian    35.0  317.0
4213       Columbian    48.0  314.0

[669 rows x 3 columns]
'''

#print(data['Product'].unique())
'''output:
['Amaretto' 'Green Tea' 'Caffe Mocha' 'Decaf Espresso' 'Chamomile' 'Lemon'
 'Mint' 'Darjeeling' 'Earl Grey' 'Columbian' 'Caffe Latte'
 'Decaf Irish Cream' 'Regular Espresso']
'''

product = ['Green Tea', 'Lemon', 'Mint']
filt = data['Product'].isin(product)
#print(data.loc[filt])
'''output:
 State  Total Expenses    Product  ...  Product Type Inventory     Type
1     California            55.0  Green Tea  ...           Tea     659.0  Regular
5     California            99.0      Lemon  ...    Herbal Tea    1268.0    Decaf
6     California            25.0       Mint  ...    Herbal Tea     541.0    Decaf
12    California            54.0  Green Tea  ...           Tea     677.0  Regular
17    California            88.0      Lemon  ...    Herbal Tea     923.0    Decaf
...          ...             ...        ...  ...           ...       ...      ...
4193   Wisconsin            25.0      Lemon  ...    Herbal Tea     842.0    Decaf
4194   Wisconsin            20.0      Lemon  ...    Herbal Tea     856.0    Decaf
4195   Wisconsin            21.0      Lemon  ...    Herbal Tea     863.0    Decaf
4230   Wisconsin            27.0      Lemon  ...    Herbal Tea     842.0    Decaf
4231   Wisconsin            25.0      Lemon  ...    Herbal Tea     772.0    Decaf

[959 rows x 11 columns]
'''
