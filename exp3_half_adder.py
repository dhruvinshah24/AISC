def neuron(inputs, weights, threshold):
    total = sum(x * w for x, w in zip(inputs, weights))
    return 1 if total >= threshold else 0


def AND(a, b):
    return neuron([a, b], [1, 1], 2)


def OR(a, b):
    return neuron([a, b], [1, 1], 1)


def NAND(a, b):
    return neuron([a, b], [-1, -1], -1)


def XOR(a, b):
    n = NAND(a, b)
    return OR(AND(a, n), AND(b, n))


print("HALF ADDER")
print("A B | SUM CARRY")

for a in [0, 1]:
    for b in [0, 1]:
        sum_bit = XOR(a, b)
        carry = AND(a, b)
        print(a, b, "|", sum_bit, "   ", carry)
