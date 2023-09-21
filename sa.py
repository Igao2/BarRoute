import numpy as np
import random as rd

def Gerar_Problema(n,dist):
    m1 = dist
    

    return m1
    """
    # N=4
    m = [[0,1,2,3],
         [1,0,2,3],
         [1,2,0,3],
         [1,2,3,0]
        ]
    """
    

def Avalia(matriz,s):
    distancia_atual = 0
    for j in range(len(s)):
        for i in range(len(s)):
            if j+1<len(s) and i==s[j+1]:
                distancia_atual+=matriz[s[j]][i]
    distancia_atual += matriz[s[-1]][s[0]]
    return distancia_atual    




def Solucao_Inicial(n):
    s = rd.sample(range(n), n) 
    return s
#def(linha)
#
#menor = 100
# for i in range(n)
    # linha = linha + i
    #   if matriz[linha]<menor
            #menor = matriz[linha]
            #posicao = i
# return menor, posicao  






