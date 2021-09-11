# 0910
# 프렌즈4블록
def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        checked = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "0":
                    continue
                if board[i][j] == board[i][j+1]:
                    if board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                        checked.append((i, j))
                        checked.append((i, j+1))
                        checked.append((i+1, j))
                        checked.append((i+1, j+1))
        print(checked)
        if len(checked) == 0:
            break
        else:
            answer += len(set(checked))
            for x, y in checked:
                board[x][y] = '0'

            for x, y in reversed(checked):
                check_n = x - 1
                put_n = x

                while check_n >= 0:
                    if board[put_n][y] == "0" and board[check_n][y] != "0":
                        board[put_n][y], board[check_n][y] = board[check_n][y], board[put_n][y]
                        put_n -= 1
                    check_n -= 1
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))