#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 两个解法的时间、空间复杂度都是O(n)

# 解法一：递归
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))
    def dfs(self, root, lower, higher):
        if not root:
            return True

        if not lower < root.val < higher:
            return False

        return self.dfs(root.left, lower, root.val) and self.dfs(root.right, root.val, higher)

# 解法二：中序遍历
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.inorder(root)
        return all(res[i] > res[i-1] for i in range(1, len(res)))
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)