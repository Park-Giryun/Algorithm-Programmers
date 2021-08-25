# 0826
# 뉴스 클러스터링
def solution(str1, str2):
    str1_list = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_list = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    inter_list = set(str1_list) & set(str2_list)
    union_list = set(str1_list) | set(str2_list)
    if len(union_list) == 0:
        return 65536
    inter = sum(min(str1_list.count(i), str2_list.count(i)) for i in inter_list)
    union = sum(max(str1_list.count(u), str2_list.count(u)) for u in union_list)
    return int(inter / union * 65536)


print(solution("aa1+aa2", "AAAA12"))