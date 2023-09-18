import random

def avalia(curso, matriz):
    distancia_total = 0.0
    for i in range(len(curso) - 1):
        bar1 = curso[i]
        bar2 = curso[i + 1]
        distancia_total += float(matriz[bar1][bar2])
    distancia_total += matriz[curso[-1]][curso[0]]
   
    return distancia_total

def subida_encosta(curso, max_iteracoes, matriz, nomes):
    curso_atual = curso[:]
    bar_nomeatual = nomes[:]
    distancia_atual = avalia(curso_atual, matriz)
    return distancia_atual
    for _ in range(max_iteracoes):
        novo_curso = curso_atual[:]
        novo_bar = bar_nomeatual[:]
        i, j = random.sample(range(len(novo_curso)), 2)
        novo_curso[i], novo_curso[j] = novo_curso[j], novo_curso[i]
        novo_bar[i], novo_bar[j] = novo_bar[j], novo_bar[i]

        nova_distancia = avalia(novo_curso, matriz)

        if nova_distancia <= distancia_atual:
            curso_atual = novo_curso
            print(curso_atual)
            bar_nomeatual = novo_bar
            distancia_atual = nova_distancia
            print(distancia_atual)

    return curso_atual, distancia_atual, bar_nomeatual

def iniciar(matriz_distancia, nomes):
    solucao_inicial = list(range(len(matriz_distancia)))
    random.shuffle(solucao_inicial)

    max_iteracoes = 10000

    melhor_percurso = subida_encosta(
        solucao_inicial, max_iteracoes, matriz_distancia, nomes
    )
   # nom = []
    #for i in melhor_percurso:
     #   nom.append(bares[i])

    return solucao_inicial, melhor_percurso







    
    
    

