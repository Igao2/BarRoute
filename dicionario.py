def conveersao(distanciaentre,nomes):
   distancia_proximo = distanciaentre.split('/')
   del distancia_proximo[0]
   nomes_bar = nomes.split('/')
   print(distancia_proximo)
   float_numero = [float(d) if d != "" else 0.0 for d in distancia_proximo]

       
  
   return nomes_bar, float_numero



# Função para dividir a lista de distâncias em sublistas
def dividir_distancias(distanciaentre):
    num_bares = int(len(distanciaentre) ** 0.5)  # Calcula o número de bares
    sublistas = []

    for i in range(num_bares):
        inicio = i * num_bares
        fim = inicio + num_bares
        sublista = distanciaentre[inicio:fim]
        sublistas.append(sublista)
    print(sublistas)
    return sublistas




# Exibir a matriz de distâncias


 
