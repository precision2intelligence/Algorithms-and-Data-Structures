# Time:  O(n)
# Space: O(1)
#需要证明：http://www.itbox.info/article/8462

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pFast, pSlow = head, head
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast == None or  pFast.next == None:
            return None
        pFast = head
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast
