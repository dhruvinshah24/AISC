X = [[0, 0], [0, 1], [1, 0], [1, 1]]
T = [0, 0, 0, 1]

w1 = 0.0
w2 = 0.0
bias = 0.0
learning_rate = 0.1

print("EPOCH    MEAN SQUARED ERROR")

for epoch in range(1, 21):
    total_error = 0.0

    for i in range(len(X)):
        x1, x2 = X[i]
        yin = x1 * w1 + x2 * w2 + bias
        error = T[i] - yin

        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        bias += learning_rate * error

        total_error += error ** 2

    mse = total_error / len(X)
    print(epoch, round(mse, 4))

print("\nFINAL WEIGHTS:", round(w1, 4), round(w2, 4))
print("FINAL BIAS:", round(bias, 4))

print("\nPREDICTIONS")
for i in range(len(X)):
    x1, x2 = X[i]
    yin = x1 * w1 + x2 * w2 + bias
    output = 1 if yin >= 0.5 else 0
    print(X[i], "Target:", T[i], "Output:", output)
