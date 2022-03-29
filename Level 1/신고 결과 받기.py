def solution(id_list, report, k):
    answer = {}
    id_dic = {}
    report_dic = {}
    for id in id_list:
        answer[id] = 0
        id_dic[id] = 0
        report_dic[id] = []
    for re in report:
        x, y = re.split(" ")
        if y in report_dic[x]:
            continue
        report_dic[x].append(y)
        id_dic[y] += 1
    for k1, v1 in id_dic.items():
        if v1 >= k:
            for k2, v2 in report_dic.items():
                if k1 in v2:
                    answer[k2] += 1
    return list(answer.values())