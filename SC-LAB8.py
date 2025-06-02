from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load real-life Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal/petal length/width)
 # Actual species (not used in clustering)

# Apply Crisp Partitioning using KMeans
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit_predict(X)  # Each point gets a hard cluster label

# Print cluster assignments
print("Cluster labels for each point:", clusters)

# Visualize clusters using two features: petal length and width
plt.scatter(X[:, 2], X[:, 3], c=clusters)
plt.title("Crisp Partitioning (K-Means) on Iris Dataset")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
