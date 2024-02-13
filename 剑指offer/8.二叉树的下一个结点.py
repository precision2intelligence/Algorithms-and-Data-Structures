# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
'''
直接寻找分为三种情况

如果给出的结点有右子节点，则最终要返回的下一个结点即右子树的最左下的结点
如果给出的结点无右子节点，且当前结点是其父节点的左子节点，则返回其父节点
如果给出的结点无右子节点，且当前结点是其父节点的右子节点，则先要沿着左上方父节点爬树，一直爬到当前结点是其父节点的左子节点为止，返回的就是这个父节点；或者没有满足上述情况的则返回为NULL
'''
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next
        return None

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        # 有右子树
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 无右子树，且是左子树
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next

        # 无右子树，且是右子树
        elif pNode.next and pNode.next.right == pNode:
            ppar = pNode.next
            while (ppar.next and ppar.next.right == ppar):
                ppar = ppar.next
            return ppar.next

        return None