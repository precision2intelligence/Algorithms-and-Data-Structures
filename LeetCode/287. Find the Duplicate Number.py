'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class Solution:
    #Method 1
    # Time: O(n)
    # Space: O(1)

    # 不能排序，空间复杂度是1，所以不能哈希
    # 类似链表的环的入口，这里用的索引，而且索引是可嵌套的
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[nums[0]], nums[0]#开始的时候，这里不能是0，否则进不了下面的while
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0#这里必须是0，不能是fast= nums[0],否则就先走了一步
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow

    # Method 2
    # Time: O(nlogn)
    # Space: O(1)

    #很不好想！
    #起始边界条件从1开始，到n，因为长度是n+1，所以是n
    #统计比mid小的，只能统计比mid小的，让mid的范围根据个数缩减
    #总之边界很不好想，还是多用几个测试用例可以想出来
    def findDuplicate2(self, nums):
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (high + low) >> 1
            count = sum(x <= mid for x in nums)
            if count > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low

s = Solution()
print(s.findDuplicate2([1,3,6,4,6,5,2]))