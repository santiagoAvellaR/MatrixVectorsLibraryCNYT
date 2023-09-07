# importing numpy as library
import numpy as np

# creating matrix of complex number
x = np.array([2 + 3j, 4 + 5j])
print("Printing First matrix:")
print(x)

y = np.array([8 + 7j, 5 + 6j])
print("Printing Second matrix:")
print(y)

# vector dot product of two matrices
z = np.vdot(x, y)
print("Product of first and second matrices are:")
print(z)

print([[(0,0) for j in range(5)] for i in range(3)])