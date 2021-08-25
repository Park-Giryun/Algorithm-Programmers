# 0826
# 메뉴 리뉴얼
# idea: counter 사용
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            temp += comb
        menu = Counter(temp).most_common()
        answer += ["".join(m) for m, cnt in menu if cnt > 1 and cnt == menu[0][1]]
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))