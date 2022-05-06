import heapq

def solution(operations):
    heap = []
    maxheap = []
    for oper in operations:
        op, v = oper.split(" ")
        if op == "I":
            heapq.heappush(heap, int(v))
            heapq.heappush(maxheap, -int(v))
        else:
            if len(heap) == 0:
                continue
            if v == "1":
                heap.remove(-heapq.heappop(maxheap))
            elif v == "-1":
                maxheap.remove(-heapq.heappop(heap))
    heap.sort()
    return [heap[-1], heap[0]] if len(heap) != 0 else [0, 0]