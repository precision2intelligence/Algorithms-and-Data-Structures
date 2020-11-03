// Time: O(n)
// Space: O(k) k是队列中最多元素个数

// 宽度优先搜索 BFS 队列

/*
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.



Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4



Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1

*/

func shortestPathBinaryMatrix(grid [][]int) int {
	// 斜着也可以到，8个方向
	var dx = []int{-1, -1, -1, 0, 1, 1, 1, 0}
	var dy = []int{-1, 0, 1, 1, 1, 0, -1, -1}

	if grid[0][0] == 1 {
		return -1
	}

	N := len(grid)

	var cells = make([][2]int, 1, N*N) // 为什么是二维
	grid[0][0] = 1
	var length int = 1
	// length := 1

	for len(cells) > 0 { // 本质为 while 循环
		size := len(cells)
		for c := 0; c < size; c++ {
			cell := cells[c]
			x, y := cell[0], cell[1]
			if x == N-1 && y == N-1 {
				return length
			}

			for k := 0; k < 8; k++ {
				i, j := x+dx[k], y+dy[k]
				if i < 0 || i >= N || j < 0 ||
					j >= N || grid[i][j] == 1 {
					continue
				}

				grid[i][j] = 1
				cells = append(cells, [2]int{i, j})
			}
		}
		length++
		cells = cells[size:] // BFS的特点，从最新的一组路径开始
	}
	return -1
}