import pandas as pd

data = pd.read_csv('Data/sales.csv')
new_col = data['Profit'] + data['Sales']
print(new_col)
'''output:
0       -22.0
1       289.0
2       314.0
3       792.0
4       395.0
        ...  
4236    110.0
4237    144.0
4238    151.0
4239    128.0
4240    169.0
Length: 4241, dtype: float64
'''

data['New_Column'] = new_col
print(data)
'''output:
          State  Total Expenses  ...     Type  New_Column
0     California            63.0  ...  Regular       -22.0
1     California            55.0  ...  Regular       289.0
2     California           143.0  ...  Regular       314.0
3     California           113.0  ...    Decaf       792.0
4     California            37.0  ...    Decaf       395.0
...          ...             ...  ...      ...         ...
4236   Wisconsin            34.0  ...  Regular       110.0
4237   Wisconsin            36.0  ...  Regular       144.0
4238   Wisconsin            86.0  ...  Regular       151.0
4239   Wisconsin            79.0  ...  Regular       128.0
4240   Wisconsin            87.0  ...  Regular       169.0

[4241 rows x 12 columns]
'''

data.drop(columns=['Product', 'State'], inplace=True)
print(data)
'''output:
      Total Expenses  Sales   Market Size  ...  Inventory     Type  New_Column
0               63.0  109.0  Major Market  ...     2947.0  Regular       -22.0
1               55.0  201.0  Major Market  ...      659.0  Regular       289.0
2              143.0  289.0  Major Market  ...      788.0  Regular       314.0
3              113.0  576.0  Major Market  ...     1744.0    Decaf       792.0
4               37.0  247.0  Major Market  ...      809.0    Decaf       395.0
...              ...    ...           ...  ...        ...      ...         ...
4236            34.0   90.0  Small Market  ...      458.0  Regular       110.0
4237            36.0  113.0  Small Market  ...      454.0  Regular       144.0
4238            86.0  150.0  Small Market  ...      506.0  Regular       151.0
4239            79.0  131.0  Small Market  ...      627.0  Regular       128.0
4240            87.0  165.0  Small Market  ...      513.0  Regular       169.0

[4241 rows x 10 columns]
'''

data.drop(index=0, inplace=True)
print(data)
'''output:
      Total Expenses  Sales   Market Size  ...  Inventory     Type  New_Column
1               55.0  201.0  Major Market  ...      659.0  Regular       289.0
2              143.0  289.0  Major Market  ...      788.0  Regular       314.0
3              113.0  576.0  Major Market  ...     1744.0    Decaf       792.0
4               37.0  247.0  Major Market  ...      809.0    Decaf       395.0
5               99.0  582.0  Major Market  ...     1268.0    Decaf       873.0
...              ...    ...           ...  ...        ...      ...         ...
4236            34.0   90.0  Small Market  ...      458.0  Regular       110.0
4237            36.0  113.0  Small Market  ...      454.0  Regular       144.0
4238            86.0  150.0  Small Market  ...      506.0  Regular       151.0
4239            79.0  131.0  Small Market  ...      627.0  Regular       128.0
4240            87.0  165.0  Small Market  ...      513.0  Regular       169.0

[4240 rows x 10 columns]
'''