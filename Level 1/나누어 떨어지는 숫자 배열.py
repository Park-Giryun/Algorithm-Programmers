# 0823
# 나누어 떨어지는 숫자 배열
# idea: 'or' 사용법: 앞이 참일경우 해당 값까지만, 거짓일경우 뒤에 것까지 호출
def solution(arr, divisor):
    return sorted([x for x in arr if x % divisor == 0]) or [-1]