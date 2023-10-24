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

def simulated_annealing(curso, matriz, temperatura_inicial, taxa_resfriamento,temperatura_final):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual, matriz)
    melhor_curso = curso_atual[:]
    melhor_distancia = distancia_atual
    temperatura = temperatura_inicial

    while temperatura>temperatura_final:
        novo_curso = curso_atual[:]
        random.shuffle(novo_curso)
        nova_distancia = avalia(novo_curso, matriz)
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

def iniciarr(matriz, nomes, long):
    solucao_inicial = list(range(len(matriz)))
    random.shuffle(solucao_inicial)

    temperatura_inicial = 1000.0
    taxa_resfriamento = 0.995
    temperatura_final = 10

    melhor_percurso, melhor_distancia = simulated_annealing(solucao_inicial, matriz, temperatura_inicial, taxa_resfriamento, temperatura_final)

    lat = []
    bares = []
    for i in range(len(melhor_percurso)):
        atual = melhor_percurso[i]
        bares.append(nomes[atual])
    for i in range(len(melhor_percurso)):
        atual = melhor_percurso[i]
        lat.append(long[atual])

    return melhor_percurso, melhor_distancia, bares, lat
