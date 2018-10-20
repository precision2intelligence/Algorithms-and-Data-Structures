# 1、 判断A当前节点开始，B是否为子结构，如果不是看下A的左子树节点，如果也不是再看下A的右子树。
#
# 2、如果是某节点开始A与B的起始节点重合：
#
# ①判断B是否匹配完了，如果匹配完了说明为子结构
#
# ②如果A匹配完了，或者A的值和B和值不等，直接返回False
#
# ③如果当前点相同，那同时看一下左子树和右子树的情况。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)
