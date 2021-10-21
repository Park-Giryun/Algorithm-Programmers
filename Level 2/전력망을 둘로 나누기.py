# 1021
# 전력망을 둘로 나누기
# idea: 서로소 집합 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def uion_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    answer = []

    for i in range(n - 1):
        parent = [x for x in range(n + 1)]
        for wire in wires[:i]+wires[i+1:]:
            a, b = wire[0], wire[1]
            uion_parent(parent, a, b)

        for j in range(1, n + 1):
            find_parent(parent, j)
        one = parent.count(1)
        two = n - one

        answer.append(abs(one - two))
    return min(answer)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))