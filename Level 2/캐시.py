# 1018
# 캐시
# idea: lru 알고리즘 구현
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    for c in cities:
        c = c.lower()
        if c not in cache:
            cache.append(c)
            answer += 5
        else:
            answer += 1
            cache.remove(c) # 값으로 삭제
            cache.append(c)
    return answer

# 회고: maxlen에는 deque의 길이의 최댓값을 설정할 수 있다. 만약 deque의 길이가 append()나 appendleft()를 통해 maxlen 이상이 될 경우, append()를 하면 맨 왼쪽의 원소가 삭제된 뒤 값이 추가되고, appendleft()를 하면 맨 오른쪽의 원소가 삭제된 뒤 값이 추가된다.