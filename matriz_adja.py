import numpy, json
#from lista_adja import CriarGrafo

#GrafoMatriz
class Grafo():
    n: int
    m: int
    M: []

def LerGrafoMontar():
    file = open("grafo20.txt", "r")
    s = file.read()
    grafo = json.loads(s)
    M = grafo['arestas']
    V = grafo['vertices']
    m_adj = numpy.zeros((len(V), len(V)))
    for l in range(len(M)):
        v1 = 0
        v2 = 0
        for c in range(2):#tamanho = sao pares (aresta)
            if c == 0:
                v1 = int(M[l][c])
            if c == 1:
                v2 = int(M[l][c])
                m_adj[v1 - 1][v2 - 1] = 1
                m_adj[v2 - 1][v1 - 1] = 1
    return m_adj

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
    vertices = []
    #y = 0
    for x in range(len(g)):
        if g[v-1][x] == 1:
            vertices.append(x + 1)
            #y = y + 1
    return vertices

def main():
    k = LerGrafoMontar()
    print('Grafo Montado')
    print(k)
    print('')
    k = AddVertice(k)
    print(k)
    k = RemVertice(k, 4)
    print(k)
    v = VerticesVizinhos(k, 5)
    print('Vertices:')
    print(v)
    AddAresta(k, 2, 3)
    print(k)
    RemAresta(k, 2, 3)
    print(k)
    #CriarGrafo()

#main()