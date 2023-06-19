graph = {
 'A' : ['D','B'],
 'B' : ['C', 'E', 'G'],
 'C' : ['A'],
 'D' : ['C'],
 'E' : ['H'],
 'F' : [],
 'G' : ['F'],
 'H' : ['G','F']
}

def bfs(g,sn):
    v=[]
    q=[sn]
    while q:
        n=q.pop()
        if n not in v:
            print(n,end = ' ')
            v.append(n)
            q.extend(g[n])
bfs(graph,'A')

#out put:
#A B G F E H C D 