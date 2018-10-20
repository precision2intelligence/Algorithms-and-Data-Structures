# 计数判奇偶

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodeStack = [pRoot]
        result = []
        times = 0
        while nodeStack:
            times += 1
            res = []
            nextStack = []
            for i in nodeStack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            nodeStack = nextStack
            if times % 2 == 0:
                res = res[::-1]
            result.append(res)
        return result
