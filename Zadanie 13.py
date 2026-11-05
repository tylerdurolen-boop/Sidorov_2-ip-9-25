m = int(input())
n = int(input())
matrix = [[10 * i for j in range(n)] for i in range(1, m + 1)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
matrix = [[5 * j for j in range(1, n + 1)] for i in range(m)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
values = [int(number) for number in input().split()]
matrix = [[values[i] for j in range(n)] for i in range(m)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
values = [int(number) for number in input().split()]
matrix = [values[:] for i in range(m)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
d = int(input())
values = [int(number) for number in input().split()]
matrix = [[values[i] + d * j for j in range(n)] for i in range(m)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
q = int(input())
values = [int(number) for number in input().split()]
matrix = [[value * q ** i for value in values] for i in range(m)]
for row in matrix:
    print(row)

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([int(number) for number in input().split()])
k = int(input())
print(matrix[k - 1])

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([int(number) for number in input().split()])
k = int(input())
print([row[k - 1] for row in matrix])

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([int(number) for number in input().split()])
for row in matrix[1::2]:
    print(row)

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([int(number) for number in input().split()])
for j in range(0, n, 2):
    for i in range(m):
        print(matrix[i][j])
