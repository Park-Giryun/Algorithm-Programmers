def solution(n):
    result = []
    answer = 0
    while n >= 1:
        result.append(int(n % 3))
        n /= 3
    i = 1
    result.reverse()
    for x in result:
        answer += int(x) * i
        i *= 3
    return answer

print(solution(45))