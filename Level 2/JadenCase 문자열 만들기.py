# 0904
# JadenCase 문자열 만들기
def solution(s):
    return ' '.join([c.capitalize() for c in s.split(" ")])
print(solution("3people unFollowed me"))