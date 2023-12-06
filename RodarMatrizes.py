import scipy
from io import StringIO
import numpy as np
from metpot import Pot
import os
import glob
import pandas as pd



caminho = 'matrizes/'
arquivos_na_pasta = glob.glob(os.path.join(caminho, '*'))

coluna_nomes = []
coluna_ordem = []
coluna_campo = []
coluna_simetria = []
coluna_ite = []
coluna_autovalor = []
coluna_erro = []

for arquivo in arquivos_na_pasta:
    ordem, _, _, _, campo, simetria = scipy.io.mminfo(arquivo)
    matriz = scipy.io.mmread(arquivo)
    matriz.A
    A = np.array(matriz.A)
    n = A.shape[1]
    yo = np.ones(n)
    
    coluna_nomes.append(arquivo)
    coluna_ordem.append(ordem)
    coluna_campo.append(campo)
    coluna_simetria.append(simetria)
    
    try:
        i, e, autovalor= Pot(A, yo)
        coluna_ite.append(i)
        coluna_autovalor.append(autovalor)
        coluna_erro.append(e)
        
    except:
        coluna_ite.append('erro no calculo')
        coluna_autovalor.append('erro no calculo')
        coluna_erro.append('erro no calculo')

dados = {
    'Matriz': coluna_nomes,
    'Autovalor': coluna_autovalor,
    'Iterações': coluna_ite,
    'Erros': coluna_erro,
    'Ordem': coluna_ordem,
    'Campo': coluna_campo,
    'Simetria': coluna_simetria
}

df = pd.DataFrame( dados )


