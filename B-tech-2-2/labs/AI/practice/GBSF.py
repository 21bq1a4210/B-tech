def best_first_search(graph, start):
    visited = set()
    priority_queue = [start]
    
    while priority_queue:
        node = priority_queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            neighbors = graph[node]
            neighbors.sort()  # Sort the neighbors alphabetically
            priority_queue = neighbors + priority_queue
    
# Graph representation
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G', 'F']
}

# Start node
start_node = 'A'

# Perform Best First Search
print("Order of nodes visited using Best First Search:")
best_first_search(graph, start_node)