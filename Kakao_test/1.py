def solution(id_list, report, k):
    answer = []
    id_dict = {id: [] for id in id_list}
    report_dict = {id: 0 for id in id_list}
    for re in report:
        x, y = re.split(" ")
        if y not in id_dict[x]:
            id_dict[x].append(y)
            report_dict[y] += 1

    for key, value in list(report_dict.items()):
        if value < k:
            del(report_dict[key])

    for key, value in id_dict.items():
        tmp = 0
        for v in value:
            if v in report_dict:
                tmp += 1
        answer.append(tmp)

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
