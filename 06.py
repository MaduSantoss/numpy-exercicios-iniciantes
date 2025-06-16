#6. Crie um array com os números de 1 a 10 e calcule: soma, média e desvio-padrão.

import numpy as np 

array = np.array([1,2,3,4])

print(array)

soma = np.sum(array)
print(f"SOMA DO ARRAY:{soma}")

media = np.mean(array)
print(f"MÉDIA DO ARRAY:{media}")

d_padrao = np.std(array)
print(f"Desvio padrão:{d_padrao}")
