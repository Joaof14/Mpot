import numpy as np
from metpot import metodo_da_potencia, Aitken, mp_mmq_linear, mp_mmq_logaritmo, mp_mmq_exponencial, mp_mmq_potencial, mp_mmq_geometrico, mp_mmq_polinomial

import scipy
from io import StringIO
import os
import glob
import pandas as pd
import time
import matplotlib.pyplot as plt




coluna_nomes = []
coluna_acelera = []
coluna_ordem = []
coluna_campo = []
coluna_simetria = []
coluna_ite = []
coluna_autovalor = []
coluna_tempo = []
coluna_ultimos = []
coluna_inicioAc = []

#acels = ['Nenhuma', 'MMQ_Linear', 'MMQ_Logaritmo', 'MMQ_Exponencial', 'MMQ_Potencial', 'MMQ_Geometrico', 'MMQ_Polinomial']

acels = {'Nenhuma': metodo_da_potencia,
         'Aitken': Aitken,
          'MMQ_Linear': mp_mmq_linear,
          'MMQ_Logaritmo': mp_mmq_logaritmo ,
          'MMQ_Geometrico': mp_mmq_geometrico ,
          'MMQ_Polinomial': mp_mmq_polinomial ,
         }



caminho = 'matrizes/'
arquivos_na_pasta = glob.glob(os.path.join(caminho, '*'))



for arquivo in arquivos_na_pasta:
    ordem, _, _, _, campo, simetria = scipy.io.mminfo(arquivo)
    matriz = scipy.io.mmread(arquivo)
    matriz.A
    A = np.array(matriz.A)
    n = A.shape[1]
    yo = np.ones(n)



    for acel, metodo in acels.items():

        coluna_nomes.append(arquivo)
        coluna_ordem.append(ordem)
        coluna_campo.append(campo)
        coluna_simetria.append(simetria)
        coluna_acelera.append(acel)
        
        

        try:
            
            inicio = time.time()
            i, e, autovalor, autovls = metodo(A, yo, p=0.0000000001)
            fim = time.time()
            coluna_ite.append(i)
            coluna_autovalor.append(autovalor)
            
            coluna_tempo.append(fim - inicio)
            """
            if acel == 'Nenhuma':
                graf, eix = plt.subplots()
                eix.scatter(np.arange(1,i), autovls[1:])
                eix.set_xlabel('Iterações')
                eix.set_ylabel('Autovalores')
                graf.savefig(arquivo+'.png')"""
            

        except:
            coluna_tempo.append('erro')
            coluna_ite.append('erro')
            coluna_autovalor.append('erro')



dados = {
    'Matriz': coluna_nomes,
    'Aceleração': coluna_acelera,
    'Autovalor': coluna_autovalor,
    'Iterações': coluna_ite,
    'Tempo': coluna_tempo, 
    'Ordem': coluna_ordem,
    'Campo': coluna_campo,
    'Simetria': coluna_simetria
}



df1 = pd.DataFrame(dados)

df1['Matriz'] = df1['Matriz'].str.lstrip('matrizes/')

df1.to_excel('resultados/analise/resultados.xlsx')
