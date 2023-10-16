import random

def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual    

def subida(curso,max_iteracoes,matriz):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual,matriz)
    for i in range(max_iteracoes):
        novo_curso = curso_atual[:]
        random.shuffle(novo_curso)
        nova_distancia = avalia(novo_curso,matriz)
        
        if nova_distancia<= distancia_atual:
            curso_atual = novo_curso
            distancia_atual = nova_distancia

    return curso_atual,distancia_atual



def iniciar(matriz_distancias,matriz_nomes,matriz_lat):
    n = len(matriz_distancias)
    sequencia_atual = random.sample(range(n), n) 
    print("Solucao inicial:"+str(sequencia_atual),"Tamanho:"+str(len(sequencia_atual)))
    curso,distancia= subida(sequencia_atual,1000,matriz_distancias)
    bares = []
    lat = []
    for i in range(len(curso)):
        atual = curso[i]
        bares.append(matriz_nomes[atual])
    for i in range(len(curso)):
        atual = curso[i]
        lat.append(matriz_lat[atual])    

    return curso,distancia,bares,lat






    
    
    

