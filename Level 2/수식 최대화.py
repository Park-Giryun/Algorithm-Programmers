# 0827
# 수식최대화
from itertools import permutations

def operation(num1, num2, op):
    if op == '*':
        return str(int(num1) * int(num2))
    elif op == '+':
        return str(int(num1) + int(num2))
    else:
        return str(int(num1) - int(num2))

def calc(op, exp):
    answer = 0
    lst = []
    tmp = ""
    for x in exp:
        if x.isdigit():
            tmp += x
        else:
            lst.append(tmp)
            lst.append(x)
            tmp = ""
    lst.append(tmp)

    for o in op:
        stack = []
        while len(lst) != 0:
            temp = lst.pop(0)
            if temp == o:
                stack.append(operation(stack.pop(), lst.pop(0), temp))
            else:
                stack.append(temp)
        lst = stack
    return abs(int(lst[0]))

def solution(expression):
    answer = 0
    perm = permutations("*+-", 3)
    for p in perm:
        answer = max(answer, calc(p, expression))

    return answer

print(solution("100-200*300-500+20"))