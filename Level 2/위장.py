# 0915
# 위장
def solution(clothes):
    answer = {}
    for name, kind in clothes:
        if kind in answer:
            answer[kind] += 1
        else:
            answer[kind] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i + 1)

    return cnt - 1