# 0901
# N개의 최소공배수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(num):
    answer = num[0]
    for n in num:
        answer = n * answer // gcd(n, answer)
    return answer

print(solution([2,6,8,14]))