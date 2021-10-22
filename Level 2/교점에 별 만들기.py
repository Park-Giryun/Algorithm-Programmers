# 1022
# 교점에 별 만들기
# idea: 구현

def solution(line):
    arr = []
    INF = float('inf')
    minx, maxx, miny, maxy = INF, -INF, INF, -INF
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E, C, D, F = *line[i], *line[j]
            d = A * D - B * C
            if d == 0: continue
            x, y = (B * F - E * D) / d, -(E * C - A * F) / d
            if x != int(x) or y != int(y): continue
            x, y = int(x), int(y)
            minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
            arr.append((x, y,))
    answer = [['.'] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]
    for x, y in arr: answer[y - miny][x - minx] = '*'
    return ["".join(a) for a in answer]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))

# 회고: 배열로 나타낼 때 y값은 x 값과 달리 배열과 부호가 반대임을 늦게 인지해서 시간을 잡아먹었다.
# 또한 인덱스 접근도 신경 써줘야함을 알았다.
# 교점 판별식 중에서 A * B * D - A * B * C 라고 하면 A B D가 각 100,000인 최댓값이고, C가 0이라면
# 결국 가장 큰 값인 (105)3 = 1015 = 1,000,000,000,000,000가 된다.
# 이럴 경우, 오버플로우가 됐거나 MAX, MIN 값을 너무 작은 것인지 한 번 확인할 것.