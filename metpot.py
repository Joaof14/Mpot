import numpy as np
from lerMatriz import *
#importar arquivo auxiliar com dados sobre a aplicação, precisão, yo, e matrizes




def Pot(A, yo):

    #Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    global ys, zs, autovls, erros, resultado
    ys = []
    zs = []
    autovls = []
    erros = []

    ys.append(yo)

    i = 0

    #iteração do método das potências

    while i < maxit:  

        #Cálculo de Z com base no valor anterior de y

        z = np.dot(A, ys[i])
        zs.append(z)

        #Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:
            autovl = zs[-1]/ys[-1]
            autovls.append(autovl)
            
            #calcular erro dos autovalores quando existem suficientes

            if i > 1: 

                err = (autovls[-1] - autovls[-2])/autovls[-1]
                err = np.abs(err)
                
                #armazenar resultado de menor erro

                mn = np.argmin(err)
                resultado = autovl[mn]
                e = np.min(err)
                erros.append(e)
                #critério de parada da precisão

                if e < p:  
                    print(resultado)
                    break

        
        #Cálculo de y com base no valor de z, tornando o vetor normalizado

        y = z/np.max(np.abs(z))
        
        ys.append(y)
        i+=1

    print(i)


"""def PotInv(A, y):
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

def Aitken(valores):
    avAitken = valores


    pass





Pot(A, yo)

