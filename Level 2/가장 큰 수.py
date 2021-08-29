# 0829
# 가장 큰 수
def solution(numbers):
    # 문자열 늘려서 비교
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))))

print(solution([3, 30, 34, 5, 9]))