# 0823
# 최대공약수와 최소공배수
def solution(n, m):
    tmp = n * m
    while m:
        n, m = m, n % m
    answer = [n, tmp // n]
    return answer