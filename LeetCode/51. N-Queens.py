# Time:  O(n!) n是皇后数量
# Space: O(n)

'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
'''

'''
1. 只用了col，dia1和dia2的一维数组存储结果
2. 遍历的是行——>列，变量比较特殊
3. 最后append方法，建议在generateAns以外
4. 注意ans形式
'''



class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = [0 for _ in range(n)]
        col, dia1, dia2 = set(), set(), set()
        res = list()
        self.backtrack(res, n, queens, col, dia1, dia2, 0)
        return res
    def backtrack(self, res, n, queens, col, dia1, dia2, begin):
        if begin == n:
            board = self.generateAns(res, n, queens)
            res.append(board)
            return res
        else:
            for i in range(n):
                if i in col or begin - i in dia1 or begin + i in dia2:
                    continue
                queens[begin] = i
                col.add(i)
                dia1.add(begin - i)
                dia2.add(begin + i)
                self.backtrack(res, n, queens, col, dia1, dia2, begin+1)
                # queen.remove(begin)
                col.remove(i)
                dia1.remove(begin - i)
                dia2.remove(begin + i)

    def generateAns(self, res, n, queen):
        # ans形式
        ans = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            ans[i][queen[i]] = 'Q'
            ans[i] = ''.join(ans[i])
        return ans
