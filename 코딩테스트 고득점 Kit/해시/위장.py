# 경우의 수
from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter([k for v, k in clothes])
    for v in counter.values():
        answer *= v + 1
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))