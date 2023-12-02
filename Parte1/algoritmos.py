import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(
    ax, 
    x_otimo, f_otimo, f, 
    epslon=5, nMaxIteracoes=100, nMaxVizinhos=10
):
    i = 0
    melhoria = True
    while i < nMaxIteracoes and melhoria:
        melhoria = False

        for j in range(nMaxVizinhos):
            x_candidato = np.random.uniform(low=x_otimo - epslon, high=x_otimo + epslon)
            F = f(x_candidato[0, 0], x_candidato[1, 0])

            if F < f_otimo:
                x_otimo = x_candidato
                f_otimo = F
                ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
                melhoria = True
                break
        i += 1
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='1', s=90, linewidths=3, color='green')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


# TODO: Tem algum problema aqui, veririficar com Cirilo
def busca_aleatoria_local(
    ax, 
    x_otimo, f_otimo, f,
    x_limite_superior,
    nMaxIteracoes=100, sigma=0.01
):
    historico_solucoes_otimas = [f_otimo]
    
    for i in range(nMaxIteracoes):
        n = np.random.normal(loc=0, scale=sigma)
        x_candidato = x_otimo + n

        if (x_candidato[0, 0] > x_limite_superior and x_candidato[1, 0] > x_limite_superior):
            x_candidato = np.array([
                [x_limite_superior],
                [x_limite_superior]
            ])

        f_candidato = f(x_candidato[0, 0], x_candidato[1, 0])

        historico_solucoes_otimas.append(f_otimo)

        if f_candidato < f_otimo:
            x_otimo = x_candidato
            f_otimo = f_candidato
            ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='1', s=90, linewidths=3, color='green')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


def busca_aleatoria_global(
    ax, 
    x_otimo, f_otimo, f,
    x_limite_inferior, x_limite_superior,
    nMaxIteracoes=100, sigma=0.01
):
    historico_solucoes_otimas = [f_otimo]
    
    for i in range(nMaxIteracoes):
        random_x1 = np.random.uniform(x_limite_inferior, x_limite_superior) 
        random_x2 = np.random.uniform(x_limite_inferior, x_limite_superior) 
        x_candidato = np.array([
                [random_x1],
                [random_x2]
            ])

        if (x_candidato[0, 0] > x_limite_superior and x_candidato[1, 0] > x_limite_superior):
            x_candidato = np.array([
                [x_limite_superior],
                [x_limite_superior]
            ])

        f_candidato = f(x_candidato[0, 0], x_candidato[1, 0])

        historico_solucoes_otimas.append(f_otimo)

        if f_candidato < f_otimo:
            x_otimo = x_candidato
            f_otimo = f_candidato
            ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='1', s=90, linewidths=3, color='green')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


def tempera_simulada():
    