#@title exp-14
import pandas as pd
import numpy as np
exam_data = {'name': ['Uzumaki Naruto', 'Monkey D. Luffy', 'Jin kazama', 'David Martinez',"Loid Forger"],
 'score': [19, 9, 16.5, np.nan, 16],
 'attempts': [1, 3, 2, 3, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(exam_data , index=labels)
print(df[(df['attempts'] < 2) & (df['score'] > 15)])