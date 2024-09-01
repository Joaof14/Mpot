### Descrição do Projeto

Este projeto implementa o **Método da Potência** para calcular autovalores dominantes de uma matriz, e busca acelerar a convergência desse método utilizando técnicas baseadas no **Método dos Mínimos Quadrados (MMQ)**. O projeto inclui diversas tentativas de aceleração aplicadas ao Método da Potência, como Aitken e diferentes variações de MMQ (linear, logarítmica, exponencial, geométrica, etc.).

### Funcionalidades

- **Método da Potência**: Cálculo do autovalor dominante utilizando iterações simples.
- **Aceleração com Aitken**: Aplicação da técnica de Aitken para acelerar a convergência do Método da Potência.
- **Aceleração com MMQ**: Utilização de diferentes abordagens de MMQ para prever autovalores futuros com base em iterações anteriores, reduzindo o número de iterações necessárias.

### Implementação

O projeto é implementado em Python e utiliza a biblioteca NumPy para operações de álgebra linear. Cada técnica de aceleração está encapsulada em uma função específica:

- `metodo_da_potencia`: Implementação básica do Método da Potência.
- `Aitken`: Implementação do método de aceleração de Aitken.
- `mp_mmq_linear`: Aceleração com MMQ utilizando uma abordagem linear.
- `mp_mmq_logaritmo`: Aceleração com MMQ utilizando uma abordagem logarítmica.
- `mp_mmq_exponencial`: Aceleração com MMQ utilizando uma abordagem exponencial.
- `mp_mmq_geometrico`: Aceleração com MMQ utilizando uma abordagem geométrica.

### Uso

Para utilizar os métodos, basta importar as funções e aplicá-las a uma matriz `A` e um vetor inicial `yo`. Cada função retorna o número de iterações realizadas, o erro associado à última iteração e o autovalor dominante calculado.

```python
from metpot import *

# Exemplo de uso
A = np.array([[2, 1], [1, 3]])
yo = np.array([1, 0])
resultado = mp_mmq_linear(A, yo)
print(f"Autovalor: {resultado[2]}, Erro: {resultado[1]}, Iterações: {resultado[0]}")
```

### Referências

FRANCO, N. M. B. Cálculo Numérico. 1. ed. São Paulo: Pearson, 2006. ISBN 8576050870.
ARNALES, Selma; DAREZZO, Artur. Cálculo Numérico: Aprendizagem com Apoio de Software. 1. ed. Rio de Janeiro: Editora ABC, 2015.
Richard L. Burden e J. Douglas Faires. Análise Numérica. 9ª ed. Cengage Learning, 2010.
788 pp.

### Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas na seção de issues.


