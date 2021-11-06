# defaultdict
from collections import defaultdict

def solution(genres, plays):
    answer = []
    cnt = defaultdict(int)
    song = defaultdict(list)

    for id, (g, p) in enumerate(zip(genres, plays)):
        cnt[g] += p
        song[g].append((-p, id))

    genres = sorted(cnt.keys(), key=lambda x: cnt[x], reverse=True)

    for g in genres:
        answer.extend([id for p, id in sorted(song[g])[:2]])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))