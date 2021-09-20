# 0920
# 땅따먹기
# idea: 다이나믹 프로그래밍
def solution(land):
    for i in range(len(land)-1):
        for j in range(4):
            land[i+1][j] = max(land[i][:j] + land[i][j+1:]) + land[i+1][j]
    return max(land[len(land)-1])