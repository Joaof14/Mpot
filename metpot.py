import numpy as np
from aux import *
#incialização




def Pot(A, yo):
    ys.append(yo)

    i = 0
    while i < maxit:  
        z = np.dot(A, ys[i])
        zs.append(z)

        if i > 0:
            autovl = zs[-1]/ys[-1]
            print(autovl)
            autovls.append(autovl)
            

        if i > 1: 
            err = (autovls[-1] - autovls[-2])/autovls[-1]
            
            err = np.abs(err)
            mn = np.argmin(err)
            resultado = autovl[mn]
            print(resultado)
            e = np.min(err)
            if e < p:   
                break

        
        
        y = z/np.max(np.abs(z))
        
        ys.append(y)
        i+=1

    print(i)


def PotInv(A, yo):
    L, U = LU(A)
    
    
    return
    



PotInv(B, 0)
#Pot(A, yo)