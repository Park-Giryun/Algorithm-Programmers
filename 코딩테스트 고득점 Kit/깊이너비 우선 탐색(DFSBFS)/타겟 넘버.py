def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(i, num):
        if i == n:
            if num == target:
                nonlocal answer
                answer += 1
            return
        dfs(i + 1, num + numbers[i])
        dfs(i + 1, num - numbers[i])
    dfs(0, 0)
    return answer