# 1022
# 가장 먼 노드
# idea: 다익스트라 알고리즘
import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    start = 1
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for e in edge:
        if (e[1], 1) in graph[e[0]]:
            continue
        else:
            graph[e[0]].append((e[1], 1))
        if (e[0], 1) in graph[e[1]]:
            continue
        else:
            graph[e[1]].append((e[0], 1))
    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start)

    distance = distance[1:]
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
