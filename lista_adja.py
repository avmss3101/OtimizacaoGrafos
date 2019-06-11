import numpy, json, random
  
def LerGrafoMontar(numV):
    grafo_nome = 'grafo' + numV +'.txt'
    file = open(grafo_nome, 'r')
    s = file.read()
    grafo = json.loads(s)
    MA = grafo['arestas']
    V = grafo['vertices']

    l_adj = [[] for i in range(len(V))]
    for i in range(len(l_adj)):
        l_adj[i].append(i)#o seu primeiro elemento sera o indicador do vertice, nao o seu indice
    for l in range(len(MA)):
        v1 = 0
        v2 = 0
        for c in range(len(MA[0])):
            if c == 0:
                v1 = int(MA[l][c])
            if c == 1:
                v2 = int(MA[l][c])
                l_adj[v1].append(v2)
                l_adj[v2].append(v1)
    #for i in range(len(l_adj)):
    #    l_adj[i] = i + 1
    return l_adj

def QtdArestas(g):
    soma = 0
    for l in range(len(g)):
        for c in range(len(g[l]) -1):
            soma = soma + 1
    return int(soma/2)

def AddVertice(g):
    tam = len(g)
    g.append([]);#p q nao direto? erro...
    g[tam].append(tam)
    return g

def RemVertice(g, numV):
    v = 0#???
    for i in range(len(g)):#exclui as dependencias de arestas em outros vertices
        if g[i][0] == numV:
            v = i
            for j in range(1,len(g[i])):
                g = RemAresta(g,g[i][1],numV)#tem q comecar do 1. sempre estarei excluindo o primeiro conforme for excluindo...
    del g[v]
    #considerei que nessa representacao seria melhor usar a primeira casa do vetor como o numero do vertice ao inves do indice
    #fiquei nessa duvida, pois teria que varrer a matriz para subtrair os vertices acima do vertice removido para manter a integridade do grafo
    return g

def AddAresta(g, v1, v2):
    for i in range(len(g)):
        if g[i][0] == v1:
            g[i].append(v2)
        if g[i][0] == v2:
            g[i].append(v1)
    return g

def RemAresta(g, v1, v2):
    for i in range(len(g)):
        if g[i][0] == v1:
            g[i].remove(v2)
        if g[i][0] == v2:
            g[i].remove(v1)
    return g

def VerticesVizinhos(g, v):
    for i in range(len(g)):
        if g[i][0] == v:
            g[i].remove(v)
            return g[i]