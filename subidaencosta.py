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


#matriz_distancias = [[3.9, 1.9, 1.6, 1.2, 1.7, 1.5, 1.6, 2.1, 2.1, 1.2, 1.2, 1.0, 1.9, 1.2, 0.8, 1.2, 0.6, 1.5, 0.9], [3.9, 0.0, 3.1, 3.1, 3.8, 2.9, 3.1, 3.9, 4.2, 4.2, 3.1, 3.1, 3.3, 2.6, 4.0, 3.5, 2.9, 3.4, 4.2], [4.0, 1.9, 3.1, 0.0, 0.4, 0.8, 0.3, 0.5, 1.0, 1.4, 1.4, 0.8, 0.7, 0.9, 0.4, 1.2, 1.1, 0.8, 1.2], [1.3, 1.4, 1.6, 3.1, 0.4, 0.0, 0.6, 0.2, 0.4, 1.0, 1.5, 1.5, 0.5, 0.4, 0.6, 0.5, 0.9, 0.8, 0.6], [0.9, 1.2, 1.1, 1.2, 3.8, 0.8, 0.6, 0.0, 0.8, 1.0, 1.1, 0.9, 0.9, 0.9, 0.4, 1.7, 0.4, 0.8, 0.7], [0.4, 1.1, 0.5, 0.6, 0.7, 2.9, 0.3, 0.2, 0.8, 0.0, 0.3, 1.2, 1.6, 1.6, 0.6, 0.6, 0.3, 1.1, 0.9], [0.6, 1.0, 3.1, 0.5, 1.0, 0.3, 0.0, 0.7, 1.0, 0.3, 1.1, 1.6, 3.9, 0.8, 0.5, 1.0, 1.4, 1.5, 1.2], [0.4, 1.4, 1.4, 0.3, 0.3, 1.8, 1.8, 0.6, 1.0, 1.6, 0.4, 1.2, 0.8, 0.8, 1.1, 0.0, 0.8, 0.4, 1.2], [1.2, 0.7, 1.4, 1.4, 2.1, 2.1, 0.3, 0.9, 0.6, 1.5, 1.5, 1.6, 1.6, 4.2, 4.2, 1.4, 1.4, 1.8, 1.8], [0.9, 0.9, 0.3, 1.8, 1.8, 1.5, 1.5, 3.1, 1.4, 1.4, 1.2, 1.8, 1.8, 1.2, 1.2, 0.0, 0.0, 0.0, 0.0], [1.2, 1.2, 0.6, 0.5, 0.9, 0.8, 0.8, 1.8, 1.8, 0.2, 36.0, 0.9, 0.4, 0.4, 0.9, 3.1, 1.2, 0.9, 0.0], [0.3, 0.6, 0.4, 0.2, 1.4, 1.4, 0.8, 1.9, 1.9, 1.6, 1.6, 2.0, 2.0, 3.3, 0.9, 0.8, 0.0, 1.2, 1.2], [1.5, 0.5, 1.7, 1.7, 0.5, 0.1, 0.8, 1.0, 1.6, 1.6, 0.6, 0.8, 36.0, 0.2, 0.9, 1.1, 0.6, 0.7, 0.9], [1.4, 0.3, 0.2, 0.4, 1.4, 1.9, 1.9, 0.8, 1.4, 1.1, 0.7, 0.7, 0.1, 1.1, 0.2, 0.7, 0.9, 0.0, 0.4], [0.9, 1.5, 0.8, 0.5, 0.0, 1.1, 0.4, 1.1, 1.4, 0.8, 0.4, 0.5, 1.3, 1.3, 0.4, 0.7, 0.0, 0.4, 0.9], [0.4, 0.4, 2.6, 1.9, 1.4, 1.3, 1.2, 0.0, 1.7, 4.0, 0.4, 1.2, 0.3, 1.0, 1.1, 1.7, 2.0, 2.0, 0.9], [1.0, 0.2, 1.2, 1.0, 0.7, 0.5, 2.9, 0.6, 0.2, 0.5, 0.6, 3.4, 3.5, 1.0, 0.5, 1.2, 1.2, 0.8, 0.8], [0.6, 0.2, 1.4, 1.4, 1.0, 0.6, 0.4, 0.5, 0.6, 0.2, 0.9, 0.8, 1.2, 0.5, 1.5, 1.5, 0.9, 1.0, 0.4], [0.0, 1.4, 0.6, 1.2, 0.5, 0.8, 0.2, 0.8, 0.5, 0.0, 0.3, 4.2, 1.1, 1.4, 0.2, 1.5, 1.3, 1.1, 1.6]]
def iniciar(matriz_distancias,matriz_nomes,matriz_lat):
    n = len(matriz_distancias)
    print(n)
    sequencia_atual = random.sample(range(n), n) 
    print("Solucao inicial:"+str(sequencia_atual),"Tamanho:"+str(len(sequencia_atual)))
    curso,distancia= subida(sequencia_atual,1000,matriz_distancias)
    bares = []
    lat = []
#matriz_nomes = ['Hayama Sushi Bar', 'PIT STOP 2', "Geninho's Bar e Boliche", 'Choperia Central', 'Bar Do Alexandre', 'Kiosque Trem Bao', 'MOTORBIER CERVEJARIA E HAMBURGUERIA', 'Bar Do Capixaba', 'Mercearia Fernandes', 'Bar Guimaraes', 'Bar do Marcinho', 'Jardim Secreto Bar', 'Mercearia São José', "Junior's CHOPERIA", "Korno's bar", 'Quintal Boteco', 'BAR DO ZICO', 'Bar e Mercearia Clarice', 'Bar do betão o point dos amigos', 'Bar do Beto B&B']
    for i in range(len(curso)):
        atual = curso[i]
        bares.append(matriz_nomes[atual])
    for i in range(len(curso)):
        atual = curso[i]
        lat.append(matriz_lat[atual])    

    return curso,distancia,bares,lat






    
    
    

