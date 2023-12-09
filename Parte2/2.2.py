# em um indivíduo nao pode ter genes iguais
# utilizar recombinação para gerar novos filhos
import numpy as np
import matplotlib.pyplot as plt
import random

#1. Fa¸ca a defini¸c˜ao de quantos pontos devem ser gerados por regi˜ao. Escolha um valor 30 < Npontos < 60.

def distance(p1,p2):    
    return np.sqrt(np.sum((p1-p2)**2))
def generate_points(N): 
    # cria 4 grupos, e dentro de 4 grupos coloca N pontos
    x_partition = np.random.uniform(-10, 10, size=(N,3))
    y_partition = np.random.uniform(0, 20, size=(N,3))
    z_partition = np.random.uniform(-20, 0, size=(N,3))
    w_partition = np.random.uniform(0, 20, size=(N,3))

    x1 = np.array([[20,-20,-20]])
    x1 = np.tile(x1,(N,1))
    x_partition = x_partition+x1

    x1 = np.array([[-20,20,20]])
    x1 = np.tile(x1,(N,1))
    y_partition = y_partition+x1

    x1 = np.array([[-20,20,-20]])
    x1 = np.tile(x1,(N,1))
    z_partition = z_partition+x1

    x1 = np.array([[20,20,-20]])
    x1 = np.tile(x1,(N,1))
    w_partition = w_partition+x1   
    # retorna um vetor com 4*N pontos
    return np.concatenate((x_partition,y_partition,z_partition,w_partition), axis=0)

# 8 pontos por agrupamento, total de 32 pontos
K = 3
points = generate_points(K)
I = np.random.permutation(K*4) #gera um vetor com 32 elementos aleatorios
inicial = I[0] #escolhe um ponto aleatorio para ser o ponto de origem
p_origem = points[inicial,:].reshape(1,3) 
points = np.delete(points,inicial,axis=0) #remove o ponto de origem da lista de pontos pois ele nao pode ser visitado novamente
taxa_recombinacao = .95
n_points = K*4-1 #numero de pontos que podem ser visitados


#2. Fa¸ca a defini¸c˜ao da quantidade N de indiv´ıduos em uma popula¸c˜ao e quantidade m´axima de gera¸c˜oes
Populacao = np.empty((0,points.shape[0]), dtype=int)
N = 50 #tamanho da pop., hiperparametro
for i in range(N): 
    #gera um individuo aleatorio
    individuo = np.random.permutation(points.shape[0]).reshape(1,points.shape[0])
    # transformar float em int
    individuo = individuo.astype(int)
    #concatena o individuo na populacao
    Populacao = np.concatenate((Populacao,individuo))

#concatena o ponto de origem no inicio e no fim de cada individuo
vetor_origem = np.tile(np.array([[int(inicial)]]),(N,1))

# seleção dos pais - torneio
# é calculada a aptidão para cada um dos dois, o que obtiver a melhor aptidão é escolhido como pai, porém, como o problema é de minimização (caminho mais curto), o que obtiver a menor aptidão é escolhido como pai
Populacao_aux = np.empty((0,points.shape[0]), dtype=int)

