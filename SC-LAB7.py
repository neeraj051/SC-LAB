import numpy as np

def obj(x):
    return x**2 + 5*np.sin(x)

wolves = np.random.uniform(-10, 10, 5)
print(wolves)
alpha = min(wolves, key=obj)

for i in range(20):
    a = 2 - i * (2/20)
    for i in range(len(wolves)):
        r1, r2 = np.random.rand(), np.random.rand()
        A = 2 * a * r1 - a
        C = 2 * r2
        D = abs(C * alpha - wolves[i])
        wolves[i] = alpha - A * D
    alpha = min(wolves, key=obj)

print("Best solution:", alpha)
