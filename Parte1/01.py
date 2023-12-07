# importando bibliotecas
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# importando métodos
from algoritmos import hill_climbing
from algoritmos import busca_aleatoria_local
from algoritmos import busca_aleatoria_global
from algoritmos import tempera_simulada
from algoritmos import print_3d_graph

# APLICAR FUNÇÕES
# ==========================================================================================================
# FUNÇÃO OBJETIVO
# ==========================================================================================================
def f(x1, x2):
    return (x1**2 + x2**2)
# ==========================================================================================================
# DEFININDO OS PARÂMETROS
# ==========================================================================================================
ls = 100
li = -100


x1 = np.linspace(li, ls, num=1000)

X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)

x_otimo = np.array([
    [100],
    [100]
])

f_otimo = f(x_otimo[0,0], x_otimo[1,0])
# ==========================================================================================================
# DEFININDO O GRÁFICO
# ==========================================================================================================
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')
ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=90, linewidths=3, color='red')
# ==========================================================================================================
# RESOLUÇÃO
# ==========================================================================================================
VETOR_hill_climbing = []
VETOR_busca_aleatoria_local = []
VETOR_busca_aleatoria_global = []
VETOR_tempera_simulada = []
for i in range(1000000):
    VETOR_hill_climbing.append(hill_climbing(ax, x_otimo, f_otimo, f, ls, li, ls, li, -1))
    VETOR_busca_aleatoria_local.append(busca_aleatoria_local(ax, x_otimo, f_otimo, f, ls, li, ls, li, -1, sigma=10))
    VETOR_busca_aleatoria_global.append(busca_aleatoria_global(ax, x_otimo, f_otimo, f, ls, li, ls, li, -1))
    VETOR_tempera_simulada.append(tempera_simulada(ax, x_otimo, f_otimo, f, 10, ls, li, ls, li, -1))

MODA_hill_climbing = stats.mode(VETOR_hill_climbing)
MODA_busca_aleatoria_local = stats.mode(VETOR_busca_aleatoria_local)
MODA_busca_aleatoria_global = stats.mode(VETOR_busca_aleatoria_global)
MODA_tempera_simulada = stats.mode(VETOR_tempera_simulada)

print(MODA_hill_climbing)
print(MODA_busca_aleatoria_local)
print(MODA_busca_aleatoria_global)
print(MODA_tempera_simulada)
