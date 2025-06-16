#9. Reshape: transforme um array de 12 elementos em uma matriz 3x4.

import numpy as np 

arr = np.arange(12)
print(f"Array:{arr}")

matriz = arr.reshape(3,4)
print(f"Matriz:\n{matriz}")
