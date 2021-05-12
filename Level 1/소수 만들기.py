from itertools import combinations
def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def solution(nums):
    data = list(combinations(nums, 3))
    count = 0
    for x in data:
        if isPrime(sum(x)) == True:
            count += 1
    return count