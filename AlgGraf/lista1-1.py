# -*- coding: utf-8 -*-
"""
Trabalho da lista 1
"""
 #exercicio 1
def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(str(input()))
        matriz.append(linha)
    return matriz
1
def imprimir_matriz(matriz):
    #print(len(matriz))
    print(matriz)
    
            
if __name__ == "__main__":
    print("começando")
    linhas = int(input("\n Entre com as linhas:"))
    colunas = int(input("\n Entre com as colunas:"))
    print("numero de linhas " + str(linhas))
    print("numero de colunas " + str(colunas))
    
    
    m1 = criar_matriz(linhas, colunas)
    imprimir_matriz(m1)
    