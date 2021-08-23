def solution(name_list):
    answer = []
    temp = ""
    for name in name_list:
        temp = name
        t = 0
        for i in range(len(name_list)):
            if name_list[i] == temp and len(name_list[i]) == 3:
                name_list[i] += chr(65 + t)
                t += 1
        temp = ""
    return name_list

print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))
