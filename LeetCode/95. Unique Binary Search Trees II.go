// 复杂度分析见官方题解，需要二叉树的知识

// 二叉搜索树：如有左子树，均小于根节点；如有右子树，均大于根节点

// 算法：分治（递归），和241题很相似

// 不太理解golang对二叉树定义的数据结构，需要再学习一下

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{} // 这里如返回 []*TreeNode{nil}，输入0的时候会得到[[]],期望值是[]
	}
	return generateBSTree(1, n)
}

func generateBSTree(start int, end int) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}
	allTrees := []*Treenode{}

	for i := start; i <= end; i++ {
		leftTrees := generateBSTree(start, i-1)
		rightTrees := generateBSTree(i+1, end)

		for _, l := range leftTrees {
			for _, r := range rightTrees {
				currTree := &TreeNode{i, nil, nil}
				currTree.Left = l
				currTree.Right = r
				allTrees = append(allTrees, currTree)
			}
		}
	}
	return allTrees
}