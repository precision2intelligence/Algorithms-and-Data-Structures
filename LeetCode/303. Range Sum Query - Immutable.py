# Time：O(1) 每次查询直接可以计算
# Space:O(n) 开辟了n大小的空间

'''
1. 注意self的用法，不用于构造函数的参数，用于自定义的成员变量
2. 理解题意，i 位置的数字是要加上的，i之前的要减掉
3. 一点trick是避免索引溢出，就在dpNums开始放了0，每个索引的和都后移1个位置
4. 空间换时间，因为会频繁调用多次
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dpNums = [0]
        for i in range(len(nums)):
            self.dpNums.append(nums[i] + self.dpNums[i])


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dpNums[j+1] - self.dpNums[i]

