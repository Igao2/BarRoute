import random

def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual

def sucessor(curso_atual,valor_atual,matriz):
        curso = curso_atual[:]
        novo_curso = curso_atual[:]
        melhor_distancia = valor_atual
        index = random.randint(0,(len(curso_atual)-1))
        for j in range(len(curso_atual)):
            posicao_random = novo_curso[index]
            posicao_atual = novo_curso[j]
            novo_curso[j]=posicao_random
            novo_curso[index]=posicao_atual
            x = avalia(novo_curso,matriz)
            if x <melhor_distancia:
                curso = novo_curso
                melhor_distancia = x
        return curso,melhor_distancia

       
def subida(curso,matriz):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual,matriz)
    print("Distancia atual subida:"+str(distancia_atual))
    while True:
        novo_curso,nova_distancia = sucessor(curso_atual,distancia_atual,matriz)
        
        
        if nova_distancia<= distancia_atual:
            return novo_curso,nova_distancia
        else:
            return curso_atual,distancia_atual

    

def iniciar(matriz_distancias,matriz_nomes,matriz_lat,si):
    
    sequencia_atual = si
    print("Solucao inicial:"+str(sequencia_atual),"Tamanho:"+str(len(sequencia_atual)))
    curso,distancia= subida(sequencia_atual,matriz_distancias)
    bares = []
    lat = []
    for i in range(len(curso)):
        atual = curso[i]
        bares.append(matriz_nomes[atual])
    for i in range(len(curso)):
        atual = curso[i]
        lat.append(matriz_lat[atual])    

    return curso,distancia,lat
