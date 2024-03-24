import matplotlib.pyplot as plt
from math import log10
import numpy as np

def plotar_grafico(x, y, linha, arquivo, nomeMetodo, ajuste):
    
    
    y = np.array(y)
    linha = np.array(linha)

    graf, eix = plt.subplots()
    eix.set_title(arquivo[21:-4])
    eix.set_xlabel('Iterações')

    if np.max(y) >= 100000:
        valor = log10(y[-1])
        valor = int(valor)
        valor = valor - 4
        y = y/(10**valor)
        linha = linha / (10**valor)
        eix.set_ylabel(rf"Autovalores $(x10^{{{valor}}})$")
    
    else:
        eix.set_ylabel('Autovalores')

    
    eix.scatter(x,y,c = 'r')
    eix.plot(linha, c = 'black')
    eix.ticklabel_format(style='plain', axis='y')
    graf.savefig(arquivo+'_' + nomeMetodo + '-' + ajuste +'.png')