# Time: O(n)
# Space: O(n)

# 递归，和105题一样，但是，后续遍历最后是根节点，根据中序的根节点作为cut，切分后续的左右子树，依然注意边界

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if (not inorder) and (not postorder):
            return

        root = TreeNode(postorder[-1])
        mid_id = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid_id],postorder[:mid_id])
        root.right = self.buildTree(inorder[mid_id+1:], postorder[mid_id:-1])
        return root