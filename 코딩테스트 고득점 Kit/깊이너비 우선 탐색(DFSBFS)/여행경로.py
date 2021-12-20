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