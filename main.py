#from lista_adja import *
#from matriz_adja import *
import random, json, lista_adja, matriz_adja

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
        num = random.randint(1,grafos12[j]*8)
        for i in range(num):
            x = str(random.randint(1,grafos12[j]))
            y = str(random.randint(1,grafos12[j]))
            if x != y:#evitar laco
                arestatem = False
                #print('olha eu aqui')
                for k in range(len(gr['arestas'])):#evitar que incida a mesma aresta
                    #print('olha eu aqui 2')
                    if ((gr['arestas'][k][0] == x and gr['arestas'][k][1] == y) or (gr['arestas'][k][0] == y and gr['arestas'][k][1] == x)):
                        #print('olha eu aqui 3: ' + str(k) + '.........')
                        arestatem = True
                if not arestatem:
                    gr['arestas'].append([x,y])

                        #if addagora:
                        #    gr['arestas'].append([x,y])
                        #    addagora = False
        s = json.dumps(gr)
        palavra = 'grafo' + str(grafos12[j]) + '.txt'
        with open(palavra, "w") as f:
            f.write(s)

def main():
    #CriarGrafo()
    print('TESTES LISTA ADJACENCIA')
    l = lista_adja.LerGrafoMontar()
    print(l)
    print('')
    l = lista_adja.AddVertice(l)
    print(l)
    print('')
    l = lista_adja.RemVertice(l,4)
    print(l)
    print('')
    l = lista_adja.AddAresta(l, 2, 3)
    print(l)
    print('')
    l = lista_adja.RemAresta(l,2,1)
    print(l)
    print('')
    v = lista_adja.VerticesVizinhos(l, 3)
    print(v)
    print('')
    ####
    print('TESTES MATRIZ ADJACENCIA')
    m = matriz_adja.LerGrafoMontar()
    print(m)
    print('')
    m = matriz_adja.AddVertice(m)
    print(m)
    print('')
    m = matriz_adja.RemVertice(m,4)
    print(m)
    print('')
    m = matriz_adja.AddAresta(m, 2, 3)
    print(m)
    print('')
    m = matriz_adja.RemAresta(m,2,1)
    print(m)
    print('')
    vm = matriz_adja.VerticesVizinhos(m, 3)
    print(vm)
    print('')

main()