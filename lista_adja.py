import numpy, json, random
  
def LerGrafoMontar(numV):
    grafo_nome = 'grafo' + numV +'.txt'
    file = open(grafo_nome, 'r')
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
                l_adj[v1].append(v2)
                l_adj[v2].append(v1)

    return l_adj

def QtdArestas(g):
    soma = 0
    for l in range(len(g)):
        for c in range(len(g[l])):
            soma = soma + 1
    return int(soma/2)

def AddVertice(g):
    tam = len(g)
    g.append([]);
    g[tam].append(tam)
    return g

def RemVertice(g, numV):
    ####MUDANCA##### com a mudanca de real p/ isomorfo
    #for i in range(len(g)):#exclui as dependencias de arestas em outros vertices
        #if g[i][0] == numV:
            #v = i
    for j in range(len(g[numV])):
        g = RemAresta(g,g[numV][0],numV)#tem q comecar do 1. sempre estarei excluindo o primeiro conforme for excluindo...
    for i in range (len(g)):#AGORA ele sera isomorfo, o que mantem suas propriedades, mas nao eh o real...
        for j in range (len(g[i])):
            if (g[i][j] > numV):
                g[i][j] = g[i][j] - 1
    del g[numV]
    #considerei que nessa representacao seria melhor usar a primeira casa do vetor como o numero do vertice ao inves do indice##DESFEITO##
    #fiquei nessa duvida, pois teria que varrer a matriz para subtrair os vertices acima do vertice removido para manter a integridade do grafo##DESFEITO##
    return g

def AddAresta(g, v1, v2):
    g[v1].append(v2)
    g[v2].append(v1)
    return g

def RemAresta(g, v1, v2):
    g[v1].remove(v2)
    g[v2].remove(v1)
    return g

def VerticesVizinhos(g, v):
    return g[v]