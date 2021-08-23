def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(csv_string, keyword):
    answer = 0
    csv_string = csv_string.split('\n')
    graph = [csv_string[i].split(',') for i in range(8)][1:]

    parent = [i for i in range(8)]
    temp = []
    for x in graph[1:]:
        if keyword in x[1]:
            temp.append(x[0])
            answer += int(x[3])

    for x in graph[1:]:
        for i in temp:
            if x[2] == i:
                answer += int(x[3])
    print(answer)
    return answer

csv_string = "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11"
keyword = "아웃"
solution(csv_string, keyword)