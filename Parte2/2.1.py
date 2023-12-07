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

# Definindo a população inicial aleatoriamente
P = np.random.uniform(low=0, high=2, size=(20, 20)).astype(int)
print(type(P))
# Quantidade máxima de gerações
nMaxGeracoes = 1000
# ==========================================================================================================
# FUNÇÃO OBJETIVO - OBJETIVO: MAXIMIZAR F(X), OU SEJA, MINIMIZAR H
# ==========================================================================================================
individuo = [5, 1, 4, 2, 6, 1, 4, 7] # TESTE DELETAR DEPOIS
#individuo = [4, 0, 3, 1, 5, 0, 3, 6] # TESTE DELETAR DEPOIS

# x = elemento
def f(x):
    return 28 - h(x)

# função aptidão
def h(x: list):
    # criar um algoritmo para identificar os pares atacantes
    tab = criar_tabuleiro(x)
    quant_pares_atacantes = procurar_pares_atacantes(tab, x)
    print(quant_pares_atacantes)
    print(tab)

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

#DEBUG
h(individuo)

# ==========================================================================================================
# SELEÇÃO
# ==========================================================================================================

# ==========================================================================================================
# RECOMBINAÇÃO
# ==========================================================================================================

# ==========================================================================================================
# MUTAÇÃO
# ==========================================================================================================

