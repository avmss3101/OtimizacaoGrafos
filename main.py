from lista_adja import *
from matriz_adja import *

def main():
    #######
    g1 = LerGrafoMontar()
    g1 = AddVertice(g1)
    print(g1)
    g1 = RemVertice(g1, 4)
    print(g1)
    #CriarGrafo()

    ######
    l = LerGrafoMontar()
    l = AddVertice(l)
    print(l)
    l = AddAresta(l,1,3)
    print(l)
    l = RemVertice(l, 3)
    print(l)
    l = AddVertice(l)
    print(l)
    l = AddAresta(l,2,4)
    print(l)
    l = RemAresta(l,2,4)
    print(l)
    vertice = VerticesVizinhos(l, 2)
    print(vertice)
    CriarGrafo()

main()


