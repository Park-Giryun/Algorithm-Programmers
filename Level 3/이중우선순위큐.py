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

print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))