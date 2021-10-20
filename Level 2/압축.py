# 1020
# 압축
# idea: 구현
# 개선된 코드
def solution(msg):
    answer = []
    dic = {chr(i+64): i for i in range(1, 27)} # dictionary comprehension
    idx = 27
    while msg:
        i = 1
        while msg[:i] in dic.keys() and i <= len(msg): # 단어가 사전에 없거나 단어 길이를 넘을때까지
            i += 1
        i -= 1 # 현재 글자
        if msg[:i] in dic.keys():
            answer.append(dic[msg[:i]])
            dic[msg[:i+1]] = idx # 새로운 글자 등록
            idx += 1
        msg = msg[i:]
    return answer

# 내가 푼 코드
def solution(msg):
    answer = []
    dic = dict()
    for i in range(1, 27):
        dic[chr(i+64)] = i
    idx = 27
    i = 0
    end = 0
    while True:
        if i == len(msg) - 1:
            if end:
                break
            answer.append(dic[msg[i]])
            break
        tmp = msg[i]
        tmp_lst = [dic[msg[i]]]
        j = i+1
        tmp += msg[j]
        while tmp in dic.keys():
            tmp_lst.append(dic[tmp])
            if j == len(msg) - 1:
                end = j
                break
            j += 1
            tmp += msg[j]
        i = j
        dic[tmp] = idx
        idx += 1
        answer.append(tmp_lst[-1])
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))