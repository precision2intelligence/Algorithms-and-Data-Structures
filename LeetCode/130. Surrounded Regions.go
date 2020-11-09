// Time: O(m×n) 只遍历一遍
// Space: O(m×n)

// dfs
// 把四个边先判断一遍，由边缘进去的都临时标为'A'，golang务必为单引号
// 最后遍历，替换A为O，原本没标记的O是X

/*
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
*/

var m, n int // 后面dfs也会用，所以是全局变量

func solve(board [][]byte) {
	// 如果直接 m, n = len(board), len(board[0])，遇到[]会报错
	if len(board) == 0 || len(board[0]) == 0 {
		return
	}
	m, n = len(board), len(board[0]) // 全局声明后，不能用冒号赋值

	for i := 0; i < m; i++ {
		dfs(board, i, 0)
		dfs(board, i, n-1)
	}

	for j := 1; j < n-1; j++ {
		dfs(board, 0, j)
		dfs(board, m-1, j)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'A' {
				board[i][j] = 'O'
			} else if board[i][j] == 'O' {
				board[i][j] = 'X'
			}
		}
	}
	return
}

func dfs(board [][]byte, x, y int) {
	if x < 0 || y < 0 || x > m-1 || y > n-1 || board[x][y] != 'O' {
		return
	}
	board[x][y] = 'A'
	dfs(board, x, y-1)
	dfs(board, x, y+1)
	dfs(board, x-1, y)
	dfs(board, x+1, y)
}