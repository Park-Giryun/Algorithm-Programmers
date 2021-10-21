# 1021
# 모음사전
# idea: 등비수열
def solution(word):
    answer = len(word)
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    s = 5**5
    for i in word:
        answer += dic[i] * (s - 1) // 4 # 등비수열의 합
        s //= 5
    return answer

print(solution("AAAAE"))