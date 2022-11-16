# Time:  O(n)
# Space: O(1)

#Note:
#方法一是双指针法，慢指针左边非0，快指针扫描非0项用于和慢指针交换
#方法二、三是trick(有问题)，但是方法三不符合要求。sort方法会改变原list而且只能是list，sorted不改变原list，如果通过赋值改变，会开辟新空间，不符合时间复杂度的要求。
#如果题目改成把负数移动到末尾而且不改变排序，那么方法一不再适用；方法二仍然有效。而且速度非常快。

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after
# calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        print(nums)
        return

    def moveZeroes2(self, nums):
        nums.sort(key=lambda x: 1 if x < 0 else 0)
        print(nums)
        return

    def moveZeroes3(self, nums):
        nums = sorted(nums,key=lambda x: 1 if x < 0 else 0)
        print(nums)
        return
if __name__ == "__main__":
    s = Solution()
    nums = [0,9,-1,0,3,-12]
    s.moveZeroes1(nums)
    s.moveZeroes2(nums)
    s.moveZeroes3(nums)
