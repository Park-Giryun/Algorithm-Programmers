from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            tmp += comb
        menu = Counter(tmp).most_common()
        answer += ["".join(m) for m, cnt in menu if cnt > 1 and cnt == menu[0][1]]
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))