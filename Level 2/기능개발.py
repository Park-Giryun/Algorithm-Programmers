# 0825
# 기능개발
def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0] < -((p-100) // s):
            answer.append([-((p-100) // s), 1])
        else:
            answer[-1][1] += 1
    print(answer)
    return [a[1] for a in answer]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))