pl=[1,3,0,3,5,6,3]
cap=3
fr=[]
#FIFO
def FIFO(pl,cap):
    fr=[]
    pf,ph=0,0
    for pg in pl:
        if pg not in fr:
            if len(fr)<cap:
                fr.append(pg)
            else:
                fr.pop()
                fr.append(pg)
            pf+=1
        else:
            ph+=1
    return pf,ph
#print(FIFO(pl,cap))
    
#LRU
def LRU(pl,cap):
    fr=[]
    lru=[]
    ph,pf=0,0
    for pg in pl:
        if pg not in fr:
            if len(fr)<cap:
                fr.append(pg)
            else:
                lru=[fr.index(i) for i in fr]
                lru.sort()
                fr.pop(lru[0])
                fr.append(pg)
            pf+=1
        else:
            ph+=1
    return pf,ph
#print(LRU(pl,cap))
#LFU
#MFU