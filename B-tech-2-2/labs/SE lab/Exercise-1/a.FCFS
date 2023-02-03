def FCFS(processes):
    ''' creating array for Completion Time, Turn Around Time, Waiting Time
        which helps to store the respective process
    '''
    ct=[0]*len(processes)
    tat=[0]*len(processes)
    wt=[0]*len(processes)
    
    #printing the table headings
    print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tTurnAround Time\tWaiting Time")
    for j in range(len(processes)):
        ct[j]=processes[j][2]+ct[j-1] #Completion Time (less than cumulative frequency of processes)
        tat[j]=ct[j]-processes[j][1]  #Turn Around Time = Completion Time - Arrival Time  
        wt[j]=tat[j]-processes[j][2]  #Waiting Time = Turnaround time - Burst Time
        #printing the table data
        print(f"{processes[j][0]}\t\t{processes[j][1]}\t\t{processes[j][2]}\t\t{ct[j]}\t\t{tat[j]}\t\t{wt[j]}")
        print()
        
    print(f"Avg TurnAround Time:{sum(tat)/len(processes)}")	#Avg TurnAround Time=(sum of indivudual Turn Around Time)/(total no.of processes) 
    print(f"Avg Wating Time:{sum(wt)/len(processes)}")		#Avg Wating Time=(sum of indivudual Wating Time)/(total no.of processes)

if __name__=='__main__':
    '''storing the basic info of process
       as follows: (Process ID, Arrival Time, Burst Time)
    '''
    processes=[('p1',0,2),('p2',1,6),('p3',2,4)]
    FCFS(processes)