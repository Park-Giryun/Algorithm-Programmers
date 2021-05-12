def solution(nums):
    nums.sort()
    answer = [nums[0]]
    for i in range(1, len(nums)):
        if len(answer) == len(nums) // 2:
            break
        else:
            if nums[i] != answer[-1]:
                answer.append(nums[i])
            else:
                    continue
    return len(answer)

# 간단한 풀이
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))