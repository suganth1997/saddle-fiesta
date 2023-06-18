import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import cg

P = np.array([[4, 2],
              [2, 0]])

A = csc_matrix(P)
b = np.array([-2, -0.5])

x = cg(A, b, x0 = [0.25, -1.5])

print(x)
