# 用后序遍历，不要重复求每个节点的深度

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.Depth(pRoot) != -1
    def Depth(self,pRoot):
        if pRoot is None: return 0
        lDepth = self.Depth(pRoot.left)
        rDepth = self.Depth(pRoot.right)
        if lDepth == -1 or rDepth == -1:return -1
        if abs(lDepth-rDepth)<=1 :return max(lDepth,rDepth)+1
        return -1
