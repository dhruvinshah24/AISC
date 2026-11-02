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


print("FULL ADDER")
print("A B Cin | SUM CARRY")

for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:
            x = XOR(a, b)
            sum_bit = XOR(x, cin)
            carry = OR(AND(a, b), AND(x, cin))
            print(a, b, cin, "|", sum_bit, "   ", carry)
