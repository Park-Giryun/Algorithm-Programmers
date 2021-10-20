# 1020
# n진수 게임
# idea: 구현
def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]

def solution(n, t, m, p):
    answer = ''
    temp = ''
    for i in range(t * m): # 모든 턴의 답
        temp += convert(i, n)
    for i in range(p - 1, t * m, m): # 튜브의 답
        answer += temp[i]
    return answer

print(solution(2, 4, 2, 1))