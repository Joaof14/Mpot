import matplotlib.pyplot as plt
from math import log10
import numpy as np

def plotar_grafico(x, y, linha, arquivo, nomeMetodo, ajuste):
    label_ajuste = 'Função '+ ajuste
    
    y = np.array(y)
    linha = np.array(linha)

    graf, eix = plt.subplots()
    # Remover o título do gráfico
    # eix.set_title(arquivo[21:-4])
    eix.set_xlabel('Iterações', fontsize=14)  # Aumentar tamanho da fonte do label do eixo x

    if np.max(y) >= 100000:
        valor = log10(y[-1])
        valor = int(valor)
        valor = valor - 4
        y = y / (10**valor)
        linha = linha / (10**valor)
        eix.set_ylabel(rf"Autovalores $(x10^{{{valor}}})$", fontsize=14)  # Aumentar tamanho da fonte do label do eixo y
    else:
        eix.set_ylabel('Autovalores', fontsize=14)  # Aumentar tamanho da fonte do label do eixo y

    eix.grid(True, alpha=0.35)
    eix.scatter(x, y, c='r', label='Autovalores do MP')
    eix.plot(linha, c='black', label=label_ajuste)
    eix.legend(fontsize='large', loc='lower right')  # Aumentar tamanho da fonte da legenda
    eix.ticklabel_format(style='plain', axis='y')

    # Aumentar o tamanho das informações da escala nos eixos
    eix.tick_params(axis='both', which='major', labelsize=14)

    

# Exemplo de uso:
# plotar_grafico(x, y, linha, 'caminho/para/arquivo', 'nomeMetodo', 'Linear')
