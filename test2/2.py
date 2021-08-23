def solution(card_numbers):
    answer = []
    even, odd = 0, 0
    for card in card_numbers:
        new_card = "".join(card.split('-'))
        for idx, number in enumerate(new_card):
            if idx % 2 == 0:
                number *= 2
                if int(number) >= 10:
                    even += (int(number) // 10) + (int(number) % 10)
                even += int(number)
            else:
                odd += int(number)
        result = even + odd
        if result % 10 == 0:
            answer += '1'
        else:
            answer += '0'
    return answer

print(solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]))