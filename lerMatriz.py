import scipy
from io import StringIO
import numpy as np

matriz = scipy.io.mmread("bcsstk05.mtx")
A = np.array(matriz.A)
n = A.shape[1]
maxit = 10000
p = 0.00001
yo = np.ones(n)
