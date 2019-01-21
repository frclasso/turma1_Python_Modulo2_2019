#!/usr/bin/env python3

matrix = [[1,2,3],[4,5,6],[7,8,9]]

new_matrix = [[row[i] for row in matrix] for i in range(3)]
print(new_matrix)


# transposed = []
# transposed_row=[]
# for i in range(3):
#     for row in matrix:
#         transposed.append(row[i])
#     #transposed.append(transposed_row)
# print(transposed)

matrix2 = [[0 for col in range(4)] for row in range(3)]
print(matrix2)
print()

matrix3 = []
for x in range(3):
    nested = []
    matrix.append(nested)
    for row in range(4):
        nested.append(0)

# matrix3 = []
# for col in range(3):
#     matrix3.append(nested)
#     for row in range(4):
#         matrix3.append(0)
# print(matrix3)