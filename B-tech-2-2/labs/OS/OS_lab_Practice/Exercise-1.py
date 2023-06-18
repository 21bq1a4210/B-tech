# # def sjf_non_preemptive(processes, arrival_time, burst_time):
# #     
# #     n = len(processes)
# #     completion_time = [0] * n
# #     turnaround_time = [0] * n
# #     waiting_time = [0] * n
# #     
# #     sorted_processes = sorted(zip(processes, arrival_time, burst_time), key=lambda x: x[1])
# #     current_time = 0
# #     print(sorted_processes)
# #     
# #     for i in range(n):
# #         process, arrival, burst = sorted_processes[i]
# #         current_time = max(current_time, arrival)
# #         completion_time[i] = current_time + burst
# #         current_time += burst
# #         turnaround_time[i] = completion_time[i] - arrival
# #         waiting_time[i] = turnaround_time[i] - burst
# # 
# #     return completion_time, turnaround_time, waiting_time
# # 
# # # Example usage
# # processes = [1, 2, 3, 4]
# # arrival_time = [0, 1, 2, 3]
# # burst_time = [5, 3, 8, 6]
# # 
# # completion_time, turnaround_time, waiting_time = sjf_non_preemptive(processes, arrival_time, burst_time)
# # 
# # print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
# # for i in range(len(processes)):
# #     print(f"{processes[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
# 
# def priority_non_preemptive(processes, arrival_time, burst_time, priority):
#     n = len(processes)
#     completion_time = [0] * n
#     turnaround_time = [0] * n
#     waiting_time = [0] * n
# 
#     sorted_processes = sorted(zip(processes, arrival_time, burst_time, priority), key=lambda x: (x[1],x[3]))
#     current_time = 0
#     print(sorted_processes)
#     for i in range(n):
#         process, arrival, burst, prio = sorted_processes[i]
#         current_time = max(current_time, arrival)
#         completion_time[i] = current_time + burst
#         current_time += burst
#         turnaround_time[i] = completion_time[i] - arrival
#         waiting_time[i] = turnaround_time[i] - burst
# 
#     return completion_time, turnaround_time, waiting_time
# 
# # Example usage
# processes = [1, 2, 3, 4,5,6,7]
# arrival_time = [0,2,1,4,6,5,7]
# burst_time = [3,5,4,2,9,4,10]
# priority = [2,6,3,5,7,4,10]
# 
# completion_time, turnaround_time, waiting_time = priority_non_preemptive(processes, arrival_time, burst_time, priority)
# 
# print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
# for i in range(len(processes)):
#     print(f"{processes[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
# 
# 
# # Process	Completion Time	Turnaround Time	Waiting Time
# # 1		5		5		0
# # 2		8		7		4
# # 3		16		14		6
# # 4		22		19		13

def pnp(p,at,bt,prio):
    n=len(p)
    CT,TT,WT=[0]*n, [0]*n, [0]*n
    sorted_p=sorted(zip(p,at,bt,prio),key=lambda x:(x[1],x[3]))
    ctime=0
    for i in range(n):
        p,a,b,prio=sorted_p[i]
        ctime=max(ctime,a)
        CT[i]=ctime+b
        ctime+=b
        TT[i]=CT[i]-a
        WT[i]=TT[i]-b
    return CT,TT,WT
processes = [1, 2, 3, 4,5,6,7]
arrival_time = [0,2,1,4,6,5,7]
burst_time = [3,5,4,2,9,4,10]
priority = [2,6,3,5,7,4,10]
print(pnp(processes,arrival_time,burst_time,priority))