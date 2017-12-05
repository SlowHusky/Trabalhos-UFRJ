# -*- coding: utf-8 -*-
"""
Trabalho da lista 1
"""
"""exercicio 1
def criar_matriz(linhas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(linhas):
            linha.append(str(input("valor da célula" + str(i+1) + \
            "," + str(j+1))))
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    #print(len(matriz))
    print(matriz)

def lista_adjacencias(matriz):
    lista_adj = []
    for i in range(len(matriz)):
        adj = []
        lista_adj.append(str(i+1))
        for j in range(len(matriz[i])):
            if int(matriz[i][j]) != 0:
                adj.append(j+1)
        lista_adj.append(adj)
    return lista_adj

            
if __name__ == "__main__":
    print("começando")
    linhas = int(input("\n Entre com as linhas:"))
    print("numero de linhas " + str(linhas))    
    
    m1 = criar_matriz(linhas)
    imprimir_matriz(m1)
    print lista_adjacencias(m1)  
    print("o algoritmo tem ordem n ao quadrado")
    print("ele funciona para digrafos")
"""    
    
"""
    exercício 2:
"""
    
"""
    exercício 3:
    Nas matrizes de adjacências sem peso, concideram que as células
    da matriz ficam 1 quando tem ligação e zero(ou vazio) quando não 
    existe. Nas matrizes com peso, os valores das células representam
    os pesos entre as ligações. Nas listas de adjacências sem peso, as 
    representações se parecem com listas encadeadas, que mostram 
    para quem existe caminho. Nas listas de adjacências com peso, além
    da informação de quem possue caminho, cada elemento deve mostrar
    qual o peso deste. Ou seja, existe uma informação a mais na cadeia.
    """

"""
    exercicio 4:

    
def contador_head_tail(n):
    lista = []
    contador = 0
    for i in range(n):
        lista.append(raw_input())
    for i in range(int(n/2)):
        base = lista[i]
        for j in range(n):
            if lista[j] != base:
                if (lista[j][0] == base[-1] or lista[j][-1] == base[0]):
                    print base
                    print lista[j]
                    contador += 1
    if contador == 0:
        print -1
        
if __name__ == "__main__":
    print "iniciando"
    n = input("\n entre com o dado: ")
    contador_head_tail(n)

"""

"""
    exercício 5
"""

