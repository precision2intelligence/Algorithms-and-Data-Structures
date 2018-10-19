#双向链表也有left和right
#如果有左子树返回左，否则返回根
#注意self的使用
#似乎树都是递归好一些

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree: return None
        if not pRootOfTree.left and not pRootOfTree.right:#root节点左右孩子均为None
            self.leftlast = pRootOfTree#有self
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)#递归左边
        if left:#如果left不为None
            self.leftlast.right = pRootOfTree#有self
            pRootOfTree.left = self.leftlast#有self
        self.leftlast = pRootOfTree#有self
        right = self.Convert(pRootOfTree.right)#递归右边
        if right:
            right.left = pRootOfTree#没有self
            pRootOfTree.right = right#没有self
        return left if left else pRootOfTree#亮点
