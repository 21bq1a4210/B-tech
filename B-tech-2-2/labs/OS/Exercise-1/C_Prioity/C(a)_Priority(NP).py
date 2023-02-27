n=int(input("Enter no. of processes : "))
print("Enter the Processes-ID,Burst Time,Priority : ")
l=[]
for i in range(n):
    l.append(list(map(int,input("\t\t").split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][2]>l[j][2]:
            #sorting the priority order
            l[i],l[j]=l[j],l[i]
ct=0
for i in  range(n):
    ct += l[i][1]
    l[i].append(ct)
tat,wt=0,0
print("PID BT  Priority   AT   TAT   WT")
for i in range(n):
    print(l[i][0],"   ",l[i][1],"   ",l[i][2],"   ",0,"   ",l[i][3],"  ",l[i][3]-l[i][1])
tat,wt=0,0
for i in range(n):
    tat += l[i][3]
    wt  += l[i][3]-l[i][1]
print("avg TAT:",tat/n)
print("avg WT:",wt/n)


"""
Output :
Enter no. of processes : 5
Enter the Processes-ID,Burst Time,Priority : 
        1 10 3
        2 1 1
        3 2 4
        4 1 5
        5 5 2
PID BT  Priority   AT   TAT   WT
2     1     1     0     1    0
5     5     2     0     6    1
1     10     3     0     16    6
3     2     4     0     18    16
4     1     5     0     19    18
avg TAT: 12.0
avg WT: 8.2
"""