import pandas as pd

myDataset={'emp name':['ravi','sarath','chandra','eswar','siva'],
           'emp id':[4236,4210,4237,4209,4200],
           'emp salary':[75000,50000,60000,65000,70000]
           }
'''
DA=salary*40)//100
HRA=salary*20)//100
TA=salary*5)//100
Bonus=salary*10//100
netsalary=salary+hra+da+ta+bouns
'''

myDataset['TA'],myDataset['DA'],myDataset['HRA'],myDataset['bonus'],myDataset['netSalary']=[],[],[],[],[]
for i in myDataset['emp salary']:
  myDataset['TA'].append((i*5)/100)
  myDataset['DA'].append((i*40)/100)
  myDataset['HRA'].append((i*20)/100)
  myDataset['bonus'].append((i*10)/100)
  myDataset["netSalary"].append(i*1.75)
  
df=pd.DataFrame(myDataset)
sorted_df = df.sort_values(by=['netSalary'], ascending=False)

print(sorted_df)
print()
print("high salary:")
print(sorted_df.head(1))
print()
print("lowest salary:")
print(sorted_df.tail(1))
print()
print("average sal:",sum(myDataset["netSalary"])/5)
