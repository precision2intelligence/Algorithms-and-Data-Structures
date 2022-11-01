## Time:O(n)
## Space:O(1)
'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
eg.
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Input: head = [2,1], x = 2
Output: [1,2]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 初始化dummy
        fdum, bdum, curr = ListNode(0), ListNode(0), head
        # 为指针赋值
        front, back = fdum, bdum
        while curr:
            if curr.val < x:
                front.next = curr
                front = curr
            else:
                back.next = curr
                back = curr
            curr = curr.next
        # 整理结果
        front.next, back.next = bdum.next, curr
        return fdum.next
