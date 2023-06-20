from queue import PriorityQueue

def best_first_search(graph, start, goal):
    # Create a priority queue to store the nodes to be explored
    queue = PriorityQueue()
    # Enqueue the start node with priority 0
    queue.put((0, start))
    # Create a set to keep track of visited nodes
    visited = set()
    
    while not queue.empty():
        # Dequeue the node with the highest priority
        current_cost, current_node = queue.get()
        
        # Check if the current node is the goal node
        if current_node == goal:
            print("Goal found!")
            return
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore the neighbors of the current node
        for neighbor, cost in graph[current_node]:
            # Enqueue the unvisited neighbors with their heuristic values as priority
            if neighbor not in visited:
                queue.put((cost, neighbor))
    
    print("Goal not found!")

# Example usage:
graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 4), ('E', 3)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}

best_first_search(graph, 'A', 'F')