#10. Crie dois arrays e calcule o produto escalar entre eles.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

p_escalar = np.dot(arr1,arr2)
print(f"Produto Escalar:{p_escalar}")
