import math

def solution(fees, records):
    records_dict = {re.split(" ")[1]: [] for re in list(records)}
    result_dict = {re.split(" ")[1]: 0 for re in list(records)}
    for re in list(records):
        split_re = re.split(" ")
        records_dict[split_re[1]].append(split_re[0])

    for key, value in records_dict.items():
        if len(value) % 2 != 0:
            records_dict[key].append("23:59")
        tmp = 0
        for i in range(0, len(value)-1, 2):
            in_h, in_m = value[i].split(":")
            out_h, out_m = value[i+1].split(":")
            h, m = int(out_h) - int(in_h), int(out_m) - int(in_m)
            tmp += 60 * h + m if m >= 0 else 60 * (h-1) + 60 + m
        result_dict[key] = fees[1] if tmp < fees[0] else int(fees[1] + math.ceil((tmp-fees[0]) / fees[2]) * fees[3])
    return [value for key, value in sorted(result_dict.items())]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

