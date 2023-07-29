import pandas as pd
data = pd.read_csv('Data/sales.csv')
print(type(data))   #output: <class 'pandas.core.frame.DataFrame'>

data.info()
''' Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4241 entries, 0 to 4240
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   State           4241 non-null   object 
 1   Total Expenses  4238 non-null   float64
 2   Product         4241 non-null   object 
 3   Sales           4239 non-null   float64
 4   Market Size     4241 non-null   object 
 5   Profit          4235 non-null   float64
 6   Market          4241 non-null   object 
 7   Marketing       4241 non-null   int64  
 8   Product Type    4241 non-null   object 
 9   Inventory       4240 non-null   float64
 10  Type            4241 non-null   object 
dtypes: float64(4), int64(1), object(6)
memory usage: 364.6+ KB
'''

des = data.describe()
print(des)
''' Output:
       Total Expenses        Sales       Profit    Marketing    Inventory
count     4238.000000  4239.000000  4235.000000  4241.000000  4240.000000
mean        53.989146   192.567351    60.840614    31.124499   747.971226
std         32.295812   150.563621   101.301672    26.983618   660.498475
min         10.000000    17.000000  -638.000000     0.000000 -3534.000000
25%         33.000000   100.000000    17.000000    13.000000   431.500000
50%         46.000000   138.000000    40.000000    22.000000   619.000000
75%         65.000000   230.000000    92.000000    39.000000   901.000000
max        190.000000   912.000000   778.000000   156.000000  8252.000000
'''

insects = ['Ants', 'Cricket', 'Bee']
print(type(insects)) #<class 'list'>
#
df = pd.DataFrame(insects, columns=['Insects'])
print(df)

''' Outpput
    Insects  
0      Ants
1  Cricket
2       Bee
'''

animals = {
    'Mammals': ['Cow', 'Sheep', 'Lion'],
    'Reptiles': ['Crocodile', 'Lizard', 'Snake'],
    'Insects': insects
}
print(type(animals)) #<class 'dict'>
df = pd.DataFrame(animals)
print(df)
''' output:
  Mammals    Replies  Insects
0     Cow  Crocodile     Ants
1   Sheep     Lizard  Cricket
2    Lion      Snake      Bee
'''
print(df['Mammals'])
''' output:
0      Cow
1    Sheep
2     Lion
Name: Mammals, dtype: object
'''
print(df.Reptiles)
''' output:
0    Crocodile
1       Lizard
2        Snake
Name: Reptiles, dtype: object
'''
print(type(df.Reptiles)) #<class 'pandas.core.series.Series'>

print(df.iloc[0])
''' output:
Mammals           Cow
Reptiles    Crocodile
Insects          Ants
Name: 0, dtype: object
'''
print(type(df.iloc[1])) #<class 'pandas.core.series.Series'>

print(df.iloc[[0,1]])
''' output:
 Mammals   Reptiles  Insects
0     Cow  Crocodile     Ants
1   Sheep     Lizard  Cricket
'''