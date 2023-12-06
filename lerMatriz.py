import scipy
from io import StringIO
import numpy as np
from metpot import *

matriz = scipy.io.mmread("matrizes/bcsstk05.mtx")
matriz.A
A = np.array(matriz.A)
#A = np.array([[3,0,1], [2,2,2], [4,2,5]], dtype=float)
n = A.shape[1]
yo = np.ones(n)

Pot(A, yo)