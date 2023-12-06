import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f(x):
    #escreva aqui a função objetivo
    pass


eixo_x = np.linspace(limite_inferior, limite_superior, 100)
plt.plot(eixo_x, f(eixo_x))

x_otimo = np.array([-2])
f_otimo = f(x_otimo)
# declaração do hiperparâmetro

nMaxIteracoes = 100
# declaração de hiperparâmetro

i = 0
melhoria = True
plt.scatter(x_otimo, f_otimo, color='pink', s=90)
plt.pause(.01)

while i < nMaxIteracoes and melhoria:
  melhoria = False

  for j in range(nMaxVizinhos):
    x_candidato = np.random.uniform(low = x_otimo - epslon, high = x_otimo + epslon) # Perturbação do ótimo
    F = f(x_candidato)

    if (F > f_otimo):
      x_otimo = x_candidato
      f_otimo = F
      plt.scatter(x_otimo, f_otimo, color='purple', s=90)
      melhoria = True
      break

plt.scatter(x_otimo, f_otimo, color='green', s=90)
plt.show()