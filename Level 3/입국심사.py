# 1021
# 입국심사
# idea: 이진탐색
def solution(n, times):
    ans = 0
    start, end = 0, max(times) * n  # 0부터 가장 오래걸리는 심사관이 모는 사람를 심사하는 데 걸리는 시간
    while start <= end:
        total = 0  # 모든 심사관들이 mid분 동안 심사한 사람의 수
        mid = (start + end) // 2
        for time in times:
            total += mid // time
        if total >= n:  # mid분 동안 심사한 사람의 수가 n명 이상일 경우
            ans = mid
            end = mid - 1
        elif total < n:  # mid분 동안 심사한 사람의 수가 n명 미만일 경우
            start = mid + 1
    return ans

print(solution(6, [7, 10]))
# 회고: 이진 탐색의 범위를 뭘로 할 건지 결정하는 게 제일 중요하다. 이 문제에서는 총 걸리는 시간을 탐색 범위로 잡았다.