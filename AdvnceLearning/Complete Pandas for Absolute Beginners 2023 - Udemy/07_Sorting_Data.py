import pandas as pd

data = pd.read_csv('Data/sales.csv')
data.sort_values(by='Sales')
print(data)
'''output:
           State  Total Expenses  ... Inventory     Type
0     California            63.0  ...    2947.0  Regular
1     California            55.0  ...     659.0  Regular
2     California           143.0  ...     788.0  Regular
3     California           113.0  ...    1744.0    Decaf
4     California            37.0  ...     809.0    Decaf
...          ...             ...  ...       ...      ...
4236   Wisconsin            34.0  ...     458.0  Regular
4237   Wisconsin            36.0  ...     454.0  Regular
4238   Wisconsin            86.0  ...     506.0  Regular
4239   Wisconsin            79.0  ...     627.0  Regular
4240   Wisconsin            87.0  ...     513.0  Regular

[4241 rows x 11 columns]
'''

data.sort_values(by=['Sales', 'Profit'], ascending=False)
print(data)
'''output:
           State  Total Expenses  ... Inventory     Type
0     California            63.0  ...    2947.0  Regular
1     California            55.0  ...     659.0  Regular
2     California           143.0  ...     788.0  Regular
3     California           113.0  ...    1744.0    Decaf
4     California            37.0  ...     809.0    Decaf
...          ...             ...  ...       ...      ...
4236   Wisconsin            34.0  ...     458.0  Regular
4237   Wisconsin            36.0  ...     454.0  Regular
4238   Wisconsin            86.0  ...     506.0  Regular
4239   Wisconsin            79.0  ...     627.0  Regular
4240   Wisconsin            87.0  ...     513.0  Regular

[4241 rows x 11 columns]
'''

data.sort_index(ascending=False)
print(data)
'''output:
           State  Total Expenses  ... Inventory     Type
0     California            63.0  ...    2947.0  Regular
1     California            55.0  ...     659.0  Regular
2     California           143.0  ...     788.0  Regular
3     California           113.0  ...    1744.0    Decaf
4     California            37.0  ...     809.0    Decaf
...          ...             ...  ...       ...      ...
4236   Wisconsin            34.0  ...     458.0  Regular
4237   Wisconsin            36.0  ...     454.0  Regular
4238   Wisconsin            86.0  ...     506.0  Regular
4239   Wisconsin            79.0  ...     627.0  Regular
4240   Wisconsin            87.0  ...     513.0  Regular

[4241 rows x 11 columns]
'''

market_sort = data['Market'].sort_values()
print(market_sort)
'''output:
4240    Central
1224    Central
1223    Central
1222    Central
1221    Central
         ...   
2142       West
2141       West
2140       West
2150       West
2120       West
Name: Market, Length: 4241, dtype: object
'''