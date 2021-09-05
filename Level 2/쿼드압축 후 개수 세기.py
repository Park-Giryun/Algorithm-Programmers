# 0905
# 쿼드압축 후 개수 세기
# dfs
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    def dfs(x, y, n):
        tmp = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != tmp:
                    m = n//2
                    dfs(x, y, m)
                    dfs(x+m, y, m)
                    dfs(x, y+m, m)
                    dfs(x+m, y+m, m)
                    return
        answer[tmp] += 1
    dfs(0, 0, n)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))