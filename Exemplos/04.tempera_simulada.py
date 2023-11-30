import numpy as np
import matplotlib.pyplot as plt

# 1.1) Declaração do número máximo de iterações
nMaxIteracoes = 100

# 1.2) TODO: Declaração de T. Temperatura inicial da temperta. 
# Quanto mais alto as particulas estão sendo atiçadas com mais intensidade
# Quanto mais baixo, menos intensidade 
T = 100

def f(x):
    return x**2
    pass

# 2.1) Definir limite inferior
limite_inferior = -5
# 2.2) Definir limite superior
limite_superior = 5

# 3) TODO: Declaração do sigma. Perturbação inicial do modelo
sigma = 0.1

# Extra: Criando e plotando o gráfico
eixo_x = np.linspace(limite_inferior, limite_superior, 100)
plt.plot(eixo_x, f(eixo_x))


# 4) Declarando x ótimo
x_otimo = np.array([-2])
# 5) Declarando f ótimo
f_otimo = f(x_otimo)
# 6) Declarando i (iterações)
i = 0

# Extra: adicionando um ponto de acordo com o cálculo de x e f ótimos
plt.scatter(x_otimo, f_otimo, color='red', s=90)

# 7) Loop While
while i < nMaxIteracoes:
    n = np.random.uniform(low=limite_inferior, high=limite_superior)
    
    x_candidato = x_otimo + n
    
    # Verificar a violação da restrição em caixa
    f_candidato = f(x_candidato)

    # DEclaração de Pij
    Pij = np.exp(-((f(x_candidato) - f(x_otimo))/T))
    
    # o algoritmo aceita as soluções ótimas...
    distribuicao = np.random.uniform(low=0, high=1)
    if (f_candidato < f_otimo):
        x_otimo = x_candidato
        f_otimo = f_candidato
    # e aceita os não ótimos por essas condições
    elif (Pij >= distribuicao):
        x_otimo = x_candidato
        f_otimo = f_candidato
    
    plt.scatter(x_otimo, f_otimo, color='orange', s=90)
    
    i += 1
    
    T = T * 0.8
    
    # plt.pause(0.01)

plt.scatter(x_otimo, f_otimo, color='green', s=90)
plt.show()