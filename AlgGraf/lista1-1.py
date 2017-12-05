# -*- coding: utf-8 -*-
"""
Trabalho da lista 1
"""
 #exercicio 1
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