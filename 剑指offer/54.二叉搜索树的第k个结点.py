# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0: return None
        res = []
        self.inOrder(pRoot, res)
        if len(res) < k:
            return None
        return res[k - 1]

    def inOrder(self, root, res):
        if not root: return
        if root.left:
            self.inOrder(root.left, res)
        res.append(root)
        if root.right:
            self.inOrder(root.right, res)
