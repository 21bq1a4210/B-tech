def SJF(process,n):
    process=sorted(process,key=lambda x:x[1])
    wt=0
    waitsum=0
    turn_sum=0
    print("Process \t BurstTime \t WaitingTime \t TurnAroundTime")
    for i in range(n):
        turn=wt+process[i][1]
        print("p"+str(process[i][0])+"\t\t"+str(process[i][1])+"\t\t"+str(wt)+"\t\t"+str(turn))
        wt += process[i][1]
        waitsum += wt
        turn_sum += turn
    waitsum -= wt
    avgwaittime=round(waitsum/n,3)
    avgturntime=round(turn_sum/n,3)
    return(avgwaittime,avgturntime)

if __name__=="__main__":
    n=int(input("Enter no. of processes :"))
    process=[]
    for i in range(1,n+1):
        process.append([i,(int(input("Enter BT:")))])
    print("\n Shortest Job First Scheduling :")
    res=SJF(process,n)
    print("\n Average Waiting Time=",res[0])
    print("Average Turn Around Time=",res[1])
    
'''
    output:
    Enter no. of processes :3
    Enter BT:10
    Enter BT:30
    Enter BT:20

    Shortest Job First Scheduling :
    Process 	 BurstTime 	 WaitingTime 	 TurnAroundTime
    p1		10		0		10
    p3		20		10		30
    p2		30		30		60

    Average Waiting Time= 13.333
    Average Turn Around Time= 33.333
'''