# Time:n的指数次方
# Space：O(n) 递归栈的深度

# 结束条件：左右括号都被消耗完
# 选择前提：剩余左括号少于右括号，左或右括号都还有剩余

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        left, right = n, n
        self.backtrack(left, right, res, '')
        return res
    def backtrack(self, left, right, res, path):
        # 达到终止条件
        if left == 0 and right == 0:
            res.append(path)
        if left <= right and left >= 0 and right >= 0:
            # 添加左括号
            path += "("
            self.backtrack(left-1, right, res, path)
            # 取出前面的括号，回退最后一个
            path = path[:-1]
            # 添加右括号
            path += ")"
            self.backtrack(left, right-1, res, path)
            path = path[:-1]
