import numpy as np


#incialização
A = np.array([[3,0,1], [2,2,2], [4,2,5]])

n = A.shape[1]
maxit = 10000
ys = []
yo = np.ones(n)
zs = []


def Pot(A, yo):
    ys.append(yo)
    autov = np.zeros()
    for i in range(maxit):  
        z = np.dot(A, ys[i])
        
        y = z/np.max(z)

        ys.append(y)


#Pot(A, yo)