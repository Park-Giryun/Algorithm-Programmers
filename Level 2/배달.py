# 0904
# 배달
# idea: 플로이드 워셜 알고리즘
def solution(n, road, k):
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for i in range(len(road)):
        a, b, c = road[i]
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    for c in range(1, n+1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

    answer = 0
    for x in graph[1][1:]:
        if x <= k:
            answer += 1

    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))