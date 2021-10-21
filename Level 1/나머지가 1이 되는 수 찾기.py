# 1020
# 나머지가 1이 되는 수 찾기
# idea: 구현
def solution(n):
    x = n - 1
    if x % 2 == 0:
        return 2
    for i in range(3, int(x**(1/2))+1):
        if n % i == 1:
            return i
    return x