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

def dfs(g,sn,v=set()):
    v.add(sn)
    print(sn,end=' ')
    for neibour in g[sn]:
        if neibour not in v:
            dfs(g,neibour,v)

dfs(graph,'A')

#Out put
#A D C B E H G F 