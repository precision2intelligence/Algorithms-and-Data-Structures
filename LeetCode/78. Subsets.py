# 用labuladong模板做，凡是回溯添加路径都是加冒号，即 res.append(path[:])

# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # 进入回溯算法
        backtrack(res, [], nums)
        return res

def backtrack(res, path, selects):
    # 添加路径
    res.append(path[:])
    # for 选择 in 选择列表
    for i in range(len(selects)):
        # 做出选择
        path.append(selects[i])
        # 回溯
        backtrack(res, path, selects[i+1:])
        # 回退选择
        path.pop()
