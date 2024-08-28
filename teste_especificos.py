import numpy as np
from metpot import metodo_da_potencia, Aitken
from mmq.MMQ import lin, logaritmo, exponencial, potencial, geometrico, polinomial
import scipy
from io import StringIO
import os
import glob
import pandas as pd
import time
import matplotlib.pyplot as plt




arquivo = 'matrizes/slot_artigo/bcsstk02.mtx'

matriz = scipy.io.mmread(arquivo)
matriz.A
A = np.array(matriz.A)
n = A.shape[0]
yo = np.ones(n)

i, e, autovls, autovetor = metodo_da_potencia(A,yo, p=0.00001)


graf, eix = plt.subplots()
eix.scatter(np.arange(1,i), np.array(autovls[1:]))
eix.set_xlabel('Iterações')
eix.set_ylabel('Autovalores')
eix.set_title(arquivo[21:-4])
eix.ticklabel_format(style='plain', axis='y')
graf.show()
graf.savefig(arquivo+'_MP' +'.png')