# cada vez que entra no for, é feita a seleção de 2 pais, e a recombinação deles, gerando 2 filhos
for i in range(N//2):
    individuo_aleatorio_1 = Populacao[np.random.randint(0,N),:]
    individuo_aleatorio_2 = Populacao[np.random.randint(0,N),:]
    individuo_aleatorio_3 = Populacao[np.random.randint(0,N),:]
    individuo_aleatorio_4 = Populacao[np.random.randint(0,N),:]


    # fazendo o calculo da aptidao com os 2 pares de pais para escolher o melhor par
    def calcula_aptidao(individuo_aleatorio):
        gene_1 = individuo_aleatorio[0]
        soma = 0
        # calcular a distância entre todos os pontos
        for gene_2 in individuo_aleatorio[1:]:
            soma += distance(points[gene_1,:],points[gene_2,:])
            gene_1 = gene_2
        return soma
        
    # calcula aptidao do individuo 1 e 2 e escolhe o  que tiver menor aptidao
    aptidao_1 = calcula_aptidao(individuo_aleatorio_1)
    aptidao_2 = calcula_aptidao(individuo_aleatorio_2)

    if aptidao_1 < aptidao_2:
        pai_1 = individuo_aleatorio_1
    else:
        pai_1 = individuo_aleatorio_2 
        
    # calcula aptidao do individuo 3 e 4 e escolhe o  que tiver menor aptidao
    aptidao_3 = calcula_aptidao(individuo_aleatorio_3)
    aptidao_4 = calcula_aptidao(individuo_aleatorio_4)

    if aptidao_3 < aptidao_4:
        pai_2 = individuo_aleatorio_3
    else:
        pai_2 = individuo_aleatorio_4
    
    # recombinação
    # não pode haver genes iguais no filho, então, é feito um mapeamento dos genes do pai 1 para o filho, e os genes do pai 2 que não estão no filho são adicionados ao filho
    print("Pai 1: ",pai_1)
    print("Pai 2: ",pai_2)
    def recombinacao_dois_pontos(pai_1, pai_2):
        
        # se a taxa de recombinação for menor que o valor gerado , retorna os pais pois não haverá recombinação
        if random.random() > taxa_recombinacao:
            return [pai_1, pai_2]

        ponto_1 = random.randint(1, n_points)
        ponto_2 = random.randint(1, n_points)
        while ponto_1 == ponto_2:
            ponto_2 = random.randint(0, n_points)

        if ponto_1 > ponto_2:
            aux = ponto_1
            ponto_1 = ponto_2
            ponto_2 = aux

        # sem numpy:
        #aux_2 = direita do ponto_2 do pai_2 + esquerda do ponto_1 do pai_2 + meio do pai 2
        #aux_2 = pai_2[ponto_2:n_points] + pai_2[0:ponto_1] + pai_2[ponto_1:ponto_2]

        #aux_1 = direita do ponto_2 do pai_1 + esquerda do ponto_1 do pai_1 + meio do pai 1
        #aux_1 = pai_1[ponto_2:n_points] + pai_1[0:ponto_1] + pai_1[ponto_1:ponto_2]

        #filho_1 = [None] * n_points
        #filho_2 = [None] * n_points
        
        # com numpy:
        aux_2 = np.concatenate((pai_2[ponto_2:n_points],pai_2[0:ponto_1],pai_2[ponto_1:ponto_2]))
        aux_1 = np.concatenate((pai_1[ponto_2:n_points],pai_1[0:ponto_1],pai_1[ponto_1:ponto_2]))
        filho_1 = np.empty((1,n_points), dtype=int)
        filho_2 = np.empty((1,n_points), dtype=int)

    #coloca os meios
        for i in range(ponto_1, ponto_2):
            #sem numpy:
            #filho_1[i] = pai_2[i]
            #filho_2[i] = pai_1[i]
            
            #com numpy:
            filho_1[0,i] = pai_2[i]
            filho_2[0,i] = pai_1[i]
    

        posAux_1 = 0
        posAux_2 = 0
        # coloca o final
        for i in range(ponto_2, n_points):
            while aux_1[posAux_1] in filho_1:
                posAux_1 += 1
            
            #sem numpy:
            #filho_1[i] = aux_1[posAux_1]
            # com numpy:
            filho_1[0,i] = aux_1[posAux_1]
            while aux_2[posAux_2] in filho_2:
                posAux_2 += 1
            #sem numpy:
            #filho_2[i] = aux_2[posAux_2]
            # com numpy:
            filho_2[0,i] = aux_2[posAux_2]

    #coloca o inicio
        for i in range(0, ponto_1):
            while aux_1[posAux_1] in filho_1:
                posAux_1 += 1
            #sem numpy:
            #filho_1[i] = aux_1[posAux_1]
            # com numpy:
            filho_1[0,i] = aux_1[posAux_1]
            while aux_2[posAux_2] in filho_2:
                posAux_2 += 1
            #sem numpy:
            #filho_2[i] = aux_2[posAux_2]
            # com numpy:
            filho_2[0,i] = aux_2[posAux_2]
        #retorna cromossomo
        return [filho_1, filho_2]

    filhos = recombinacao_dois_pontos(pai_1, pai_2)
    print("Filhos: ",filhos)

    # vamos colocar os filhos na população nova
    Populacao_aux = np.concatenate((Populacao_aux,filhos[0],filhos[1]))

#essa matriz pode ser utilizado para aptidao:
caminhos = np.concatenate((vetor_origem,Populacao,vetor_origem),axis=1)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#plota os pontos e a origem 
ax.scatter(points[:,0], points[:,1], points[:,2], c='#248DD2', marker='o')
ax.scatter(p_origem[0:,0], p_origem[0:,1], p_origem[0:,2], c='green', marker='x',linewidth=3,s=30)


#exemplo caminho a partir da origem.
p2 = points[0,:].reshape(1,3)
#plota a linha que liga a origem ao ponto
line, = ax.plot([p_origem[0,0],p2[0,0]],[p_origem[0,1],p2[0,1]],[p_origem[0,2],p2[0,2]],color='k')

plt.tight_layout()
plt.show()

