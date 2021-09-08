# 0908
# 튜플

# 나의 풀이
# def solution(s):
#     arr = []
#     answer = []
#     tmp = ''
#     for c in s[1:-1]:
#         if c.isdecimal() or c == ',':
#             tmp += c
#         if c[-1] == '}':
#             arr.append(tmp)
#             tmp = ''
#     arr.sort(key=len)
#     for s in arr:
#         for c in s.split(','):
#             if c.isdecimal() and int(c) not in answer:
#                 answer.append(int(c))
#     return answer

# 다른 사람의 풀이
from collections import Counter

def solution(s):
    arr = [c.replace('{', '').replace('}', '') for c in s.split(',')]
    return [int(c[0]) for c in sorted(Counter(arr).items(), key=lambda x: x[1], reverse=True)]

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))

# 회고: Counter 함수 사용