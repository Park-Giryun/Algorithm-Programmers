def solution(student, k):
    answer = set()
    if student.count(1) < k:
        return 0
    for i in range(1, len(student)+1):
        for j in range(len(student)-i+1):
            if student[j:j+i].count(1) == k:
                answer.add(tuple(student[j:j+i]))
    return len(answer)

print(solution([0, 1, 0, 0, 1, 1, 0], 2))