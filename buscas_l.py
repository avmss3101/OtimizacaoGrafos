import lista_adja, matriz_adja, numpy

def busca_rot(g):
    tam_e = lista_adja.QtdArestas(g);
    visitado = [[] for i in range(len(g))]

    for i in range(len(g)):
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
            for j in range(len(gc[tam -1])):
                explorada[cont].append(tam-1),
                descoberta[cont].append(tam-1)
                explorada[cont].append(gc[tam-1][j])
                descoberta[cont].append(gc[tam-1][j])
                explorada[cont].append(False)
                descoberta[cont].append(False)
                cont = cont + 1
        gc = lista_adja.RemVertice(gc, tam-1)##tam-i###sempre deleto o ultimo vertice depois de pegar suas arestas

    return visitado, explorada, descoberta

def busca(v, e, d, r):#slide 5
    v[r] = True

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

def busca_completa(v, e, d):#slide 6

    for r in range(len(v)):
        if (v[r] == False):
            v, e, d = busca(v, e, d, r)
    return v, d

def EhConexo(v, e, d):#slide 9
    r = 0#g[0][0]
    v, e, d = busca(v, e, d, r)
    for i in range(len(v)):
        if (v[i] == False):
            return False
    return True

def TemCiclo(v, e, d):#slide 10
    v, d = busca_completa(v, e, d)
    for i in range(len(d)):
        if (d[i][2] == False):
            return True
    return False

def EhFloresta(v, e, d):#slide 11
    return not TemCiclo(v, e, d)

def EhArvore_1(v, e, d):#slide 12
    r = 0#g[0][0]
    v, e, d = busca(v, e, d, r)
    for i in range(len(v)):
        if (not v[i]):
            return False
    for i in range(len(e)):
        if (not d[i][2]):
            return False
    return True

def EhArvore_2(v, e, d):#slide 13
    return EhConexo(v, e, d) and not TemCiclo(v, e, d)

def ObterFlorestaGeradora(v, e, d):#slide 17
    v, d = busca_completa(v, e, d)
    r = 0#g[0][0]
    t = [[] for i in range(len(v))]

    for i in range(len(d)):
        if (d[i][2]):
            t = lista_adja.AddAresta(t, d[i][0], d[i][1])
    return t

def PrimeiroViz(g, v):#funcao auxiliar para slide 26
    priv = -1
    if (len(g[v]) > 0):##()and (g[i][0] == v
        priv = g[v][0]
    return priv


def ProximoViz(g, v, w):#funcao auxiliar para slide 26
    prov = -1
    for j in range(len(g[v])):
               #if (j < len(g[i]) -2):#-1?
        if ((g[v][j] == w) and (len(g[v]) -1 > j)):#DUVIDA
            prov = g[v][j+1]
    return prov

def BuscaProfundidade(g, v, vis, e, d):#slide 26
    p = []#pilha
    priv = -1#inicia como -1, pois se nao tiver primeiroviz ficara com tal valor ja que na minha implementacao 0 pode ser vertice
    
    vis[v] = True
    priv = PrimeiroViz(g, v)
    
    #empilha
    p.append(v)
    p.append(priv)

    tam_p = len(p)
    while(tam_p > 0):
        w = p.pop()
        v = p.pop()
        if (w > -1):
            p.append(v)
            p.append(ProximoViz(g, v, w))
            if (vis[w]):#errado, eh o w
                    for j in range(len(e)):
                        if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                            e[j][2] = True
            else:
                    for j in range(len(e)):
                        if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                            e[j][2] = True
                            d[j][2] = True
                            vis[w] = True
                            p.append(w)
                            p.append(PrimeiroViz(g, w))
        tam_p = len(p)

##SERA PRECISO USAR O BUSCA_ROT ANTES##
def BuscaProfundidade_r(v, vis, e, d):#slide 27
    vis[v] = True
    for i in range(v, len(vis)):#i, eh o w
        if (vis[i]):
            for j in range(len(e)):
                if ((e[j][0] == i and e[j][1] == v and e[j][2] == False) or (e[j][1] == i and e[j][0] == v  and e[j][2] == False)):
                    e[j][2] = True  
        else:
            for j in range(len(e)):
                if ((e[j][0] == i and e[j][1] == v) or (e[j][1] == i and e[j][0] == v)):
                    e[j][2] = True
                    d[j][2] = True
                    BuscaProfundidade_r(i, vis, e, d)

def BuscaLargura(v, vis, e, d):#slide 57
    f = []#fila

    vis[v] = True
    f.append(v)

    tam_f = len(f)

    while(tam_f > 0):
        v = f.pop(0)
        for w in range(len(vis)):
            if vis[w]:
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                        e[j][2] = True
            else:
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                        e[j][2] = True
                        d[j][2] = True
                        vis[w] = True
                        f.append(w)
        tam_f = len(f)

def DeterminarDistancias(v, vis, e, d):#slide 62
    f = []#fila

    dist = [[] for i in range(len(vis))]
    vis[v] = True
    f.append((v, 1))

    tam_f = len(f)

    while(tam_f > 0):
        v, niv = f.pop(0)
        for w in range(len(vis)):
            if vis[w]:
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                        e[j][2] = True
            else:
                for j in range(len(e)):
                    if ((e[j][0] == v and e[j][1] == w and not e[j][2]) or (e[j][1] == v and e[j][0] == w and not e[j][2])):
                        e[j][2] = True
                        d[j][2] = True
                        vis[w] = True
                        dist[w] = niv
                        f.append((w, niv + 1))
        tam_f = len(f)