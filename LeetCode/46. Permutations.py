# Time：O(n*n!)
# Space:O(n) 递归深度，等于数组长度

# 回溯法
# 还是利用了python对数组操作的技巧：copy，remove，insert
# remove和insert都是改变原数组的，返回为空，不要在赋值，赋值也为空
# 注意跳出条件是nums长度为1，就可以往里面加入数字了

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
class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        res = list()
        for num in nums:
            tmpNum = nums.copy()
            tmpNum.remove(num)

            for item in self.permute(tmpNum):
                item.insert(0, num)
                res.append(item)
        return res
