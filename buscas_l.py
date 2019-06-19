import lista_adja, matriz_adja, numpy

def busca_rot(g):
    tam_e = lista_adja.QtdArestas(g);
    visitado = [[] for i in range(len(g))]

    for i in range(len(g)):
        #visitado[i].append(g[i][0])
        visitado[i] = False
    
    explorada = [[] for i in range(tam_e)]
    descoberta = [[] for i in range(tam_e)]
    cont = 0
    
    #Copiar g
    gc = []
    for elem in g:
        gc.append(list(elem))
   
    for i in range(len(gc)):
        tam = len(gc)
        if (tam != 0):
            #print('grafo')
            #print(gc)
            #print('tam do gc')
            #print(tam)
            for j in range(len(gc[tam -1])):
                explorada[cont].append(tam-1),
                descoberta[cont].append(tam-1)
                explorada[cont].append(gc[tam-1][j])
                descoberta[cont].append(gc[tam-1][j])
                explorada[cont].append(False)
                descoberta[cont].append(False)
                #print('e')
                #print(explorada)
                #print('d')
                #print(descoberta)
        #explorada[cont].append(g[i][0])
        #descoberta[cont].append(g[i][0])
        #tam = len(gc)
        #for j in range(tam):
        #    explorada[cont].append(j)#
        #    descoberta[cont].append(gc[i][j])
        #    explorada[cont].append(i)
        #    descoberta[cont].append(i)
        #    explorada[cont].append(False)
        #    descoberta[cont].append(False)
                cont = cont + 1
        gc = lista_adja.RemVertice(gc, tam-1)##tam-i###sempre deleto o ultimo vertice depois de pegar suas arestas

        #r = 
    #print('grafo fim')
    #print(gc)
    #print('explorada')
    #print(explorada)
    #print('descoberta')
    #print(descoberta)
    return visitado, explorada, descoberta

def busca(g, v, e, d, r):#slide 5
    v, e, d = busca_rot(g)
    #r = v[0][0]
    #for i in range(len(v)):
    #    if (v[i][0] == r):
    #        v[i][1] = True
    v[r] = True

    #for l in range(len(v)):
     #   r = v[l][0]
    i = 0
    while (i < len(e)):
        if (v[e[i][0]] and e[i][2] == False):
            e[i][2] = True
            if (v[e[i][1]] == False):
                v[e[i][1]] = True
                d[i][2] = True
                i = 0
        else:
            if (v[e[i][1]] and e[i][2] == False):
                e[i][2] = True
                if (v[e[i][0]] == False):
                    v[e[i][0]] = True
                    d[i][2] = True
                    i = 0
        i += 1
    return v, e, d#tirei o g

def busca_completa(g):#slide 6
    v, e, d = busca_rot(g)

    for r in range(len(v)):
        if (v[r] == False):
            v, e, d = busca(g, v, e, d, r)
    #print(v)
    #print()
    #print(e)
    #print()
    #print(d)
    return v, d

def EhConexo(g):#slide 9
    v, e, d = busca_rot(g)
    print('v')
    print(v)
    print('e')
    print(e)
    print('d')
    print(d)
    r = 0#g[0][0]
    v, e, d = busca(g, v, e, d, r)
    print('v_d')
    print(v)
    print('e_d')
    print(e)
    print('d_d')
    print(d)
    for i in range(len(v)):
        if (v[i] == False):
            return False
    return True

def TemCiclo(g):#slide 10
    v, d = busca_completa(g)
    #print('d')
    #print(d)
    for i in range(len(d)):
        if (d[i][2] == False):
            return True
    return False

def EhFloresta(g):#slide 11
    return not TemCiclo(g)

def EhArvore_1(g):#slide 12
    v, e, d = busca_rot(g)
    r = 0#g[0][0]
    v, e, d = busca(g, v, e, d, r)
    for i in range(len(v)):
        if (not v[i]):
            return False
    for i in range(len(e)):
        if (not d[i][2]):
            return False
    return True

def EhArvore_2(g):#slide 13
    return EhConexo(g) and not TemCiclo(g)

def ObterFlorestaGeradora(g):#slide 17
    v, d = busca_completa(g)
    r = 0#g[0][0]
    t = [[] for i in range(len(g))]

    #add_vertice ou isso:
    #for i in range(len(g)):
    #    t[i].append(g[i][0])

    for i in range(len(d)):
        if (d[i][2]):
            t = lista_adja.AddAresta(t, d[i][0], d[i][1])
            #t[d[i][0]].append(d[i][1])
            #t[d[i][1]].append(d[i][0])
    return t

def PrimeiroViz(g, v):#funcao auxiliar para slide 26
    priv = -1
    #for i in range(len(g)):
    if (len(g[v]) > 0):##()and (g[i][0] == v
        priv = g[v][0]
    return priv


def ProximoViz(g, v, w):#funcao auxiliar para slide 26
    prov = -1
    #for i in range(len(g)):
        #if (g[i][0] == v):
    for j in range(len(g[v])):
               #if (j < len(g[i]) -2):#-1?
        if ((g[v][j] == w) and (len(g[v]) -1 > j)):#DUVIDA
            prov = g[v][j+1]
    return prov

def BuscaProfundidade(g, v):#slide 26
    p = []
    priv = -1#inicia como -1, pois se nao tiver primeiroviz ficara com tal valor ja que na minha implementacao 0 pode ser vertice
    vis, e, d = busca_rot(g)
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

##SERA PRECISO USAR O BUSCA_ROT ANTES##
def BuscaProfundidade_r(g, v, vis, e, d):#slide 27
    vis[v] = True
    for i in range(v, len(vis)):#i, eh o w
        if (vis[i]):
            for j in range(len(e)):
                if ((e[j][0] == i and e[j][2] == False) or (e[j][1] == i and e[j][2] == False)):#if ((e[j][0] == i and e[j][1] == v and e[j][2] == False) or (e[j][1] == i and e[j][0] == v and e[j][2] == False)):
                    e[j][2] = True  
        else:
            for j in range(len(e)):
                if ((e[j][0] == i) or (e[j][1] == i)):
                    e[j][2] = True
                    d[j][2] = True
                    BuscaProfundidade_r(g, i, vis, e, d)
    #print('BuscaProfundidade')
    print('Grafo')
    print(g)
    print(vis)
    print()
    print(e)
    print()
    print(d)

def BuscaLargura(g, v):
