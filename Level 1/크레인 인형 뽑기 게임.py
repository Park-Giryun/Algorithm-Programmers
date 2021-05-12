from collections import deque

def solution(board, moves):
    q = deque()
    count = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                if len(q) > 0 and q[len(q) - 1] == board[i][move - 1]:
                    q.pop()
                    board[i][move - 1] = 0
                    count += 1
                    break
                else:
                    q.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    break
    return count * 2