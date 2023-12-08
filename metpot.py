import numpy as np
from mmq.MMQ import *
#from lerMatriz import *




def metodo_das_potencias(A, yo, maxit = 10000,
p = 0.0000000001, acel = 'Nenhuma', inicio_acel = 10):

    #Inicialização de vetores para armazenar valores de z e y, adicionando o yo
    #global ys, zs, autovls, erros, resultados, autovalor
    y = yo
    autovls = []
    erros = []
    



    i = 1

    #iteração do método das potências

    while i < maxit:  

        #Cálculo de Z com base no valor anterior de y

        z = np.dot(A, y)
        
        y = z/np.linalg.norm(z)
        
        #Cálcular vetor com possíveis autovalores caso iterações sejam suficientes para tal

        if i > 0:
            
            if i < inicio_acel or acel == 'Nenhuma':
                autovalor = np.linalg.norm(z)
                autovls.append(autovalor)
            
            
            #calcular erro dos autovalores quando existem suficientes

            elif acel == 'MMQ_Linear' and i > inicio_acel:
    
                pass
            
            elif acel == 'MMQ_Logaritmo'and i > inicio_acel:
                    
                pass
                
            elif acel == 'MMQ_Exponencial' and i > inicio_acel:
                    
                pass
                
            elif acel == 'MMQ_Potencial' and i > inicio_acel:
                    
                pass
                
            elif acel == 'MMQ_Geometrico' and i > inicio_acel:
                   
                pass
                
                
                
                
            if i > 1: 

                erro = np.abs(autovls[-1] - autovls[-2]) / np.abs(autovls[-1])
                erros.append(erro)
                
                #critério de parada da precisão
                if erro < p:
                    break
               
            

        #Cálculo de y com base no valor de z, tornando o vetor normalizado

    
        i+=1
        
    return [i, erro, autovalor]

#Pot(A, yo)

def Aitken(valores):
    avAitken = valores


    pass































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