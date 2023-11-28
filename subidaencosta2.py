import random

def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual

def sucessor(curso_atual,matriz):
        curso = curso_atual[:]
        novo_curso = curso_atual[:]
        melhor_distancia = 100
        index = random.randint(0,(len(curso_atual)-1))
        for i in range(len(curso_atual)):
            if i == index:
                for j in range(len(curso_atual)):
                    if i!=j and j!=0:
                        posicao_random = novo_curso[index]
                        posicao_atual = novo_curso[j]
                        novo_curso[j]=posicao_random
                        novo_curso[index]=posicao_atual
                        x =avalia(novo_curso,matriz)
                        if x <melhor_distancia:
                            curso = novo_curso
                            melhor_distancia = x
        return curso,melhor_distancia

       
def subida(curso,matriz,tmax):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual,matriz)
    print("Distancia atual subida*:"+str(distancia_atual))
    t = 1
    
    while True:
        novo_curso,nova_distancia = sucessor(curso_atual,matriz)
        if nova_distancia>=distancia_atual:
                    
            if t>tmax:
                return novo_curso,nova_distancia
            else:
                t=t+1


        else:
            distancia_atual = nova_distancia
            curso_atual = novo_curso             
            t=1
        
        

def iniciars(matriz_distancias,matriz_nomes,matriz_lat,si):
    
    sequencia_atual = si
    print("Solucao inicial:"+str(sequencia_atual),"Tamanho:"+str(len(sequencia_atual)))
    curso,distancia = subida(sequencia_atual,matriz_distancias,16)
    bares = []
    lat = []
    for i in range(len(curso)):
        atual = curso[i]
        bares.append(matriz_nomes[atual])
    for i in range(len(curso)):
        atual = curso[i]
        lat.append(matriz_lat[atual])    

    return curso,distancia,lat