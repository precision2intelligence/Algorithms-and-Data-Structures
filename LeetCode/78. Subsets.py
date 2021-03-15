#注意python的list用法，含错误
#dfs，这里没给终止条件，因为内部有for i in range().
#把dfs的第一步想清楚就好了

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
        m = len(nums)
        res = [[]]
        for i in range(m):
            newarr = []
            dfs(newarr, res, i, m, nums)
        return res

def dfs(newarr, res, i, m, nums):
    if i == m:
        return
    newarr = newarr + [nums[i]]
    res.append(newarr)
    for j in range(i+1,m):
        dfs(newarr, res, j, m, nums)