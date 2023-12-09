# em um indivíduo nao pode ter genes iguais
# utilizar recombinação para gerar novos filhos
import numpy as np
import matplotlib.pyplot as plt
import random
import time

tempo = time.time()
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
K = 30
points = generate_points(K)
I = np.random.permutation(K*4) #gera um vetor com 32 elementos aleatorios
inicial = I[0] #escolhe um ponto aleatorio para ser o ponto de origem
p_origem = points[inicial,:].reshape(1,3) 
points = np.delete(points,inicial,axis=0) #remove o ponto de origem da lista de pontos pois ele nao pode ser visitado novamente
taxa_recombinacao = .95
n_points = K*4-1 #numero de pontos que podem ser visitados
taxa_mutacao = .01
geracoes_max = 100000



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

def calcula_aptidao(individuo_aleatorio):
    gene_1 = individuo_aleatorio[0]
    soma = 0
    # calcular a distância entre todos os pontos
    for gene_2 in individuo_aleatorio[1:]:
        soma += distance(points[gene_1,:],points[gene_2,:])
        gene_1 = gene_2
    
    # adiciona a distancia do ultimo ponto ao ponto de origem
    soma += distance(points[gene_1,:],p_origem)
    return soma

geracao_atual = 0
melhor_atual = Populacao[0,:]
melhor_aptidao_atual = 20000
posicao_melhor = 0
elite = 2 #numero de individuos que serao mantidos na proxima geracao
while geracao_atual < geracoes_max:
    # seleção dos pais - torneio
    # é calculada a aptidão para cada um dos dois, o que obtiver a melhor aptidão é escolhido como pai, porém, como o problema é de minimização (caminho mais curto), o que obtiver a menor aptidão é escolhido como pai
    Populacao_aux = np.empty((0,points.shape[0]), dtype=int)
    
    Populacao_elite = np.empty((0,points.shape[0]), dtype=int)
    aptidao_auxiliar = [None] * elite 
    for i in range(N):
        aptidao_temporaria = calcula_aptidao(Populacao[i,:])
        # se a aptidao auxiliar tiver algum elemento vazio, coloca o individuo na posicao vazia
        if None in aptidao_auxiliar:
            posicao_vazia = aptidao_auxiliar.index(None)
            aptidao_auxiliar[posicao_vazia] = aptidao_temporaria
            Populacao_elite = np.concatenate((Populacao_elite,Populacao[i,:].reshape(1,Populacao.shape[1])))
        # se a aptidao auxiliar nao tiver nenhum elemento vazio, verifica se a aptidao do individuo atual é menor que a maior aptidao da aptidao auxiliar
        elif aptidao_temporaria < max(aptidao_auxiliar):
            # se for menor, pega a posição da maior aptidao e substitui o individuo naquela posição
            posicao_maior = aptidao_auxiliar.index(max(aptidao_auxiliar))
            aptidao_auxiliar[posicao_maior] = aptidao_temporaria
            Populacao_elite[posicao_maior,:] = Populacao[i,:]
            
    
    # cada vez que entra no for, é feita a seleção de 2 pais, e a recombinação deles, gerando 2 filhos
    for i in range(N//2 - (elite//2)):
        individuo_aleatorio_1 = Populacao[np.random.randint(0,N),:]
        individuo_aleatorio_2 = Populacao[np.random.randint(0,N),:]
        individuo_aleatorio_3 = Populacao[np.random.randint(0,N),:]
        individuo_aleatorio_4 = Populacao[np.random.randint(0,N),:]


        # fazendo o calculo da aptidao com os 2 pares de pais para escolher o melhor par
        
            
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
        #print("Pai 1: ",pai_1)
        #print("Pai 2: ",pai_2)
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
            # aux_2 = direita do ponto_2 do pai_2 + esquerda do ponto_1 do pai_2 + meio do pai 2
            # aux_2 = pai_2[ponto_2:n_points] + pai_2[0:ponto_1] + pai_2[ponto_1:ponto_2]

            # aux_1 = direita do ponto_2 do pai_1 + esquerda do ponto_1 do pai_1 + meio do pai 1
            # aux_1 = pai_1[ponto_2:n_points] + pai_1[0:ponto_1] + pai_1[ponto_1:ponto_2]

            # filho_1 = [None] * n_points
            # filho_2 = [None] * n_points

            # com numpy:
            aux_2 = np.concatenate(
                (pai_2[ponto_2:n_points], pai_2[0:ponto_1], pai_2[ponto_1:ponto_2])
            )
            aux_1 = np.concatenate(
                (pai_1[ponto_2:n_points], pai_1[0:ponto_1], pai_1[ponto_1:ponto_2])
            )
            filho_1 = [None] * n_points
            filho_2 = [None] * n_points

            # coloca os meios
            for i in range(ponto_1, ponto_2):
                filho_1[i] = pai_2[i]
                filho_2[i] = pai_1[i]

            posAux_1 = 0
            posAux_2 = 0

            # coloca o final
            for i in range(ponto_2, n_points):
                while aux_1[posAux_1] in filho_1:
                    posAux_1 += 1
                filho_1[i] = aux_1[posAux_1]
                while aux_2[posAux_2] in filho_2:
                    posAux_2 += 1
                filho_2[i] = aux_2[posAux_2]

            # coloca o inicio
            for i in range(0, ponto_1):
                while aux_1[posAux_1] in filho_1:
                    posAux_1 += 1
                filho_1[i] = aux_1[posAux_1]
                while aux_2[posAux_2] in filho_2:
                    posAux_2 += 1
                filho_2[i] = aux_2[posAux_2]

            # retorna cromossomo
            return [filho_1, filho_2]

        filhos = recombinacao_dois_pontos(pai_1, pai_2)
        #print("Filhos: ",filhos)

        # vamos colocar os filhos na população nova
        Populacao_aux = np.concatenate((Populacao_aux, np.array([filhos[0]]), np.array([filhos[1]])), axis=0)

    #print("Populacao aux: ",Populacao_aux)

    # para cada indivíduo da nova população, aplica-se a mutação
    for i in range(Populacao_aux.shape[0]):
        # se a taxa de mutação for menor que o valor gerado , retorna o individuo pois não haverá mutação
        if random.random() > taxa_mutacao:
            continue

        ponto_1 = random.randint(0, n_points-1)
        ponto_2 = random.randint(0, n_points-1)
        while ponto_1 == ponto_2:
            ponto_2 = random.randint(0, n_points-1)

        # fazendo a mutação, trocando os genes de posição
        aux = Populacao_aux[i, ponto_1]
        Populacao_aux[i, ponto_1] = Populacao_aux[i, ponto_2]
        Populacao_aux[i, ponto_2] = aux

    Populacao = Populacao_aux
    
    # elitismo
    # o melhor par de indivíduos da geração anterior é mantido na nova população
    while Populacao_elite.shape[0] > 0:
        Populacao = np.concatenate((Populacao,Populacao_elite[0,:].reshape(1,Populacao_elite.shape[1])))
        Populacao_elite = np.delete(Populacao_elite,0,axis=0)
    
    for i in range(N):
        individuo_atual = Populacao[i,:]
        aptidao_atual = calcula_aptidao(individuo_atual)
        
        # se achar um melhor, substitui
        if aptidao_atual < melhor_aptidao_atual:
            melhor_aptidao_atual = aptidao_atual
            melhor_atual = individuo_atual
            posicao_melhor = geracao_atual
            print("Geracao atual do melhor: ",geracao_atual)
    geracao_atual += 1

    # Parada quando nenhuma melhoria é observada ao longo de uma quantidade de gerações:
    #• Esta pode ser identificada ao monitorar a aptidão do melhor indivíduo.
    #• Se não há mudança significante ao longo de uma janela de gerações, então o EA deve ser
    #parado.
    #checando se a diferença entre a geração atual e a posição do melhor é maior que 6000, ou seja, se não melhorou em 1000 gerações, não irá melhorar mais
    if geracao_atual - posicao_melhor > 6000:
        break

# print time em horas, minutos e segundos
tempo = time.time() - tempo
print("Tempo de execução: ", tempo/3600, " horas" ,
        (tempo%3600)/60, " minutos",
        (tempo%3600)%60, " segundos")
      

#essa matriz pode ser utilizado para aptidao:
#caminhos = np.concatenate((vetor_origem,Populacao,vetor_origem),axis=1)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#plota os pontos e a origem 
ax.scatter(points[:,0], points[:,1], points[:,2], c='#248DD2', marker='o')
ax.scatter(p_origem[0:,0], p_origem[0:,1], p_origem[0:,2], c='green', marker='x',linewidth=3,s=30)

# plotar todas as linhas do melhor
gene_1 = melhor_atual[0]
for gene_2 in melhor_atual[1:]:
    p1 = points[gene_1,:].reshape(1,3)
    p2 = points[gene_2,:].reshape(1,3)
    line, = ax.plot([p1[0,0],p2[0,0]],[p1[0,1],p2[0,1]],[p1[0,2],p2[0,2]],color='k')
    gene_1 = gene_2

# plotar a linha que liga o ponto inicial ao final
p2 = points[melhor_atual[0],:].reshape(1,3)
line, = ax.plot([p_origem[0,0],p2[0,0]],[p_origem[0,1],p2[0,1]],[p_origem[0,2],p2[0,2]],color='k')
p2 = points[melhor_atual[-1],:].reshape(1,3)
line, = ax.plot([p_origem[0,0],p2[0,0]],[p_origem[0,1],p2[0,1]],[p_origem[0,2],p2[0,2]],color='k')


#exemplo caminho a partir da origem.
#p2 = points[0,:].reshape(1,3)
#plota a linha que liga a origem ao ponto
#line, = ax.plot([p_origem[0,0],p2[0,0]],[p_origem[0,1],p2[0,1]],[p_origem[0,2],p2[0,2]],color='k')

plt.tight_layout()
plt.show()

