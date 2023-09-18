import numpy as np
import random as rd

def Gerar_Problema(n,dist):
    m1 = dist
    m2 = np.zeros((n,n),int)

    for i in range(n):
        for j in range(n):
            if i!=j:
                m2[i][j] = dist[i][j]

    return m1, m2
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
        valor += 2*m1[s[i]][s[i+1]]+ 1/8*(m2[s[i]][s[i+1]]*0.1)
    
    valor += 2*m1[s[n-1]][s[0]]+1/8*m2[s[n-1]][s[0]]
    
    return valor

def Solucao_Inicial(n):
    s = []
    
    for i in range(n):
        s.append(i)
    
    rd.shuffle(s)
    return s





