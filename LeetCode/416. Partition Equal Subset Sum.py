# Time: O(n*target) 每个位置数字都填了一次表
# Space: O(target) 空间优化，只用了一维表，因为true可以一直保存

# 0-1背包问题，优化为一维数组
# trick是奇数的计算和“或等于”的表示，如果和是奇数要提前退出

'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total & 1:
            return False

        target = total // 2

        dp = [True] + [False] * target

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] |= dp[j-nums[i]]

        return dp[target]