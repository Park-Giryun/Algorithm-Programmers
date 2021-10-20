# 1020
# 파일명 정리
# idea: 구현
# 개선된 코드
import re

def solution(files):
    a = sorted(files, key=lambda file: int(re.findall('\d{1,5}', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])
    return b

# 내가 푼 코드
def solution(files):
    answer = []
    temp = []
    for idx, file in enumerate(files):
        for i, v in enumerate(file):
            if v.isdigit():
                head, body = file[:i].lower(), file[i:]
                if body.isdigit():
                    num = int(body)
                else:
                    for j, w in enumerate(body):
                        if not w.isdigit():
                            num, tail = int(body[:j]), body[j:]
                            break
                break
        temp.append([head, num, idx])
    temp.sort(key=lambda x: (x[0], x[1], x[2]))
    for tmp in temp:
        answer.append(files[tmp[2]])
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# 회고: re, findall