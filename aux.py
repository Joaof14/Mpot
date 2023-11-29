import numpy as np
A = np.array([[3,0,1], [2,2,2], [4,2,5]], dtype=float)
B = np.array([[2,1,0], [2,5,3], [0,1,6]], dtype=float)
n = A.shape[1]
maxit = 10000
p = 0.0000000000001
yo = np.ones(n)

   

from scipy.linalg import lu_factor 


def LU(A):
    mALU, piv = lu_factor(A)
    L = np.identity(n, dtype = float)
    U = np.zeros((n,n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i,j] = mALU[i, j]
            else:
                L[i,j] = mALU[i, j]

    return L, U

def retrosub(C,D, ts):
    global output
    n = len(C)
    C = np.array(C, dtype=float)
    D = np.array(D, dtype=float)
    z = np.zeros(n)
    if ts == True:
        for i in range(n-1, -1, -1):
            soma = 0
            for j in range(i+1, n):
                soma += C[i][j]* z[j]
            z[i] = (D[i] - soma) / C[i][i]   # Fórmula da matriz;
       

    else:
        for i in range(n):
            soma = 0
            for j in range(i-1,-1,-1):
                soma += C[i][j]* z[j]
            z[i] = (D[i] - soma) / C[i][i]
        
    
    return z