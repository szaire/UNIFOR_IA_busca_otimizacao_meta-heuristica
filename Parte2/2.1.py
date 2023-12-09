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
    tab = criar_tabuleiro(x)
    quant_pares_atacantes = procurar_pares_atacantes(tab, x)
    return quant_pares_atacantes

def procurar_pares_atacantes(tab: np.ndarray, x: list):
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
def roleta(P):
    somatorio_den_pi = 0
    for ind in P:
        somatorio_den_pi += f(ind)
    
    individuos_otimos = np.empty((0,P.shape[1]))
    for _ in range(len(P)):
        i = 0
        # r ~ U(0, 1)
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
    xi1 = int(np.random.uniform(low=1, high=len(P[0]) - 2))
    xi2 = int(np.random.uniform(low=1, high=len(P[0]) - 2))
    
    if xi1 > xi2:
        xi1, xi2 = xi2, xi1
    
    mascara = gerar_mascara(xi1, xi2)
    
    r_prob = np.random.uniform(0, 1)

    #if (r_prob < prob_recombinacao): # 0 é debug
    #    inds = np.delete(inds, index, axis=0)
    #    return 

    #for i in range(0, inds.shape[0]-1, 2):
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
melhor_individuo = None
solucoes = []
geracao_atual = 0

print(f(np.array([3, 5, 7, 2, 0, 6, 4, 1])))

while len(solucoes) < 92:
    print
    
    while melhor_aptidao != 28 and geracao_atual < nMaxGeracoes:
        ind_otimos = roleta(P)
        prob_rec = 0.85

        pass

        for i in range(0, ind_otimos.shape[0]-1, 2):
            recombinacao_dois_pontos(ind_otimos, i, prob_rec)

        pass

        for i in range(ind_otimos.shape[0]):
            mutacao(ind_otimos, i)

        # guardar o melhor indivíduo da população atual:
        for i in range(1, ind_otimos.shape[0]):
            temp = f(ind_otimos[i])
            if (temp > melhor_aptidao):
                melhor_aptidao = temp
                melhor_individuo = ind_otimos[i]
        
        pass
        # a nova população
        P = ind_otimos

        geracao_atual += 1
        #pass

    if melhor_aptidao == 28:
        if not melhor_individuo in solucoes:
            solucoes.append(melhor_individuo)
        print('😇terminou rodada com um indivíduo ótimo\ngeração atual:',geracao_atual,'\nquantidade de soluções encontradas:',len(solucoes),'\n')
    else:
        print('🤬terminou rodada geração atual:',geracao_atual,'\nquantidade de soluções encontradas:',len(solucoes),'\n')


print(melhor_individuo)
print(criar_tabuleiro(melhor_individuo))
print(melhor_aptidao)

# ==========================================================================================================
# MUTAÇÃO 
# ==========================================================================================================

