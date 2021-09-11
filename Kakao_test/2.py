def convert(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def isPrime(x):
    if x == 0 or x == 1: return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    x = list(convert(n, k))
    tmp = ''
    for i in x:
        tmp += i
        if i == '0':
            if tmp[-1] == '0' and isPrime(int(tmp[:-1])):
                answer += 1
            elif tmp[0] == '0' and isPrime(int(tmp[1:])):
                answer += 1
            elif tmp[-1] == '0' and tmp[0] == '0' and isPrime(int(tmp[0:-1])):
                answer += 1
            elif tmp != '' and isPrime(int(tmp[0:-1])):
                answer += 1
            tmp = '0'
    if isPrime(int(tmp)):
        answer += 1
    return answer

print(solution(110011, 10))