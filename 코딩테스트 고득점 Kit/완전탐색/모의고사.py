def solution(answers):
    answer = []

    count = [0] * 3
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, a in enumerate(answers):
        for num, x in enumerate([one, two, three]):
            if a == x[idx % len(x)]:
                count[num] += 1

    for idx, c in enumerate(count):
        if c == max(count):
            answer.append(idx + 1)

    return answer