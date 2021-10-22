# 1022
# n^2 배열 자르기
# idea: 수학
def solution(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]

print(solution(3, 2, 5))