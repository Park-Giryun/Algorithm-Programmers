# 0831
# 괄호 회전하기
# idea: 딕셔너리 구조 사용

def solution(s):
    answer = 0
    dic = {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        right = list(s[i:]+s[:i])
        left = []
        while right:
            tmp = right.pop(0)
            if not left:
                left.append(tmp)
            else:
                if left[-1] in '}])':
                    break
                if dic[left[-1]] == tmp:
                    left.pop()
                else:
                    left.append(tmp)
        if not left:
            answer += 1
    return answer

print(solution("[)(]"))