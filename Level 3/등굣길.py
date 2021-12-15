def solution(m, n, puddles):
    puddles = [[y, x] for x, y in puddles]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    B[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                B[i][j] = 0
            else:
                B[i][j] = (B[i - 1][j] + B[i][j - 1]) % 1000000007
    return B[n][m]