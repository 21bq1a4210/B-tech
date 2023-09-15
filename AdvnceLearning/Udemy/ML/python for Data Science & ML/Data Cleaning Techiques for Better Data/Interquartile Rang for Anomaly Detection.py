'''
IQR::
* we can also use iqr of detecting anomalies in the data
* a quartile divides the dataset (sorted from smallest to largest) into 3 points and 4 intervals
* the IQR is difference b/w 3rd and 1st
    IQR = Q3 - Q1   (intterquartile)
* consider the following series
    x = [2.3, 2.2, 4.5, 2.1, 2.5]
* we first sort this list form smallest to largest
    x = [2.1, 2.2, 2.3, 2.5, 4.5]
* the first quartile 25%, which is 2.2
* the second quartile is 50%, which is 2.3 (median)
* the 3rd quartile is 75%, which is 2.5
* use the np.percentile() to get the quartiles of a dataset
    * Automatically sorts the data from smallest to largest
* Anyvalue less than (Q1 - 1.5 x IQR) or greater than (Q3 + 1.5 x IQR) is considered an anomaly
'''

import pandas as pd
import numpy as np

data = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
Q1, Q3 = np.percentile(data, [25, 75])
IQR = Q3 - Q1
outliers = []

for itm in data:
    if itm < (Q1 - 1.5 * IQR) or itm > (Q3 + 1.5 * IQR):
        outliers.append(itm)

print(outliers)