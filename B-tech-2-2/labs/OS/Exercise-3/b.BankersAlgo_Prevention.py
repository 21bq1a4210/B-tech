def banker_algo(processes, resources, max_resources, allocated):
    # Calculate the need matrix
    need = [[max_resources[i][j] - allocated[i][j] for j in range(len(resources))] for i in range(len(processes))]
    
    # Initialize the safe sequence and the work and finish arrays
    safe_seq = []
    work = resources[:]
    finish = [False] * len(processes)
    
    # Loop through the processes until all are finished or there is a deadlock
    while False in finish:
        # Assume there is a deadlock
        deadlock = True
        
        # Loop through the processes to check if any can be allocated
        for i in range(len(processes)):
            if not finish[i] and all([need[i][j] <= work[j] for j in range(len(resources))]):
                # This process can be allocated, so add it to the safe sequence and update the work and finish arrays
                safe_seq.append(processes[i])
                finish[i] = True
                work = [work[j] + allocated[i][j] for j in range(len(resources))]
                deadlock = False
        
        # If there is a deadlock, break out of the loop and return None
        if deadlock:
            return None
    
    # If all processes are finished without a deadlock, return the safe sequence
    return safe_seq
if __name__=="__main__":
    processes = ["P0", "P1", "P2", "P3", "P4"]
    resources = [10, 5, 7]
    max_resources = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

    safe_seq = banker_algo(processes, resources, max_resources, allocated)

    if safe_seq is None:
        print("Deadlock detected!")
    else:
        print("Safe sequence: " + " -> ".join(safe_seq))

