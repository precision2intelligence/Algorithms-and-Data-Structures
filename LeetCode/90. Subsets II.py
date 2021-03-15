# Time : O(2^n*2^n)=O(2^(n+1)), 个人答案，每个位置都判断是否包含某个元素，且子集有2^n-1个
# Space ： O((2^n-1)*n) 个人理解，所有子集，最多包含n个元素，是个松上界

# labuladong模板法，res.append(path[:]) 一定加冒号

'''
总之：return结束方法；continue结束本次循环，循环还将继续；break跳出所有循环，方法继续
------------------------------return--------------------------------------
return关键字并不是专门用于跳出循环的，return的功能是结束一个方法。
一旦在循环体内执行到一个return语句，return语句将会结束该方法，循环自然也随之结束。
与continue和break不同的是，return直接结束整个方法，不管这个return处于多少层循环之内。

-----------------------------continue------------------------------------
continue的功能和break有点类似，区别是continue只是中止本次循环，接着开始下一次循环。
而break则是完全中止循环。

-----------------------------break-----------------------------------------
break用于完全结束一个循环，跳出循环体。
不管是哪种循环，一旦在循环体中遇到break，系统将完全结束循环，开始执行循环之后的代码。
break不仅可以结束其所在的循环，还可结束其外层循环。
'''

'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        backtrack(res, [], nums)
        return res

def backtrack(res, path, selects):
    # why??? res.append(path)不对
    res.append(path[:])
    for i in range(len(selects)):
        if i > 0 and selects[i] == selects[i-1]:
            continue
        else:
            path.append(selects[i])
            backtrack(res, path, selects[i+1:])
            path.pop()