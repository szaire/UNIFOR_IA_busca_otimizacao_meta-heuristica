# TODOs:
# DONE: 1. Fa¸ca a defini¸c˜ao da quantidade N de indiv´ıduos em uma popula¸c˜ao e quantidade m´axima de gera¸c˜oes.
# DONE: 2. Projete o operador de sele¸c˜ao, baseado no m´etodo da roleta.
# DONE: 3. Na etapa de recombina¸c˜ao, escolha um entre os seguintes operadores: Recombina¸c˜ao de um ponto ou
# Recombina¸c˜ao de dois pontos. A probabilidade de recombina¸c˜ao nesta etapa deve ser entre 85 < pc < 95%.
# DONE: 4. Na prole gerada, deve-se aplicar a muta¸c˜ao com probabilidade de 1% (neste caso, ´e interessante avaliar os
# diferentes procedimentos exibidos).
# TODO: 5. O algoritmo deve parar quando atingir o m´aximo n´umero de gera¸c˜oes ou quando a fun¸c˜ao custo atingir seu valor
# ´otimo.
# ==========================================================================================================
import numpy as np
import matplotlib.pyplot as plt
import time
# ==========================================================================================================
# TEMPO t0
# ==========================================================================================================
tempo = time.time()
# ==========================================================================================================
# DEFINIÇÕES INICIAIS
# ==========================================================================================================
# Número de pares
n = 20
# Definindo a população inicial aleatoriamente
P = np.random.uniform(low=0, high=8, size=(n, 8)).astype(int)
# Quantidade máxima de gerações
nMaxGeracoes = 10000
# ==========================================================================================================
# FUNÇÃO OBJETIVO - OBJETIVO: MAXIMIZAR F(X), OU SEJA, MINIMIZAR H
# ==========================================================================================================
# função aptidão
def f(x):
    return 28 - h(x)

def h(x: list):
    # criar um algoritmo para identificar os pares atacantes
    #tab = criar_tabuleiro(x)
    quant_pares_atacantes = procurar_pares_atacantes(x)
    return quant_pares_atacantes

def procurar_pares_atacantes(x: list):
    pares = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j]:
                pares += 1
            elif x[i] == x[j] - (j - i):
                pares += 1
            elif x[i] == x[j] + (j - i):
                pares += 1
    return pares
    
def criar_tabuleiro(x: list):
    temp_tab = np.zeros((8, 8))
    rows, cols = temp_tab.shape
    i_local = 0
    for j in range(cols):
        for i in range(rows):
            if i == x[i_local]:
                temp_tab[i][j] = 1
        i_local += 1
    return temp_tab
# ==========================================================================================================
# ALGORITMOS
# ==========================================================================================================
# SELEÇÃO (OK) 
def roleta(P: np.ndarray):
    somatorio_den_pi = 0
    for ind in P:
        somatorio_den_pi += f(ind)
    individuos_otimos = np.empty((0,P.shape[1])).astype(int)
    for _ in range(len(P)):
        i = 0
        r = np.random.uniform(0, 1)
        s = f(P[i,:])/somatorio_den_pi
        while s < r:
            i += 1
            Pi = f(P[i,:])/somatorio_den_pi
            s += Pi
        individuos_otimos = np.concatenate((individuos_otimos, P[i].reshape(1,8)))
        # --> [ind, ind, ind, ind... ind]
    return individuos_otimos

# RECOMBINAÇÃO (OK) 
def recombinacao_dois_pontos(inds: np.ndarray, index, prob_recombinacao):
    xi1 = int(np.random.uniform(low=1, high=len(P[0]) - 1))
    xi2 = int(np.random.uniform(low=1, high=len(P[0]) - 1))
    
    if xi1 > xi2:
        xi1, xi2 = xi2, xi1
    
    mascara = gerar_mascara(xi1, xi2)
    
    r_prob = np.random.uniform(0, 1)

    if (r_prob < prob_recombinacao):
        i = index
        for j in range(inds.shape[1]):
            if mascara[j] == 1:
                inds[i][j], inds[i+1][j] = inds[i+1][j], inds[i][j]

def gerar_mascara(xi1, xi2):
    masc = np.zeros((len(P[0])))
    for j in range(xi1, xi2+1):
        masc[j] = 1
    return masc

# MUTAÇÃO [uniforme] (OK)
def mutacao(inds: np.ndarray, index):
    for g in range(inds.shape[1]): # g as gene
        Pm = np.random.uniform(0, 1)
        if Pm <= 0.1:
            inds[index][g] = int(np.random.uniform(low=0, high=8))
            
    
# ==========================================================================================================
# RESOLUÇÃO
# ==========================================================================================================
melhor_aptidao = 0
melhor_individuo = np.array([])
solucoes = []
quantidade_solucoes = 0
geracao_atual = 0

while quantidade_solucoes < 92:
    melhor_aptidao = 0
    geracao_atual = 0
    P = np.random.uniform(low=0, high=8, size=(n, 8)).astype(int)

    
    while melhor_aptidao < 28 and geracao_atual < nMaxGeracoes:
        ind_otimos = roleta(P)
        prob_rec = 0.85

        for i in range(0, ind_otimos.shape[0]-1, 2):
            recombinacao_dois_pontos(ind_otimos, i, prob_rec)

        pass
        
        for i in range(ind_otimos.shape[0]):
            mutacao(ind_otimos, i)

        pass

        # guardar o melhor indivíduo da população atual:
        for i in range(0, ind_otimos.shape[0]):
            temp = f(ind_otimos[i])
            if (temp > melhor_aptidao):
                melhor_aptidao = temp
                melhor_individuo = ind_otimos[i]
        
        pass
        
        # a nova população
        P = ind_otimos.copy(order='F')
        
        geracao_atual += 1
        #pass
        if geracao_atual % 100 == 0:
            print(f'melhor aptidão {melhor_aptidao} da geração {geracao_atual}')
   
    if melhor_aptidao == 28:
        if (len(solucoes) == 0):
            solucoes.append(melhor_individuo)
            quantidade_solucoes += 1
        tai = False # taí? = está aí?
        for ind in solucoes:
            if ind is melhor_individuo:
               tai = True
        if tai == False:
            solucoes.append(melhor_individuo)
            quantidade_solucoes += 1
    print('length:',len(solucoes),'//array:',solucoes)

tempo = time.time() - tempo
print(tempo)