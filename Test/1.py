from collections import Counter

def solution(s):
    return "".join([c * i for c, i in sorted(Counter(s).most_common(), key=lambda x: (-x[1], ord(x[0])))])

print(solution('kdkDKKGkdkgks'))