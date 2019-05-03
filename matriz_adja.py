#from typing import namedtuple
import numpy, json

#GrafoMatriz
class MatrizAdjacencia():
    n: int
    m: int
    M: []           #char, Binario, matriz
    d: []           #int
    Explorado: []   #bool, matriz

#    def _init_(n, m, M, d, Explorado):
#        self.n = n
#        self.m = m
#        self.M = M
#        self.d = d
#        self.Explorado = Explorado


#Matriz Adjacencia
def ResolverProblema(g):
    g.Explorado = numpy.zeros((g.n, g.n))
    g.d = numpy.zeros(g.n)
    for u in range(g.n):
        for v in range(g.n):
            if g.M[u][v] == 1:
                g.d[u] = g.d[u] + 1
                if not g.Explorado[u][v]:
                    g.Explorado[u][v] = True
                    g.Explorado[v][u] = True
    for v in range(g.n):
        print(g.d[v])

def LerGrafoMontar():
    file = open("grafos.txt", "r")
    s = file.read()
    grafo = json.loads(s)
    M = grafo['arestas']
    V = grafo['vertices']
    #print(M)
    m_adj = numpy.zeros((len(V), len(V)))
    for l in range(len(M)):
        v1 = 0
        v2 = 0
        for c in range(len(M[0])):
            if c == 0:
                v1 = int(M[l][c])
            if c == 1:
                v2 = int(M[l][c])
                m_adj[v1 - 1][v2 - 1] = 1
                m_adj[v2 - 1][v1 - 1] = 1
    #return m_adj
    m_adj = AddVertice(m_adj)
    print(m_adj)

def QtdArestas(m_adj):
    qtd = 0
    for l in range(len(m_adj)):
        for c in range(len(m_adj[0])):
            if m_adj[l][c] == 1:
                qtd = qtd + 1
    return qtd/2
# QtdVertices = len(m_adj)

def AddVertice(g):
    #g.resize((len(g) + 1, 1), refcheck=False)
    z = numpy.zeros((len(g)+1,len(g)+1))
    z[:-1,:-1] = g
    #zl = numpy.zeros((len(g), len(g)))
        #g[0][i] = 0
        #g[len(g)-1][i] = 0
    return z

def RemVertice(g, numV):
    g = numpy.delete(g, (numV - 1), axis = 0)
    g = numpy.delete(g, (numV - 1), axis = 1)
    return g

def AddAresta(g, v1, v2):
    g[v1 - 1][v2 - 1] = 1
    g[v2 - 1][v1 - 1] = 1
    return g

def RemAresta(g, v1, v2):
    g[v1 - 1][v2 - 1] = 0
    g[v2 - 1][v1 - 1] = 0
    return g

def VerticesVizinhos(g, v):
    y = 0
    for x in range(len(g)):
        if g[v][x] == 1:
            vertices[y] = x + 1
            y = y + 1
    return vertices

def main():
    m = numpy.array([[1,0], [1,0]])
    d = []
    e = []

    g = MatrizAdjacencia()
    g.n = 2
    g.m = 1
    g.M = m
    g.d = d
    g.Explorado = e

    ResolverProblema(g)
    LerGrafoMontar()

main()