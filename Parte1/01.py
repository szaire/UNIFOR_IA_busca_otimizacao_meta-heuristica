# importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# TODO: Como adaptar as funções deuma funcao 2d para uma 3d?

# FUNÇÃO OBJETIVO
# =====================================================
def f(x1, x2):
    return (x1**2 + x2**2)

# DEFININDO AS DIMENSÕES
# =====================================================
ls = 100
li = -100

x1 = np.linspace(li, ls, num=1000)
X1, X2 = np.meshgrid(x1, x1)

Y = f(X1, X2)

p0, p1 = 100, 100

x_otimo = np.array([
    [100],
    [100]
])

#x1_candidato, x2_candidato = p0, p1

f_otimo = f(x_otimo[0,0], x_otimo[1,0])

# DEFININDO O GRÁFICO
# =====================================================
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')
ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=90, linewidths=3, color='red')

# APLICAR FUNÇÃO
# ==============

epslon = 5

nMaxIteracoes = 100
nMaxVizinhos = 10

i = 0
melhoria = True

while i < nMaxIteracoes and melhoria:
  melhoria = False

  for j in range(nMaxVizinhos):
    x_candidato = np.random.uniform(low=x_otimo-epslon, high=x_otimo+epslon) # Perturbação do ótimo
    # - Perturbação = uma variação de um x previamente obtido. 
    # Valores para além dos limites estabelecidos serão reajustados
    F = f(x_candidato[0,0],  x_candidato[1,0])

    if (F < f_otimo):
      x_otimo = x_candidato
      f_otimo = F
      
      ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='purple')
      
      melhoria = True
      break
  
  i += 1

ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='1', s=90, linewidths=3, color='green')

# ==============

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x1,x2)')
plt.tight_layout()
plt.show()
