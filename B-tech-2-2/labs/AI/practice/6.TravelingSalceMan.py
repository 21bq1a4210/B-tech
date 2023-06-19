from itertools import permutations as perm
def tsm(g,sn):
    v=range(len(g))
    mc=float('inf')
    for p in perm(v):
        if p[0]==sn:
            c=sum(g[p[i]][p[i+1]] for i in range(len(p)-1))
            c+=g[p[-1]][p[0]]
            mc=min(c,mc)
    return mc

g=[[0,10,6,20],[5,0,9,10],[6,13,0,12],[20,10,12,0]]
print(tsm(g,0))
#out put:
#33