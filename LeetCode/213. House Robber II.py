#Time O(n)
#Space O(1)

#简化空间复杂度
#按照是否偷第一家分类
#注意如果有两家，偷其中一家不警报

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return max(nums)
        return max(nums[0]+dp_rob(nums[2:-1]), dp_rob(nums[1:]))
def dp_rob(nums):
    last, now = 0, 0
    for num in nums:
        last, now = now, max(num+last, now)
    return now


