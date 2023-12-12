# Método dos Mínimos Quadrados Linear e Ajustes não Linares

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# funções para calcular


# criar função tabela


# funções para calcular
def calcula_reg(coluna_x, coluna_y):

   # tabelamento
    n = len(coluna_x)
    soma_x = np.sum(coluna_x)
    soma_y = np.sum(coluna_y)
    soma_x2 = np.sum(coluna_x * coluna_x)
    soma_xy = np.sum(coluna_x * coluna_y)

   # calculo dos coeficientes a e b
    a = ((n * soma_xy) - (soma_x * soma_y)) / \
        ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / \
        ((soma_x * soma_x) - (n * soma_x2))

    return a, b


def calcula_r2(coluna_x, coluna_y, a, b):

    fx = a * coluna_x + b
    ym = np.mean(coluna_y)
    r2 = np.sum((fx - ym)**2) / np.sum((coluna_y - ym)**2)

    return r2


'''
def plotgrafico( x,  y , linha):
    plt.scatter(x,y)
    plt.plot(x, linha, label='linear', )
    plt.ylabel('autovalores')
    plt.xlabel('iterações')
    plt.title('Grafíco')
    plt.grid()
    plt.legend()
    return plt.show()
    '''

# formar tabela


def lin(x, y, pont):

    # Calculos de coeficientes
    a, b = calcula_reg(x, y)
    # Calculo r2
    r2 = calcula_r2(x, y, a, b)
    # criar return
    atv = a*pont + b
    # Gráficos
    linha = a*x, y + b
    # criar file text
    return atv

    # formar tabela log


def logaritmo(x, y, pont):

    x = np.log(x)

    # Calculos de coeficientes
    a, b = calcula_reg(x, y)
    # Calculo r2
    r2 = calcula_r2(x, y, a, b)
    # criar return
    atv = a*np.log(pont) + b
    # Gráficos
    linha = a*np.log(x) + b
    # criar file text
    return atv


def potencial(x, y, pont):

    x = np.log(x)
    y = np.log(y)

    # Calculos de coeficientes
    a, b = calcula_reg(x, y)
    # Calculo r2
    r2 = calcula_r2(x, y, a, b)
    # criar return
    atv = b*pont**a
    # Conversão dos coeficientes
    b = np.exp(b)
    # Gráficos
    linha = a*x + b
    # criar file text
    return atv


def exponencial(x, y, pont):

    y = np.log(y)

    # Transformações (g2 e gj)

    # Calculos de coeficientes
    a, b = calcula_reg(x, y)
    # Calculo r2
    r2 = calcula_r2(x, y, a, b)
    # criar return
    atv = b*np.exp(a*pont)
    # Conversão dos coeficientes (se necessário)
    b = np.exp(b)
    # Gráficos
    linha = b*np.exp(a*x)
    # criar file text
    return atv


def geometrico(x, y, pont):

    y = np.log(y)

    # Calculos de coeficientes
    a, b = calcula_reg(x, y)
    # Calculo r2
    r2 = calcula_r2(x, y, a, b)
    # Conversão dos coeficientes (se necessário)
    a = np.exp(a)
    b = np.exp(b)
    # Gráficos
    linha = b*a**x
    # criar return
    atv = b*a**pont
    # criar file text
    return atv


def polinomial(x, y, pont, grau=2):

    n = grau + 1
    mA = np.zeros((n, n))
    mB = np.zeros(n)

    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (x**(i + j)).sum()
        mB[i] = (y * (x**(i))).sum()

    resul = np.linalg.solve(mA, mB)
    atv = np.sum(c*(pont**i)for i, c in enumerate(resul))
    fx = np.sum(c*(x**i)for i, c in enumerate(resul))
    ym = np.mean(y)
    r2 = np.sum((fx - ym)**2) / np.sum((y - ym)**2)
    linha = fx

    return atv


"""


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
pont = 5

resultado = lin(x,y,pont)
print('Linear: ', resultado)

resultado = logaritmo(x,y,pont)
print('Logaritmo: ', resultado)

resultado = exponencial(x,y,pont)
print('exponencial: ', resultado)

resultado = potencial(x,y,pont)
print('potencial: ', resultado)

resultado = geometrico(x,y,pont)
print('geometrico: ', resultado)


"""