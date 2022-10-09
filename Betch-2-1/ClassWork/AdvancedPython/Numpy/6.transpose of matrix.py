#transpose of math
from numpy import *
a1=array([[1,2,3],[4,5,6],[7,8,9]])   # 2D array
r,c=a1.shape
print("original math:")
for i in range(r):
  for j in range(c):
    print(a1[i][j],end=" ")
  print()
print("\ntransposed math:")
for i in range(r):
  for j in range(c):
    print(a1[j][i],end=" ")
  print()
