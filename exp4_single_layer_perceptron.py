X = [[0, 0], [0, 1], [1, 0], [1, 1]]
T = [0, 0, 0, 1]

w1 = 0.0
w2 = 0.0
bias = 0.0
learning_rate = 0.1

print("EPOCH    W1      W2      BIAS")

for epoch in range(1, 11):
    for i in range(len(X)):
        x1, x2 = X[i]
        yin = x1 * w1 + x2 * w2 + bias
        output = 1 if yin > 0 else 0
        error = T[i] - output

        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        bias += learning_rate * error

    print(epoch, round(w1, 2), round(w2, 2), round(bias, 2))

    correct = True
    for i in range(len(X)):
        x1, x2 = X[i]
        output = 1 if (x1 * w1 + x2 * w2 + bias) > 0 else 0
        if output != T[i]:
            correct = False
            break

    if correct:
        break

print("\nFINAL OUTPUT")
for i in range(len(X)):
    x1, x2 = X[i]
    yin = x1 * w1 + x2 * w2 + bias
    output = 1 if yin > 0 else 0
    print(X[i], "Target:", T[i], "Output:", output)
