req=[2,43,6,49,57]
head=50

import matplotlib.pyplot as plt
def plot_move(move):
    #plt.plot(range(len(move)),[m[0] for m in move], 'bo-')
    plt.plot(range(len(move)),[m[1] for m in move], 'ro-')
    plt.title("Name of Algo..")
    plt.xlabel("Request")
    plt.ylabel("Disk Cylinder")
    plt.legend(['Start Position', 'Disk Requests'])
    plt.grid(True)
    plt.show()
    
#a) FCFS
def fcfs(req,head):
    td=0
    move=[]
    cpos=head
    for r in req:
        dis=abs(cpos-r)
        td+=dis
        move.append((cpos,r))
        cpos=r
    return td,move

# td,move=fcfs(req,head)
# print(td,move)
# plot_move(move)


#b) SSTF
def sstf(req,head):
    td=0
    move,rreq=[],req[:]
    cpos=head
    
    while rreq:
        dis=[abs(cpos-r) for r in rreq]
        sdi=dis.index(min(dis))
        nr=rreq.pop(sdi)
        d=dis[sdi]
        td+=d
        move.append((cpos,nr))
        cops=nr
    return td,move

# td,move=sstf(req,head)
# print(td,move)
# plot_move(move)

#c) SCAN
def scan(req,head,d):
    td=0
    move=[]
    cpos=head
    
    lr=[l for l in req if l<cpos]
    lr.sort(reverse=True)
    lr.insert(len(lr),0)
    
    rr=[r for r in req if r>cpos]
    rr.sort()
    #rr.insert(len(rr),199)
    
    if d==0:
        for r in lr:
            dis=abs(cpos-r)
            td+=dis
            move.append((cpos,r))
            cpos=r
        
        for r in rr:
            dis=abs(cpos-r)
            td+=dis
            move.append((cpos,r))
            cpos=r
    #else
    return td,move

td,move=scan(req,head,d=0)
print(td,move)
plot_move(move)
#d) C-SCAN
#e) LOOK
#f) C-LOOK