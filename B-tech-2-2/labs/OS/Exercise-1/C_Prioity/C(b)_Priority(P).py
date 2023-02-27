def findWaitingTime(proc ,n,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i]=proc[i-1][1]+wt[i-1]
def findTurnAroundTime(proc,n,wt,tat):
    for i in range(n):
        tat[i]=proc[i][1]+wt[i-1]
def findavgTime(proc,n):
    wt=[0]*n
    tat=[0]*n
    findWaitingTime(proc,n,wt)
    findTurnAroundTime(proc,n,wt,tat)
    print("\n Processes  BT  WT  TAT ")
    total_wt=0
    total_tat=0
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print("  ",proc[i][0],"\t\t",proc[i][1],"\t\t",wt[i],"\t\t",tat[i])
    print("\n avg wt=%5f"%(total_wt/n))
    print("\n avg tat=",total_tat/n)
def priorityScheduling(proc,n):
    proc=sorted(proc,key=lambda proc:proc[2],reverse=True)
    print("Order in which processes gets executed")
    for i in proc:
        print(i[0],end="  ")
    findavgTime(proc,n)
if __name__=="__main__":
    proc=[[1,10,1],[2,5,0],[3,8,1]]
    n=3
    priorityScheduling(proc,n)
"""
Order in which processes gets executed
1  3  2  
 Processes  BT  WT  TAT 
   1         10          0       28
   3         8       10          8
   2         5       18          15

 avg wt=9.333333
 avg tat= 17.0
"""