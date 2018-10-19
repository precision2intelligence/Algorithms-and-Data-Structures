#要学习的点是，如何不用把target每次都传入dfs，用self
#错过的地方是，默认所有值都是正数，然后跳出了，其实可以为复数

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root: return res
        self.target = expectNumber#这样全局可以调用了
        self.dfs(root, res, [root.val])
        return res

    def dfs(self, root, res, path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, path + [root.right.val])
