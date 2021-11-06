# 0922
# 큰 수 만들기
# idea: 정렬
from itertools import combinations

def solution(number, k):
    return sorted(["".join(cb) for cb in combinations(number, len(number)-k)])[-1]

# idea: 스택큐
def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
print(solution("1924", 2))
print(solution("4177252841", 4))