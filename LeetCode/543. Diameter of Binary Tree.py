# 解法一：递归
# Time:O(n)
# Space:O(depth) 递归栈深度，最坏情况退化成1条链，复杂度为O(n)
# helper写法很妙，返回的是深度，中间过程做的最大值更新
# curMax 是全局变量，self前缀；开始赋值不用self

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    curMax = 0
    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.curMax = max(self.curMax, l+r)
        return max(l,r) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.curMax

# 解法二：遍历
# Time:O(n^2)
# Space:O(n)
# 因为调用了很多次求最大深度的函数，所以复杂度高。所以二叉树尽量递归

class Solution(object):
    curMax = 0

    def maxDepthOfBinaryTree(self, root):
        if not root:
            return 0
        l = self.maxDepthOfBinaryTree(root.left)
        r = self.maxDepthOfBinaryTree(root.right)
        maxDepth = max(l, r) + 1
        return maxDepth

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l = self.maxDepthOfBinaryTree(root.left)
        r = self.maxDepthOfBinaryTree(root.right)
        step = l + r
        self.curMax = max(step, self.curMax)
        # 这里别忘了继续调用
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.curMax