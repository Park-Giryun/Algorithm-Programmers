def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    # 플로이드 워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # a->b,b->c이면 table[a][c] 와 table[c][a] 의 값이 승패 기록을 위해 같이 기록
                if (0 < graph[i][k] < INF and 0 < graph[k][j] < INF) or (graph[i][k] < 0 and graph[k][j] < 0):
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    continue

    for i in range(1, n + 1):
        if INF not in graph[i][1:]:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 회고: 알게된 접근법으로 풀었다
# 접근법: 선수가 총 n명이 존재할 때, 다른 n-1명의 선수들과의 승패를 확실하게 알 수만 있으면 순위가 정해집니다.
# 예를 들어, 총 5명의 선수가 있을 때, 1번 선수의 순위가 확실시 되는지를 알고 싶다면, 나머지 2번부터 5번까지 선수와의 경기 승패결과가 모두 있어야 합니다.
# 그렇지만 주어진 간선정보만으로는 충분하지 않습니다.
# 가령 results= [[1,2],[2,3]] 의 경우, 우리는 직관적으로는 '1번 선수가 3번 선수도 이겼네' 라고 알 수 있지만, [1,2] 간선은 results에서는 주어지지 않았고, 이 점이 우리가 그래프를 만들 때 난관으로 작용합니다.
# 그리고 이 부분이 우리가 이제껏 배운 알고리즘 개념이 적용되는 부분입니다.
# 우리가 배웠던 그래프, 최단거리 알고리즘 중에서 특정 정점에서 모든 정점을 거쳐 다른 정점까지의 최단거리를 구했던 알고리즘이 있습니다.
# 바로 플로이드-워셜 알고리즘이지요. 그렇지만 이 문제는 최단거리를 구하는 문제는 아닙니다.
# 이 문제에서 위 알고리즘이 적용되는 부분은, 2차원 배열 그래프에 모든 선수들 끼리의 '승리와 패배를 동시에 기록'하는 것입니다.
# 즉, a->b,b->c이면 table[a][c] 와 table[c][a] 의 값이 승패 기록을 위해 같이 기록되어야 한다는 것입니다.
# 그리고 a->b이지만 b<-c인 경우에 a와 c의 승패는 알 수 없다는 점도 기억해야 합니다.