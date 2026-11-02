                                              
                                                              

                                                              
                              
                                     
                                                              

print("\n========== PART A: FUZZY SET OPERATIONS ==========")

A = [0, 0.75, 1, 0.5, 0]
B = [0, 0.25, 0.75, 1, 0.5]

union = []
intersection = []

for i in range(len(A)):
    union.append(max(A[i], B[i]))
    intersection.append(min(A[i], B[i]))

complement_A = [1 - x for x in A]
complement_B = [1 - x for x in B]
complement_union = [1 - x for x in union]
complement_intersection = [1 - x for x in intersection]

print("A =", A)
print("B =", B)
print("A union B =", union)
print("A intersection B =", intersection)
print("Complement of A =", complement_A)
print("Complement of B =", complement_B)
print("Complement of union =", complement_union)
print("Complement of intersection =", complement_intersection)


                                                              
                                    
                                                                   
                                                              

print("\n========== PART B: FUZZY ALGEBRAIC OPERATIONS ==========")

A = [0.2, 0.3, 0.4, 0.5]
B = [0.1, 0.2, 0.2, 1.0]

algebraic_sum = []
algebraic_product = []
bounded_sum = []
bounded_difference = []

for i in range(len(A)):
    a = A[i]
    b = B[i]

    algebraic_sum.append(round(a + b - a * b, 2))
    algebraic_product.append(round(a * b, 2))
    bounded_sum.append(round(min(1, a + b), 2))
    bounded_difference.append(round(max(0, a - b), 2))

print("A =", A)
print("B =", B)
print("Algebraic Sum =", algebraic_sum)
print("Algebraic Product =", algebraic_product)
print("Bounded Sum =", bounded_sum)
print("Bounded Difference =", bounded_difference)


                                                              
                                 
                                                              
                                                              

print("\n========== PART C: FUZZY CARTESIAN PRODUCT ==========")

A = [0.3, 0.7, 1.0]
B = [0.4, 0.9]

relation = []

for i in range(len(A)):
    row = []
    for j in range(len(B)):
        row.append(min(A[i], B[j]))
    relation.append(row)

print("Set A =", A)
print("Set B =", B)
print("Cartesian Product Matrix:")
for row in relation:
    print(row)


                                                              
                                    
                                     
                                                              

print("\n========== PART D: FUZZY RELATION COMPOSITION ==========")

R = [
    [0.6, 0.3],
    [0.2, 0.9]
]

S = [
    [1.0, 0.5, 0.3],
    [0.8, 0.4, 0.7]
]

max_min = []

for i in range(len(R)):
    row = []
    for j in range(len(S[0])):
        values = []
        for k in range(len(S)):
            values.append(min(R[i][k], S[k][j]))
        row.append(max(values))
    max_min.append(row)

max_product = []

for i in range(len(R)):
    row = []
    for j in range(len(S[0])):
        values = []
        for k in range(len(S)):
            values.append(R[i][k] * S[k][j])
        row.append(round(max(values), 2))
    max_product.append(row)

print("Max-Min Composition:")
for row in max_min:
    print(row)

print("\nMax-Product Composition:")
for row in max_product:
    print(row)
