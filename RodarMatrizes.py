import numpy as np
from metpot import *


import scipy
from io import StringIO
import os
import glob
import pandas as pd



caminho = 'matrizes/'
arquivos_na_pasta = glob.glob(os.path.join(caminho, '*'))

coluna_nomes = []
coluna_acelera = []
coluna_ordem = []
coluna_campo = []
coluna_simetria = []
coluna_ite = []
coluna_autovalor = []
coluna_erro = []

#acels = ['Nenhuma', 'MMQ_Linear', 'MMQ_Logaritmo', 'MMQ_Exponencial', 'MMQ_Potencial', 'MMQ_Geometrico', 'MMQ_Polinomial']
acels = ['Nenhuma', 'Aitken']

for arquivo in arquivos_na_pasta:
    ordem, _, _, _, campo, simetria = scipy.io.mminfo(arquivo)
    matriz = scipy.io.mmread(arquivo)
    matriz.A
    A = np.array(matriz.A)
    n = A.shape[1]
    yo = np.ones(n)
    
    for ac in acels:
        if acel == 'Nenhuma':
            
            i, e, autovalor= metodo_das_potencias(A, yo, acel=ac)
        
        elif acel  == 'Aitken':
            
            i, e, autovalor= metodo_das_potencias(A, yo, acel=ac)
            
            pass
             
        elif acel == 'MMQ_Linear' a:

            pass
        
        elif acel == 'MMQ_Logaritmo':
                
            pass
            
        elif acel == 'MMQ_Exponencial':
                
            pass
            
        elif acel == 'MMQ_Potencial' :
                
            pass
            
        elif acel == 'MMQ_Geometrico':
               
            pass
        
        elif acel == 'MMQ_Geometrico':
            
        
        coluna_nomes.append(arquivo)
        coluna_ordem.append(ordem)
        coluna_campo.append(campo)
        coluna_simetria.append(simetria)
        coluna_acelera.append(ac)
        
        
        
        coluna_ite.append(i)
        coluna_autovalor.append(autovalor)
        coluna_erro.append(e)
        

dados = {
    'Matriz': coluna_nomes,
    'Aceleração': coluna_acelera,
    'Autovalor': coluna_autovalor,
    'Iterações': coluna_ite,
    'Erros': coluna_erro,
    'Ordem': coluna_ordem,
    'Campo': coluna_campo,
    'Simetria': coluna_simetria
}

df1 = pd.DataFrame( dados )


