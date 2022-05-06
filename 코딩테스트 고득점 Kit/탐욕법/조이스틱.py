def solution(name):
    change = [min(ord(x) - ord('A'), ord('Z') - ord(x) + 1) for x in name]
    answer = 0
    i = 0
    while True:
        answer += change[i]
        change[i] = 0
        if change.count(0) == len(name):
            return answer
        left, right = 1, 1
        while change[i-left] == 0:
            left += 1
        while change[i+right] == 0:
            right += 1
        answer += left if left < right else right
        i += -left if left < right else right
    return answer