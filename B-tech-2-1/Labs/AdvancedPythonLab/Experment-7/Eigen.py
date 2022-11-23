import numpy as np
row,col=list(map(int,input('Enter row and col:').split()))
A=np.array(list(map(int,input('Enter matrix A:').split())))
A.shape=row,col
print(A)
print()
if(row==col):
    e1,e2=np.linalg.eig(A)
    print("Eigenvalues of the said matrix")
    print(e1,'\n')
    print("Eigenvalues of the said matrix")
    print(e2)
else:
    print("Not a square matrix")