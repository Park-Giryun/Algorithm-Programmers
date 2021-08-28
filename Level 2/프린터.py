# 0828
# 프린터
# idea: any 사용
# def solution(priorities, location):
#     stack = []
#     loc = [i for i in range(len(priorities))]
#     while len(priorities) != 0:
#         for p, l in zip(priorities, loc):
#             if p < max(priorities):
#                 priorities.append(priorities.pop(0))
#                 loc.append(loc.pop(0))
#                 break
#             else:
#                 stack.append((p, l))
#                 priorities.pop(0)
#                 loc.pop(0)
#                 break
#     return [idx+1 for idx, x in enumerate(stack) if x[1] == location][0]

def solution(priorities, location):
    answer = 0
    q = [(i, p) for i, p in enumerate(priorities)]
    while True:
        x = q.pop(0)
        if any(x[1] < y[1] for y in q):
            q.append(x)
        else:
            answer += 1
            if x[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))