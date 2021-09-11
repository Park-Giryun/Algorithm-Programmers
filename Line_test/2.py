from collections import Counter

def solution(research, n, k):
    answer = []
    temp = []
    for re in research:
        for key, v in Counter(re).items():
            if v >= k:
                temp.append(key)
    arr = Counter(temp).most_common()
    answer += sorted(["".join(key) for key, v in arr if v >= n and v == arr[0][1]])
    return answer[0]

from itertools import combinations
from collections import Counter

def solution(research, n, k):
    answer = []
    for cb in combinations(research, n):
        temp = []
        tmp = dict()
        for re in cb:
            for key, v in Counter(re).items():
                tmp[key] = 0
                temp.append((key, v))
        for key, v in temp:
            tmp[key] += v
        for key, v in tmp.items():
            if v >= 2 * n * k:
                answer.append(key)
    if len(answer) == 0:
        return "None"
    return Counter(answer).most_common()[0][0]

print(solution(["yxxy","xxyyy","yz"], 2, 1))