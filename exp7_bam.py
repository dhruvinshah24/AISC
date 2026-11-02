X = [1, -1, 1]
Y = [1, 1]

weights = []

for i in range(len(X)):
    row = []
    for j in range(len(Y)):
        row.append(X[i] * Y[j])
    weights.append(row)

Y_result = []

for j in range(len(Y)):
    net = 0
    for i in range(len(X)):
        net += X[i] * weights[i][j]
    Y_result.append(1 if net >= 0 else -1)

X_result = []

for i in range(len(X)):
    net = 0
    for j in range(len(Y)):
        net += weights[i][j] * Y_result[j]
    X_result.append(1 if net >= 0 else -1)

print("Input X:", X)
print("Target Y:", Y)
print("Weight Matrix:")
for row in weights:
    print(row)
print("Forward Recall Y:", Y_result)
print("Backward Recall X:", X_result)
