# 0905
# 삼각 달팽이
# idea: 리스트 합치기: sum(list, [])
def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1, n+1)] # 삼각형 구조 만들기
    x, y = -1, 0 # 좌표 초기화, 처음 시작은 아래로 내려가므로 x = -1
    num = 1
    for i in range(n): # 방향
        for _ in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            else: # 위
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1

    return sum(answer, [])

print(solution(6))