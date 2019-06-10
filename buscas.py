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
                            g, v, e, d = busca_slide5_l(g, v, e, d, v[k][0])
                            d[i][2] = True
                if (j == 1):
                    for k in range(len(v)):
                        if (e[i][0] == v[k][0] and v[k][1] == False):
                    #if ((v[k][1] == True and e[i][0]  != r) or (v[k][1] == True and e[i][1]  != r)):#v[k][0] == e[i][1] and ##v[k][0] == e[i][j] and 
                        #print('v')
                        #print(v)
                            g, v, e, d = busca_slide5_l(g, v, e, d, v[k][0])
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
    return g, v, e, d

def busca_completa_slide6_l(g):
    v, e, d = busca_rot(g)

    for r in range(len(v)):
        if (v[r][1] == False):
            g, v, e, d = busca_slide5_l(g, v, e, d, r)
    #print(v)
    #print()
    #print(e)
    #print()
    #print(d)
    return g, d

def EhConexo_l(g):#slide 9
    v, e, d = busca_rot(g)
    r = g[0][0]
    g, v, e, d = busca_slide5_l(g, v, e, d, r)
    for i in range(len(v)):
        if (v[i][1] == False):
            return False
    return True

def TemCiclo_l(g):#slide 10
    g, d = busca_completa_slide6_l(g)
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
    g, v, e, d = busca_slide5_l(g, v, e, d, r)
    for i in range(len(v)):
        if (not v[i][1]):
            return False
    for i in range(len(e)):
        if (not d[i][2]):
            return False
    return True

def EhArvore_l_2(g):#slide 13
    return EhConexo_l(g) and not TemCiclo_l(g)