# Vector
# Vector를 파이썬으로 표현하는 다양한 방법 존재
# 값의 변경 유무, 속성값 유무에 따라 선택할 수 있음
# 기본적으로 list로 vector 연산 사용
# Vector의 덧셈
u = [2, 2]
v = [2, 3]
z = [3, 5]
result = [sum(t) for t in zip(u, v, z)]
print(result)

# Vector의 뺄셈
u = [2, 2, 3]
v = [2, 4, 6]
z = [2, 5, 7]
result = [sum(t) for t in zip(u, v, z)]
sub = result[0]
print(result)

for i, v in enumerate(result):
    result[i] = v - sub
print(result)

# Scalar-Vector
u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha * sum(t) for t in zip(u, v)]
print(result)

# Matrix
matrix_a = [[3, 6], [4, 5]]     # List로 표현
matrix_b = [[5, 8], [6, 7]]     # Tuple로 표현
matrix_c = {(0, 0): 3, (0, 1): 6, (1, 0): 4, (1, 1): 5}     # dict로 표현

# Matrix 덧셈
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

# Scala-Matrix
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]
print(result)

# Matrix Transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

# Matrix의 곱셈
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
