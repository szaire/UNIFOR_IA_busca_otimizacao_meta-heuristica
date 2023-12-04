import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(
    ax, 
    x_otimo, f_otimo, f,
    x_limite_superior, x_limite_inferior,
    y_limite_superior, y_limite_inferior, 
    minimizacao_ou_maximizacao: bool = 1,
    epslon=5, nMaxIteracoes=100, nMaxVizinhos=10
):
    i = 0
    melhoria = True
    while i < nMaxIteracoes and melhoria:
        melhoria = False

        for j in range(nMaxVizinhos):
            x_candidato = np.random.uniform(low=x_otimo - epslon, high=x_otimo + epslon)

            if (x_candidato[0, 0] > x_limite_superior): 
                x_candidato[0, 0] = x_limite_superior
            if (x_candidato[1, 0] > y_limite_superior):
                x_candidato[1, 0] = y_limite_superior
            if (x_candidato[0, 0] < x_limite_inferior): 
                x_candidato[0, 0] = x_limite_inferior
            if (x_candidato[1, 0] < y_limite_inferior):
                x_candidato[1, 0] = y_limite_inferior

            F = f(x_candidato[0, 0], x_candidato[1, 0])
            
            if minimizacao_ou_maximizacao == 1:
                if F > f_otimo:
                    x_otimo = x_candidato
                    f_otimo = F
                    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
                    melhoria = True
                    break
            else:
                if F < f_otimo:
                    x_otimo = x_candidato
                    f_otimo = F
                    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
                    melhoria = True
                    break
        i += 1
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=500, linewidths=3, color='green', zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


# TODO: Tem algum problema aqui, veririficar com Cirilo
def busca_aleatoria_local(
    ax, 
    x_otimo, f_otimo, f,
    x_limite_superior, x_limite_inferior,
    y_limite_superior, y_limite_inferior,
    minimizacao_ou_maximizacao: bool = 1,
    nMaxIteracoes=100, sigma=0.01
):
    historico_solucoes_otimas = [f_otimo]
    
    for i in range(nMaxIteracoes):
        n = np.random.normal(loc=0, scale=sigma)
        x_candidato = x_otimo + n

        if (x_candidato[0, 0] > x_limite_superior): 
            x_candidato[0, 0] = x_limite_superior
        if (x_candidato[1, 0] > y_limite_superior):
            x_candidato[1, 0] = y_limite_superior
        if (x_candidato[0, 0] < x_limite_inferior): 
            x_candidato[0, 0] = x_limite_inferior
        if (x_candidato[1, 0] < y_limite_inferior):
            x_candidato[1, 0] = y_limite_inferior
    
        F = f(x_candidato[0, 0], x_candidato[1, 0])

        historico_solucoes_otimas.append(f_otimo)

        if minimizacao_ou_maximizacao == 1:
            if F > f_otimo:
                x_otimo = x_candidato
                f_otimo = F
                ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
        else:
            if F < f_otimo:
                x_otimo = x_candidato
                f_otimo = F
                ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=500, linewidths=3, color='green', zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


def busca_aleatoria_global(
    ax, 
    x_otimo, f_otimo, f,
    x_limite_superior, x_limite_inferior,
    y_limite_superior, y_limite_inferior,
    minimizacao_ou_maximizacao: bool = 1,
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
        
        if (x_candidato[0, 0] > x_limite_superior): 
            x_candidato[0, 0] = x_limite_superior
        if (x_candidato[1, 0] > y_limite_superior):
            x_candidato[1, 0] = y_limite_superior
        if (x_candidato[0, 0] < x_limite_inferior): 
            x_candidato[0, 0] = x_limite_inferior
        if (x_candidato[1, 0] < y_limite_inferior):
            x_candidato[1, 0] = y_limite_inferior

        F = f(x_candidato[0, 0], x_candidato[1, 0])

        historico_solucoes_otimas.append(f_otimo)

        if minimizacao_ou_maximizacao == 1:
            if F > f_otimo:
                x_otimo = x_candidato
                f_otimo = F
                ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
        else:
            if F < f_otimo:
                x_otimo = x_candidato
                f_otimo = F
                ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=500, linewidths=3, color='green', zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()


def tempera_simulada(
    ax, 
    x_otimo, f_otimo, f,
    T,
    x_limite_superior, x_limite_inferior,
    y_limite_superior, y_limite_inferior,
    minimizacao_ou_maximizacao: bool = 1,
    nMaxIteracoes=100, sigma=0.01
):
    i = 0
    while i < nMaxIteracoes:
        n = np.random.uniform(low=x_limite_inferior, high=x_limite_superior)

        x_candidato = x_otimo + n

        if (x_candidato[0, 0] > x_limite_superior): 
            x_candidato[0, 0] = x_limite_superior
        if (x_candidato[1, 0] > y_limite_superior):
            x_candidato[1, 0] = y_limite_superior
        if (x_candidato[0, 0] < x_limite_inferior): 
            x_candidato[0, 0] = x_limite_inferior
        if (x_candidato[1, 0] < y_limite_inferior):
            x_candidato[1, 0] = y_limite_inferior

        F = f(x_candidato[0, 0], x_candidato[1, 0])

        # if minimizacao_ou_maximizacao == 1:
        #     Pij = np.exp(-((f(x_candidato[0, 0], x_candidato[1, 0]) + f(x_otimo[0,0], x_otimo[1,0]))/T))
        # else:
        Pij = np.exp(-((f(x_candidato[0, 0], x_candidato[1, 0]) - f(x_otimo[0,0], x_otimo[1,0]))/T))
        
        distribuicao = np.random.uniform(low=0, high=1)

        
        if minimizacao_ou_maximizacao == 1:
            if (F > f_otimo):
                x_otimo = x_candidato
                f_otimo = F
            elif (Pij <= distribuicao):
                x_otimo = x_candidato
                f_otimo = F
        else:
            if (F < f_otimo):
                x_otimo = x_candidato
                f_otimo = F
            elif (Pij >= distribuicao):
                x_otimo = x_candidato
                f_otimo = F
            
        
        ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='o', s=90, linewidths=3, color='k')
        i += 1
        
        
        if minimizacao_ou_maximizacao == 1:
            T = T * 1.8
        else:
            T = T * 0.8
    ax.scatter(x_otimo[0], x_otimo[1], f_otimo, marker='x', s=500, linewidths=3, color='green', zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_title('f(x1,x2)')
    plt.tight_layout(); plt.show()