# O(Time):O(n)
# O(Time):O(1)

# 双指针思想，但是在链表中，本来就是指针，所以不用虚拟指针
# 注意，这原地删除，所以返回head就可以，不用虚拟节点dummy

'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                curr.next = curr.next .next
        return head