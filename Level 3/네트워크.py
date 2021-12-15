from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(a):
        nonlocal n, computers, visited
        q = deque([a])
        while q:
            x = q.popleft()
            visited[x] = True
            for y in range(n):
                if y != x and computers[x][y] == 1 and not visited[y]:
                    q.append(y)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(5, [[1,1,1,0,0], [1,1,0,0,0], [1,0,1,0,0], [0,0,0,1,1], [0,0,0,1,1]]))