def TowerOfHonoie(n,s,a,d):
    if n==1:
        print(f"move disk 1 from {s} to {d}")
        return
    TowerOfHonoie(n-1,s,d,a)
    print(f"move disk {n} from {s} to {d}")
    TowerOfHonoie(n-1,a,s,d)
TowerOfHonoie(3,'a','b','c')

#out put
# move disk 1 from a to c
# move disk 2 from a to b
# move disk 1 from c to b
# move disk 3 from a to c
# move disk 1 from b to a
# move disk 2 from b to c
# move disk 1 from a to c

