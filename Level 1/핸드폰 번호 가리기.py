# 0823
# 핸드폰 번호 가리기
def solution(phone_number):
    return phone_number.replace(phone_number[:-4], '*'*len(phone_number[:-4]))

print(solution("01033334444"))