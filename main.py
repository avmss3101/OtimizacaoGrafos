import random, json, lista_adja, matriz_adja, buscas_l

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
    #CriarGrafo()
    gr = "5"
    g = lista_adja.LerGrafoMontar(gr)
    
    print(gr)
    print('Eh conexo?')
    print(buscas_l.EhConexo(g))
    print('Tem Ciclo?')
    print(buscas_l.TemCiclo(g))
    print('Tem Floresta?')
    print(buscas_l.EhFloresta(g))
    print('Eh Arvore_1?')
    print(buscas_l.EhArvore_1(g))
    print('Eh Arvore_2?')
    print(buscas_l.EhArvore_2(g))
    #print('Grafo normal:')
    #print(g)
    #print('Floresta Geradora:')
    #t = buscas_l.ObterFlorestaGeradora(g)
    #print(t)
    #buscas_l.BuscaProfundidade(g, 0)
    #print('BuscaProfundidade com Recursividade')
    #buscas_l.BuscaProfundidade_r(g, v)

main()