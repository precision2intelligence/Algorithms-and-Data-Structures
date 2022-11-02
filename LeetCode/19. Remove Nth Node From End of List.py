## Time:O(n)
## Space:O(1)
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy
        dummy = ListNode(0, head)
        pfront, pback = head, dummy
        while n > 0:
            pfront = pfront.next
            n -= 1
        while pfront:
            pback = pback.next
            pfront = pfront.next

        tmp = pback.next.next
        pback.next = tmp
        return dummy.next