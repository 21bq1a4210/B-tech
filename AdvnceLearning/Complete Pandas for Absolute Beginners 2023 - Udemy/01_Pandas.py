import pandas as pd
data = pd.read_csv('Data/sales.csv')
#print(data)

head = data.head()
#print(head)

head = data.head(10)
#print(head)

tail = data.tail(10)
#print(tail)

shape = data.shape
print(shape)    # (4241, 11)