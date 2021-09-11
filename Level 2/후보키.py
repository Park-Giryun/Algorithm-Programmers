# 0910
# 후보키
from itertools import combinations

def solution(relation):
    n, m = len(relation), len(relation[0])
    # combinations을 통해서 가능한 모든 경우의 수를 생성
    candidates = []
    for i in range(m):
        candidates.extend(combinations(range(m), i+1))
    # 가능한 모든 경우의 수에서 유일성을 만족하는 지 확인
    final = []
    for keys in candidates:
        # 튜플 형태로 해당하는 값을 추출해서 길이가 맞는 지 확인
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n:
            final.append(keys)
    # 최소성을 만족하는 부분만 추출
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            # intersection을 통해서 겹치는 변수가 원본 변수가 같은게 있는 지 확인
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))