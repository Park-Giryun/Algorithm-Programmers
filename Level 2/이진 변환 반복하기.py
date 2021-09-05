# 0905
# 이진 변환 반복하기
def solution(s):
    total, cnt = 0, 0
    while s != '1':
        num = s.count("1")
        cnt += len(s) - num
        s = bin(num)[2:]
        total += 1
    return [total, cnt]

print(solution("110010101001"))