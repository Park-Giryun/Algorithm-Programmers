def solution(answers):
    cnt = [0] * 3
    patterns = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            if a == p[i % len(p)]:
                cnt[j] += 1

    return [i+1 for i, v in enumerate(cnt) if v == max(cnt)]