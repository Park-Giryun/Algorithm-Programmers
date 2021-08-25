# 0825
# 멀쩡한 사각형
# idea: 3진법
def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]