# importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# importando métodos
from algoritmos import hill_climbing
from algoritmos import busca_aleatoria_local
from algoritmos import busca_aleatoria_global
from algoritmos import tempera_simulada

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
# HILL CLIMBING
# ==========================================================================================================
# hill_climbing(ax, x_otimo, f_otimo, f, -1)
# ==========================================================================================================
# BUSCA ALEATÓRIA LOCAL
# ==========================================================================================================
# busca_aleatoria_local(ax, x_otimo, f_otimo, f, ls, -1) # TODO: Verificar se algoritmo está realmente funcionando
# ==========================================================================================================
# BUSCA ALEATÓRIA GLOBAL
# ==========================================================================================================
# busca_aleatoria_global(ax, x_otimo, f_otimo, f, li, ls, -1)
# ==========================================================================================================
# TÊMPERA SIMULADA
# ==========================================================================================================
tempera_simulada(ax, x_otimo, f_otimo, f, 100, li, ls, -1)