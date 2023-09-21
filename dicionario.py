def conveersao(distanciaentre,nomes,distanciainicial):
   distancia_proximo = distanciaentre.split('/')
   distancia_inicial = distanciainicial.split('/')
   del distancia_proximo[0]
   nomes_bar = nomes.split('/')
   
   float_numero = [float(d) if d != "" else 0.0 for d in distancia_proximo]

   float_numero2 = [float(d) if d != "" else 0.0 for d in distancia_inicial]
       
 
   return nomes_bar, float_numero, float_numero2



# Função para dividir a lista de distâncias em sublistas
def dividir_distancias(distanciaentre):
    num_bares = int(len(distanciaentre) ** 0.5)  # Calcula o número de bares
    sublistas = []

    for i in range(num_bares):
        inicio = i * num_bares
        fim = inicio + num_bares
        sublista = distanciaentre[inicio:fim]
        sublistas.append(sublista)
    
    return sublistas

def alterar_valores(matriz1,matriz2):
    for linha in matriz1:
        processar_linha(linha, matriz2)
    return matriz1

def processar_linha(linha, matriz_distancias_ate_origem):
  for m in matriz_distancias_ate_origem:
    for j in range(len(m)):
        for i in range(len(linha)):
            if linha[i] == 0:
                linha.insert(0, matriz_distancias_ate_origem[j])
                linha[i] = 0
    

def dic(matriz1,nomes):
    dicionario_distancias = {}
    for i, nome_bar in enumerate(nomes):
        dicionario_distancias[nome_bar] = {nomes[j]: matriz1[i][j] for j in range(len(nomes))}

# Exibir o dicionário de distâncias
    for bar, distancias in dicionario_distancias.items():
         print(f"{bar}: {distancias}")
    
    return dicionario_distancias    

    