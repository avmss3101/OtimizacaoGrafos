import math, lista_adja, matriz_adja, random

#Add Pesos nas arestas, nao importa se usarei grafo representado por lista ou matriz, o q importa eh o retorno com o mesmos pesos nas arestas
def AddPesos(g):
    tam_e = lista_adja.QtdArestas(g);
    e = [[] for i in range(tam_e)]

    cont = 0
    
    #Copiar g
    gc = []
    for elem in g:
        gc.append(list(elem))
   
    for i in range(len(gc)):
        tam = len(gc)
        if (tam != 0):
            for j in range(len(gc[tam -1])):
                e[cont].append(tam-1),
                e[cont].append(gc[tam-1][j])
                e[cont].append(random.randint(0, 50))
                cont = cont + 1
        gc = lista_adja.RemVertice(gc, tam-1)##tam-i###sempre deleto o ultimo vertice depois de pegar suas arestas
    return e

#Caminhos Minimos
def Dijkstra_l(g, e, s):#e: arestas com os pesos
    d = [[] for i in range(len(g))]
    t = [[] for i in range(len(g))]

    for i in range(len(g)):
        t[i] = False
        d[i] = math.inf

    p = [[] for i in range(len(g))]

    d[s] = 0

    for i in range(len(g)):
        if (not t[v]):
            u = values.index(min(d))#argmin(d)
            t[u] = True
            for v in lista_adja.VerticesVizinhos(g, u):
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == u and d[v] > e[j][2] + d[u]) or (e[j][1] == v and e[j][0] == u and  d[v] > e[j][2] + d[u])):
                        d[v] = e[j][2] + d[u]
    return d, p

def Dijkstra_m(g, e, s):#e: arestas com os pesos
    d = [[] for i in range(len(g))]
    t = [[] for i in range(len(g))]

    for i in range(len(g)):
        t[i] = False
        d[i] = math.inf

    p = [[] for i in range(len(g))]

    d[s] = 0

    for i in range(len(g)):
        if (not t[v]):
            u = values.index(min(d))#argmin(d)
            t[u] = True
            for v in matriz_adja.VerticesVizinhos(g, u):
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == u and d[v] > e[j][2] + d[u]) or (e[j][1] == v and e[j][0] == u and  d[v] > e[j][2] + d[u])):
                        d[v] = e[j][2] + d[u]
    return d, p