def solution(arr):
    arr.sort()

    result = (255, len(arr)) # 임계값, a와 b의 차이
    for i in range(max(arr), 0, -1):
        total = 0
        for x in arr:
            if i > x: total += 1
            else: total -= 1
        if abs(total) <= result[1]:
            result = (i, abs(total))
    return result[0]

print(solution([1,52,125,10,25,201,244,192,128,23,203,98,154,255]))