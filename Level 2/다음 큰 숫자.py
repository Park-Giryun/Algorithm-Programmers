# 0917
# 다음 큰 숫자
def solution(n):
    temp = bin(n).count('1')
    for m in range(n+1, 1000001):
        if bin(m).count('1') == temp:
            return m