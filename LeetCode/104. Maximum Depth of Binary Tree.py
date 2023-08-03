

# 解法一：递归
# Time:O(n)
# Space:O(depth) 递归栈深度，最坏情况退化成1条链，复杂度为O(n)
# 左右子树深度都知道，直接求深度；退出条件是当前到根节点，深度就是0；注意最开始判断条件return 是数字不是空

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 # 深度
        l = self.maxDepth(root.left) if root.left else 0
        r = self.maxDepth(root.right) if root.right else 0
        maxdepth = max(l,r)+ 1
        return maxdepth


# 解法二：宽度遍历（本质是队列）
# Time:O(n)
# Space:O(n) 每一层的节点都要入队列
# 只要队列有数，就先求一共要出对多少次，每次出队都继续入队左右子树
# 注意：初始化队列和深度

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth