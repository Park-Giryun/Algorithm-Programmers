# 0825
# 더 맵게
# idea: 우선 순위 큐 사용
import heapq

def solution(scoville, K):
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)

    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (2 * heapq.heappop(heap)))
        except IndexError:
            return -1
        cnt += 1

    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))