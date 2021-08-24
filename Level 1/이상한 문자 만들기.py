# 0823
# 이상한 문자 만들기
def solution(s):
    answer = []
    for w in s.split():
        new = ''
        for i, c in enumerate(w):
            if i % 2 == 0:
                new += c.upper()
            else:
                new += c.lower()
        answer.append(new)
    return ' '.join(answer)

print(solution("try hello world"))