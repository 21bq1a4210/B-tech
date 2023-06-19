req=[2,43,6,49,57]
head=50

import matplotlib.pyplot as plt
def plot_move(move):
    plt.plot(range(len(move)),[m[0] for m in move], 'bo-')
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

td,move=fcfs(req,head)
print(td,move)
plot_move(move)
#b) SSTF
#c) SCAN
#d) C-SCAN
#e) LOOK
#f) C-LOOK