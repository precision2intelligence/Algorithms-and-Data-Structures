# Time: O(logn)
# Space: O(1)

'''
思路
先找左边界，再找右边界，注意判罚为空的地方。
只要长度不是0，就可以放心找到边界
二分查找的模板
[left, right]
while left <= right:
    mid = left + ((right-left) >> 1)
    if nums[mid] < target:
    elif nums[mid] > target:
    elif nums[mid] == target:
左边界：检查left是否超出，返回left
if left == len(nums): return -1
return left if nums[left] == target else -1
右边界：检查left-1是否为负，返回left-1
if left-1 < 0: return -1
return left-1 if nums[left-1] == target else -1
'''

class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

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
        return [l, r]

