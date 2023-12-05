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
    return np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))
# ==========================================================================================================
# DEFININDO OS PARÂMETROS
# ==========================================================================================================
x_ls = 5
x_li = -2

y_ls = 4
y_li = -2

num = 1000

x1 = np.linspace(x_li, x_ls, num)
x2= np.linspace(y_li, y_ls, num)
X1, X2 = np.meshgrid(x1, x2)

Y = f(X1, X2)

x_otimo = np.array([
    [-2],
    [-2]
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
#hill_climbing(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, epslon=5, nMaxVizinhos=200)
# ==========================================================================================================
# BUSCA ALEATÓRIA LOCAL
# ==========================================================================================================
# busca_aleatoria_local(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, sigma=0.1)
# ==========================================================================================================
# BUSCA ALEATÓRIA GLOBAL
# ==========================================================================================================
# busca_aleatoria_global(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, sigma=1)
# ==========================================================================================================
# TÊMPERA SIMULADA
# ==========================================================================================================
tempera_simulada(ax, x_otimo, f_otimo, f, 10, x_ls, x_li, y_ls, y_li, sigma=1)

print_3d_graph(ax)