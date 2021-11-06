from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque((i, p) for i, p in enumerate(priorities))
    while queue:
        i, p = queue.popleft()
        if any(p < q for j, q in queue):
            queue.append((i, p))
        else:
            answer += 1
            if i == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))