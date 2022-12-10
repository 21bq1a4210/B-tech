#@title 17. Implement Graph and its operations
def add_node(g,v):
  if v in g:
    print(f"{v} is in graph")
  else:
    g[v]=[]

def add_edge_to_undirected(g,v1,v2,cost=None):
  if v1 not in g:
    print(f"{v1} is not present in graph")
  elif v2 not in g:
    print(f"{v2} is not present in graph")
  else:
    if cost==None:
      g[v1].append(v2)
      g[v2].append(v1)
    else:
      g[v1].append([v2,cost])
      g[v2].append([v1,cost])
def printGraph():
  for x,y in undirected_graph.items():
    print(f"{x}-{y}")

  
undirected_graph={}

print("after adding nodes:")
add_node(undirected_graph,'A')
add_node(undirected_graph,'B')
add_node(undirected_graph,'C')
printGraph()
print()

print("After adding edge to undirected graph:")
add_edge_to_undirected(undirected_graph,"A","B")
add_edge_to_undirected(undirected_graph,"A","C")
printGraph()
print()