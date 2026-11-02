import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

iris = load_iris()
X = iris.data
y = iris.target
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

map_rows = 10
map_cols = 10
learning_rate = 0.5
initial_radius = max(map_rows, map_cols) / 2
epochs = 100

rng = np.random.default_rng(42)
weights = rng.random((map_rows, map_cols, X.shape[1]))

for epoch in range(epochs):
    rate = learning_rate * (1 - epoch / epochs)
    radius = initial_radius * (1 - epoch / epochs)

    for sample in rng.permutation(X):
        distances = np.linalg.norm(weights - sample, axis=2)
        winner = np.unravel_index(np.argmin(distances), distances.shape)

        for row in range(map_rows):
            for col in range(map_cols):
                distance_to_winner = np.sqrt((row - winner[0]) ** 2 + (col - winner[1]) ** 2)
                if distance_to_winner <= radius:
                    influence = np.exp(-(distance_to_winner ** 2) / (2 * radius ** 2 + 1e-9))
                    weights[row, col] += rate * influence * (sample - weights[row, col])

neuron_labels = np.full((map_rows, map_cols), -1)

for sample, label in zip(X, y):
    distances = np.linalg.norm(weights - sample, axis=2)
    winner = np.unravel_index(np.argmin(distances), distances.shape)
    neuron_labels[winner] = label

plt.figure(figsize=(8, 7))
for row in range(map_rows):
    for col in range(map_cols):
        if neuron_labels[row, col] >= 0:
            plt.scatter(col, row, c=[["red", "green", "blue"][neuron_labels[row, col]]], s=180)
        else:
            plt.scatter(col, row, c="lightgray", s=35)
plt.gca().invert_yaxis()
plt.title("Kohonen Self-Organizing Map - Iris Dataset")
plt.xlabel("Map Column")
plt.ylabel("Map Row")
plt.grid(True)
plt.show()

prototypes_per_class = 1
prototypes = []
prototype_labels = []

for class_label in np.unique(y):
    class_samples = X[y == class_label]
    prototypes.append(class_samples[0].copy())
    prototype_labels.append(class_label)

prototypes = np.array(prototypes, dtype=float)
prototype_labels = np.array(prototype_labels)
lvq_learning_rate = 0.1
lvq_epochs = 100

for epoch in range(lvq_epochs):
    rate = lvq_learning_rate * (1 - epoch / lvq_epochs)
    for index in rng.permutation(len(X)):
        sample = X[index]
        true_label = y[index]
        distances = np.linalg.norm(prototypes - sample, axis=1)
        winner = np.argmin(distances)

        if prototype_labels[winner] == true_label:
            prototypes[winner] += rate * (sample - prototypes[winner])
        else:
            prototypes[winner] -= rate * (sample - prototypes[winner])

predictions = []

for sample in X:
    distances = np.linalg.norm(prototypes - sample, axis=1)
    predictions.append(prototype_labels[np.argmin(distances)])

predictions = np.array(predictions)
accuracy = np.mean(predictions == y) * 100

print("Kohonen SOM")
print("Map dimensions:", map_rows, "x", map_cols)
print("Training samples:", len(X))
print("SOM training completed.")

print("\nLearning Vector Quantization")
print("Number of prototypes:", len(prototypes))
print("Predicted classes:", predictions)
print("Actual classes:", y)
print("Classification accuracy:", round(accuracy, 2), "%")

plt.figure(figsize=(7, 5))
for class_label, color, name in zip([0, 1, 2], ["red", "green", "blue"], iris.target_names):
    plt.scatter(X[y == class_label, 0], X[y == class_label, 1], color=color, label=name, alpha=0.6)
plt.scatter(prototypes[:, 0], prototypes[:, 1], marker="X", s=250, color="black", label="LVQ Prototypes")
plt.title("LVQ Prototypes on Iris Dataset")
plt.xlabel("Normalized Sepal Length")
plt.ylabel("Normalized Sepal Width")
plt.legend()
plt.show()
