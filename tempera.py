import random
import math

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
        
        index = random.randint(0,(len(curso_atual)-1))
        index2 = random.randint(0,(len(curso_atual)-1))
        
        posicao_random = novo_curso[index]
        posicao_atual = novo_curso[index2]
        novo_curso[index2]=posicao_random
        novo_curso[index]=posicao_atual
        x =avalia(novo_curso,matriz)
        curso = novo_curso
        
        return curso,x     

def simulated_annealing(curso, matriz, temperatura_inicial, taxa_resfriamento,temperatura_final):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual, matriz)
    melhor_curso = curso_atual[:]
    melhor_distancia = distancia_atual
    print("Distancia atual tempera:"+str(distancia_atual))
    temperatura = temperatura_inicial

    while temperatura>temperatura_final:
        novo_curso,nova_distancia = sucessor(curso_atual,matriz)
        e = nova_distancia - distancia_atual
        if e>=0:
            rd = random.randint(0,1)
            aux = math.exp(-e/temperatura)
            if rd >=aux:
                distancia_atual = nova_distancia
                curso_atual = novo_curso

        
        if nova_distancia < melhor_distancia:
            melhor_curso = curso_atual[:]
            melhor_distancia = nova_distancia
       
            
        
        temperatura *= taxa_resfriamento

   

    return melhor_curso, melhor_distancia

def iniciarr(matriz, nomes, long,si):
    solucao_inicial = si
    temperatura_inicial = 500.0
    taxa_resfriamento = 0.99
    temperatura_final = 5

    melhor_percurso, melhor_distancia = simulated_annealing(solucao_inicial, matriz, temperatura_inicial, taxa_resfriamento, temperatura_final)

    lat = []
    bares = []
    for i in range(len(melhor_percurso)):
        atual = melhor_percurso[i]
        bares.append(nomes[atual])
    for i in range(len(melhor_percurso)):
        atual = melhor_percurso[i]
        lat.append(long[atual])

    return melhor_percurso, melhor_distancia, lat
