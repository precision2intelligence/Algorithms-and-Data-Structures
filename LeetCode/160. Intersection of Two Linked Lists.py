#Time: O(m+n)
#Space: O(1)

# 简单问题注意举例特殊情况来验证边界
# 如这道题，要想到不相交的情况，避免进入一直交换指针永远同时走不到None节点的情况

# 统计两个链表的长度，去掉长列表的长度，然后遍历知道找到相同的节点
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法一：双指针法，核心在于构造共同前进距离，所以两个指针都有两个长度；两个链表如果相交，会相遇在交点；不相交，会走完两个链表长度到达None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            if pa == None:
                pa = headB
            else:
                pa = pa.next

            if pb == None:
                pb = headA
            else:
                pb = pb.next
        return pa

# 解法二：同解法一，就是避免出错，反复check两个节点是否相等（移动前比较，移动后比较）

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb: # 第一次比较

            pa = pa.next
            pb = pb.next
            if pa == pb: # 第二次比较，移动后马上比较
                break
            if pa == None:
                pa = headB
            if pb == None:
                pb = headA

        return pa


# 解法三：先取得两链表长度，长链表节点先走差值，再并进。缺点是遍历两遍
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m,n = self.GetLength(headA),self.GetLength(headB)
        if m > n:
            for i in range(m-n):
                headA = headA.next
            while headA != headB and headA and headB:
                headA = headA.next
                headB = headB.next
            return headA
        else:
            for i in range(n-m):
                headB = headB.next
            while headA != headB and headA and headB:
                headA = headA.next
                headB = headB.next
            return headA
    #统计链表长度
    def GetLength(self,pHead):
        if not pHead:
            return 0
        count = 0
        while pHead:
            pHead = pHead.next
            count += 1
        return count
