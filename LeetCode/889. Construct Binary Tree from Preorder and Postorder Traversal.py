# Time: O(n)
# Space: O(n)

# 与105,106题一样，但是这题的难点在于从前序遍历的第二个数在后续中确定索引，再得到左右子树的范围。不像之前的题那么直接划分左右子树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if (not pre) and (not post):
            return

        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        mid_id = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:mid_id+2], post[:mid_id+1])
        root.right = self.constructFromPrePost(pre[mid_id+2:], post[mid_id+1:-1])
        return root
