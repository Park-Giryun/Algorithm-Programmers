# 0920
# 숫자의 표현
def solution(n):
    return len([i for i in range(1, n+1, 2) if n % i is 0])