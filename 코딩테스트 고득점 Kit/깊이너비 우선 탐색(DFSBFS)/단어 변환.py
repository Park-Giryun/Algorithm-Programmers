from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    visited = [False] * len(words)

    def bfs(begin):
        q = deque([begin])
        while q:
            word = q.popleft()
            if word == target:
                return
            for i in range(len(words)):
                if visited[i]:
                    continue
                cnt = 0
                for x, y in zip(word, words[i]):
                    if x != y:
                        cnt += 1
                if cnt == 1:
                    q.append(words[i])
                    visited[i] = True
                    nonlocal answer
                    answer += 1

    bfs(begin)
    return answer