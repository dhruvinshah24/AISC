import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


x1 = 0.5
x2 = 0.8
target = 1

w11, w21 = 0.2, 0.3
w12, w22 = 0.4, 0.5
v1, v2 = 0.6, 0.7

b1 = b2 = bo = 0.1
learning_rate = 0.5

for epoch in range(1, 6):
    h1 = sigmoid(x1 * w11 + x2 * w21 + b1)
    h2 = sigmoid(x1 * w12 + x2 * w22 + b2)
    output = sigmoid(h1 * v1 + h2 * v2 + bo)

    error = target - output

    delta_output = error * output * (1 - output)
    delta_h1 = h1 * (1 - h1) * delta_output * v1
    delta_h2 = h2 * (1 - h2) * delta_output * v2

    v1 += learning_rate * delta_output * h1
    v2 += learning_rate * delta_output * h2
    bo += learning_rate * delta_output

    w11 += learning_rate * delta_h1 * x1
    w21 += learning_rate * delta_h1 * x2
    b1 += learning_rate * delta_h1

    w12 += learning_rate * delta_h2 * x1
    w22 += learning_rate * delta_h2 * x2
    b2 += learning_rate * delta_h2

    print("Epoch:", epoch, "Output:", round(output, 4),
          "Error:", round(error, 4))

h1 = sigmoid(x1 * w11 + x2 * w21 + b1)
h2 = sigmoid(x1 * w12 + x2 * w22 + b2)
final_output = sigmoid(h1 * v1 + h2 * v2 + bo)

print("\nFinal Output:", round(final_output, 4))
