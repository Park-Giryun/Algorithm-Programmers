# 경우의 수
def solution(clothes):
    answer = {}
    for n, k in clothes:
        if k in answer:
            answer[k] += 1
        else:
            answer[k] = 1
    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))