pattern = [1, -1, 1, -1, 1]
noisy_input = [-1, -1, 1, -1, 1]
n = len(pattern)

weights = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            weights[i][j] = pattern[i] * pattern[j]

recalled = []

for i in range(n):
    net = 0
    for j in range(n):
        net += weights[i][j] * noisy_input[j]
    recalled.append(1 if net >= 0 else -1)

print("Original Pattern:", pattern)
print("Noisy Input:", noisy_input)
print("Recalled Pattern:", recalled)
