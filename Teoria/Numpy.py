'''
Pacote Numpy, uma abreviação de Numerical Python.
Este é um dos pacotes mais importantes para processamento numérico no Python. Há a:
Disponibilidade de um poderoso objeto array multidimensional, 
Funções matemáticas sofisticadas para operações com arrays sem a necessidade de utilização de laços for, e 
Recursos de algebra linear e geração de números aleatórios. 

Arrays Numpy podem ter várias dimensões;
Diferente das listas do Python, que podem conter tipos variados em uma mesma sequência, arrays Numpy suportam somente um tipo de dado por vez.

'''

import numpy as np
np.arange(10)


km = np.array([1000,2000,3000])
print(km)
type(km)