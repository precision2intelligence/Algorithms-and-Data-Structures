# Time: O(logn)
# Space: O(1)

'''
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109

'''

# 二分查找，左右边界。左边界不存在直接返回0

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        # leftSearch
        def leftSearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    right = mid - 1
            if left == len(nums): return -1
            return left if nums[left] == target else -1

        # rightSearch
        def rightSearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    left = mid + 1
            if left - 1 < 0: return -1
            return left - 1 if nums[left - 1] == target else -1

        l = leftSearch(nums, target)
        r = rightSearch(nums, target)
        return 0 if l == -1 else r-l+1