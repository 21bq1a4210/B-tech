'''
DEALING WITH MISSING VALUES IN PANDAS::
* Apart from outliers/anomalies, data alsos often contains missing values.
* In pandas, an NaN indicates a missing value.
* Consider the following dataframe called data with one missing value in the 'Age' column
            Name    Age
        ----------------
        0 Edison    28
        1 Edward    27
        2 James     NaN   <--- missing value
        3 Neesham   36
'''

'''
* FINDING MISSING VALUES IN PANDAS
    * The .isnull() tells us if a cell is empty or not.
    * Use the .sum() with the .isnull() to find total no.of missing values in the data.
        >> data.isnull()
                Name    Age
            ----------------
            0 False    False
            1 False    False
            2 False    True
            3 False    False

        >>data,isnull().sum()
            Names   0
            Age     1
            dtype:  int64
'''

from numpy import NaN
import pandas as pd
data1 = {'Name': ["Edison", "Edward", "James", "Neesham"],
         "Age": [28, 27, NaN, 36]}
df1 = pd.DataFrame(data1)
print(df1)
# output:
#       Name   Age
# 0   Edison  28.0
# 1   Edward  27.0
# 2    James   NaN
# 3  Neesham  36.0

print(df1.isnull())
#output:
#    Name    Age
# 0  False  False
# 1  False  False
# 2  False   True
# 3  False  False

print(df1.isnull().sum())
#output:
# Name    0
# Age     1
# dtype: int64

'''
* There are a no.of ways to deal with these missing values.
* Which method to use depends upon the kind of data and the task the
    data is supposed to accomplish.
* Different Methods Used are;
    * Deleting rows with missing values.
    * Replacing missing values with mean/ median/ mode.
'''

'''
DELETING ROWS WITH MISSING VALUES:
* One way to deal with the missing values is to delete the rows containing missing
    values.
* Use the .dropna() with inplace set to True to remove missing values from thr dataset.
    >data.dropna(inplace=True)
    >data
            Name    Age
        ----------------
        0 Edison    28
        1 Edward    27
        3 Neesham   36
'''
del_missing_val_row = df1.dropna()
print(del_missing_val_row)
# output:
#       Name   Age
# 0   Edison  28.0
# 1   Edward  27.0
# 3  Neesham  36.0

'''
REPLACING MISSING VALUES WITH MEAN/ MEDIAN/ MODE:
* We can also replace the missing values in each column with one of the the
    statistical measures (mean/ median/ mode) of the column.
* Use the .fillna() method to fill the missing values with mean, median or mode.
    > data.fillna(data.mean(), inplace = True)
    > data
             Name    Age
        ----------------
        0 Edison    28.000000
        1 Edward    27.000000
        2 James     30.333333
        3 Neesham   36.000000
'''

#MEAN
mean_data = df1.copy()
mean_data['Age'] = pd.to_numeric(df1['Age'], errors='coerce')
print(mean_data)
# output:
#      Name   Age
# 0   Edison  28.0
# 1   Edward  27.0
# 2    James   NaN
# 3  Neesham  36.0
print(mean_data['Age'].mean()) #30.333333333333332
mean_data['Age'].fillna(df1['Age'].mean(), inplace=True)
print(mean_data)
#output:
#       Name        Age
# 0   Edison  28.000000
# 1   Edward  27.000000
# 2    James  30.333333
# 3  Neesham  36.000000

#MODE
mode_data = df1.copy()
mode_data['Age'] = pd.to_numeric(df1['Age'], errors='coerce')
print(mode_data)
#output:
#       Name   Age
# 0   Edison  28.0
# 1   Edward  27.0
# 2    James   NaN
# 3  Neesham  36.0
mode_data['Age'].fillna(df1['Age'].mode(), inplace=True)
print(mode_data)
#output:
#       Name   Age
# 0   Edison  28.0
# 1   Edward  27.0
# 2    James  36.0
# 3  Neesham  36.0