import numpy as np

num_cities = 5
pheromone = np.ones((num_cities, num_cities))
distance = np.random.randint(1, 100, (num_cities, num_cities)).astype(float)
np.fill_diagonal(distance, np.inf)

for iteration in range(10):
    for ant in range(5):
        path = [0]
        while len(path) < num_cities:
            current = path[-1]
            probs = pheromone[current] / distance[current]
            probs[list(path)] = 0
            next_city = np.argmax(probs)
            path.append(next_city)
        # Update pheromone
        for i in range(len(path)-1):
            pheromone[path[i]][path[i+1]] += 1.0 / distance[path[i]][path[i+1]]

print("Final pheromone matrix:\n", pheromone)
