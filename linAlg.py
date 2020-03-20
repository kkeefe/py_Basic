#!/usr/bin/env python3

# from scipy import linalg
from scipy.sparse import linalg
import numpy as np

matrix1 = np.matrix('1.3 0.6; 4.7 1.5; 3.1 5.2')
print(matrix1)
b = np.array([3.3, 13.5, -0.1])
print(b)

print("least squares solution is:")
matrix = np.loadtxt('matrix.txt', usecols=range(3))
print(matrix)
print(linalg.lsqr(matrix1, b)[0])
