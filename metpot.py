import numpy as np
from mmq.MMQ import *
#from lerMatriz import *


def metodo_da_potencia(A, yo, maxit=10000,
                       p=0.00001):

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

            autovls.append(autovalor)

            if i > 1:
                erro = np.abs(autovls[-1] - autovls[-2]) / np.abs(autovls[-1])
                erros.append(erro)

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor]

#Pot(A, yo)


def Aitken(A, yo, maxit=10000,
           p=0.00001, inicio_acel=6):

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




def mp_mmq_linear(A, yo, maxit=10000,
                  p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = lin(x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
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


def mp_mmq_logaritmo(A, yo, maxit=10000,
                     p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = logaritmo(
                    x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
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


def mp_mmq_potencial(A, yo, maxit=10000,
                     p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = potencial(
                    x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
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


def mp_mmq_exponencial(A, yo, maxit=10000,
                       p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = exponencial(
                    x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
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


def mp_mmq_geometrico(A, yo, maxit=10000,
                      p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = geometrico(
                    x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)
            
            autovalor = np.linalg.norm(z)
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


def mp_mmq_polinomial(A, yo, maxit=10000,
                      p=0.00001, inicio_acel=6):

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

            if i >= inicio_acel:
                ac_Autovalor = polinomial(
                    x=np.arange(i-5, i), y=autovls[-5:], pont=i)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
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


"""

def PotInv(A, y):
    ys = []
    zs = []
    autovls = []

    L, U = LU(A)
    

    i = 0
    while i < maxit:
        ys.append(y)  
        x = retrosub(L,y,False)
        z = retrosub(U,x,True)
        zs.append(z)
        i += 1


        if i > 0:
            autovl = zs[-1]/ys[-1]
            autovls.append(autovl)
            

        if i > 1: 
            err = (autovls[-1] - autovls[-2])/autovls[-1]
            
            err = np.abs(err)
            mn = np.argmin(err)
            resultado = autovl[mn]
            e = np.min(err)
            if e < p:  
                print(resultado) 
                print(1/resultado)
                print(y)
                break




        y = z/np.max(np.abs(z))

    print(i)
        

    return
"""
