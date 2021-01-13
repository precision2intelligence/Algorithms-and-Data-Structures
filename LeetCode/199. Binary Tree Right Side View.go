// BFS 二叉树层次遍历，每读到队列的最后一个，就加入结果

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	// 队列定义
	Q, res := []*TreeNode{root}, []int{}
	for len(Q) > 0 {
		// 记录现在队列的长度，后面会更新
		l := len(Q)
		for i := 0; i < l; i++ {
			if Q[i].Left != nil {
				Q = append(Q, Q[i].Left)
			}
			if Q[i].Right != nil {
				Q = append(Q, Q[i].Right)
			}
			if i == l-1 {
				res = append(res, Q[i].Val)
				Q = Q[l:]
			}
		}
	}
	return res
}