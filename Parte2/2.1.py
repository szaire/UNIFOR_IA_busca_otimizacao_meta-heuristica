# TODOs:
# 1. Fa¸ca a defini¸c˜ao da quantidade N de indiv´ıduos em uma popula¸c˜ao e quantidade m´axima de gera¸c˜oes.
# 2. Projete o operador de sele¸c˜ao, baseado no m´etodo da roleta.
# 3. Na etapa de recombina¸c˜ao, escolha um entre os seguintes operadores: Recombina¸c˜ao de um ponto ou
# Recombina¸c˜ao de dois pontos. A probabilidade de recombina¸c˜ao nesta etapa deve ser entre 85 < pc < 95%.
# 4. Na prole gerada, deve-se aplicar a muta¸c˜ao com probabilidade de 1% (neste caso, ´e interessante avaliar os
# diferentes procedimentos exibidos).
# 5. O algoritmo deve parar quando atingir o m´aximo n´umero de gera¸c˜oes ou quando a fun¸c˜ao custo atingir seu valor
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

# Quantidade máxima de gerações
nMaxGerações = 1000
# ==========================================================================================================
# FUNÇÃO OBJETIVO - OBJETIVO: MAXIMIZAR F(X), OU SEJA, MINIMIZAR H
# ==========================================================================================================
def f(x):
    return x 
# ==========================================================================================================
# DEFININDO OS PARÂMETROS
# ==========================================================================================================

# ==========================================================================================================
# DEFININDO O GRÁFICO
# ==========================================================================================================

# ==========================================================================================================
# PROBLEMA DO DOMÍNIO DISCRETO
# ==========================================================================================================

