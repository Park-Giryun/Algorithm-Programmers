# set, dict에서 element 찾는 속도는 list보다 훨~씬 더 빠르다
def solution(phone_book):
    pb = set(phone_book)
    for number in phone_book:
        tmp = ''
        for nb in number:
            tmp += nb
            if tmp in pb and tmp != number:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))