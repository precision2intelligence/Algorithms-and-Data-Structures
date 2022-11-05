## Time:O(n)
## Space:O(1)

'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

## 快慢指针，快指针2步，慢指针1步

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pfast, pslow = head, head
        while pfast and pfast.next:
            pfast = pfast.next.next
            pslow = pslow.next
        return pslow