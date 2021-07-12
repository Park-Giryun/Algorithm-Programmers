def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    num = ''
    arr = []
    for x in dartResult:
        if x.isdigit():
            num += x
        elif x in 'SDT':
            num = int(num)**bonus[x]
            arr.append(num)
            num = ''
        else:
            if x == '*' and len(arr) > 1:
                arr[-2] *= 2
                arr[-1] *= 2
                print(arr)
            elif x == '*':
                arr[-1] *= 2
            else:
                arr[-1] *= -1
    answer = sum(arr)
    return answer

dR = '1S*2T*3S'
print(solution(dR))