import random, json, lista_adja, matriz_adja, buscas_l, buscas_m, time, cam_min

def CriarGrafo():#gera arquivos txt no formato json
    grafos12 = [5,6,7,8,9,10,20,50,100,200,500,1000]    #numeros de vertices
    for j in range(12):
        gr = {}
        gr['nome'] = []
        gr['vertices'] = []
        gr['arestas'] = []
        partenome = str(grafos12[j])
        gr['nome'].append('grafo_' + partenome)
        for i in range(grafos12[j]):
            gr['vertices'].append(str(i))
        num = random.randint(0,grafos12[j]*8-1)
        for i in range(num):
            x = str(random.randint(0,grafos12[j]-1))
            y = str(random.randint(0,grafos12[j]-1))
            if x != y:#evitar laco
                arestatem = False
                for k in range(len(gr['arestas'])):#evitar que incida a mesma aresta
                    if ((gr['arestas'][k][0] == x and gr['arestas'][k][1] == y) or (gr['arestas'][k][0] == y and gr['arestas'][k][1] == x)):
                        arestatem = True
                if not arestatem:
                    gr['arestas'].append([x,y])
        s = json.dumps(gr)
        palavra = 'grafo' + str(grafos12[j]) + '.txt'
        with open(palavra, "w") as f:
            f.write(s)

def main():
    #g = lista_adja.LerGrafoMontar("1000")
    #st_m = time.clock()
    #g = lista_adja.RemAresta(g, 333, 70)
    #et_m = time.clock()
    #print('tempo fora: ', et_m-st_m)

    #CriarGrafo()
    grafos12 = [5,6,7,8,9,10,20,50,100,200,500,1000]
    for ww in range(12):
        print('gr = ', grafos12[ww])
        gr = str(grafos12[ww])
        gm = matriz_adja.LerGrafoMontar(gr)
        gl = lista_adja.LerGrafoMontar(gr)

        v, e, d = buscas_m.busca_rot(gm)
        #v, e, d = buscas_l.busca_rot(gl)

        #atribuindo peso as arestas
        ew = cam_min.AddPesos(gl)
        #print(ew)

        st_l = time.clock()
        for i in range(1):
            ###d, p = cam_min.Dijkstra_m(gm, ew, 0)
            #d, p = cam_min.Dijkstra_l(gl, ew, 0)
            #buscas_l.DeterminarDistancias(0, v, e, d)
            #buscas_l.BuscaLargura(0, v, e, d)
            #buscas_l.BuscaProfundidade_r(0, v, e, d)
            #buscas_m.BuscaProfundidade(gm, 0, v, e, d)
            #buscas_l.BuscaProfundidade(gl, 0, v, e, d)
            #t = buscas_m.ObterFlorestaGeradora(v, e, d)
            #t = buscas_l.ObterFlorestaGeradora(v, e, d)
            #result = buscas_l.EhArvore_2(v, e, d)
            #result = buscas_l.EhArvore_1(v, e, d)
            #result = buscas_l.EhFloresta(v, e, d)
            #result = buscas_l.TemCiclo(v, e, d)
            #result = buscas_l.EhConexo(v, e, d)
            #v, d = buscas_l. busca_completa(v, e, d)
            #v, e, d = buscas_l.busca(v, e, d, 0)
            #v, e, d = buscas_m.busca_rot(gm)
            #v, e, d = buscas_l.busca_rot(gl)
            #g = matriz_adja.VerticesVizinhos(gm, 2)
            #g = lista_adja.VerticesVizinhos(gl, 2)
            #g = matriz_adja.RemAresta(gm, 3, 2)
            #g = lista_adja.RemAresta(gl, 3, 2)
            #g = matriz_adja.AddAresta(gm, 1, 2)
            #g = lista_adja.AddAresta(gl, 1, 2)
            #g = matriz_adja.RemVertice(gm, 3)
            #g = lista_adja.RemVertice(gl, 3)
            #g = matriz_adja.AddVertice(gm)
            #g = lista_adja.AddVertice(gl)
            #g = matriz_adja.LerGrafoMontar(gr)
            #g = lista_adja.LerGrafoMontar(gr)
        et_l = time.clock()
        #print(g)
        #print('v: ', v)
        #print('e: ', e)
        #print('d: ', d)
        #print('Eh Conexo? ', result)
        #print('Tem ciclo? ', result)
        #print('Eh Floresta? ', result)
        #print('Eh Arvore? ', result)
        #print('Floresta Geradora: ', t)
        #print('d: ', d)
        #print('p: ', p)
        print('Tempo: ', '%.5f'%((et_l-st_l)*1000))
        #st_m = time.clock()
        #for i in range(1):
        #    d, p = cam_min.Dijkstra_m(gm, ew, 0)
        #et_m = time.clock()
        #print('Tempo_m: ', (et_m-st_m))

    
    #print(gr)
    #print('Busca Rot Matriz')
    #v, e, d = buscas_m.busca_rot(gm)
    #print('v')
    #print(v)
    #print('e')
    #print(e)
    #print('d')
    #print(d)
    #print('Eh conexo?')
    #print(buscas_l.EhConexo(gm, v, e, d))
    #print(buscas_l.EhConexo(g))
    
    #print('Tem Ciclo?')
    #print(buscas_l.TemCiclo(g))
    
    #print('Tem Floresta?')
    #print(buscas_l.EhFloresta(g))
    
    #print('Eh Arvore_1?')
    #print(buscas_l.EhArvore_1(g))
    
    #print('Eh Arvore_2?')
    #print(buscas_l.EhArvore_2(g))
    #print('Grafo normal:')
    #print(g)
    
    #print('Floresta Geradora:')
    #t = buscas_l.ObterFlorestaGeradora(g)
    #print(t)
    #buscas_l.BuscaProfundidade(g, 0)
    #print('BuscaProfundidade com Recursividade')
    #vis, e, d = buscas_l.busca_rot(g)
    #buscas_l.BuscaProfundidade_r(g, 0, vis, e, d)

main()