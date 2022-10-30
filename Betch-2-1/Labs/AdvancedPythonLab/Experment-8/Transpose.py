import numpy as np
row,col=list(map(int,input('Enter row and col:').split()))
A=np.array(list(map(int,input('Enter matrix A:').split())))

A.shape=(int(row),int(col))
print("Given Array:\n",A)
print()
print("Transpose:\n",np.transpose(A))
