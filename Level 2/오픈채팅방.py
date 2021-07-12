idDict = dict()

def solution(record):
    answer = []
    array = []
    for rc in record:
        x = rc.split()
        if x[0] == 'Leave':
            array.append([x[1], "님이 나갔습니다."])
        elif x[0] == 'Enter':
            idDict[x[1]] = x[2]
            array.append([x[1], "님이 들어왔습니다."])
        else:
            idDict[x[1]] = x[2]
    for arr in array:
        answer.append(idDict[arr[0]] + arr[1])

    return answer

rc = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(rc))
