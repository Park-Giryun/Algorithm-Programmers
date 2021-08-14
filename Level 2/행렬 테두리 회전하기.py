def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i].append(i*columns + (j+1))

    for x1, y1, x2, y2, in queries:
        tmp = board[x1-1][y1-1]
        min_ = tmp

        # 서쪽 회전
        for k in range(x1-1, x2-1):
            board[k][y1-1] = board[k+1][y1-1]
            min_ = min(min_, board[k][y1-1])

        # 남쪽 회전
        for y in range(y1-1, y2-1):
            board[x2-1][y] = board[x2-1][y+1]
            min_ = min(min_, board[x2-1][y])

        # 동쪽 회전
        for x in range(x2 - 1, x1 - 1, -1):
            board[x][y2 - 1] = board[x - 1][y2 - 1]
            min_ = min(min_, board[x][y2 - 1])

        # 북쪽 회전
        for y in range(y2 - 1, y1 - 1, -1):
            board[x1 - 1][y] = board[x1 - 1][y - 1]
            min_ = min(min_, board[x1 - 1][y])

        board[x1 - 1][y1] = tmp
        answer.append(min_)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))