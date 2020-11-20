// Time：O(MN*3^L), L是单词长度，第一个位置会进4个位置，其余最多三个位置
// Space：O(MN) visited数组大小

/*
非常标准的dfs代码
1.全局变量声明四个方向
2.主函数，visited初始化，进入dfs
3.验证是否超过边界的函数
4.dfs函数定义
5.如果：不超边界，没有visited，dfs返回为真，则返回真
××6××：注意return false要有
*/

// golang的很多细节

/*
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 200
1 <= word.length <= 103
board and word consists only of lowercase and uppercase English letters.

*/

//dir := [][]int{ // 全局变量必须用var声明
var dir = [][]int{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func exist(board [][]byte, word string) bool {
	visited := make([][]bool, len(board))
	for i := 0; i < len(board); i++ {
		// visited[i] := make([]bool, len(visited[0])) 这里不能是visited，只能是board
		// visited := make([]bool, len(board[0])) 只要不是第一次出现，就不能用:=
		visited[i] = make([]bool, len(board[0]))
	}
	for i, v := range board {
		for j := range v {
			if searchWord(board, visited, word, 0, i, j) {
				return true
			}
		}
	}
	return false
}

func isInBoard(board [][]byte, x, y int) bool {
	return x >= 0 && x < len(board) && y >= 0 && y < len(board[0])
}

func searchWord(board [][]byte, visited [][]bool, word string, index, x, y int) bool {
	if index == len(word)-1 {
		return board[x][y] == word[index]
	}
	if board[x][y] == word[index] {
		visited[x][y] = true
		for i := 0; i < 4; i++ {
			newx := x + dir[i][0]
			newy := y + dir[i][1]
			if isInBoard(board, newx, newy) && !visited[newx][newy] && searchWord(board, visited, word, index+1, newx, newy) {
				return true
			}
		}
		// 这里不懂，为什么又变成了false
		// 官方：回溯时还原已访问的单元格
		visited[x][y] = false
	}
	return false
}
