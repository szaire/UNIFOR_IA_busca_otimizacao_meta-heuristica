import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(np.pi*10*x)*x+1

x_axis = np.linspace(-1, 2, 1000) 

plt.plot(x_axis, f(x_axis))
plt.grid(True)
plt.xlim(-1.1, 2.1)

#LRS (LOCAL RANDOM SEARCH)

x_limite_inferior = -1
x_limite_superior = 2
sigma = 0.001 # Encontrar o menor sigma que ache o ótimo
# O resultado é a moda das soluções
# Para 100 rodadas, cada iteração contará o ponto registrado e calculará a moda final

x_otimo = np.random.uniform(low=x_limite_inferior, high=x_limite_superior)
f_otimo = f(x_otimo)
maximo_iteracoes = 1000
historico_solucoes_otimas = [f_otimo]

plt.scatter(x_otimo, f_otimo, marker='1', color='blue', s=90, linewidth=3)
for i in range(maximo_iteracoes):
  # A cada solução é gerada uma solução candidata (x_candidato) com base no ótimo atual
  # Será utilizada a perturbação com base nos limites do domínio estabelecido (n). Esta perturbação é gaussiana
  # - Perturbação = uma variação de um x previamente obtido. Valores para além dos limites estabelecidos serão reajustados
  n = np.random.normal(loc=0, scale=sigma)
  # Algoritmo aleatorio de busca global: x_candidato = np.random.uniform(x_limite_inferior, x_limite_superior)
  x_candidato = x_otimo + n # O x_candidato é uma perturbação do x_otimo

  # Verificando se o candidato feriu os limites
  if (x_candidato > x_limite_superior):
    x_candidato = x_limite_superior
  if (x_candidato > x_limite_superior):
    x_candidato = x_limite_superior

  f_candidato = f(x_candidato)
  #plt.scatter(x_candidato, -1, color='red')

  historico_solucoes_otimas.append(f_otimo)

  if (f_candidato > f_otimo):
    x_otimo = x_candidato
    f_otimo = f_candidato
    plt.scatter(x_otimo, f_otimo, color='k')

#   plt.pause(0.01)

plt.scatter(x_otimo, f_otimo, marker='1', color='green', s=90, linewidth=3)

plt.plot(historico_solucoes_otimas) # Mostra o histórico (ocorrências) de valores y de f_otimo ao longo do tempo

plt.show()