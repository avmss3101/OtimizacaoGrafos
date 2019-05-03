import numpy, json

#class ListaAdjacencia:
#    valor = None
#    proximo = None
#    def getValor(self):
#        return(self.valor)
#    def getProximo(self):
#        return(self.proximo)
#    def setValor(self, valor):
#        self.valor = valor
#    def setProximo(self, proximo):
#        self.proximo = proximo

class NoAresta:
    #Viz: int
    #Proximo = None
    def _init_(self, data):
        self.Viz = data
        self.Proximo = None

class Grafo():
    n: int
    m: int
    L: []

def LerGrafoMontar():
    file = open("grafos.txt", "r")
    s = file.read()
    grafo = json.loads(s)
    MA = grafo['arestas']
    V = grafo['vertices']
    #print(MA)
    #m_adj = numpy.zeros((len(V), len(V)))
    l_adj = [[] for i in range(len(V))]
    
    for l in range(len(MA)):
        v1 = 0
        v2 = 0
        for c in range(len(MA[0])):
            if c == 0:
                v1 = int(MA[l][c])
            if c == 1:
                v2 = int(MA[l][c])
                l_adj[v1-1].append(v2-1)
                l_adj[v2-1].append(v1-1)
    return l_adj
    #print (l_adj)

def AddVertice(g):
    g.append([]);
    return g

def RemVertice(g, numV):
    #tam = len(g)-1
    #x = numV-1
    #while x != tam:
    #    g[x] = g[x+1]
    #    x = x + 1
    del g[numV-1]

    #g = numpy.delete(g, (numV - 1), axis = 0
    #g = numpy.delete(g, (numV - 1), axis = 1)
    return g

def AddAresta(g, v1, v2):
    g[v1-1].append(v2-1)
    g[v2-1].append(v1-1)
    return g

def main():
    l = LerGrafoMontar()
    l = AddVertice(l)
    print(l)
    l = AddAresta(l,1,3)
    print(l)
    l = RemVertice(l, 3)
    print(l)
    l = AddVertice(l)
    print(l)

main()