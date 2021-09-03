# 0904
# 2개 이하로 다른 비트
# idea: (rfind: 문자열 내부에서 특정문자를 오른쪽부터 찾음) 사용
def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = list('0' + bin(num)[2:])
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'
        if num % 2 == 1:
            bin_num[idx+1] = '0'
        answer.append(int(''.join(bin_num), 2))
    return answer

print(solution([2, 7]))

# 회고:
# 1) 짝수의 경우
# 예를 들어 4일 땐 이진수로는 100인데, 4보다 크면서 2개 이하로 다른 수는 101이다.
# 즉, 가장 뒤에 있는 0을 1로 바꿔주면 된다.
# 2) 홀수의 경우
# 예를 들어 4일 땐 이진수로 0111인데,
# 먼저 짝수처럼 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꾼다. -> 1111
# 그런 다음 idx+1인 인덱스의 값을 0으로 바꾼다. -> 1011(정답)
