# 0829
# 소수 찾기

from itertools import permutations

def prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, n ** 0.5 + 1):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))
        for a in arr:
            a = int(''.join(a))
            if prime(a):
                answer.append(a)
    return len(set(answer))

print(solution("17"))