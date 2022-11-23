#printing in the format of array 
from numpy import *
a1=array([[1,2,3],[4,5,6],[7,8,9]])   # 2D array
r,c=a1.shape
for i in range(r):
  for j in range(c):
    print(a1[i][j],end=" ")
  print()
