#!pip install pandas

#!pip install numpy

import pandas as pd
import numpy as np
import math


# Criar um array bidimensional com dados diferentes dos utilizados em sala
array_bi = np.array([[20,35,44],[100,200,300]])
print(f"O array bidimensional é :\n {array_bi}")

print('\n--------------------------------------------------------------------')

# Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis);
print(f" A media de cada linha da matriz é dada por :\n {array_bi.mean(axis=1)}")
print(f" O valor maximo de cada linha é dado por :\n {array_bi.max(axis=1)}")
desvio_padrao = np.std(array_bi)
print(" O valor do desvio padrao do array é dado por :\n",desvio_padrao)

print('\n--------------------------------------------------------------------')
# Obter a transposta da matriz e realizar uma operação com ela;
matriz_t = np.transpose(array_bi)
print(f" O valor da raiz quadrada de cada elemento da matriz transposta é dada por :\n {np.sqrt(matriz_t)}")

print('\n--------------------------------------------------------------------')

# Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
m1 = np.array([[10, 20, 30], [30, 40, 50]])
m2 = np.array([[5, 10, 15], [15, 20, 25]])

if m1.shape == m2.shape:
    produto_escalar = np.sum(m1 * m2)
    print(f"O Produto Escalar das Matrizes se mostra como: \n{produto_escalar}")
else:
    print("As matrizes não têm as mesmas dimensões logo não podem ser multiplicadas.\n")

print('\n--------------------------------------------------------------------')

# Criar um filtro para a sua matriz;
print(f'Filtro 1:\n {m1[m1<25]}')

print('\n--------------------------------------------------------------------')

# Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
print(f'Um exemplo de operação aritmética m1 * m2 tem como resultado : \n {m1 * m2}')

print('\n--------------------------------------------------------------------')