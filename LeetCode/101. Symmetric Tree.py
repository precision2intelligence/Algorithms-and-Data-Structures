#注意子函数的嵌套

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSameTree(p, q):
            if not p and not q:  # 两二叉树皆为空，递归边界，两者皆为空返回真
                return True
            if p and q and p.val == q.val:
                l = isSameTree(p.left, q.right)  # ，与leetcode100有区别。递归，每次重新从函数入口处进行，每次进行递归边界判断
                r = isSameTree(p.right, q.left)
                return l and r  # and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值
            else:
                return False

        if not root:
            return True
        else:
            # p=root.left;q=root.right
            return isSameTree(root.left, root.right)

