import pandas as pd

data = pd.read_csv('Data/sales.csv')

print(data.iloc[4]) #iloc --> integer loc
''' Output:
State               California
Total Expenses            37.0
Product              Chamomile
Sales                    247.0
Market Size       Major Market
Profit                   148.0
Market                    West
Marketing                   26
Product Type        Herbal Tea
Inventory                809.0
Type                     Decaf
Name: 4, dtype: object
'''

data = pd.read_csv('Data/sales.csv', index_col='State')

print(data.loc['California'])
''' output:
            Total Expenses         Product  ...  Inventory     Type
State                                       ...                    
California            63.0        Amaretto  ...     2947.0  Regular
California            55.0       Green Tea  ...      659.0  Regular
California           143.0     Caffe Mocha  ...      788.0  Regular
California           113.0  Decaf Espresso  ...     1744.0    Decaf
California            37.0       Chamomile  ...      809.0    Decaf
...                    ...             ...  ...        ...      ...
California            31.0            Mint  ...      548.0    Decaf
California            36.0      Darjeeling  ...      777.0  Regular
California            40.0      Darjeeling  ...      897.0  Regular
California            33.0       Earl Grey  ...      441.0  Regular
California            83.0     Caffe Latte  ...     1778.0  Regular

[281 rows x 10 columns]
'''

new_data = data.head()
print(new_data)
''' output:
            Total Expenses         Product  ...  Inventory     Type
State                                       ...                    
California            63.0        Amaretto  ...     2947.0  Regular
California            55.0       Green Tea  ...      659.0  Regular
California           143.0     Caffe Mocha  ...      788.0  Regular
California           113.0  Decaf Espresso  ...     1744.0    Decaf
California            37.0       Chamomile  ...      809.0    Decaf

[5 rows x 10 columns]
'''

index = ['one', 'two', 'three', 'four', 'five']
new_data.set_index([index], inplace=True)
print(new_data)
''' output:
       Total Expenses         Product  Sales  ... Product Type  Inventory     Type
one              63.0        Amaretto  109.0  ...       Coffee     2947.0  Regular
two              55.0       Green Tea  201.0  ...          Tea      659.0  Regular
three           143.0     Caffe Mocha  289.0  ...     Espresso      788.0  Regular
four            113.0  Decaf Espresso  576.0  ...     Espresso     1744.0    Decaf
five             37.0       Chamomile  247.0  ...   Herbal Tea      809.0    Decaf

[5 rows x 10 columns]
'''
print(new_data.loc['two'])
''' output:
Total Expenses            55.0
Product              Green Tea
Sales                    201.0
Market Size       Major Market
Profit                    88.0
Market                    West
Marketing                   24
Product Type               Tea
Inventory                659.0
Type                   Regular
Name: two, dtype: object
'''
print(type(new_data.loc['one'])) #<class 'pandas.core.series.Series'>