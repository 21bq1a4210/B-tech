def LRU(pages,cap):
    memory=[]
    lru=[]
    pagefaults=0
    for page in pages:
        if page not in memory:
            if len(memory)<cap:
                pagefaults+=1
                memory.append(page)
                lru.append(page)
            else:
                pagefaults+=1
                index=memory.index(lru[0])
                memory[index]=page
                lru.pop(0)
                lru.append(page)
        else:
            index = lru.index(page)
            lru.pop(index)
            lru.append(page)
    return pagefaults

page=list(map(int,input("enter the sequence").split()))
cap=int(input("enter the max capasity:"))
print("Ans:",LRU(page,cap))
