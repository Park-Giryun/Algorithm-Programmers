def solution(scores):
    answer = ''
    grade = []
    for i in range(len(scores)):
        s = []
        my = 0
        for j in range(len(scores)):
            if j == i:
                my = scores[j][i]
            s.append(scores[j][i])
        if (my == max(s) or my == min(s)) and s.count(my) == 1:
            grade.append((sum(s) - my) / (len(s) - 1))
        else:
            grade.append(sum(s) / len(s))

    for x in grade:
        if int(x) >= 90:
            answer += 'A'
        elif 80 <= int(x) < 90:
            answer += 'B'
        elif 70 <= int(x) < 80:
            answer += 'C'
        elif 50 <= int(x) < 70:
            answer += 'D'
        else:
            answer += 'F'
    return answer

print(solution([[50,90],[50,87]]))