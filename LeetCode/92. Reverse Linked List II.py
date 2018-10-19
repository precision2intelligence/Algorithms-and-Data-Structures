#构建初始的0结点，注释中提示了结点类的定义
#两次计数要注意边界

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy, partial_len = ListNode(0), n - m
        dummy.next = head
        prev, curr = dummy, dummy.next
        # 取出mn之间的结点，并反转
        while m > 1:  # pre是开始反转的结点
            prev, curr = curr, curr.next
            m -= 1
        last_unswapped, first_swapped = prev, curr
        while curr and partial_len >= 0:  # pre是结束反转的结点
            curr.next, prev, curr = prev, curr, curr.next
            partial_len -= 1
        # 重新连接结点
        last_unswapped.next, first_swapped.next = prev, curr
        return dummy.next

