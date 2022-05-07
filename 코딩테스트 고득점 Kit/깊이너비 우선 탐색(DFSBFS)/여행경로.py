from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for x, y in tickets:
        graph[x].append(y)
    for x in graph.keys():
        graph[x].sort()

    def dfs(graph, n, key, footprint):

        if len(footprint) == n + 1:
            return footprint

        for idx, country in enumerate(graph[key]):
            graph[key].pop(idx)

            tmp = footprint[:]
            tmp.append(country)

            ret = dfs(graph, n, country, tmp)

            graph[key].insert(idx, country)

            if ret:
                return ret

    answer = dfs(graph, len(tickets), "ICN", ["ICN"])

    return answer