def find_prime(n):
    answer = n
    a = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    for p in primes:
        if n % p == 0:
            answer = min(answer, p)
    return answer

def solution(n):
    answer = []
    temp = [i+1 for i in range(n)]
    print(temp)
    p = find_prime(n)
    answer = [[] for _ in range(p)]
    return answer

print(solution(12))