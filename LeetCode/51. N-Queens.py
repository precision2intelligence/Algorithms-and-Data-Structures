# Time:  O(n!) n是皇后数量
# Space: O(n)

# labuladong 回溯模板

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
1. 只用了col，dia1和dia2的一维数组存储结果，正对角线上：row-col相同；反对角线：row+col相等
2. 遍历的是行——>列，变量比较特殊
3. 注意ans形式，可以由列表转字符串，因为字符串不支持直接赋值
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        colSet, dia1, dia2 = set(), set(), set()
        backtrack(res, [], n, 0, colSet, dia1, dia2)
        ans = mkres(res, n)
        return ans
def backtrack(res, path, n, begin, colSet, dia1, dia2):
    if begin == n:
        res.append(path[:])

    for col in range(n):
        if col not in colSet and (begin - col) not in dia1 and (begin + col) not in dia2:
            path.append(col)
            colSet.add(col)
            dia1.add(begin-col)
            dia2.add(begin+col)
            backtrack(res, path, n, begin+1, colSet, dia1, dia2)
            path.pop()
            colSet.remove(col)
            dia1.remove(begin-col)
            dia2.remove(begin+col)

def mkres(res, n):
    m = len(res)
    ans = []
    for i in range(m):
        labels = [['.' for _ in range(n)] for _ in range(n)]
        for j, idx in enumerate(res[i]):
            labels[j][idx] = "Q"
            labels[j] = ''.join(labels[j])
        ans.append(labels[:])
    return ans
