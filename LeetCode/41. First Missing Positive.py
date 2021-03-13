# Time: O(n)
# Space: O(1)

# 主要是trick，利用数组的索引

'''
Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        for i in range(m):
            if nums[i] <= 0:
                nums[i] = m + 1
        # 一定是先遍历变负数为n+1，再遍历
        for i in range(m):
            # 为了保证改动后的值仍能取到，所以取绝对值
            chg = abs(nums[i])
            if chg <= m:
                # 这里为了保证为负号，加入绝对值限制
                nums[chg-1] = -abs(nums[chg-1])

        for i in range(m):
            if nums[i] > 0:
                return i + 1
        return m+1

