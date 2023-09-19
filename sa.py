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
    

def Avalia(m1):
    
    linha = m1[1]
    print("alinha uai"+str(linha))

    soma = 0
    for valor in linha:
        soma += valor
        print(soma)
    return soma

def Solucao_Inicial(n,matriz):
    s = []
    s = matriz[rd.randint(0, len(matriz) - 1)]
    return s
    
   





