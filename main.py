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
    #as excecoes nao foram tratadas

    #CriarGrafo()
    resp = input('Criar Grafos? S(im) ou N(ao)')
    if resp == 's' or resp == 'S':
        CriarGrafo()
    print('TESTES LISTA ADJACENCIA')
    numV = input('Usar qual grafo? (5,6,7,8,9,10,20,50,100,200,500,1000)')
    l = lista_adja.LerGrafoMontar(numV)
    print(l)
    print('')
    resp = input('Adicionar Vertice em grafo? S(im) ou N(ao)')
    if resp == 's' or resp == 'S':
        l = lista_adja.AddVertice(l)
        print(l)
    print('')
    resp_n = int(input('Remover que vertice?'))
    l = lista_adja.RemVertice(l,resp_n)
    print(l)
    print('')
    v1 = int(input('Qual aresta adicionar? (um vertice por entrada)'))
    v2 = int(input())
    l = lista_adja.AddAresta(l, v1, v2)
    print(l)
    print('')
    v1 = int(input('Qual aresta remover? (um vertice por entrada)'))
    v2 = int(input())
    l = lista_adja.RemAresta(l,v1,v2)
    print(l)
    print('')
    resp_n = int(input('Mostrar vizinhos de qual vertice?'))
    v = lista_adja.VerticesVizinhos(l, resp_n)
    print(v)
    print('')
    ####
    ####
    print('TESTES MATRIZ ADJACENCIA')
    numV = input('Usar qual grafo? (5,6,7,8,9,10,20,50,100,200,500,1000)')
    l = matriz_adja.LerGrafoMontar(numV)
    print(l)
    print('')
    resp = input('Adicionar Vertice em grafo? S(im) ou N(ao)')
    if resp == 's' or resp == 'S':
        l = matriz_adja.AddVertice(l)
        print(l)
    print('')
    resp_n = int(input('Remover que vertice?'))
    l = matriz_adja.RemVertice(l,resp_n)
    print(l)
    print('')
    v1 = int(input('Qual aresta adicionar? (um vertice por entrada)'))
    v2 = int(input())
    l = matriz_adja.AddAresta(l, v1, v2)
    print(l)
    print('')
    v1 = int(input('Qual aresta remover? (um vertice por entrada)'))
    v2 = int(input())
    l = matriz_adja.RemAresta(l,v1,v2)
    print(l)
    print('')
    resp_n = int(input('Mostrar vizinhos de qual vertice?'))
    v = matriz_adja.VerticesVizinhos(l, resp_n)
    print(v)
    print('')

main()