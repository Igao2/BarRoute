import random
import math

def avalia(curso, matriz):
    distancia_total = 0.0
    for i in range(len(curso) - 1):
        bar1 = curso[i]
        bar2 = curso[i + 1]
        distancia_total += float(matriz[bar1][bar2])
    distancia_total += matriz[curso[-1]][curso[0]]
    return distancia_total

def simulated_annealing(curso, matriz, nomes, temperatura_inicial, taxa_resfriamento, max_iteracoes):
    curso_atual = curso[:]
    bar_nomeatual = nomes[:]
    distancia_atual = avalia(curso_atual, matriz)
    melhor_curso = curso_atual[:]
    melhor_distancia = distancia_atual
    temperatura = temperatura_inicial

    for _ in range(max_iteracoes):
        i, j = random.sample(range(len(curso_atual)), 2)
        novo_curso = curso_atual[:]
        novo_bar = bar_nomeatual[:]
        novo_curso[i], novo_curso[j] = novo_curso[j], novo_curso[i]
        novo_bar[i], novo_bar[j] = novo_bar[j], novo_bar[i]
        nova_distancia = avalia(novo_curso, matriz)

        
        if nova_distancia <= distancia_atual or random.random() < math.exp((distancia_atual - nova_distancia) / temperatura):
            curso_atual = novo_curso
            bar_nomeatual = novo_bar
            distancia_atual = nova_distancia

        
        if nova_distancia < melhor_distancia:
            melhor_curso = curso_atual[:]
            melhor_distancia = nova_distancia

        
        temperatura *= taxa_resfriamento

    nom = []
    for i in melhor_curso:
        nom.append(bar_nomeatual[i])

    return melhor_curso, melhor_distancia, nom

def iniciarr(matriz, nomes):
    solucao_inicial = list(range(len(matriz)))
    random.shuffle(solucao_inicial)

    temperatura_inicial = 1000.0
    taxa_resfriamento = 0.995
    max_iteracoes = 10000

    melhor_percurso, melhor_distancia, bares = simulated_annealing(solucao_inicial, matriz, nomes, temperatura_inicial, taxa_resfriamento, max_iteracoes)

    return melhor_percurso, melhor_distancia, bares
