def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for x in new_id:
        if x.isalpha() or x.isdigit() or x in '-_.':
            answer += x
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.') 
    # 4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # 5
    answer = 'a' if answer == '' else answer
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7        
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    return answer