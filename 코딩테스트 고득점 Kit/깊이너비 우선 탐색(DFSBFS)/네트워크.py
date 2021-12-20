from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque([start])
        while q:
            x = q.popleft()
            visited[x] = True
            for y in range(n):
                if y != x and computers[x][y] and not visited[y]:
                    q.append(y)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer