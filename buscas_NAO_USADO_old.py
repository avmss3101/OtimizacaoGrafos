import lista_adja, matriz_adja, numpy

def busca_rot(g):
    tam_e = lista_adja.QtdArestas(g);
    visitado = [[] for i in range(len(g))]

    for i in range(len(g)):
        visitado[i].append(g[i][0])
        visitado[i].append(False)
    
    explorada = [[] for i in range(tam_e)]
    descoberta = [[] for i in range(tam_e)]
    cont = 0
    
    #Copiar g
    gc = []
    for elem in g:
        gc.append(list(elem))
   
    for i in range(len(gc)):
        #explorada[cont].append(g[i][0])
        #descoberta[cont].append(g[i][0])
        tam = len(gc[0])-1
        for j in range(tam):
            explorada[cont].append(gc[0][0])#sempre 0 pois irei deletando o vertice
            descoberta[cont].append(gc[0][0])
            explorada[cont].append(gc[0][j+1])
            descoberta[cont].append(gc[0][j+1])
            explorada[cont].append(False)
            descoberta[cont].append(False)
            cont = cont + 1
        gc = lista_adja.RemVertice(gc, gc[0][0])

        #r = 
    return visitado, explorada, descoberta

def busca_slide5_l(g, v, e, d, r):
    #v, e, d = busca_rot(g)
    #r = v[0][0]
    for i in range(len(v)):
        if (v[i][0] == r):
            v[i][1] = True

    #for l in range(len(v)):
     #   r = v[l][0]
    for i in range(len(e)):
        for j in range(2):
            if (r == e[i][j] and e[i][2] == False ):#and v[l][1]    
                e[i][2] = True
                if (j == 0):
                    for k in range(len(v)):
                        if (e[i][1] == v[k][0] and v[k][1] == False):
                    #if ((v[k][1] == True and e[i][0]  != r) or (v[k][1] == True and e[i][1]  != r)):#v[k][0] == e[i][1] and ##v[k][0] == e[i][j] and 
                        #print('v')
                        #print(v)
                        
                            #v[k][1] = True
                            v, e, d = busca_slide5_l(g, v, e, d, v[k][0])
                            d[i][2] = True
                if (j == 1):
                    for k in range(len(v)):
                        if (e[i][0] == v[k][0] and v[k][1] == False):
                    #if ((v[k][1] == True and e[i][0]  != r) or (v[k][1] == True and e[i][1]  != r)):#v[k][0] == e[i][1] and ##v[k][0] == e[i][j] and 
                        #print('v')
                        #print(v)
                            v, e, d = busca_slide5_l(g, v, e, d, v[k][0])
                            #v[k][1] = True
                            d[i][2] = True
                        
                        #print('d')
                        #print(d)
                    #if (v[k][1] == False and e[i][1]  == v[k][0] and j == 1):#v[k][0] == e[i][1] and ##v[k][0] == e[i][j] and 
                    #    print('v')
                    #    print(v)
                    #    v[k][1] = True
                    #    d[i][2] = True
                    #    print('d')
                    #    print(d)
                    #if (j == 1):
                    #    for k in range(len(v)):
                    #        if (v[k][0] == e[i][j] and v[k][1] == False):#v[k][0] == e[i][0] and 
                    #            v[k][1] = True
                    #            d[i][2] = True
                    #if (v[])
    #print(v)
    #print(e)
    #print(d)
    return v, e, d#tirei o g

def busca_completa_slide6_l(g):
    v, e, d = busca_rot(g)

    for r in range(len(v)):
        if (v[r][1] == False):
            v, e, d = busca_slide5_l(g, v, e, d, r)
    #print(v)
    #print()
    #print(e)
    #print()
    #print(d)
    return v, d

def EhConexo_l(g):#slide 9
    v, e, d = busca_rot(g)
    r = g[0][0]
    v, e, d = busca_slide5_l(g, v, e, d, r)
    for i in range(len(v)):
        if (v[i][1] == False):
            return False
    return True

def TemCiclo_l(g):#slide 10
    v, d = busca_completa_slide6_l(g)
    print('d')
    #print(d)
    for i in range(len(d)):
        if (d[i][2] == False):
            return True
    return False

def EhFloresta_l(g):#slide 11
    return not TemCiclo_l(g)

def EhArvore_l_1(g):#slide 12
    v, e, d = busca_rot(g)
    r = g[0][0]
    v, e, d = busca_slide5_l(g, v, e, d, r)
    for i in range(len(v)):
        if (not v[i][1]):
            return False
    for i in range(len(e)):
        if (not d[i][2]):
            return False
    return True

def EhArvore_l_2(g):#slide 13
    return EhConexo_l(g) and not TemCiclo_l(g)

def ObterFlorestaGeradora_l(g):#slide 17
    v, d = busca_completa_slide6_l(g)
    r = g[0][0]
    t = [[] for i in range(len(g))]

    #add_vertice ou isso:
    for i in range(len(g)):
        t[i].append(g[i][0])

    for i in range(len(d)):
        if (d[i][2]):
            t = lista_adja.AddAresta(t, d[i][0], d[i][1])
            #t[d[i][0]].append(d[i][1])
            #t[d[i][1]].append(d[i][0])
    return t

def PrimeiroViz(g, v):#funcao auxiliar para slide 26
    priv = -1
    for i in range(len(g)):
        if ((len(g[i]) > 1) and (g[i][0] == v)):
            priv = g[i][1]
    return priv


def ProximoViz(g, v, w):#funcao auxiliar para slide 26
    prov = -1
    for i in range(len(g)):
        if (g[i][0] == v):
            for j in range(1, len(g[i])):
                if (j < len(g[i]) -2):#-1?
                    if (g[i][j] == w):
                        prov = g[i][j+1]
    return prov

def BuscaProfundidade_l(g, v):#slide 26
    p = []
    priv = -1#inicia como zero, pois se nao tiver primeiroviz ficara com tal valor ja que na minha implementacao 0 pode ser vertice
    vis, e, d = busca_rot(g)
    for i in range(len(g)):
        if (g[i][0] == v):
            vis[i][1] = True
            #aproveitar esse for para achar PrimeiroViz
            if (len(g[i]) > 1):
                priv = g[i][1]
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
            for i in range(len(vis)):
                if (vis[i][0] == w and vis[i][1]):#errado, eh o w
                    for j in range(len(e)):
                        for k in range(2):
                            if (((e[j][0] == v and e[j][1] == w) or (e[j][1] == v and e[j][0] == w)) and not e[j][2]):
                                 e[j][2] = True
                if (vis[i][0] == w and vis[i][1] == False):
                    for j in range(len(e)):
                        for k in range(2):
                            if (((e[j][0] == v and e[j][1] == w) or (e[j][1] == v and e[j][0] == w)) and not e[j][2]):
                                 e[j][2] = True
                                 d[j][2] = True
                                 for l in range(len(vis)):
                                    if (vis[l][0] == w):
                                        vis[l][1] = True
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

def BuscaProfundidade_l_r(g, v):#slide 27
    for i in range(len(g)):
        if (g[i][0] == v):
            vis[i][1] = True

    