def solution(n, arr1, arr2):
    result = []
    for x in zip(arr1, arr2):
        bin1 = format(x[0], 'b')
        bin2 = format(x[1], 'b')
        if len(bin1) != n:
            for _ in range(n-len(bin1)):
                bin1 = '0' + bin1           
        if len(bin2) != n:
            for _ in range(n-len(bin2)):
                bin2 = '0' + bin2
        for y in zip(bin1, bin2):
            if int(y[0]) > 0 or int(y[1]) > 0:
                result.append("#")
            else:
                result.append(" ")
    return ["".join(result[i:i+n]) for i in range(0, len(result), n)]