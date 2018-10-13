#Time: O(n)
#Space: O(1)

#思路：贪心
#错过的地方：用了for循环，导致后面有 100，前面全是1也能取到100，永远返回true
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last,index = 0, 0
        l = len(nums)
        while index <= last:
            last = max(last,nums[index] + index)
            if last >= l-1:
                return True
            index += 1
        return False