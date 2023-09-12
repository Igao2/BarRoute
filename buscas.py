import numpy as np
import random as rd
def Gerar_Problema(n,me1,ma1,me2,ma2):
    m1 = np.zeros((n,n),int)
    m2 = np.zeros((n,n),int)
    
    for i in range(n):
        for j in range(n):
            if i!=j:
                m1[i][j] = rd.randint(me1,ma1)
                m2[i][j] = rd.randint(me2,ma2)
    """
    # N=4
    m = [[0,1,2,3],
         [1,0,2,3],
         [1,2,0,3],
         [1,2,3,0]
        ]
    """
    return m1, m2

def Avalia(n,s,m1,m2):
    valor = 0
    for i in range(0,n-1):
        valor += 2*m1[s[i]][s[i+1]]+ 1/8*m2[s[i]][s[i+1]]
    
    valor += 2*m1[s[n-1]][s[0]]+1/8*m2[s[n-1]][s[0]]
    
    return valor

def Solucao_Inicial(n):
    s = []
    
    for i in range(n):
        s.append(i)
    
    rd.shuffle(s)
    return s


# MÓDULO PRINCIPAL
N   = 5    # TAMANHO DO PROBLEMA
MIN1 = 10   # VALOR MÍNIMO PARA O CUSTO ENTRE PONTOS
MAX1 = 30   # VALOR MÁXIMO PARA O CUSTO ENTRE PONTOS
MIN2 = 2    # VALOR MÍNIMO PARA O CUSTO ENTRE PONTOS
MAX2 = 8    # VALOR MÁXIMO PARA O CUSTO ENTRE PONTOS

mat1, mat2 = Gerar_Problema(N,MIN1,MAX1,MIN2,MAX2)
print("Matriz de Adjacências para o Problema")
print(mat1)
print(mat2)

si = Solucao_Inicial(N)
print("\nSolução inicial")
print(si)
vi = Avalia(N,si,mat1,mat2)
print("Valor da solução inicial: ",vi)
