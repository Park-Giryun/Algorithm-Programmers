# def maxlength(nums):
#     cnt, tmp = 0, 0
#     for n in nums:
#         if n: tmp += 1
#         else:
#             cnt = max(cnt, tmp)
#             tmp = 0
#     return cnt
#
# def solution(nums, k):
#     ans = maxlength(nums)
#     zero = [i for i in range(len(nums)) if not nums[i]]
#     visited = [False] * len(zero)
#
#     def dfs(nums, i):
#         if i == k:
#             nonlocal ans
#             ans = max(ans, maxlength(nums))
#             return
#         else:
#             for j in range(len(zero)):
#                 if not visited[j]:
#                     visited[j] = True
#                     nums[zero[j]] = 1
#                     dfs(nums, i+1)
#                     visited[j] = False
#                     nums[zero[j]] = 0
#
#     dfs(nums, 0)
#     return ans

# 슬라이딩 윈도우 알고리즘
def solution(nums, k):
    ans, cnt, lc = 0, 0, 0
    length = len(nums)
    for rc in range(length):
        if not nums[rc]: cnt += 1
        while cnt > k:
            if not nums[lc]:
                cnt -= 1
            lc += 1
        ans = max(ans, rc - lc + 1)
    return ans

print(solution([1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], 2))