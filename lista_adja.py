import numpy, json, random

def CriarGrafo():#gera arquivos txt no formato json
    grafos12 = [5,6,7,8,9,10,20,50,100,200,500,1000]    #numeros de vertices
    for j in range(12):
        gr = {}
        gr['nome'] = []
        gr['vertices'] = []
        gr['arestas'] = []
        gr['nome'].append('grafo1')
        for i in range(grafos12[j]):
            gr['vertices'].append(str(i))
        num = random.randint(1,grafos12[j]*5)
        for i in range(num):
            x = random.randint(1,grafos12[j])
            y = random.randint(1,grafos12[j])
            if x != y:
                gr['arestas'].append([x,y])
        s = json.dumps(gr)
        palavra = 'grafo' + str(grafos12[j]) + '.txt'
        with open(palavra, "w") as f:
            f.write(s)
    
def LerGrafoMontar():
    file = open("grafo10.txt", "r")
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
                l_adj[v1-1].append(v2-1)
                l_adj[v2-1].append(v1-1)
    return l_adj

def AddVertice(g):
    g.append([]);
    return g

def RemVertice(g, numV):
    del g[numV-1]
    return g

def AddAresta(g, v1, v2):
    g[v1-1].append(v2-1)
    g[v2-1].append(v1-1)
    return g

def RemAresta(g, v1, v2):
    g[v1-1].remove(v2-1)
    g[v2-1].remove(v1-1)
    return g

def VerticesVizinhos(g, v):
    return g[v-1]

def main():
    l = LerGrafoMontar()
    print('Grafo Montado lista:')
    print(l)
    l = AddVertice(l)
    print(l)
    l = AddAresta(l,1,3)
    print(l)
    l = RemVertice(l, 3)
    print(l)
    l = AddVertice(l)
    print(l)
    l = AddAresta(l,2,4)
    print(l)
    l = RemAresta(l,2,4)
    print(l)
    vertice = VerticesVizinhos(l, 2)
    print(vertice)
    CriarGrafo()

main()