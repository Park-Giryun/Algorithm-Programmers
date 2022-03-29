from itertools import permutations


def solution(numbers):
    answer = 0
    pm = []
    for i in range(len(numbers)):
        pm += list(permutations(list(numbers), i + 1))
    nums = list(set(int(''.join(p)) for p in pm))

    for n in nums:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                check = False
                break
        if check:
            answer += 1
    return answer