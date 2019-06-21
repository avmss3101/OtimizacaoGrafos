import lista_adja, matriz_adja, numpy, buscas_l

def busca_rot(g):
    tam_e = matriz_adja.QtdArestas(g);
    visitado = [[] for i in range(len(g))]

    for i in range(len(g)):
        visitado[i] = False
    
    explorada = [[] for i in range(tam_e)]
    descoberta = [[] for i in range(tam_e)]

    cont = 0
    t = 1
    for i in range(len(g)):
        for j in range(t, len(g)):
            if g[i][j] == 1:
                explorada[cont].append(i)
                explorada[cont].append(j)
                explorada[cont].append(False)
                descoberta[cont].append(i)
                descoberta[cont].append(j)
                descoberta[cont].append(False)
                cont += 1
        t += 1
    
    return visitado, explorada, descoberta

#slide 5, BUSCA eh igual para ambos
#slide 6, BUSCA_COMPLETA eh igual para ambos
#slide 9, EhCONEXO eh igual para ambos
#slide 10, TEM_CICLO eh igual para ambos
#slide 11, EhFLORESTA eh igual para ambos
#slide 12, EhARVORE_1 eh igual para ambos
#slide 13, EhARVORE_2 eh igual para ambos

def ObterFlorestaGeradora(g, v, e, d):#slide 17
    v, d = buscas_l.busca_completa(g, v, e, d)#pq eh igual
    r = 0#g[0][0]
    t = numpy.zeros((len(v), len(v)))

    for i in range(len(e)):
        if (d[i][2]):
            t = matriz_adja.AddAresta(t, d[i][0], d[i][1])

    return t



def PrimeiroViz(g, v):#funcao auxiliar para slide 26
    
    for i in range(len(g)):
        if g[v][i] == 1:
            return i
    return 0

def ProximoViz(g, v, w):#funcao auxiliar para slide 26

    for i in range(w + 1, len(g)):
        if g[v][i] == 1:
            return i
    return 0

def BuscaProfundidade(g, vis, e, d, v):#slide 26, mesma estrutura do buscas_l porem as funcoes auxiliares sao mudadas
    p = []
    priv = -1#inicia como -1, pois se nao tiver primeiroviz ficara com tal valor ja que na minha implementacao 0 pode ser vertice
    #vis, e, d = busca_rot(g)
    print('vis')
    print(vis)
    vis[v] = True
    print('vis')
    print(vis)
    priv = PrimeiroViz(g, v)
    #empilha
    p.append(v)
    p.append(priv)

    tam_p = len(p)
    while(tam_p > 0):
        w = p.pop()
        v = p.pop()
        if (w > -1):
            print('vis')
            print(vis)
            p.append(v)
            p.append(ProximoViz(g, v, w))
            if (vis[w]):#errado, eh o w
                    for j in range(len(e)):
                        if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                            e[j][2] = True
            else:#if (vis[w] == False):
                    for j in range(len(e)):
                        if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                            e[j][2] = True
                            d[j][2] = True
                            vis[w] = True
                            p.append(w)
                            p.append(PrimeiroViz(g, w))
        tam_p = len(p)
    print('BuscaProfundidade')
    print('Grafo')
    print(g)
    print(vis)
    print()
    print(e)
    print()
    print(d)

#slide 27, BUSCA_PROFUNDIDADE_R eh igual para ambos
#slide 57, BUSCA_LARGURA eh igual para ambos
#slide 62, DETER<INAR_DISTANCIAS eh igual para ambos