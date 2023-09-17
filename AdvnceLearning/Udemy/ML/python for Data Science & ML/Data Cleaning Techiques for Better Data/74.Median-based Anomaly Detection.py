import numpy as np
import pandas as pd
data = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
median = np.median(data)
threshold = 2
outliers = []
for itm in data:
    if abs(itm - median) > threshold:
        outliers.append(itm)
print(outliers)