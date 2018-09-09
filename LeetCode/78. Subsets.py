#注意python的list用法，含错误
#dfs，这里没给终止条件，因为内部有for i in range().
#把dfs的第一步想清楚就好了

# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        def dfs(lists,idx,subs,results):
            results.append(subs)
            for i in range(idx,len(lists)):
                dfs(lists,i+1,subs+[lists[i]],results)
                #这里有个不易发现的错误：dfs(lists,i+1,subs.append(lists[i]),results)
                #如果用了append函数，那么subs会变成‘None’
                #eg. a = [45]  a.append(89) >>>  print(a) 结果是[45,89] ;print(a.append(89)) 结果是None
                #eg. a = [45] a + 89 会报错；a + [89] >> a = [45],a+ [89] 结果是[45,89], a的值不会改变
        res = []
        sub = []
        dfs(nums,0,sub,res)
        return res
if __name__ == '__main__':
    solu = Solution()
    print(solu.subsets([1,2,3]))