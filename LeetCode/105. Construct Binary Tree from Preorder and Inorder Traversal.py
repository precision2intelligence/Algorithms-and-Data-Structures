# Time: O(n)
# Space: O(n)

# 递归，注意初始化的时候root=TreeNode类，而不是int的值；注意index获取的索引不是直接用，要注意边界，排除已经用的
# 在中序中获得的root索引即为下一次切分的点，这个点也是前序中应该包含的数量

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (not preorder) and (not inorder):
            return
        root = TreeNode(preorder[0])
        mid_id = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid_id+1], inorder[:mid_id])
        root.right = self.buildTree(preorder[mid_id+1:], inorder[mid_id+1:])
        return root # 返回的是树