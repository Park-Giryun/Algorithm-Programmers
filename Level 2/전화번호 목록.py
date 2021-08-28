# 0828
# 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]) and phone_book[i] in phone_book[i+1]:
                return False
    return True

print(solution(["123","456","789"]))