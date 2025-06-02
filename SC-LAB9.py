import numpy as np

X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
Y = np.array([1, -1, -1, -1])
W = np.zeros(2)

for i in range(len(X)):
    W += X[i] * Y[i]

print("Weight vector using Hebb's Rule:", W)
