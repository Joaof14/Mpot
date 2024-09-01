import numpy as np
from mmq.MMQ import *
#from lerMatriz import *

autovalor_global = 1

def metodo_da_potencia(A, yo, maxit=10000,
                       p=0.00001, inicio_acel=None, pontos = None, prev = None):
    """

   Método das potências para calcular autovalores de um determinado matriz.

   :param A: matriz do sistema.
   
   :param yo: vetor inicial de iteração.
   
   :param maxit: número máximo de iterações.
   
   :param p: critério de parada para a precisão.
   
   :return: tupla contendo o número de iterações, o erro da iteração e o autovalor encontrado.

   """
   #global ys, zs, autovls, erros, resultados, autovalor
    #Yo atribuido a y e inicialização de vetores para armazenar valores de erro e autovalores
    
    y = yo
    autovls = []
    erros = []
    

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

    return [i, erro, autovalor, autovls]

#Pot(A, yo)


def Aitken(A, yo, maxit=10000,
           p=0.00001, inicio_acel=6, pontos = None, prev = None):
    
    
    """

    Função para encontrar o autovalor dominante de uma Matriz A usando o método de Aitken.

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    inicio_acel = 4

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
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_linear(A, yo, maxit=10000,
                  p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """
   
    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:

                #Chama mmq linear com os ultimos 5 autovalores e iterações para descobrir autovalor resultante

                ac_Autovalor = lin(x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                    
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_logaritmo(A, yo, maxit=10000,
                     p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """

    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:

                #Chama mmq logaritmo com os ultimos 5 autovalores e iterações para descobrir autovalor resultante


                ac_Autovalor = logaritmo(
                    x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_potencial(A, yo, maxit=10000,
                     p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """

    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:

                #Chama mmq potencial com os ultimos 5 autovalores e iterações para descobrir autovalor resultante


                ac_Autovalor = potencial(
                    x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_exponencial(A, yo, maxit=10000,
                       p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """

    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:

                #Chama mmq exponencial com os ultimos 5 autovalores e iteraçõespara descobrir autovalor resultante


                ac_Autovalor = exponencial(
                    x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_geometrico(A, yo, maxit=10000,
                      p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """

    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:
                ac_Autovalor = geometrico(
                    x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:

                #Chama mmq geometrico com os ultimos 5 autovalores e iterações para descobrir autovalor resultante


                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)
                else:
                    erro = np.abs(
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]


def mp_mmq_polinomial(A, yo, maxit=10000,
                      p=0.00001, inicio_acel=6, pontos = -5, prev = 0):

    
    """

    Função para encontrar o autovalor dominante de uma matriz A usando o método dos mínimos quadrados

    :param A: matriz A.
    
    :param yo: vetor de autovetores iniciais.
    
    :param maxit: número máximo de iterações.
    
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

    while i < maxit:

        # Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)

        y = z/np.linalg.norm(z)

        # Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:

            if i >= inicio_acel:

                #Chama mmq polinomial com os ultimos 5 autovalores e iterações para descobrir autovalor resultante


                ac_Autovalor = polinomial(
                    x=np.arange(i+pontos, i), y=autovls[+pontos:], pont=i+prev)
                ac_Autovls.append(ac_Autovalor)

            autovalor = np.linalg.norm(z)
            autovls.append(autovalor)

            if i > 1:
                
                #Calcular erro de forma normal no metodo da potencia antes da aceleração

                if i <= inicio_acel:
                    erro = np.abs(autovls[-1] - autovls[-2]
                                  ) / np.abs(autovls[-1])
                    erros.append(erro)

                #Calcular erro com base nos autovalores da aceleração caso ela ja tenha iniciado e rodado no mínimo duas vezes
                
                else:
                    erro = np.abs(
                        #ac_Autovls[-1] - autovalor_global) / np.abs(autovalor_global)
                        ac_Autovls[-1] - ac_Autovls[-2]) / np.abs(ac_Autovls[-2])
                    erros.append(erro)
                    autovalor = ac_Autovalor

                # critério de parada da precisão
                if erro < p:
                    break

        # Cálculo de y com base no valor de z, tornando o vetor normalizado

        i += 1

    return [i, erro, autovalor, autovls]