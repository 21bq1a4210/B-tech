# def sjf_non_preemptive(processes, arrival_time, burst_time):
#     
#     n = len(processes)
#     completion_time = [0] * n
#     turnaround_time = [0] * n
#     waiting_time = [0] * n
#     
#     sorted_processes = sorted(zip(processes, arrival_time, burst_time), key=lambda x: x[1])
#     current_time = 0
#     print(sorted_processes)
#     
#     for i in range(n):
#         process, arrival, burst = sorted_processes[i]
#         current_time = max(current_time, arrival)
#         completion_time[i] = current_time + burst
#         current_time += burst
#         turnaround_time[i] = completion_time[i] - arrival
#         waiting_time[i] = turnaround_time[i] - burst
# 
#     return completion_time, turnaround_time, waiting_time
# 
# # Example usage
# processes = [1, 2, 3, 4]
# arrival_time = [0, 1, 2, 3]
# burst_time = [5, 3, 8, 6]
# 
# completion_time, turnaround_time, waiting_time = sjf_non_preemptive(processes, arrival_time, burst_time)
# 
# print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
# for i in range(len(processes)):
#     print(f"{processes[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

def priority_non_preemptive(processes, arrival_time, burst_time, priority):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    sorted_processes = sorted(zip(processes, arrival_time, burst_time, priority), key=lambda x: x[1])
    current_time = 0

    for i in range(n):
        process, arrival, burst, prio = sorted_processes[i]
        current_time = max(current_time, arrival)
        completion_time[i] = current_time + burst
        current_time += burst
        turnaround_time[i] = completion_time[i] - arrival
        waiting_time[i] = turnaround_time[i] - burst

    return completion_time, turnaround_time, waiting_time

# Example usage
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [5, 3, 8, 6]
priority = [2, 1, 3, 2]

completion_time, turnaround_time, waiting_time = priority_non_preemptive(processes, arrival_time, burst_time, priority)

print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")