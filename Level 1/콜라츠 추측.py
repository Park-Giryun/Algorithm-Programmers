# 0823
# 콜라츠 추측
def solution(num):
    cnt = 0
    while True:
        if num == 1:
            return cnt
        if cnt > 500:
            return -1
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        cnt += 1