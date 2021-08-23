# 0823
# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i+1)
    return answer - money if answer >= money else 0