# 0823
# 행렬의 덧셈
def solution(arr1, arr2):
    return [[x + y for x, y in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))