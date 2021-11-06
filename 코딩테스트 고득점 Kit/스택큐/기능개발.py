def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        t = -((p-100) // s)  # 작업 기간
        if len(answer) == 0 or answer[-1][0] < t:
            answer.append([t, 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]

print(solution([93, 30, 55], [1, 30, 5]))