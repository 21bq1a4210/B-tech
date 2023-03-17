# A Node class for GBFS Pathfinding
class Node:
    def __init__(self, v, weight):
        self.v=v
        self.weight=weight

# pathNode class will help to store the path from src to dest.
class pathNode:
    def __init__(self, node, parent):
        self.node=node
        self.parent=parent

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))

# Declaring the adjacency list
adj = []
# Greedy best first search algorithm function
def GBFS(h, V, src, dest):
    """ 
    This function returns a list of integers that denote the shortest
    path found using the GBFS algorithm.  If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList.
    openList = []
    closeList = []

    # Inserting src in openList.
    openList.append(pathNode(src, None))

    # Iterating while the openList  is not empty.
    while (openList):

        currentNode = openList[0]
        currentIndex = 0
        # Finding the node with the least 'h' value
        for i in range(len(openList)):
            if(h[openList[i].node] < h[currentNode.node]):
                currentNode = openList[i]
                currentIndex = i

        # Removing the currentNode from  the openList and adding it in   the closeList.
        openList.pop(currentIndex)
        closeList.append(currentNode)
        
        # If we have reached the destination node.
        if(currentNode.node == dest):
            # Initializing the 'path' list. 
            path = []
            cur = currentNode

            # Adding all the nodes in the  path list through which we have  reached to dest.
            while(cur != None):
                path.append(cur.node)
                cur = cur.parent
            

            # Reversing the path, because  currently it denotes path  from dest to src.
            path.reverse()
            return path
        
        # Iterating over adjacents of 'currentNode'  and adding them to openList if
        # they are neither in openList or closeList.
        for node in adj[currentNode.node]:
            for x in openList:
                if(x.node == node.v):
                    continue
            
            for x in closeList:
                if(x.node == node.v):
                    continue
            
            openList.append(pathNode(node.v, currentNode))

    return []


# Driver Code
# The total number of vertices.
V = 10
## Initializing the adjacency list
for i in range(V):
    adj.append([])

addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)

# Defining the heuristic values for each node.
h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]
path = GBFS(h, V, 0, 9)
for i in range(len(path) - 1):
    print(path[i], end = " --> ")
print(f'{path[(len(path)-1)]}.')
