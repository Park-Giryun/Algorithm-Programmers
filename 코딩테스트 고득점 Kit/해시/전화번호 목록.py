# set, dict에서 element 찾는 속도는 list보다 훨~씬 더 빠르다
def solution(phone_book):
    pb = {}
    for number in phone_book:
        pb[number] = 1
    for number in phone_book:
        tmp = ""
        for n in number:
            tmp += n
            if tmp in pb and tmp != number:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))