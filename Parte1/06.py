import numpy as np
import matplotlib.pyplot as plt

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
    return (x1 * np.sin(4 * np.pi * x1)) - (x2 * np.sin((4 * np.pi * x2) + np.pi)) + 1
# ==========================================================================================================
# DEFININDO OS PARÂMETROS
# ==========================================================================================================
ls = 3
li = -1

num = 1000

x1 = np.linspace(li, ls, num)
x2 = np.linspace(li, ls, num)

X1, X2 = np.meshgrid(x1, x2)

Y = f(X1, X2)

x_otimo = np.array([
    [0],
    [0]
])

f_otimo = f(x_otimo[0, 0], x_otimo[1, 0])
# ==========================================================================================================
# DEFININDO O GRÁFICO
# ==========================================================================================================
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')
ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=90, linewidths=3, color='red')
# ==========================================================================================================
# HILL CLIMBING
# ==========================================================================================================
# hill_climbing(ax, x_otimo, f_otimo, f, ls, li, ls, li, epslon=5)
# ==========================================================================================================
# BUSCA ALEATÓRIA LOCAL
# ==========================================================================================================
# busca_aleatoria_local(ax, x_otimo, f_otimo, f, ls, li, ls, li, sigma=1) # TODO: Verificar se algoritmo está realmente funcionando
# ==========================================================================================================
# BUSCA ALEATÓRIA GLOBAL
# ==========================================================================================================
# busca_aleatoria_global(ax, x_otimo, f_otimo, f, ls, li, ls, li, sigma=0.01)
# ==========================================================================================================
# TÊMPERA SIMULADA
# ==========================================================================================================
# tempera_simulada(ax, x_otimo, f_otimo, f, 5, ls, li, ls, li, sigma=0.01) # TODO: Não consigo procurar o menor ponto

print_3d_graph(ax)