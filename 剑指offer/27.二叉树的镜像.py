# 从根节点开始，有左右节点就交换
#直到叶子节点

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root