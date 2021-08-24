# 0823
# 정수 내림차순으로 배치하기
def solution(n):
    return int("".join(sorted(str(n))[::-1]))

print(solution(12345))