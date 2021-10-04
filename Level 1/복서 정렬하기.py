def solution(weights, head2head):
    d = dict()
    n = len(weights)
    for idx, (w, h) in enumerate(zip(weights, head2head)):
        tmp = [0, 0, w]
        for i, v in enumerate(h):
            if v == 'W':
                tmp[0] += 1
                if w < weights[i]:
                    tmp[1] += 1
        if n-1 != 0:
            tmp[0] /= (n-1)
        d[idx+1] = tmp
    return [x[0] for x in sorted(d.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))]


# print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))