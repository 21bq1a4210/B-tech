#@title exp-13
import pandas as pd
import numpy as np
exam_data = {'name': ['Uzumaki Naruto', 'Monkey D. Luffy', 'jin kazama', 'David Martinez',"Loid Forger"],
 'score': [12.5, 9, 16.5, np.nan, 9],
 'attempts': [1, 3, 2, 3, 2],
 'qualify': ['yes', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(exam_data , index=labels)
print(df)