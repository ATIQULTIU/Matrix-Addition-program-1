# Matrix Addition Program (Without NumPy)
# Author: MD. Atiqul Islam (Atik)
# Email: atikcmttiu1001@gmail.com

# First matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second matrix
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Empty result matrix
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Matrix addition using loops
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nResult (Addition):")
for row in result:
    print(row)