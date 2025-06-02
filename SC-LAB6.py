import numpy as np

def f(x):
    return x**2 + 4*x + 4

pos = np.random.uniform(-10, 10, 10)
print(pos)
vel = np.zeros(10)
print(vel)
pbest = pos
gbest = min(f(pbest))
print(gbest)
for _ in range(50):
    r1, r2 = np.random.rand(), np.random.rand()
    vel = 0.5*vel + 0.8*r1*(pbest - pos) + 0.9*r2*(gbest - pos)
    pos += vel
    for i in range(len(pos)):
      if(pos[i]<pbest[i]):
        pbest[i]=pos[i]
        i=i+1
      else:
        pbest[i]=pbest[i]
        i=i+1
    gbest = pbest[np.argmin(f(pbest))]

print("Best solution found:", gbest)
