import heapq

def solution(jobs):
    answer = 0
    start, time, cnt = -1, 0, len(jobs)
    heap = []
    while cnt > 0:
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, (j[1], j[0]))
        if len(heap) > 0:
            now = heapq.heappop(heap)
            start = time
            time += now[0]
            answer += (time - now[1])
            cnt -= 1
        else:
            time += 1
    return int(answer / len(jobs))