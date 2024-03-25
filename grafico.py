import matplotlib.pyplot as plt
from math import log10
import numpy as np

def plotar_grafico(x, y, linha, arquivo, nomeMetodo, ajuste):
    label_ajuste = 'ajuste ' + ajuste
    
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

    eix.grid(True, alpha = 0.35)
    eix.scatter(x,y,c = 'r', label = 'Autovalores do Método da Potência')
    eix.plot(linha, c = 'black', label = label_ajuste)
    eix.legend(fontsize='small', loc='lower right')
    eix.ticklabel_format(style='plain', axis='y')
    graf.savefig(arquivo+'_' + nomeMetodo + '-' + ajuste +'.png')