def solution(arr):
    result = []
    for x in arr:
        if result[-1:] == [x]: continue
        result.append(x)
    return result