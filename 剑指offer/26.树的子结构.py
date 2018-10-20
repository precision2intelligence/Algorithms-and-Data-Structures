# 1、 判断A当前节点开始，B是否为子结构，如果不是看下A的左子树节点，如果也不是再看下A的右子树。
#
# 2、如果是某节点开始A与B的起始节点重合：
#
# ①判断B是否匹配完了，如果匹配完了说明为子结构
#
# ②如果A匹配完了，或者A的值和B和值不等，直接返回False
#
# ③如果当前点相同，那同时看一下左子树和右子树的情况。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.has2tree( pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    def has2tree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return  True
        if pRoot1 == None:
            return  False
        if pRoot1.val != pRoot2.val:
            return False
        return self.has2tree(pRoot1.left,pRoot2.left) and self.has2tree(pRoot1.right , pRoot2.right)
