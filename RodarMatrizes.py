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
coluna_erro = []

#MP = ['Metodo da Potencia', 'MMQ_Linear', 'MMQ_Logaritmo', 'MMQ_Exponencial', 'MMQ_Potencial', 'MMQ_Geometrico', 'MMQ_Polinomial']

metodosDaPotencia = {'MP': metodo_da_potencia,
         'MP_Aitken': Aitken
         }

metodoMinQua = {
    'Linear': lin,
    'Logaritmo': logaritmo,
    'Exponencial': exponencial,
    'Geometrico': geometrico,
    'Potencial': potencial,
    'Polinomial': polinomial
}
coluna_nomes2 = []
coluna_metodo2 = []
coluna_parametro_seg_grau = []
coluna_parametro_p_grau = []
coluna_parametro_ind = []
coluna_ajuste = []
coluna_r2 = []
coluna_erroMMQ = []

caminho = 'matrizes/slot_artigo/'
arquivos_na_pasta = glob.glob(os.path.join(caminho, '*'))



for arquivo in arquivos_na_pasta:
    ordem, _, _, _, campo, simetria = scipy.io.mminfo(arquivo)
    matriz = scipy.io.mmread(arquivo)
    matriz.A
    A = np.array(matriz.A)
    n = A.shape[0]
    yo = np.ones(n)
    



    for nomeMetodo, metodo in metodosDaPotencia.items():

        coluna_nomes.append(arquivo)
        coluna_ordem.append(ordem)
        coluna_campo.append(campo)
        coluna_simetria.append(simetria)
        coluna_acelera.append(nomeMetodo)

        inicio = time.time()
        i, e, autovls, autovetor = metodo(A,yo, p=0.00001)
        fim = time.time()
        coluna_ite.append(i)
        coluna_autovalor.append(autovls[-1])
        
        coluna_tempo.append(fim - inicio)
        
        for ajuste, mmq in metodoMinQua.items():
            
            coluna_ajuste.append(ajuste)
            coluna_nomes2.append(arquivo)
            coluna_metodo2.append(nomeMetodo)
            p2, p1, p0, r2 = mmq(np.arange(1, i+1), autovls)
            coluna_parametro_seg_grau.append(p2)
            coluna_parametro_p_grau.append(p1)
            coluna_parametro_ind.append(p0)
            coluna_r2.append(r2)


        graf, eix = plt.subplots()
        eix.scatter(np.arange(1,i), np.array(autovls[1:])/(10**9))
        eix.set_xlabel('Iterações')
        eix.set_ylabel('Autovalores (x 10⁹)')
        eix.set_title(arquivo[21:-4])
        eix.ticklabel_format(style='plain', axis='y')
        graf.savefig(arquivo+'_' + nomeMetodo +'.png')

            
            


"""
fig, ax = plt.subplots()
ax.scatter(np.arange(1, i), autovls[1:])
ax.set_xlabel('Iterações')
ax.set_ylabel('Autovalores')
ax.set_title('Título do Gráfico')
ax.ticklabel_format(style='plain', axis='y')  # Removendo a notação científica do eixo y

# Formatando os valores do eixo y com 4 casas decimais
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.4f}".format(x)))

dados1 = {
    'Matriz': coluna_nomes,
    'Método': coluna_acelera,
    'Autovalor': coluna_autovalor,
    'Iterações': coluna_ite,
    'Tempo': coluna_tempo, 
    'Ordem': coluna_ordem,
    'Campo': coluna_campo,
    'Simetria': coluna_simetria
}

dados2 = {
    'Matriz': coluna_nomes2,
    'Metodo': coluna_metodo2,
    'r2': coluna_r2,
    'ajuste': coluna_ajuste,
    'segundo grau': coluna_parametro_seg_grau,
    'primeiro grau': coluna_parametro_p_grau,
    'independente': coluna_parametro_ind
}


df1 = pd.DataFrame(dados1)

df2 = pd.DataFrame(dados2)

df1['Matriz'] = df1['Matriz'].str.lstrip('matrizes/slot_artigo/')

df1.to_excel('resultados/resultados_slot_artigo.xlsx')

df2['Matriz'] = df2['Matriz'].str.lstrip('matrizes/slot_artigo/')

df2.to_excel('resultados/comportamentoMMQ_slot_artigo.xlsx')

""" 