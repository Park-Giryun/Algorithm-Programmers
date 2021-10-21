# 1021
# N으로 표현
# idea: 다이나믹 프로그래밍,
def solution(N, number):
    answer = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        temp = [int(str(N)*i)]
        for j in range(1, i//2 + 1):
            for x in answer[j]:
                for y in answer[i - j]:
                    temp.append(x + y)
                    temp.append(x - y)
                    temp.append(y - x)
                    temp.append(x * y)
                    if y != 0:
                        temp.append(x / y)
                    if x != 0:
                        temp.append(y / x)
            if number in temp:
                return i
            answer.append(temp)
    return -1

print(solution(5, 12))

