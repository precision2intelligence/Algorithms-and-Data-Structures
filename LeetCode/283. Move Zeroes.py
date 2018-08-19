# Time:  O(n)
# Space: O(1)

#Note:
#方法一是双指针法，慢；
#方法二、三是trick，但是方法三不符合要求。sort方法会改变原list而且只能是list，sorted不改变原list，如果通过赋值改变，会开辟新空间，不符合时间复杂度的要求。
#如果题目改成把负数移动到末尾而且不改变排序，那么方法一不再适用；方法二仍然有效。而且速度非常快。

class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return
        n = len(nums)
        for i in range(n-1):
            if nums[i] == 0:
                for j in range(i+1,n):
                    if nums[j] != 0:
                        nums[i],nums[j] = nums[j], nums[i]
                        j += 1
                        i += 1
                    else:
                        i += 1
                        j += 1
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