# 0904
# 행렬의 곱셈
def solution(a, b):
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))