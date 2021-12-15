from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    n = len(words)
    visited = [False] * n

    def bfs():
        nonlocal begin, target, words, answer, n, visited
        q = deque([begin])
        while q:
            word = q.popleft()
            if word == target:
                return
            for i in range(n):
                if visited[i]:
                    continue
                cnt = 0
                for x, y in zip(word, words[i]):
                    if x != y:
                        cnt += 1
                if cnt == 1:
                    print(words[i])
                    q.append(words[i])
                    visited[i] = True
                    answer += 1
    bfs()
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))