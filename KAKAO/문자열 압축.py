def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        tmp_s = ""
        tmp = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if s[j:j+i] == tmp:
                cnt += 1
            else:
                tmp_s += str(cnt) + tmp if cnt >= 2 else tmp
                tmp = s[j:j+i]
                cnt = 1
        tmp_s += str(cnt) + tmp if cnt >= 2 else tmp
        print(tmp_s)
        answer = min(answer, len(tmp_s))
    return answer

print(solution("aabbaccc"))