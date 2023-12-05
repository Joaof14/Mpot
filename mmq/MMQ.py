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


    #formar tabela
def lin(x, y):
    df = formar_tabela(x,y)
    df["g"] = df["g"] 
    df["j"] = df["j"]
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = a*x + b
    #Gráficos
   
    #criar file text

    # formar tabela log
def logaritmo(x,y):
    df = formar_tabela(x,y)
    df["g"] = np.log(df["g"]) 
    df["j"] = df["j"]
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = a*np.log(x) + b
    #Gráficos
    
    #criar file text

def potencial(x,y): 
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
    atv = b*x**a
    #Conversão dos coeficientes
    b = np.exp(b)
    #Gráficos
    #criar file text

def exponencial(x,y):
    df = formar_tabela(x,y)
    df["j"] = np.log(df["j"])
    df["g"] = df["g"] 
    df["gj"] = df["g"] * df["j"]
    df["g2"] = df["g"] * df["g"]
    
    #Transformações (g2 e gj)

    #Calculos de coeficientes
    a, b = calcula_reg(df)
    #Calculo r2
    r2 = calcula_r2(df, a, b)
    #criar return
    atv = b*np.exp(a*x)
    #Conversão dos coeficientes (se necessário)
    b = np.exp(b)
    #Gráficos
    
    #criar file text

def geometrico(x,y):
    df = formar_tabela(x,y)
    df["j"] = np.log(df["j"])
    df["g"] = df["g"]
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
    #criar return
    atv = b*a**x
    #criar file text

def polinomial(x,y,grau = 2):
    df = formar_tabela(x,y)
    

    #Transformações (g2 e gj)

    #Calculos de coeficientes

    #Calculo r2  
   
    #Conversão dos coeficientes (se necessário)

    #Gráficos