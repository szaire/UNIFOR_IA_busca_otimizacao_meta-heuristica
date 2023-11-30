import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(
    ax, # scatter
    epslon,
    numero_maximo_iteracoes, numero_maximo_vizinhos,
    x_candidatos
    f
    ):
    
    i = 0
    melhoria = True
    
    # Como se faria o scatter aqui?

    while i < numero_maximo_iteracoes and melhoria:
        melhoria = False

        for j in range(numero_maximo_vizinhos):
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


def busca_aleatoria_local():
    pass
def busca_aleatoria_global():
    pass
def tempera_simulada():
    pass