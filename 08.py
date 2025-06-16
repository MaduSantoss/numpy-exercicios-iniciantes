#8. Filtre os elementos maiores que 5 de um array.

import numpy as np 

arr = np.array([3, 7, 1, 9, 4, 6])
maiores_5 = (arr[arr > 5])

print(f"Maiores que 5:{maiores_5}")
