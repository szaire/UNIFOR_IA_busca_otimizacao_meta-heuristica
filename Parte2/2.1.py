# TODOs:
# DONE: 1. Fa¸ca a defini¸c˜ao da quantidade N de indiv´ıduos em uma popula¸c˜ao e quantidade m´axima de gera¸c˜oes.
# TODO: 2. Projete o operador de sele¸c˜ao, baseado no m´etodo da roleta.
# TODO: 3. Na etapa de recombina¸c˜ao, escolha um entre os seguintes operadores: Recombina¸c˜ao de um ponto ou
# Recombina¸c˜ao de dois pontos. A probabilidade de recombina¸c˜ao nesta etapa deve ser entre 85 < pc < 95%.
# TODO: 4. Na prole gerada, deve-se aplicar a muta¸c˜ao com probabilidade de 1% (neste caso, ´e interessante avaliar os
# diferentes procedimentos exibidos).
# TODO: 5. O algoritmo deve parar quando atingir o m´aximo n´umero de gera¸c˜oes ou quando a fun¸c˜ao custo atingir seu valor
# ´otimo.
# ==========================================================================================================
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# ==========================================================================================================
# DEFINIÇÕES INICIAIS
# ==========================================================================================================
# Número de pares
h = int 

n = 20

# Definindo a população inicial aleatoriamente
P = np.random.uniform(low=0, high=8, size=(n, 8)).astype(int)
# Quantidade máxima de gerações
nMaxGeracoes = 1000
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
    quant_pares_atacantes = 0
    # percorrer horizontal
    for i in range(len(x)):
        soma = sum(tab[i])
        if soma > 1:
            quant_pares_atacantes += soma            
    # percorrer diagonal superior
    i = x[0]-1
    j = 0
    while i >= 0 and i <= 7:
        if tab[i][j] == 1:
            quant_pares_atacantes += 1
        i -= 1
        j += 1
    # percorrer diagonal inferior
    i = x[0]-1
    j = 0
    while i >= 0 and i <= 7:
        if tab[i][j] == 1:
            quant_pares_atacantes += 1
        i += 1
        j += 1
    return quant_pares_atacantes
    
def criar_tabuleiro(x: list):
    temp_tab = np.zeros((8, 8))
    rows, cols = temp_tab.shape
    i_local = 0
    for j in range(cols):
        for i in range(rows):
            if i+1 == x[i_local]:
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

# RECOMBINAÇÃO (  ) 
def recombinacao_dois_pontos(ind_otimos: np.ndarray, prob_recombinacao):
    ind_novos = np.array((ind_otimos.shape))
    
    xi1 = int(np.random.uniform(low=1, high=len(P[0]) - 2))
    xi2 = int(np.random.uniform(low=1, high=len(P[0]) - 2))
    
    if xi1 > xi2:
        xi1, xi2 = xi2, xi1
    
    mascara = gerar_mascara(xi1, xi2)
    
    r_prob = np.random.uniform(0, 1)
    #if (r_prob >= prob_recombinacao):
    if (True):
        for i, j in range(ind_novos): # ERRO
            pass

    pass

def gerar_mascara(xi1, xi2):
    masc = np.zeros((len(P[0])))
    
    for j in range(xi1, xi2+1):
        masc[j] = 1
    
    return masc

ind_otimos = roleta(P)
recombinacao_dois_pontos(ind_otimos, 0.85)
# ==========================================================================================================
# RESOLUÇÃO
# ==========================================================================================================

# ======================================================================================================
selecionados = roleta(P)
# ==========================================================================================================
# MUTAÇÃO 
# ==========================================================================================================

