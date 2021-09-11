from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    info = info[::-1]
    tmp = 0
    for cb in combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n):
        temp_a, temp_b = 0, 0
        temp = [0 for _ in range(11)]
        for x in cb:
            temp[x] += 1
        for i, (a, b) in enumerate(zip(info, temp)):
            if a == 0 and b == 0:
                continue
            if a >= b:
                temp_a += i
            else:
                temp_b += i
        if temp_b > temp_a :
            if temp_b - temp_a > tmp:
                answer = []
                answer.append(temp)
                tmp = temp_b - temp_a
            elif temp_b - temp_a == tmp:
                answer.append(temp)
    return answer[0][::-1] if len(answer) > 0 else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))