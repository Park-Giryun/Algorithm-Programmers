# 0906
# 스킬트리
# def solution(tree, skill_trees):
#     answer = 0
#     arr = []
#     for i in range(len(tree)):
#         arr.append(tree[0:i + 1])
#     for skill in skill_trees:
#         tmp = ''
#         for s in skill:
#             if s in tree:
#                 tmp += s
#         if tmp == '':
#             answer += 1
#         if tmp in arr:
#             answer += 1
#     return answer

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
