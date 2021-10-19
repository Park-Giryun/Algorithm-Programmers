# 1019
# 방금그곡
# idea: 구현

def change(m):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return m

def solution(m, musicinfos):
    answer = []
    m = change(m)
    for idx, music in enumerate(musicinfos):
        starttime, endtime, title, segment = music.split(',')
        segment = change(segment)
        hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
        if hour == 0:
            time = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
        else:
            time = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])
        q, r = time // len(segment), time % len(segment)
        melody = segment * q + segment[:r]
        if m in melody:
            answer.append([time, idx, title])
    if len(answer) != 0:
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]
    else:
        return "(None)"

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# 회고: #이 붙은 음을 구별해주기 위해 소문자로 바꿔준다.