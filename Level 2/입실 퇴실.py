# 0916
# 입실 퇴실
def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    e_idx = 0
    for l in leave:
        # 퇴실할 사람이 방에 들어올때까지 입실
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        # 퇴실할 사람이 방에 들어온다면 해당 사람을 퇴실시킨다.
        room.remove(l)
        # 현재 방에 있는 사람들이 만난 사람 수에 1씩 더해준다.
        for p in room:
            answer[p - 1] += 1
        # 퇴실한 사람의 만난 사람 수에 현재 방 인원수를 더해준다.
        answer[l - 1] += len(room)
    return answer


print(solution([1, 3, 2], [1, 2, 3]))
# print(solution([1,4,2,3], [2,1,3,4]))
# print(solution([3,2,1], [2,1,3]))
# print(solution([3,2,1], [1,3,2]))
# print(solution([1,4,2,3], [2,1,4,3]))
