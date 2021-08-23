def solution(seconds):
    time = [300, 130, 120, 20]
    answer = 0
    for t in time:
        answer += seconds // t
        seconds %= t
    return answer