'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre - order traversal of the binary tree.

Example 1:
Input: root = [1, 2, 5, 3, 4, null, 6]
Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]

Example2:
Input: root = []
Output: []
Example3:

Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range[0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

# 解法一：前序指针
# Time:O(n)
# Space:O(1)
# 不占用额外空间，始终找到左子树的最右边子节点，构造前序指针pre
# 注意：root不变，所以用cur变量存储当前节点

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        return

# 解法二：递归+前序遍历
# Time:O(n)
# Space:O(n)
# 先左右子树递归，排序好左右子树
# 最后把左右子树按题目要求整理好，不涉及root的再赋值

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root.right
            root.right = root.left
            root.left = None
        return


