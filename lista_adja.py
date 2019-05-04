import numpy, json, random
  
def LerGrafoMontar():
    file = open("grafo1000.txt", "r")
    s = file.read()
    grafo = json.loads(s)
    MA = grafo['arestas']
    V = grafo['vertices']

    l_adj = [[] for i in range(len(V))]
    
    for l in range(len(MA)):
        v1 = 0
        v2 = 0
        for c in range(len(MA[0])):
            if c == 0:
                v1 = int(MA[l][c])
            if c == 1:
                v2 = int(MA[l][c])
                l_adj[v1-1].append(v2)
                l_adj[v2-1].append(v1)
    return l_adj

def AddVertice(g):
    g.append([]);
    return g

def RemVertice(g, numV):
    for i in range(len(g[numV-1])):#exclui as dependencias de arestas em outros vertices
        g = RemAresta(g,g[numV-1][0],numV)#sempre estarei excluindo o primeiro conforme for excluindo...
    del g[numV-1]
    return g

def AddAresta(g, v1, v2):
    tamV = len(g[v1])
    verifica = False
    for i in range(tamV):
        if g[v1-1][i] == v2:
           verifica = True
    if not verifica:
        g[v1-1].append(v2)
        g[v2-1].append(v1)
    return g

def RemAresta(g, v1, v2):
    g[v1-1].remove(v2)
    g[v2-1].remove(v1)
    return g

def VerticesVizinhos(g, v):
    return g[v-1]