# Branch `congresso`

Este repositório contém um conjunto de scripts em Python dedicados à execução de métodos numéricos para análise de matrizes, incluindo o Método da Potência e a aplicação de Ajustes por Mínimos Quadrados (MMQ) para modelagem e análise de autovalores.

## Descrição Geral

Este projeto tem como objetivo principal calcular autovalores de matrizes utilizando diferentes métodos numéricos e realizar ajustes estatísticos sobre os resultados obtidos. Os métodos implementados incluem:

- **Método da Potência**: Para calcular o autovalor dominante de uma matriz.
- **Método de Aitken**: Uma variante acelerada do Método da Potência.
- **Ajustes por Mínimos Quadrados (MMQ)**: Diversos ajustes (linear, logarítmico, exponencial, potencial, polinomial e geométrico) são aplicados sobre os autovalores para análise do comportamento das iterações.

## Estrutura de Arquivos

- **`metpot.py`**: Contém as implementações dos métodos da potência e de Aitken para cálculo de autovalores.
- **Scripts principais**: Executam os métodos sobre as matrizes e salvam os resultados em arquivos Excel.
- **Pasta `matrizes/`**: Contém as matrizes utilizadas para os cálculos.
- **Pasta `resultados/`**: Contém os arquivos de resultados gerados pelo script, incluindo os ajustes de MMQ.

## Requisitos

Para rodar os scripts, certifique-se de ter os seguintes pacotes Python instalados:

- `numpy`
- `scipy`
- `pandas`
- `matplotlib`

Você pode instalar os pacotes necessários usando o pip:

```bash
pip install numpy scipy pandas matplotlib
```

## Como Rodar

1. **Executar os Scripts**: Os scripts são configurados para iterar sobre todas as matrizes na pasta `matrizes/slot_artigo/`. Para rodar o script, execute:

   ```bash
   python nome_do_script.py
   ```

2. **Resultados**: Os resultados serão gerados em arquivos Excel na pasta `resultados/`, com informações sobre autovalores, tempos de execução, iterações e ajustes de MMQ.

## Funções Principais

- **`metodo_da_potencia(A, yo, max_it=10000, p=0.00001)`**: Implementa o método da potência para encontrar o autovalor dominante.
  
- **`Aitken(A, yo, max_it=10000, p=0.00001, inicio_acel=4)`**: Implementa o método de Aitken para acelerar a convergência do método da potência.

## Exemplo de Uso

```python
import numpy as np
from metpot import metodo_da_potencia, Aitken

A = np.array([[-4, 14, 0],
              [-5, 13, 0],
              [-1, 0, 2]])

yo = np.ones(A.shape[0])

# Calcular autovalores usando o método da potência
i, erro, autovalores, autovetor = metodo_da_potencia(A, yo, p=1e-4)

# Calcular autovalores usando o método de Aitken
i_aitken, erro_aitken, autovalores_aitken, autovetor_aitken = Aitken(A, yo, p=1e-4)
```

## Autor

Este projeto foi desenvolvido para o congresso, com o objetivo de analisar o comportamento de métodos numéricos aplicados a matrizes.

