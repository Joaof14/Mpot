import scipy
from io import StringIO
import numpy as np

matriz = scipy.io.mmread("bcsstk01.mtx")
A = np.array(matriz.A)
print(A)

