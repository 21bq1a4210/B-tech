'''
FEATURE SCALING ::
* Sometimes, we might wish to normalize the range of rach feature (column) of the
    given dataset.
* For example, consider the given dataframe where the range of each
    featur (column) is different.
* we would like to scale all the features to the same range, eg. 0-1, 1-100, etc.
    df
        Age     Salary
    ------------------
    0   28.0    10_000
    1   27.0    15_000
    2   30.0    11_000
    3   36.0    11_000
    4   27.0    13_000
'''
import pandas as pd
data = {
    "Age": [28.0, 27.0, 30.0, 36.0, 27.0],
    "Salary": [10000, 15000, 11000, 11000, 13000]
}
df = pd.DataFrame(data)
print(df)
#output:
#     Age  Salary
# 0  28.0   10000
# 1  27.0   15000
# 2  30.0   11000
# 3  36.0   11000
# 4  27.0   13000

'''
NORMALIZATION ::
* One simple method of feature scaling is normalization, also called min-max scaling.
* For every value in a feature, we subtract the min value of the particular
    feature from it and divide it by the difference of max and min
    value of the feature
        * Normalized Value = (original value - min value) / (max value - min value)
* This method scales the features in the range [0,1]
* For min-max scaling, use the following lines of code:
    normalized_df = (df - df.min())/ (df.max() - df.min())
* Pandas will automatically use feature min-max value for each feature.
'''
normalized_df = (df - df.min()) / (df.max() - df.min())
print(normalized_df)
#output:
#   Age        Salary
# 0  0.111111     0.0
# 1  0.000000     1.0
# 2  0.333333     0.2
# 3  1.000000     0.2
# 4  0.000000     0.6

'''
STANDARDIZATION ::
* In this, for every value of a feature, we substract the mean of that
    feature from the value and divide the result by the standard devation of that
    feature.
    * Standardized value = (original value - mean) / standard deviation
*  As a result, the standard deviation of the feature becomes 1
'''
standardized_df = (df - df.min() / (df.max() - df.min()))
print(standardized_df)
#output:
#     Age   Salary
# 0  25.0   9998.0
# 1  24.0  14998.0
# 2  27.0  10998.0
# 3  33.0  10998.0
# 4  24.0  12998.0
print(standardized_df.std())
#output:
# Age          3.781534
# Salary    2000.000000
# dtype: float64