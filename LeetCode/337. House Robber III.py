#Time：O(n)
#Space：O(logn)

# 二叉树只要“无连接”就不会触发报警
# res[0],res[1]分别表示抢当前节点和不抢当前节点

'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = dp_rob(root)
        # res是数组，下面等价于 return max(res[0], res[1])
        return max(res)
def dp_rob(root):
    if not root:
        return [0,0]
    left = dp_rob(root.left)
    right = dp_rob(root.right)
    return [root.val + left[1] + right[1], max(left)+max(right)]