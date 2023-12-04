import numpy as np
import matplotlib.pyplot as plt

from algoritmos import hill_climbing
from algoritmos import busca_aleatoria_local
from algoritmos import busca_aleatoria_global
from algoritmos import tempera_simulada

# APLICAR FUNÇÕES
# ==========================================================================================================
# FUNÇÃO OBJETIVO
# ==========================================================================================================
def f(x1, x2):
    return (x1 - 1)**2 + (100 * (x2 - x1**2)**2)
# ==========================================================================================================
# DEFININDO OS PARÂMETROS
# ==========================================================================================================
x_ls = 2
x_li = -2

y_ls = 3
y_li = -1

num = 1000

x1 = np.linspace(-2, 2, num)
x2 = np.linspace(-1, 3, num)

X1, X2 = np.meshgrid(x1, x2)

Y = f(X1, X2)

x_otimo = np.array([
    [2],
    [-1]
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
# hill_climbing(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, -1, epslon=0.1)
# ==========================================================================================================
# BUSCA ALEATÓRIA LOCAL
# ==========================================================================================================
# busca_aleatoria_local(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, -1, sigma=0.01) # TODO: Verificar se algoritmo está realmente funcionando
# ==========================================================================================================
# BUSCA ALEATÓRIA GLOBAL
# ==========================================================================================================
# busca_aleatoria_global(ax, x_otimo, f_otimo, f, x_ls, x_li, y_ls, y_li, -1, sigma=0.01)
# ==========================================================================================================
# TÊMPERA SIMULADA
# ==========================================================================================================
tempera_simulada(ax, x_otimo, f_otimo, f, 10, x_ls, x_li, y_ls, y_li, -1, nMaxIteracoes=100, sigma=0.01) # TODO: Não consigo procurar o menor ponto