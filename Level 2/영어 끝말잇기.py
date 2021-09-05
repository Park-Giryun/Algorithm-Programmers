# 0905
# 영어 끝말잇기
def solution(n, words):
    array = [words[0]]
    for i in range(1, len(words)):
        word = words[i]
        if word in array or word[0] != array[-1][-1]:
            return [i%n+1, i//n+1]
        array.append(word)
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))