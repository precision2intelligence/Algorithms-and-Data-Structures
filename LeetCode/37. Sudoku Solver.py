# Time:没找到
# Space:O(m),m为留空的个数。

''' 递归+回溯
1. 不能重复用数字，所以要用集合，集合可以作减法，但是不改变原集合的值
2. 用row，col和block分别表示行、列和宫
3. 原地改变board，输入参数是全局变量，不能用global声明，但是要传参
4. 一定返回True，不然少判断条件
'''

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        global nums, row, col, block, blank
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]
        blank = list()


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[i//3][j//3].add(board[i][j])


        self.backtrack(board, 0)

    def backtrack(self, board, n):
        if n == len(blank):
            return True # 这里一定有返回，不然判断条件进不去

        # for (i, j) in blank:
        i, j = blank[n]
        subNums = nums - row[i] - col[j] - block[i//3][j//3]
        # subNums = nums - (row[i] | col[j] | block[i//3][j//3]) 可行
        if len(subNums) == 0:
            return False
        for num in subNums:
            board[i][j] = num
            row[i].add(num)
            col[j].add(num)
            block[i//3][j//3].add(num)
            if self.backtrack(board, n+1):
                return True
            row[i].remove(num)
            col[j].remove(num)
            block[i//3][j//3].remove(num)

s = Solution()
a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(a)
print(a)