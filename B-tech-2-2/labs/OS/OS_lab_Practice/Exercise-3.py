##deadlock_avoid

n,m=5,3
alloc=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
avil=[3,3,2]

need=[[max[i][j]-alloc[i][j] for j in range(m)]
       for i in range(n)]

fin=[0]*n
seq=[]

while 0 in fin:
    for i in range(n):
        if fin[i]==0 and all([need[i][j] <= avil[j] for j in range(m)]):
            fin[i]=1
            seq.append(i)
            avil=[alloc[i][j]+avil[j] for j in range(m)]
print(seq)
            