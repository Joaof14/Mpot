# Método dos Mínimos Quadrados Linear e Ajustes não Linares

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# funções para calcular


# criar função tabela
def formar_tabela( coluna_x, coluna_y):

    tabela = pd.DataFrame()
    tabela['g'] = coluna_x
    tabela['j'] = coluna_y
    return tabela 


# funções para calcular
def calcula_reg(dataframe):

   # tabelamento
    n = len(dataframe['g'])
    soma_x = dataframe['g'].sum()
    soma_y = dataframe['j'].sum()
    soma_x2 = dataframe['g2'].sum()
    soma_xy = dataframe['gj'].sum()
    
   # calculo dos coeficientes a e b
    a = ((n * soma_xy) - (soma_x * soma_y)) / ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / ((soma_x * soma_x) - (n * soma_x2))
    
    
    return a, b     

def calcula_r2(dataframe, a , b):
    
     fx = a * dataframe["g"] + b
     ym = dataframe["j"].mean()
     r2 = np.sum((fx - ym )**2) / np.sum((dataframe["j"] - ym)**2)
     
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


    #formar tabela
def lin(x, y, pont):
    df = formar_tabela(x,y)
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = a*pont + b
    #Gráficos
    linha = a*df["g"] + b
    #criar file text
    return atv

    # formar tabela log
def logaritmo(x,y, pont):
    df = formar_tabela(x,y)
    df["g"] = np.log(df["g"]) 
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = a*np.log(pont) + b
    #Gráficos
    linha = a*np.log(df["g"]) + b
    #criar file text
    return atv 

def potencial(x,y,pont): 
    df = formar_tabela(x,y)
    df["g"] = np.log(df["g"])
    df["j"] = np.log(df["j"])
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = b*pont**a
    #Conversão dos coeficientes
    b = np.exp(b)
    #Gráficos
    linha = a*df["g"] + b
    #criar file text
    return atv

def exponencial(x,y, pont):
    df = formar_tabela(x,y)
    df["j"] = np.log(df["j"])
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Transformações (g2 e gj)

    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = b*np.exp(a*pont)
    #Conversão dos coeficientes (se necessário)
    b = np.exp(b)
    #Gráficos
    linha = b*np.exp(a*df['g'])
    #criar file text
    return atv 

def geometrico(x,y, pont):
    df = formar_tabela(x,y)
    df["j"] = np.log(df["j"])
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]

    
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #Conversão dos coeficientes (se necessário)
    a = np.exp(a)
    b = np.exp(b)
    #Gráficos
    linha = b*a**df["g"]
    #criar return
    atv = b*a**pont
    #criar file text
    return atv

def polinomial(x, y, pont, grau=2):
    df = formar_tabela(x, y)
    n = grau + 1
    mA = np.zeros((n, n))
    mB = np.zeros(n)

    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (df['g']**(i + j)).sum()
        mB[i] = (df['j'] * (df['g']**(i))).sum()
        
    resul = np.linalg.solve(mA, mB)
    atv = np.sum(c*(pont**i)for i,c in enumerate(resul))
    fx = np.sum(c*(df["g"]**i)for i,c in enumerate(resul))
    ym = df["j"].mean()
    r2 = np.sum((fx - ym )**2) / np.sum((df["j"] - ym)**2)
    linha = fx
        
    return atv



