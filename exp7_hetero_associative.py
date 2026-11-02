X = [1, -1, 1]
Y = [1, 1]

weights = []

for i in range(len(X)):
    row = []
    for j in range(len(Y)):
        row.append(X[i] * Y[j])
    weights.append(row)

output = []

for j in range(len(Y)):
    net = 0
    for i in range(len(X)):
        net += X[i] * weights[i][j]
    output.append(1 if net >= 0 else -1)

print("Input Pattern:", X)
print("Target Pattern:", Y)
print("Weight Matrix:")
for row in weights:
    print(row)
print("Recalled Output:", output)
