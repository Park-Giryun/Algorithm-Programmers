# 0823
# 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return [-1] if arr == [] else arr

print(solution([4,3,2,1]))