// O(Time): O(n)
// O(Space): O(1)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// 边界检查
	if headA == nil || headB == nil {
		return nil
	}
	pA, pB := headA, headB
	// 第一次遍历交换链表头，这样消除了链表长度差；之后遍历直到节点相等
	// 相等节点是nil就是不相交
	for pA != pB {
		if pA == nil {
			pA = headB
		} else {
			// Go的指针用法
			pA = pA.Next
		}

		if pB == nil {
			pB = headA
		} else {
			pB = pB.Next
		}
	}
	return pA
}