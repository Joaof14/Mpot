import numpy as np
from metpot import metodo_da_potencia, Aitken, mp_mmq_linear, mp_mmq_logaritmo, mp_mmq_exponencial, mp_mmq_potencial, mp_mmq_geometrico, mp_mmq_polinomial
import scipy
from io import StringIO
import os
import glob
import pandas as pd


#defina estrategia: 
#o inicio deve ser maior que a quantidade de pontos estimados
inicio = 6
quantidade = 5
previsao_a_frente = 3



# Listas para armazenar os resultados
coluna_nomes = []       # Nome do arquivo
coluna_acelera = []     # Método de aceleração
coluna_ordem = []       # Ordem da matriz
coluna_campo = []       # Campo
coluna_simetria = []    # Simetria
coluna_ite = []         # Número de iterações
coluna_autovalor = []   # Autovalor
coluna_erro = []        # Erro

#acels = ['Nenhuma', 'MMQ_Linear', 'MMQ_Logaritmo', 'MMQ_Exponencial', 'MMQ_Potencial', 'MMQ_Geometrico', 'MMQ_Polinomial']

# Dicionário mapeando o nome do método de aceleração para a função correspondente
acels = {'Nenhuma': metodo_da_potencia,
         'Aitken': Aitken,
          'MMQ_Linear': mp_mmq_linear,
          'MMQ_Logaritmo': mp_mmq_logaritmo ,
          #'MMQ_Exponencial': mp_mmq_exponencial ,
          'MMQ_Potencial': mp_mmq_potencial ,
          #'MMQ_Geometrico': mp_mmq_geometrico ,
          'MMQ_Polinomial': mp_mmq_polinomial ,
         }

# Diretórios onde estão armazenados os arquivos de matriz
slots = ['slot01','slot02', 'slot03', 'slot04', 'slot06', 'slot09', 'slot10', 'slot11']

# Itera sobre cada diretório ('slot')
for slot in slots:
    caminho = 'matrizes/' + slot + '/'
    arquivos_na_pasta = glob.glob(os.path.join(caminho, '*'))

    # Itera sobre cada arquivo na pasta
    for arquivo in arquivos_na_pasta:
        # Obtém informações sobre a matriz
        ordem, _, _, _, campo, simetria = scipy.io.mminfo(arquivo)
        # Lê a matriz
        matriz = scipy.io.mmread(arquivo)
        matriz.A
        A = np.array(matriz.A)
        n = A.shape[1]
        yo = np.ones(n)

        # Itera sobre cada método de aceleração
        for acel, metodo in acels.items():

            # Armazena as informações relevantes em listas
            coluna_nomes.append(arquivo)
            coluna_ordem.append(ordem)
            coluna_campo.append(campo)
            coluna_simetria.append(simetria)
            coluna_acelera.append(acel)
            
            # Executa o método de aceleração e armazena os resultados
            i, e, autovalor, autovls = metodo(A, yo, p=0.00001, inicio_acel=inicio, pontos = - quantidade, prev = previsao_a_frente)
            coluna_ite.append(i)
            coluna_autovalor.append(autovalor)
            coluna_erro.append(e)

# Organiza os dados em um dicionário
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

# Cria um DataFrame do Pandas com os dados
df1 = pd.DataFrame(dados)
estrategia = f"Inicio{inicio}-Ultimos{quantidade}-prev{previsao_a_frente}"
# Salva os resultados em um arquivo Excel
df1.to_excel('resultados' + estrategia + '.xlsx')