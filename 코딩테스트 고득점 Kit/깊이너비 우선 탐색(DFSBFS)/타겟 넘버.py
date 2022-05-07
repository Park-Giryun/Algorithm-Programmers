def solution(numbers, target):
    answer = 0
    n = len(numbers)
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


def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])