def conveersao(distanciaatual,distanciaentre,nomes):
   
   distancia_atual = distanciaatual.split('/')
   distancia_proximo = distanciaentre.split('/')

   nome = nomes.split(',')
# Crie um dicionário com as informações organizadas
   dicionario_bares = {}
   for i in range(len(nome)):
        x = nome[i]
        distancia_atual_bar = distancia_atual[i]
        distancia_proximo_bar = distancia_proximo[i]
        dicionario_bares[x] = {'Distancia Atual': distancia_atual_bar, 'Distancia para o Próximo': distancia_proximo_bar}

# Exibir o dicionário resultante
   print(dicionario_bares)
