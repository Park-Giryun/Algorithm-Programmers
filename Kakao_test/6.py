from bisect import bisect_left

def solution(board, skill):
    answer = len(board[0]) * len(board)
    for s in sorted(skill):
        type, r1, c1, r2, c2, degree = s
        for b in board[r1:r2 + 1]:
            b[c1:c2 + 1] = list(map(lambda x: x - degree if type == 1 else x + degree, b[c1:c2 + 1]))
    for b in board:
        answer -= bisect_left(sorted(b), 1)
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))