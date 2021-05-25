# Time:O(N^2) 遍历和枚举的乘积
# Space:O(n)  存储了排序后的数组
# 先排序，再双指针

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []

        res = []
        # 注意这里，要得到返回值，才是排序后的数组
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            total_sum = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == total_sum:
                    ans = [nums[i], nums[l], nums[r]]
                    # 这里有个去重，需要特别注意，还没想到好方法
                    if ans not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < total_sum:
                    l += 1
                elif nums[l] + nums[r] > total_sum:
                    r -= 1
        return res
