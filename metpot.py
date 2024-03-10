import numpy as np
from mmq.MMQ import *
#from lerMatriz import *
import matplotlib.pyplot as plt

def metodo_da_potencia(A, yo, max_it=10000,
                       p=0.00001):
    """

   Método das potências para calcular autovalores de um determinado matriz.

   :param A: matriz do sistema.
   
   :param yo: vetor inicial de iteração.
   
   :param max_it: número máximo de iterações.
   
   :param p: critério de parada para a precisão.
   
   :return: tupla contendo o número de iterações, o erro da iteração e o autovalor encontrado.

   """
    
    autovls = []
    erros = []
    y = yo
    

    i = 1

    # iteração do método das potências

    while i < max_it:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            autovalor = np.linalg.norm(z)

            autovls.append(autovalor)

            if i > 1:
                erro = np.abs(autovls[-1] - autovls[-2]) / np.abs(autovls[-2])
                erros.append(erro)

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovls, z]

#Pot(A, yo)


def Aitken(A, yo, max_it=10000,
           p=0.00001, inicio_acel = 4):
    
    
    """

    Função para encontrar o autovalor dominante de um operador linear A usando o método de Aitken.

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param max_it: número máximo de iterações.
    
    :param p: critério de parada para a precisão.
    
    :param inicio_acel: índice para começar a aplicar aceleração.
    
    :return: tupla contendo o número de iterações, o erro da iteração e o autovalor encontrado.

    """
    #global ys, zs, autovls, erros, resultados, autovalor
    #Inicialização de vetores para armazenar autavalores normais e de aceleração, adicionando o yo a y
    
    y = yo
    autovls = []
    erros = []
    ac_Autovls = []

    i = 1

    # iteração do método das potências

    while i < max_it:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            autovalor = np.linalg.norm(z)

            if i >= inicio_acel:
                ac_Autovalor = autovls[-2] - ((autovls[-1] - autovls[-2])**2) / (
                    autovalor - 2 * autovls[-1] + autovls[-2])
                ac_Autovls.append(ac_Autovalor)

            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-2])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovls[:3] + ac_Autovls, z]
# Example usage:
"""
A = np.array([[-4, 14, 0],
              [-5, 13, 0],
              [-1, 0, 2]])

prec = 1e-4
max_iter = 10000

n = A.shape[0]
yo = np.ones(n)



i, erro, autovalores, autovetor = metodo_da_potencia(A, yo, p  = prec)

i_aitken, erro_aitken, autovalores_aitken, autovetor_aitken = Aitken(A, yo, p  = prec)


 """
