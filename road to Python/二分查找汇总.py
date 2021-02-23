# 整理二分查找
'''
1. 各判断位置加等号
2. 搜哪个边界检查反向越界
3. 搜哪个边界返回哪个索引
'''

# 搜索目标值
def searchTar(nums, target):
    if not nums:
        return -1

    m = len(nums)
    if m == 1:
        return 0 if nums[0] == target else -1

    l,r = 0, m-1
    while l <= r:
        mid = l + ((r-l) >> 1)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid -1
        elif nums[mid] == target:
            return mid
    return -1

# 搜索左边界
def searchLeft(nums, target):
    if not nums:
        return -1

    m = len(nums)
    if m == 1:
        return 0 if nums[0] == target else -1

    l,r = 0, m-1
    while l <= r:
        mid = l + ((r-l) >> 1)
        if nums[mid] < target:
            l = mid +1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] == target:
            r = mid - 1

    # 左边界怕越右边界
    if l >= m or nums[l] != target:
        return -1

    return l

# 搜索右边界
def searchRight(nums, target):
    if not nums:
        return -1

    m = len(nums)
    if m == 1:
        return 0 if nums[0] == target else -1

    l,r = 0, m-1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if nums[mid] > target:
            r = mid -1
        elif nums[mid] < target:
            l = mid -1
        elif nums[mid] == target:
            l = mid +1

    # 右边界怕越左边界
    if r < 0 or nums[r] != target:
        return -1
    return r


nums = [1,1,3,3,3,3,4,5]
print(searchTar(nums,5))
print(searchLeft(nums,3))
print(searchRight(nums,3))