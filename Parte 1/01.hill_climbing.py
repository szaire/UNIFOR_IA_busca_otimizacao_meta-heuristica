import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-(x**2))

eixo_x = np.linspace(-2, 2, 100)
plt.plot(eixo_x, f(eixo_x))

x_otimo = np.array([-2])
f_otimo = f(x_otimo)
epslon = .1

nMaxIteracoes = 100
nMaxVizinhos = 10

i = 0
melhoria = True
plt.scatter(x_otimo, f_otimo, color='pink', s=90)
plt.pause(.01)

while i < nMaxIteracoes and melhoria:
  melhoria = False

  for j in range(nMaxVizinhos):
    x_candidato = np.random.uniform(low=x_otimo-epslon, high=x_otimo+epslon) # Perturbação do ótimo
    # - Perturbação = uma variação de um x previamente obtido. 
    # Valores para além dos limites estabelecidos serão reajustados
    F = f(x_candidato)

    if (F > f_otimo):
      x_otimo = x_candidato
      f_otimo = F
      plt.scatter(x_otimo, f_otimo, color='purple', s=90)
      plt.pause(0.1)
      melhoria = True
      break
  
  i += 1

plt.scatter(x_otimo, f_otimo, marker='1', color='green', s=130, linewidth=5)
plt.show()