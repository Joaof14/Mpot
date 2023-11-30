# Método dos Mínimos Quadrados Linear e Ajustes não Linares

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# funções para calcular



# criar função tabela
def formar_tabela( dataframe, coluna_x, coluna_y):

    tabela = pd.DataFrame()
    tabela['g'] = coluna_x
    tabela['j'] = coluna_y
    return tabela 


# funções para calcular
def calcula_reg(dataframe):

   # tabelamento
    n = len(dataframe)
    soma_x = dataframe['g'].sum()
    soma_y = dataframe['j'].sum()
    soma_x2 = dataframe['g2'].sum()
    soma_xy = dataframe['gj'].sum()
    
   # calculo dos coeficientes a e b
    a = ((n * soma_xy) - (soma_x * soma_y)) / ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / ((soma_x * soma_x) - (n * soma_x2))
    
    
    return a, b

def calcula_r2(dataframe, a , b):
    
     fx = a * dataframe["x"] + b
     ym = dataframe["y"].mean()
     r2 = np.sum((fx - ym )**2) / np.sum((dataframe["y"] - ym)**2)
     
     return r2

def plotgrafico(dataframe, titulo, texto):
    pass

def lin(x, y):
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Gráficos


def logaritmo(x,y):
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Conversão dos coeficientes (se necessário)

    #Gráficos


def potencial(x,y): 
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Conversão dos coeficientes (se necessário)

    #Gráficos

def exponencial(x,y):
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Conversão dos coeficientes (se necessário)

    #Gráficos

def geometrico(x,y):
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Conversão dos coeficientes (se necessário)

    #Gráficos

def polinomial(x,y):
    df = formar_tabela(x,y)

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2

    #Conversão dos coeficientes (se necessário)

    #Gráficos