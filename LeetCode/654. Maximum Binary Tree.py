'''
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Example 1:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:
Input: nums = [3,2,1]
Output: [3,null,2,null,1]

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
All integers in nums are unique.
'''

# 解法一：单调栈
# Time:O(n)
# Space:O(logn) 递归栈深度，最坏情况退化成1条链，复杂度为O(n)
# 栈内单调递减，然后用栈顶元素和下一个num比较，只需要一次遍历。这个解法关键要理解，大数左侧数字要放在要放在左侧子树，小数进来要放在右侧子树
# 易错：while在前，if在后，先把大数左子树挂好，因为大数处理要不断pop，影响栈顶。最终还是为了把大数放到正确位置

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        stack = []

        for num in nums:
            cur = TreeNode(num)
            while stack and num > stack[-1].val:
                cur.left = stack.pop()

            if stack and num < stack[-1].val:
                stack[-1].right = cur

            stack.append(cur)  # cur
        return stack[0]


# 解法二：递归
# Time:O(n^2) 最坏情况数组单调，需要递归n层，第i层需要遍历n-i求最大值
# Space:O(n) 递归栈深度，最坏情况使用的栈空间
# 类似于给定前序和中序遍历构建二叉树，通过index分治


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        maxValue = max(nums)
        root = TreeNode(maxValue)

        pivot = nums.index(maxValue)

        root.left = self.constructMaximumBinaryTree(nums[:pivot])
        root.right = self.constructMaximumBinaryTree(nums[pivot+1:])

        return root
