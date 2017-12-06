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

"""
    exercício 3:
caso 1:numero dois
uma forma, 1+1

caso 2: numero 3
duas formas, 1+1+1, 2+1

caso 3: numero 4
três formas: 1+1+1+1, 2+1+1, 3+1

caso 4: numero 5
seis formas: 1 + 1 + 1 + 1 +1, 2 + 1 +1 +1, 3 + 1 + 1, 4 + 1, 3 + 2, 2 + 2 + 1

caso n:
n - 1 * n -2
"""

"""
    Exercício 4

"""