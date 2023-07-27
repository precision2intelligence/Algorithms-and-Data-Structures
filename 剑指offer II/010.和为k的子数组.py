# Time:O(n)
# Space:O(n)

# leetcode 560
# 一次遍历取得结果
# 利用前缀和+哈希节约查找时间，利用S(p,q) = S(0,q)-S(0,p)
# 对于python来说，一个if都要简化，不然超时

'''
给定一个整数数组和一个整数k ，请找到该数组中和为k的连续子数组的个数。

示例1：

输入: nums = [1, 1, 1], k = 2
输出: 2
解释: 此题[1, 1]与[1, 1]为两种不同的情况

示例2：

输入: nums = [1, 2, 3], k = 3
输出: 2

提示:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = {0:1}
        cur_sum = 0
        cnt = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cnt += pre_sum.get(cur_sum-k,0)
            pre_sum[cur_sum] = pre_sum.get(cur_sum,0) + 1
        return cnt