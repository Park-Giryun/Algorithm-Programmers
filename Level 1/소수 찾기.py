# 0823
# 소수 찾기
def solution(n):
    cnt = [True] * (n + 1)
    for i in range(2, n + 1):
        if cnt[i] == True:
            for j in range(i + i, n + 1, i):
                cnt[j] = False
    answer = 0
    for i in range(2, n + 1):
        if cnt[i]:
            answer += 1
    return answer