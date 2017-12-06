#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lista de exercícios 3
Victor Ribeiro Pires
113051532
"""

"""
    exercício 1:

def andar(n):
    lista = []
    contador = 0
    for i in range(n):
        lista.append(str(i+1))
    #for i in range(n):
        if lista[i][-1] == "4":
            contador += 1
    numero = int(lista[-1])
    resultado = numero + contador
    if (str(resultado) == "4"):
        resultado += 1
        print resultado
        return resultado
    print resultado
    return resultado
    

if __name__ == "__main__":
    n = input()
    andar(n)
"""

"""
   # exercício 2


def relacionamento(n, m, q):
    matriz = []
    materias = []
    contador = 0
    for i in range(q):
        lista = []
        for j in range(2):
            lista.append(input())
        matriz.append(lista)
    for i in range(q):
        materias.append(i)
    for i in range(q):
        for j in range(len(matriz[i])):
            if matriz[i][j] in materias:
                contador += 1
                materias.remove(matriz[i][j])
    print contador
if __name__ == "__main__":
    n = input()
    m = input()
    q = input()
    relacionamento(n,m,q)
"""