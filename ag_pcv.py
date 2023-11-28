import copy as cp
import numpy as np
import random as rd
import math as mh

# método de ordenação (BUBBLE SORT)

def Sort(p,f,qp):
    for i in range(qp-1):
        for j in range(i+1,qp):
            if f[i]<f[j]:
                aux_f = cp.deepcopy(f[i])
                f[i]  = cp.deepcopy(f[j])
                f[j]  = cp.deepcopy(aux_f)

                aux_p = cp.deepcopy(p[i])
                p[i]  = cp.deepcopy(p[j])
                p[j]  = cp.deepcopy(aux_p)
    #print(p)
    return p, f

# função para gerar matriz de adjacências


# Função para gerar população inicial
def Cromossomo(n):
    ind = np.zeros(n,int)
    for i in range(n):
        ind[i] = i
    rd.shuffle(ind)
    print(ind)
    return ind


def PopIni(n,tp):
    pop = np.zeros((tp,n),int)

    for i in range(tp):
        pop[i] = Cromossomo(n)

    return pop
    
def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual



def Aptidao(n,tp,pop,mat):
    
    f = np.zeros(tp,float)

    for i in range(tp):
        f[i] = 1/avalia(pop[i],mat)
    
    soma = sum(f)
    
    # frequencia relativa
    f = f/soma
    
    return f

# ROTINA ROLETA
def Roleta(f):
    ale = rd.uniform(0,1)
    ind=0
    soma = f[ind]
    
    while soma<ale:
        ind += 1
        soma += f[ind]
    return ind

# ROTINA TORNEIO
def Torneio(f,tp):
    i1 = rd.randrange(0,tp)
    i2 = rd.randrange(0,tp)
    if f[i1]>f[i2]:
        return i1
    else:
        return i2

# função para execução do operador de cruzamento
def Crossover(n,pop,fit,tp,tc):

    # quantidade de cruzamentos
    qc = mh.ceil(tc*tp)
    
    # um ponto de corte
    corte = rd.randrange(0,n)

    desc = []
    for i in range(qc):
        # pai 1
        pai1 = Roleta(fit)

        # pai 2
        pai2 = Roleta(fit)

        # primeiro descendente
        aux = []
        for j in range(0,corte):
            aux.append(pop[pai1][j])
        for j in range(corte,n):
            aux.append(pop[pai2][j])
        desc.append(aux)

        # segundo descendente
        aux = []
        for j in range(0,corte):
            aux.append(pop[pai2][j])
        for j in range(corte,n):
            aux.append(pop[pai1][j])
        desc.append(aux)

    return corte, desc

def Ajusta_Restricao(n,desc,qd,corte):
    for i in range(len(desc)):
        alfabeto = list(range(0,n))
        for j in range(0,corte):
            alfabeto.remove(desc[i][j])
            rd.shuffle(alfabeto)

        j = corte
        while(len(alfabeto)>0):
            if(desc[i].count(alfabeto[0])==0):
                if(desc[i].count(desc[i][j])>1):
                    desc[i][j] = alfabeto[0]
                    del alfabeto[0]
                    j += 1
                else:
                    j += 1
            else:
                del alfabeto[0]
    
    return desc

# função para execução do operador de mutação
def Mutacao(n,desc,tp,tm):
    
    # Quantidade de mutaçãoes
    qm = mh.ceil(tp*tm)
    
    # Quantidade de descendentes
    q_desc = len(desc)

    for i in range(qm):
        
        # Selecionar o descendente
        jd = rd.randrange(0,q_desc)
        
        # faz cópia do descendente
        aux = cp.deepcopy(desc[jd])
        
        # translocação
        p1 = rd.randrange(0,n)
        p2 = rd.randrange(0,n)

        x = aux[p1]
        aux[p1] = aux[p2]
        aux[p2] = x

        # inclui em descendentes
        desc.append(aux)

    return desc

# função para gerar a nova população
def NovaPop(pop,desc,tp,ig):
    elite = mh.ceil(tp*ig)

    j= 0
    for i in range(elite,tp):
        pop[i] = cp.deepcopy(desc[j])
        j += 1
        if j==len(desc):
            break


    return pop

# Rotina Algoritmo Genético
def ag(mat,n,tp,ng,tc,tm,ig,latitude):
    #======> Gera população inicial
    pop = PopIni(n,tp)
    print("População Inicial:")
    print(pop)
    
    #======> calcula fitness da população
    fit = Aptidao(n,tp,pop,mat)
    print(fit,sum(fit))

    #======> Ciclo AG
    for g in range(ng):
        #======> Aplica cruzamento
        corte, desc = Crossover(n,pop,fit,tp,tc)
        #print("\nDescendentes com restrição:")
        #print(desc)
        
        # ajusta descendentes para atender a restrição do problema
        desc = Ajusta_Restricao(n,desc,len(desc),corte)
        #print("\nDescendentes corrigidos:")
        #print(desc)
        
        #======> Aplica mutação
        desc = Mutacao(n,desc,tp,tm)
        #print("\nDescendentes após operadores:")
        #print(desc)
        
        #======> calcula fitness de descendentes
        fit_d = Aptidao(n,len(desc),desc,mat)
    
        #======> Ordena população atual
        pop, fit = Sort(pop,fit,tp)
        #print(pop)

        #======> Ordena descendentes
        desc, fitd_d = Sort(desc,fit_d,len(desc))

        #======> Gera nova população
        pop = NovaPop(pop,desc,tp,ig)

        #======> Fitness da população
        fit = Aptidao(n,tp,pop,mat)
        pop, fit = Sort(pop,fit,tp)
        #sol = pop[0]
        #print("Solução: ",sol)
        #print("Geração: ",g+1,Custo_Caminho(sol,n,mat))
        

    #pop, fit = Sort(pop,fit,tp)
    lat = []
    z = pop[0]
    for f in range(len(z)):
        atual = z[f]
        lat.append(latitude[atual])

    return pop[0],lat

# definição dos parâmetros do problema
N  =  10                   # TAMANHO DO CROMOSSOMO
TP =  20     # TAMANHO DA POPULAÇÃO
NG =  0        # NÚMERO DE GERAÇÕES
TC =  0.8        # TAXA DE CRUZAMENTO
TM =  0.1        # TAXA DE MUTAÇÃO
IG =  0.1        # INTERVALO DE GERAÇÃO

minimo = 5       # valor mínimo para a matriz de adjacência
maximo = 50      # valor máximo para a matriz de adjacência

# GERA PROBLEMA - MATRIZ DE ADJACÊNCIAS



