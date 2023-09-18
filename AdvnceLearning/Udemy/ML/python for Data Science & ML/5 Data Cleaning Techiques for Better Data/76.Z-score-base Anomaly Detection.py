'''
Z-score::
* another technique for anomaly detection is Z-score
* it is a statistical measure showing how many std certain value is from the mean
* it is defined as:
    z = (value - mean) / std
* if the z-score of a value is greater than a reasonable threshold, it is considered an anomaly
'''

import numpy as np
import pandas as pd

data = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
mean = np.mean(data)
std = np.std(data)
threshold = 1.5
outliers = []

for itm in data:
    z_score = (itm - mean) / std
    if z_score > threshold:
        outliers.append(itm)
print(outliers)