# Time：O(n*n!)
# Space:O(n) 递归深度，等于数组长度

# 注意，排列组合，得回头看
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        m  = len(nums)
        self.backtrack(res, nums, [], m)
        return res
    def backtrack(self, res, nums, path, m):
        if len(path) == m:
            res.append(path[:])
        for i in range(m):
            if nums[i] not in path:
                path.append(nums[i])
                self.backtrack(res, nums, path, m)
                path.pop()
