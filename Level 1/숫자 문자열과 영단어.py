# 0812
# 숫자 문자열과 영단어
# idea: 완전 탐색
# 나의 풀이
def solution(s):
    keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    values = [str(i) for i in range(10)]
    dic = dict(zip(keys, values))

    answer, change = "", ""
    for x in s:
        if x.isdigit(): answer += x
        elif x.isalpha():
            change += x
            if change in dic.keys():
                answer += dic[change]
                change = ''
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

# 개선된 풀이
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def solution(s):
    answer = s
    for i in range(len(words)):
        answer = answer.replace(words[i], str(i))
    return int(answer)
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

# 회고: replace라는 함수를 잘 알아두자. replace(바꾸길 원하는 값, 바꿀값:str). 비슷한 문제에 잘 활용할 수 있을 듯