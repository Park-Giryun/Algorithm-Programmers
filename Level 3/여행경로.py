from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for a, b in tickets:
        routes[a].append(b)
    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# 회고: 스택 사용