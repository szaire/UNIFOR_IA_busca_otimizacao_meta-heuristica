import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 28 - h(x)

def h(x: list):
    # criar um algoritmo para identificar os pares atacantes
    tab = criar_tabuleiro(x)
    quant_pares_atacantes = procurar_pares_atacantes(tab, x)
    return quant_pares_atacantes

def procurar_pares_atacantes(tab: np.ndarray, x: list):
    quant_pares_atacantes = 0
    # percorrer horizontal
    for i in range(len(x)):
        soma = sum(tab[i])
        if soma > 1:
            quant_pares_atacantes += soma            
    # percorrer diagonal superior
    i = x[0]-1
    j = 0
    while i >= 0 and i <= 7:
        if tab[i][j] == 1:
            quant_pares_atacantes += 1
        i -= 1
        j += 1
    # percorrer diagonal inferior
    i = x[0]-1
    j = 0
    while i >= 0 and i <= 7:
        if tab[i][j] == 1:
            quant_pares_atacantes += 1
        i += 1
        j += 1
    return quant_pares_atacantes
    
def criar_tabuleiro(x: list):
    temp_tab = np.zeros((8, 8))
    rows, cols = temp_tab.shape
    i_local = 0
    for j in range(cols):
        for i in range(rows):
            if i+1 == x[i_local]:
                temp_tab[i][j] = 1
        i_local += 1
    return temp_tab