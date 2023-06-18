pl = [ 6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0]
cap=3
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
print(FIFO(pl,cap))
    
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
print(LRU(pl,cap))

#LFU
def LFU(pl,cap):
    fr={}
    lru=[]
    ph,pf=0,0
    for pg in pl:
        if pg not in fr:
            if len(fr)<cap:
                fr[pg]=1
                #print(fr)
            else:
                rm=min(fr,key=lambda k: fr[k])
                del fr[rm]
                fr[pg]=1
                #print(fr)
            pf+=1
        else:
            fr[pg]+=1
            ph+=1
    return pf,ph
print(LFU(pl,cap))
                
#MFU
def MFU(pl,cap):
    fr={}
    lru=[]
    ph,pf=0,0
    for pg in pl:
        if pg not in fr:
            if len(fr)<cap:
                fr[pg]=1
                #print(fr)
            else:
                rm=max(fr,key=lambda k: fr[k])
                del fr[rm]
                fr[pg]=1
                #print(fr)
            pf+=1
        else:
            fr[pg]+=1
            ph+=1
    return pf,ph
print(MFU(pl,cap))