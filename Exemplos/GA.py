import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Método do torneio
def torneio(P, tamanho_torneio = 2):
    S = np.empty((0, P.shape[1]))

    while S.shape[0] != P.shape[0]:
        # Seleciona dois indivíduos aleatórios da população para se enfrentarem no torneio
        selecionado = np.random.uniform(0, P.shape[0], size=(tamanho_torneio)).astype(int)
        
        x1 = P[selecionado[0],:]
        x2 = P[selecionado[1],:]
        
        x1_real = decodificador(x1, -1, 2)
        x2_real = decodificador(x2, -1, 2)

        if (f(x1_real) > f(x2_real)):
            S = np.concatenate((S, x1.reshape(1, P.shape[1])))
        else:
            S = np.concatenate((S, x2.reshape(1, P.shape[1])))
    
    return S


def decodificador(x, li, ls):
    somatorio = 0
    for l in range(len(x)):
        somatorio += 2**l*x[len(x)-1-l]
    return li + ((li - ls)/(2**len(x)-1))*somatorio

def f(x):
    x*np.sin(x*np.pi*10)+1

# Definindo a população inicial aleatoriamente
P = np.random.uniform(low=0, high=2, size=(20, 20)).astype(int)

li, ls = -1, 2 # limite inferior e superior

# todas as aptidões definidas em um vetor
P_real = np.array([decodificador(P[i,:], li, ls) for i in range(P.shape[0])]) #define seu valor no eixo x em número real
Aptidao = f(P_real) # define seu valor no eixo y

# Dica
S = np.copy(torneio(P))

x_axis = np.linspace(-1, 2, 1000)
plt.scatter
plt.xlim
plt.plot(x_axis, f(x_axis))

# Método do Torneio