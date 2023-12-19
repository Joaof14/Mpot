import numpy as np
from mmq.MMQ import *
import scipy
from io import StringIO
import os
import glob



def metodo_da_potencia(A, yo, maxit=10000,
                       p=0.0000000001):

    global autovalores_pot
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovalores_pot, erros, resultados, autovalor
    y = yo
    autovalores_pot = []
    erros = []
    ac_Autovalores_pot = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            autovalor = np.linalg.norm(z)

            autovalores_pot.append(autovalor)

            if i > 1:
                erro = np.abs(autovalores_pot[-1] - autovalores_pot[-2]) / np.abs(autovalores_pot[-1])
                erros.append(erro)

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]

#Pot(A, yo)


def Aitken(A, yo, maxit=10000,
           p=0.00001, inicio_acel=5):

    global ac_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    ac_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

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
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]



def mmq_linear(A, yo, maxit=10000,
                  p=0.0000000001, inicio_acel=5):

    global acLinear_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acLinear_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = lin(x=np.arange(1, i), y=autovls, pont=i)
                acLinear_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)



            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acLinear_Autovls[-1] - acLinear_Autovls[-2]) / np.abs(acLinear_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]



def mmq_logaritmo(A, yo, maxit=10000,
                     p=0.0000000001, inicio_acel=5):

    global acLogaritmo_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acLogaritmo_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = logaritmo(
                    x=np.arange(1, i), y=autovls, pont=i)
                acLogaritmo_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            

            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acLogaritmo_Autovls[-1] - acLogaritmo_Autovls[-2]) / np.abs(acLogaritmo_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]


def mmq_potencial(A, yo, maxit=10000,
                     p=0.0000000001, inicio_acel=5):

    global acPotencial_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acPotencial_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = potencial(
                    x=np.arange(1, i), y=autovls, pont=i)
                acPotencial_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)
  

            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acPotencial_Autovls[-1] - acPotencial_Autovls[-2]) / np.abs(acPotencial_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]


def mmq_exponencial(A, yo, maxit=10000,
                       p=0.0000000001, inicio_acel=5):

    global acExponencial_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acExponencial_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = exponencial(
                    x=np.arange(1, i), y=autovls, pont=i)
                acExponencial_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            

            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acExponencial_Autovls[-1] - acExponencial_Autovls[-2]) / np.abs(acExponencial_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]


def mmq_geometrico(A, yo, maxit=10000,
                      p=0.0000000001, inicio_acel=5):

    global acGeometrico_Autovls, autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acGeometrico_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = geometrico(
                    x=np.arange(1, i), y=autovls, pont=i)
                acGeometrico_Autovls.append(ac_Autovalor)
            
            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            

            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acGeometrico_Autovls[-1] - acGeometrico_Autovls[-2]) / np.abs(acGeometrico_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]


def mmq_polinomial(A, yo, maxit=10000,
                      p=0.0000000001, inicio_acel=5):

    global acPolinomial_Autovls
    # Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    acPolinomial_Autovls = []

    i = 1

    # iteração do método das potências

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = polinomial(
                    x=np.arange(1, i), y=autovls, pont=i)
                acPolinomial_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            

            if i > 1:
                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        acPolinomial_Autovls[-1] - acPolinomial_Autovls[-2]) / np.abs(acPolinomial_Autovls[-1])
                    erros.append(erro)
                    autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]



acels = {'Nenhuma': metodo_da_potencia,
         'Aitken': Aitken,
          'MMQ_Linear': mmq_linear,
          'MMQ_Logaritmo': mmq_logaritmo ,
          'MMQ_Exponencial': mmq_exponencial ,
          'MMQ_Potencial': mmq_potencial ,
          'MMQ_Geometrico': mmq_geometrico ,
          'MMQ_Polinomial': mmq_polinomial ,
         }


"""

Livro Neide Franco Cálculo Numérico

#Livro página 210 exercício 7.5
A = np.array([[1,-1,3],[-1,1,3],[3,-3,9]])

#Livro página 210 exercício 7.6
A = np.array([[2,-1,0],[-1,2,-1],[0,-1,-2]])

#Livro página 210 exercício 7.8, resposta ja no enunciado
A = np.array([[4,-1,1],[1,1,1],[-2,0,6]])


"""


#Livro página 204 exemplo 7.4
A = np.array([[3,0,1],[2,2,2],[4,2,5]])


n = A.shape[1]
yo = np.ones(n)

coluna_acelera = []
coluna_ite = []
coluna_autovalor = []
coluna_erro = []



for acel, metodo in acels.items():

    coluna_acelera.append(acel)

    try:
        i, e, autovalor = metodo(A, yo, p=0.00001)
        coluna_ite.append(i)
        coluna_autovalor.append(autovalor)
        coluna_erro.append(e)

    except:
        coluna_ite.append('erro')
        coluna_autovalor.append('erro')
        coluna_erro.append('erro')




dados = {
    'Aceleração': coluna_acelera,
    'Autovalor': coluna_autovalor,
    'Iterações': coluna_ite,
    'Erros': coluna_erro,
}

dfteste = pd.DataFrame(dados)




