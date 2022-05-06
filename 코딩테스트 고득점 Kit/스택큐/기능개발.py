def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        # t = (100 - p) // s  # 완수율이 2.xx일 경우, 실제 배포에 걸리는 일자는 3일
        t = -((p - 100) // s)  # 반례 [96, 94], [3, 3]
        if not answer or answer[-1][1] < t:
            answer.append([1, t])
        else:
            answer[-1][0] += 1
    return [a[0] for a in answer]

print(solution([93, 30, 55], [1, 30, 5]))