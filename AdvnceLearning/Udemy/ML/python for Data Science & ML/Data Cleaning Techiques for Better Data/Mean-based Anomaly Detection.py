import numpy as np
import pandas as pd
data = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
mean = np.mean(data)
std = np.std(data)
outliers = []
for itm in data:
    if itm < mean - std or itm > mean + std:
        outliers.append(itm)
print(outliers)