def solution(array, commands):
    answer = []
    for c in commands:
        res = array[c[0]-1:c[1]]
        res.sort()
        answer.append(res[c[2]-1])
    return answer

#
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))