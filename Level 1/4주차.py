# 0823
# 직업군 추천하기
def solution(table, languages, preference):
    answer = []
    for data in table:
        num = 0
        for idx, value in enumerate(data.split(" ")):
            for pair in zip(languages, preference):
                if value == pair[0]:
                    num += (6 - idx) * pair[1]
        answer.append((num, data.split(" ")[0]))
    return sorted(answer, key=lambda x: (-x[0], x[1]))[0][1]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))