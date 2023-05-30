import numpy as np
import json

def soma_matrizes(matriz1, matriz2):
    n = len(matriz1)
    res = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = matriz1[i][j] + matriz2[i][j]
            linha.append(elemento)
        res.append(linha)
    
    return res

def subtrai_matrizes(matriz1, matriz2):
    n = len(matriz1)
    res = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = matriz1[i][j] - matriz2[i][j]
            linha.append(elemento)
        res.append(linha)
    
    return res

def multiplica_matrizes(matriz1, matriz2):
    n = len(matriz1)
    res = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = 0
            for k in range(n):
                elemento += matriz1[i][k] * matriz2[k][j]
            linha.append(elemento)
        res.append(linha)
    
    return res

#Exemplo para ver se funciona! 

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

resultado_soma = soma_matrizes(matriz1, matriz2)
print("Soma das matrizes:")
for linha in resultado_soma:
    print(linha)

resultado_subtracao = subtrai_matrizes(matriz1, matriz2)
print("Subtração das matrizes:")
for linha in resultado_subtracao:
    print(linha)

resultado_multiplicacao = multiplica_matrizes(matriz1, matriz2)
print("Multiplicação das matrizes:")
for linha in resultado_multiplicacao:
    print(linha)

##

def transposta_Real(matriz):
    n = len(matriz)
    matriz_transposta = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
    
    return matriz_transposta

def transposta_Complexos(matriz):
    n = len(matriz)
    matriz_transposta = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = matriz[j][i].conjugate()
            linha.append(elemento)
        matriz_transposta.append(linha)
    
    return matriz_transposta



def calcular_autovalores_autovetores(matriz):
    autovalores, autovetores = np.linalg.eig(matriz)
    return autovalores, autovetores

