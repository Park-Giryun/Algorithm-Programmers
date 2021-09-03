# 0904
# 피보나치 수
# idea: 다이나믹 프로그래밍
def solution(n):
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        d[i] = d[i-2] + d[i-1]
    return d[n] % 1234567

print(solution(3))