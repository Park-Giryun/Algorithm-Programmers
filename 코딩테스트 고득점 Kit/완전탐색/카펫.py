def solution(brown, yellow):
    n = brown + yellow
    for l in range(n, -1, -1):
        if n % l == 0:
            c = n // l
            if yellow == (l-2) * (c-2):
                return [l, c]